# ------------------------------------------------------
# #  # # # # # # # Test.py # # # # # # # # # # # # # # #
# Create by Delirium https://github.com/Delirium111111
# # # # # # # # # # # # Tue May 17 2022 # # # # # # # # # # # #
# ------------------------------------------------------

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QSystemTrayIcon, QMenu

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("C:\\Users\seryo\Documents\WorkSpace\Python\OffTimer\Icons\Icon.png")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()
action = QAction("A menu item")
menu.addAction(action)

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

app.exec_()