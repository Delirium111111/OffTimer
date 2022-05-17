# ------------------------------------------------------
# #  # # # # # # # OffTimer.py # # # # # # # # # # # # # # #
# Create by Delirium https://github.com/Delirium111111
# # # # # # # # # # # # Thu May 12 2022 # # # # # # # # # # # #
# ------------------------------------------------------

import sys
import threading
from tkinter import S
import os
import time
from unicodedata import name

import qtmodern.styles
import qtmodern.windows

from PySide6.QtWidgets import QApplication, QMainWindow

from Window import Ui_MainWindow

# --------------------------------------
# ? Зачем я это делаю?


class OffTimer(QMainWindow):
    h, m, s = 0, 0, 0
    timer_on = False
    dot = "."

    def __init__(self):
        super(OffTimer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.HS_Value.sliderReleased.connect(self.sldRealise)
        self.ui.HS_Value.valueChanged.connect(self.SyncNumbers)

    def update(self, i):
        thr = threading.Timer(1, self.update, [i+1])
        if threading.active_count() <= 2:
            thr.start()
        else:
            thr.cancel()
        
        self.s = self.s - 1
        self.Calc(self.s)
        # self.ui.L_Value_text.setText(str(self.s // 60))
        self.ui.LCD_Amount.display(self.MakeStr())
        if self.s < 0:
            thr.cancel()
        print(self.s)

    def sldRealise(self):
        self.Calc()
        print("REALISED")
        self.update(1)

    def SyncNumbers(self):
        self.ui.L_Value_text.setText(str(self.TakeAmount()))
        self.ui.LCD_Amount.display(self.MakeStr())

    def MakeStr(self) -> str:
        if self.dot == ".":
            self.dot = " "
        else:
            self.dot = "."
        str_ = str(self.h) + self.dot + str(self.m)
        return str_

    def Calc(self, value = None):
        if value == None:
            value = self.TakeAmount()
            self.h = int(value) // 60
            self.m = int(value) % 60
            self.s = int(value) * 60
        else: 
            self.h = (int(value) // 60) // 60
            self.m = (int(value) // 60) % 60

    def TakeAmount(self) -> int:
        return int(self.ui.HS_Value.value())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OffTimer()
    window.Calc()

    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()

    sys.exit(app.exec())
