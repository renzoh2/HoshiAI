from PySide6.QtWidgets import QWidget, QGridLayout, QComboBox
import json
from ..util.contants import Contants

class LanguageSwitchWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.language_options = self._load_language_options()
        self._layout_components()

    def _load_language_options(self):
        with open(Contants.LANGUAGE_OPTIONS_FILE, 'r') as file:
            return json.load(file)

    def _layout_components(self):
        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addWidget(self.language_widget('from_language'), 0, 0)
        self.layout.addWidget(self.language_widget('to_language'), 0, 1)
        self.setLayout(self.layout)

    def language_widget(self, language_type):
        from_language_dropbox = QComboBox()
        from_language_dropbox.setContentsMargins(0, 0, 0, 0)
        from_language_dropbox.addItems(self.language_options[language_type]['options'])
        return from_language_dropbox