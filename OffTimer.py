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
import PySide6

import qtmodern.styles
import qtmodern.windows

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QSystemTrayIcon, QMenu

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

    def SetUp(self):
        finish = QAction("Quit", self)
        finish.triggered.connect(self.closeEvent)

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

    def Calc(self, value=None):
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

    # TODO Сделать сворачивание в трей, а не закрытие программы
    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        self.hide()
        return super().closeEvent(event)


# TODO Сделать нормальное отображение тёмной темы
def ShowForm():
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = OffTimer()
    window.Calc()

    icon = QIcon(
        "C:\\Users\seryo\Documents\WorkSpace\Python\OffTimer\Icons\Icon.png")

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Creating the options
    menu = QMenu()
    option1 = QAction("Geeks for Geeks")
    option2 = QAction("GFG")
    menu.addAction(option1)
    menu.addAction(option2)

    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    tray.setContextMenu(menu)
    # qtmodern.styles.dark(app)
    # mw = qtmodern.windows.ModernWindow(window)

    # mw.show()
    # menu.aboutToShow.connect(ShowForm)
    # TODO Сделать открытие формы по клику на трей
    tray.activated.connect(ShowForm)
    sys.exit(app.exec())
