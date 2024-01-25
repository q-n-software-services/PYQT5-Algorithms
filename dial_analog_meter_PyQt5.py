from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout,QDial, QTextEdit, QLCDNumber,QMessageBox,QListWidget, QListWidgetItem, QListView, QPushButton, QCalendarWidget, QLabel, QWidget, QTableWidget, QTableWidgetItem
import sys, calendar, datetime
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QSize, QTime, QTimer
import time
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle("Message_Box_PyQt5")
        self.setWindowIcon(QIcon("burger.ico"))

        self.create_dial_box()

    def create_dial_box(self):
        self.dial = QDial()
        self.dial.setStyleSheet("background-color:green")
        self.dial.setMaximum(360)
        self.dial.setMinimum(180)
        self.dial.valueChanged.connect(self.value)




        vbox = QVBoxLayout()
        self.label = QLabel("Hello")
        self.label.setFont(QFont("sanserif", 22))

        vbox.addWidget(self.dial)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def value(self):
        valuu = self.dial.value()

        self.label.setText("value is:\t\t\n" + str(valuu))
        # self.dial.setValue(90)






app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
