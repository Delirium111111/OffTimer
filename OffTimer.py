# ------------------------------------------------------
# #  # # # # # # # OffTimer.py # # # # # # # # # # # # # # #
# Create by Delirium https://github.com/Delirium111111
# # # # # # # # # # # # Thu May 12 2022 # # # # # # # # # # # #
# ------------------------------------------------------

import sys

import qtmodern.styles
import qtmodern.windows

from PySide6.QtWidgets import QApplication, QMainWindow

from Window import Ui_MainWindow

class OffTimer(QMainWindow):
    def __init__(self):
        super(OffTimer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = OffTimer()

    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()

    sys.exit(app.exec())