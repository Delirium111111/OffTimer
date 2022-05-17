# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Window.ui'
##
# Created by: Qt User Interface Compiler version 6.3.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QMainWindow,
                               QSizePolicy, QSlider, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 250)
        MainWindow.setMinimumSize(QSize(300, 250))
        MainWindow.setMaximumSize(QSize(300, 250))
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 291, 241))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LCD_Amount = QLCDNumber(self.verticalLayoutWidget)
        self.LCD_Amount.setObjectName(u"LCD_Amount")

        self.verticalLayout.addWidget(self.LCD_Amount)

        self.L_Value_text = QLabel(self.verticalLayoutWidget)
        self.L_Value_text.setObjectName(u"L_Value_text")
        font = QFont()
        font.setPointSize(16)
        self.L_Value_text.setFont(font)
        self.L_Value_text.setLayoutDirection(Qt.LeftToRight)
        self.L_Value_text.setScaledContents(False)
        self.L_Value_text.setAlignment(Qt.AlignCenter)
        self.L_Value_text.setWordWrap(False)

        self.verticalLayout.addWidget(self.L_Value_text)

        self.HS_Value = QSlider(self.verticalLayoutWidget)
        self.HS_Value.setObjectName(u"HS_Value")
        self.HS_Value.setMaximum(480)
        self.HS_Value.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.HS_Value)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"OffTimer", None))
        self.L_Value_text.setText(QCoreApplication.translate(
            "MainWindow", u"TextLabel", None))
    # retranslateUi
