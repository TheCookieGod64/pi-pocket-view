import sys
import os

# Add src folder to python path if executing directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from PyQt6.QtWidgets import QApplication
from src.pi_pocket_view.gui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("pi-pocket-view")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
