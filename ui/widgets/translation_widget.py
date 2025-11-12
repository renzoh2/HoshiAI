from PySide6.QtWidgets import QWidget, QGridLayout
from .language_switch_widget import LanguageSwitchWidget

class TranslationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._layout_components()
        self.setContentsMargins(0, 0, 0, 0)
        

    def _layout_components(self):
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        layout.addWidget(LanguageSwitchWidget(), 0, 0)