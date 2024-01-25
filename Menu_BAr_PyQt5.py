from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QDialog,QComboBox,QSlider, QFontComboBox, QVBoxLayout, QHBoxLayout,QDial, QTextEdit, QLCDNumber,QMessageBox,QListWidget, QListWidgetItem, QListView, QPushButton, QCalendarWidget, QLabel, QWidget, QTableWidget, QTableWidgetItem
import sys, calendar, datetime
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QSize, QTime, QTimer
import time
from random import randint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle("Menu_PyQt5")
        self.setWindowIcon(QIcon("burger.ico"))

        self.create_main_menu()


    def create_main_menu(self):
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("File")

        new_action = QAction(QIcon('burger.ico'), 'New', self)
        new_action.setShortcut('ctrl+N')
        file_menu.addAction(new_action)

        save_action = QAction(QIcon('masjid.ico'), 'Save', self)
        save_action.setShortcut('ctrl+S')
        file_menu.addAction(save_action)

        file_menu.addSeparator()

        copy_action = QAction(QIcon('burger.ico'), 'Copy', self)
        copy_action.setShortcut('ctrl+C')
        file_menu.addAction(copy_action)

        paste_action = QAction(QIcon('masjid.ico'), 'Paste', self)
        paste_action.setShortcut('ctrl+V')
        file_menu.addAction(paste_action)

        cut_action = QAction(QIcon('burger.ico'), 'Cut', self)
        cut_action.setShortcut('ctrl+X')
        file_menu.addAction(cut_action)

        exit_action = QAction(QIcon('masjid.ico'), 'Exit', self)
        # exit_action.setShortcut('Alt+F4')
        file_menu.addAction(exit_action)
        exit_action.triggered.connect(self.close_window)



        hbox = QHBoxLayout()

    def close_window(self):
        self.close()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
