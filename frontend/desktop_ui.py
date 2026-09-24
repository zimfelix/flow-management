"""Desktop controls for the in-memory work-day domain."""

from collections.abc import Callable
from datetime import date, datetime

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from backend.exceptions import DomainError
from backend.time_period import BreakPeriod, WorkPeriod
from backend.work_day import WorkDay
from backend.work_session import WorkSession


class DesktopWindow(QWidget):
    def __init__(self, clock: Callable[[], datetime] = datetime.now) -> None:
        super().__init__()
        self._clock = clock
        self._days: dict[date, WorkDay] = {}
        self._active_day: WorkDay | None = None
        self._active_session: WorkSession | None = None

        self.setWindowTitle("Flow Management")
        self.status = QLabel()
        self.error = QLabel()
        self.entries = QListWidget()
        self.start_button = QPushButton("Arbeit starten")
        self.break_button = QPushButton("Pause beginnen")
        self.resume_button = QPushButton("Arbeit fortsetzen")
        self.end_button = QPushButton("Arbeit beenden")

        buttons = QHBoxLayout()
        for button in (
            self.start_button,
            self.break_button,
            self.resume_button,
            self.end_button,
        ):
            buttons.addWidget(button)

        layout = QVBoxLayout(self)
        layout.addWidget(self.status)
        layout.addLayout(buttons)
        layout.addWidget(self.entries)
        layout.addWidget(self.error)

        self.start_button.clicked.connect(self.start_work)
        self.break_button.clicked.connect(self.start_break)
        self.resume_button.clicked.connect(self.resume_work)
        self.end_button.clicked.connect(self.end_work)
        self._refresh()

    def start_work(self) -> None:
        started_at = self._clock()
        day = self._days.get(started_at.date())
        if day is None:
            day = WorkDay(started_at.date())

        try:
            session = day.start_session(started_at)
        except DomainError as error:
            self.error.setText(str(error))
            return

        self._days[day.day] = day
        self._active_day = day
        self._active_session = session
        self._refresh()

    def start_break(self) -> None:
        if self._active_day is None:
            return
        try:
            self._active_day.start_break(self._clock())
        except DomainError as error:
            self.error.setText(str(error))
            return
        self._refresh()

    def resume_work(self) -> None:
        if self._active_day is None:
            return
        try:
            self._active_day.resume_work(self._clock())
        except DomainError as error:
            self.error.setText(str(error))
            return
        self._refresh()

    def end_work(self) -> None:
        if self._active_day is None:
            return
        try:
            self._active_day.end_session(self._clock())
        except DomainError as error:
            self.error.setText(str(error))
            return
        self._active_day = None
        self._active_session = None
        self._refresh()

    def _refresh(self) -> None:
        active_period = self._active_session.active_period if self._active_session else None
        is_working = isinstance(active_period, WorkPeriod)
        is_break = isinstance(active_period, BreakPeriod)
        self.status.setText(
            "Arbeit läuft" if is_working else "Pause läuft" if is_break else "Keine aktive Session"
        )
        self.start_button.setEnabled(active_period is None)
        self.break_button.setEnabled(is_working)
        self.resume_button.setEnabled(is_break)
        self.end_button.setEnabled(active_period is not None)
        self.error.clear()

        self.entries.clear()
        for day in sorted(self._days.values(), key=lambda value: value.day):
            for session in day.work_sessions:
                end = session.end_time.isoformat(sep=" ", timespec="minutes") if session.end_time else "läuft"
                self.entries.addItem(
                    f"Session: {session.start_time.isoformat(sep=' ', timespec='minutes')} → {end}"
                )
                periods = sorted(
                    [*session.work_periods, *session.break_periods],
                    key=lambda period: period.start_time,
                )
                for period in periods:
                    kind = "Arbeit" if isinstance(period, WorkPeriod) else "Pause"
                    start = period.start_time.strftime("%H:%M")
                    finish = period.end_time.strftime("%H:%M") if period.end_time else "läuft"
                    self.entries.addItem(f"  {kind}: {start} → {finish}")
