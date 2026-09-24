"""Coordinate the in-memory work-day workflow independently of the desktop UI."""

from collections.abc import Callable
from datetime import date, datetime

from backend.exceptions import ActiveSessionAlreadyExistsError, NoActiveSessionError
from backend.work_day import WorkDay
from backend.work_session import WorkSession


class FlowManager:
    def __init__(self, clock: Callable[[], datetime] = datetime.now) -> None:
        self._clock = clock
        self._days: dict[date, WorkDay] = {}
        self._active_day: WorkDay | None = None
        self._active_session: WorkSession | None = None

    @property
    def active_session(self) -> WorkSession | None:
        return self._active_session

    @property
    def work_days(self) -> tuple[WorkDay, ...]:
        """Return the days for display without exposing the mutable collection."""
        return tuple(sorted(self._days.values(), key=lambda day: day.day))

    def start_work(self) -> WorkSession:
        if self.active_session is not None:
            raise ActiveSessionAlreadyExistsError()

        started_at = self._clock()
        day = self._days.get(started_at.date())
        if day is None:
            day = WorkDay(started_at.date())

        session = day.start_session(started_at)
        self._days[day.day] = day
        self._active_day = day
        self._active_session = session
        return session

    def start_break(self) -> WorkSession:
        day = self._require_active_day()
        return day.start_break(self._clock())

    def resume_work(self) -> WorkSession:
        day = self._require_active_day()
        return day.resume_work(self._clock())

    def end_work(self) -> WorkSession:
        day = self._require_active_day()
        session = day.end_session(self._clock())
        self._active_day = None
        self._active_session = None
        return session

    def _require_active_day(self) -> WorkDay:
        if self._active_day is None:
            raise NoActiveSessionError()
        return self._active_day
