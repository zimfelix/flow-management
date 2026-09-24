"""Desktop controls for the in-memory work-day domain."""

from collections.abc import Callable
from datetime import datetime

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from backend.exceptions import DomainError
from backend.flow_manager import FlowManager
from backend.time_period import BreakPeriod, WorkPeriod


class DesktopWindow(QWidget):
    def __init__(self, clock: Callable[[], datetime] = datetime.now) -> None:
        super().__init__()
        self._flow = FlowManager(clock)

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
        self._run_action(self._flow.start_work)

    def start_break(self) -> None:
        self._run_action(self._flow.start_break)

    def resume_work(self) -> None:
        self._run_action(self._flow.resume_work)

    def end_work(self) -> None:
        self._run_action(self._flow.end_work)

    def _run_action(self, action: Callable[[], object]) -> None:
        try:
            action()
        except DomainError as error:
            self.error.setText(str(error))
            return
        self._refresh()

    def _refresh(self) -> None:
        session = self._flow.active_session
        active_period = session.active_period if session else None
        is_working = isinstance(active_period, WorkPeriod)
        is_break = isinstance(active_period, BreakPeriod)
        self.status.setText(
            "Arbeit läuft"
            if is_working
            else "Pause läuft"
            if is_break
            else "Keine aktive Session"
        )
        self.start_button.setEnabled(active_period is None)
        self.break_button.setEnabled(is_working)
        self.resume_button.setEnabled(is_break)
        self.end_button.setEnabled(active_period is not None)
        self.error.clear()

        self.entries.clear()
        for day in self._flow.work_days:
            for session in day.work_sessions:
                end = (
                    session.end_time.isoformat(sep=" ", timespec="minutes")
                    if session.end_time
                    else "läuft"
                )
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
                    finish = (
                        period.end_time.strftime("%H:%M")
                        if period.end_time
                        else "läuft"
                    )
                    self.entries.addItem(f"  {kind}: {start} → {finish}")
