"""Launch the local Flow Management desktop application."""

import sys

from PySide6.QtWidgets import QApplication

from frontend.desktop_ui import DesktopWindow


def main() -> int:
    app = QApplication(sys.argv)
    window = DesktopWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
