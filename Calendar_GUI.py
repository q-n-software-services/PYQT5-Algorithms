from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLCDNumber, QPushButton, QCalendarWidget, QLabel
import sys, calendar, datetime
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, QTime, QTimer
import time
from random import randint




class Window(QDialog):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle("QLCDNubmer_PyQt5")
        self.setWindowIcon(QIcon("burger.ico"))

        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)


        self.label = QLabel("Blank Label")
        self.label.setFont(QFont("Sanserif", 22))
        self.label.setStyleSheet("background-color:yellow")
        self.calendar.selectionChanged.connect(self.calendar_date)

        vbox.addWidget(self.calendar)
        vbox.addWidget(self.label)


        self.setLayout(vbox)

    def calendar_date(self):
        date_selected = self.calendar.selectedDate()
        date_in_string = str(date_selected.toPyDate())



        self.label.setText("Date is: " + date_in_string )







app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
