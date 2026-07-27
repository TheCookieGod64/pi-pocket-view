import sys
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QSplitter,
    QLabel,
    QLineEdit,
    QPushButton
)
from PyQt6.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("pi-pocket-view")
        self.resize(1280, 720)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(5, 5, 5, 5)

        # Control Bar for IP / Connection
        control_layout = QHBoxLayout()

        ip_label = QLabel("Pi IP Address:", self)
        control_layout.addWidget(ip_label)

        self.ip_input = QLineEdit(self)
        self.ip_input.setText("192.168.7.2")
        control_layout.addWidget(self.ip_input)

        connect_btn = QPushButton("Connect", self)
        connect_btn.clicked.connect(self.load_views)
        control_layout.addWidget(connect_btn)

        main_layout.addLayout(control_layout)

        # Splitter to hold Video View and Terminal View
        self.splitter = QSplitter(Qt.Orientation.Vertical, self)

        # Top view: Video Stream
        self.video_view = QWebEngineView(self)
        self.splitter.addWidget(self.video_view)

        # Bottom view: Embedded ttyd Web Terminal
        self.terminal_view = QWebEngineView(self)
        self.splitter.addWidget(self.terminal_view)

        # Set initial size distribution (50/50 split)
        self.splitter.setSizes([360, 360])

        main_layout.addWidget(self.splitter)

        # Initial view load
        self.load_views()

    def load_views(self):
        ip = self.ip_input.text().strip()
        if not ip:
            return

        video_url = f"http://{ip}:8080"
        terminal_url = f"http://{ip}:7681"

        self.video_view.setUrl(QUrl(video_url))
        self.terminal_view.setUrl(QUrl(terminal_url))
