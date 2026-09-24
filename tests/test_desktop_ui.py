from datetime import datetime

import pytest
from PySide6.QtWidgets import QApplication

from frontend.desktop_ui import DesktopWindow


@pytest.fixture(scope="module")
def app():
    application = QApplication.instance() or QApplication([])
    yield application


def clock_at(*times: datetime):
    moments = iter(times)
    return lambda: next(moments)


def test_window_starts_without_session_and_only_allows_start(app):
    window = DesktopWindow(clock_at(datetime(2026, 7, 20, 9)))

    assert window.status.text() == "Keine aktive Session"
    assert window.entries.count() == 0
    assert window.start_button.isEnabled()
    assert not window.break_button.isEnabled()
    assert not window.resume_button.isEnabled()
    assert not window.end_button.isEnabled()

    window.close()


def test_buttons_record_work_break_resume_and_end_with_visible_times(app):
    window = DesktopWindow(
        clock_at(
            datetime(2026, 7, 20, 9),
            datetime(2026, 7, 20, 10),
            datetime(2026, 7, 20, 10, 15),
            datetime(2026, 7, 20, 17),
        )
    )

    window.start_button.click()
    assert window.status.text() == "Arbeit läuft"
    assert not window.start_button.isEnabled()
    assert window.break_button.isEnabled()
    assert window.entries.item(0).text() == "Session: 2026-07-20 09:00 → läuft"

    window.break_button.click()
    assert window.status.text() == "Pause läuft"
    assert not window.break_button.isEnabled()
    assert window.resume_button.isEnabled()
    assert window.entries.item(1).text() == "  Arbeit: 09:00 → 10:00"

    window.resume_button.click()
    assert window.status.text() == "Arbeit läuft"
    assert window.entries.item(2).text() == "  Pause: 10:00 → 10:15"

    window.end_button.click()
    assert window.status.text() == "Keine aktive Session"
    assert window.start_button.isEnabled()
    assert window.entries.item(0).text() == "Session: 2026-07-20 09:00 → 2026-07-20 17:00"
    assert window.entries.item(3).text() == "  Arbeit: 10:15 → 17:00"

    window.close()


def test_end_during_break_keeps_entry_and_allows_new_start(app):
    window = DesktopWindow(
        clock_at(
            datetime(2026, 7, 20, 9),
            datetime(2026, 7, 20, 10),
            datetime(2026, 7, 20, 10, 30),
            datetime(2026, 7, 20, 11),
        )
    )
    window.start_button.click()
    window.break_button.click()
    window.end_button.click()

    assert window.entries.item(2).text() == "  Pause: 10:00 → 10:30"
    window.start_button.click()
    assert window.status.text() == "Arbeit läuft"
    assert window.entries.count() == 5
    assert window.entries.item(3).text() == "Session: 2026-07-20 11:00 → läuft"

    window.close()


def test_invalid_time_keeps_work_running_and_displays_domain_error(app):
    window = DesktopWindow(
        clock_at(datetime(2026, 7, 20, 9), datetime(2026, 7, 20, 8, 59))
    )
    window.start_button.click()
    before = [window.entries.item(index).text() for index in range(window.entries.count())]
    window.break_button.click()

    assert window.status.text() == "Arbeit läuft"
    assert window.error.text() == "End time cannot be before start time"
    assert [window.entries.item(index).text() for index in range(window.entries.count())] == before
    assert window.break_button.isEnabled()

    window.close()
