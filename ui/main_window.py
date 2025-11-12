from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QBoxLayout, QPushButton, QSizePolicy
from PySide6.QtCore import Qt
from .util.contants import Contants
from .widgets.translation_widget import TranslationWidget

class MainWindow(QMainWindow):
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
        #Set central widget
        self.main_widget = QWidget()
        self.main_widget.setContentsMargins(0, 0, 0, 0) #To remove default margins
        self.setCentralWidget(self.main_widget)

        #Main Grid Layout
        grid = QGridLayout()
        grid.setContentsMargins(0, 0, 0, 0) #To remove default margins
        grid.setSpacing(0)
        
        grid.addWidget(TranslationWidget(),0, 0)
        grid.addWidget(QPushButton("Column 2"),0, 1)
        
        self.main_widget.setLayout(grid)

        self.main_widget.show()