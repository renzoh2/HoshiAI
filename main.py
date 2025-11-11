import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

#ENTRYPOINT
if __name__ == "__main__":
   app = QApplication([])
   window = MainWindow()
   window.show()
   sys.exit(app.exec())