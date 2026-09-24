from datetime import datetime

import pytest

from backend.exceptions import (
    ActiveSessionAlreadyExistsError,
    EndBeforeStartError,
    NoActiveSessionError,
)
from backend.flow_manager import FlowManager
from backend.time_period import BreakPeriod, WorkPeriod


def clock_at(*times: datetime):
    moments = iter(times)
    return lambda: next(moments)


def test_manager_coordinates_workflow_without_a_ui():
    manager = FlowManager(
        clock_at(
            datetime(2026, 7, 20, 9),
            datetime(2026, 7, 20, 10),
            datetime(2026, 7, 20, 10, 15),
            datetime(2026, 7, 20, 17),
        )
    )

    session = manager.start_work()
    day = manager.work_days[0]
    assert day.work_sessions == [session]
    assert manager.active_session is session
    assert isinstance(session.active_period, WorkPeriod)

    assert manager.start_break() is session
    assert isinstance(session.active_period, BreakPeriod)
    assert manager.resume_work() is session
    assert isinstance(session.active_period, WorkPeriod)

    assert manager.end_work() is session
    assert session.end_time == datetime(2026, 7, 20, 17)
    assert manager.active_session is None
    assert manager.work_days == (day,)


def test_second_start_does_not_add_a_day_or_change_active_session():
    manager = FlowManager(clock_at(datetime(2026, 7, 20, 9)))
    session = manager.start_work()
    days_before = manager.work_days

    with pytest.raises(ActiveSessionAlreadyExistsError):
        manager.start_work()

    assert manager.work_days == days_before
    assert manager.active_session is session
    assert session.end_time is None


def test_missing_session_is_rejected_without_creating_a_day():
    manager = FlowManager()

    with pytest.raises(NoActiveSessionError):
        manager.start_break()

    assert manager.work_days == ()
    assert manager.active_session is None


def test_invalid_break_time_keeps_session_and_work_period_active():
    manager = FlowManager(
        clock_at(datetime(2026, 7, 20, 9), datetime(2026, 7, 20, 8, 59))
    )
    session = manager.start_work()
    original_period = session.active_period

    with pytest.raises(EndBeforeStartError):
        manager.start_break()

    assert manager.active_session is session
    assert session.active_period is original_period
    assert original_period is not None
    assert original_period.end_time is None
    assert session.break_periods == []
