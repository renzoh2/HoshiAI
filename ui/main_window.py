from PyQt6.QtWidgets import QWidget, QGridLayout, QBoxLayout, QPushButton, QSizePolicy
from PyQt6.QtCore import Qt
from .util.contants import Contants

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self._window_configuration()
        self._layout_components()

    def _window_configuration(self):
        self.setWindowTitle(Contants.APPLICATION_NAME)

        g = self.screen()
        xScreen = int(g.availableGeometry().width() / 2) - int(582 / 2)
        yScreen = int(g.availableGeometry().height() / 2) - int(241 / 2)
        self.setGeometry(xScreen, yScreen, 582, 241)

    def _layout_components(self):
        box = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        box.setContentsMargins(0, 0, 0, 0)
        box.setSpacing(0)
        self.setLayout(box)

        grid = QGridLayout()
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(0)

        btn1 = QPushButton("WEW1")
        btn2 = QPushButton("WEW2")

        btn1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        btn2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)

        box.addLayout(grid)