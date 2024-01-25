from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLCDNumber, QPushButton, QCalendarWidget, QLabel, QWidget, QTableWidget, QTableWidgetItem
import sys, calendar, datetime
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, QTime, QTimer
import time
from random import randint




class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle("QLCDNubmer_PyQt5")
        self.setWindowIcon(QIcon("burger.ico"))

        self.create_tables()

    def create_tables(self):
        vbox = QVBoxLayout()

        table_widget = QTableWidget()
        table_widget.setRowCount(3)
        table_widget.setColumnCount(3)

        table_widget.setItem(0, 0, QTableWidgetItem("Name"))
        table_widget.setItem(0, 1, QTableWidgetItem("Email"))
        table_widget.setItem(0, 2, QTableWidgetItem("Phone "))

        table_widget.setItem(1, 0, QTableWidgetItem("MOHIB"))
        table_widget.setItem(1, 1, QTableWidgetItem("mmohib.me13scme"))
        table_widget.setItem( 1,  2, QTableWidgetItem("1227292"))

        table_widget.setItem(2, 0, QTableWidgetItem("Hassaan"))
        table_widget.setItem(2, 1, QTableWidgetItem("mhassaan.me16scme"))
        table_widget.setItem(2, 2, QTableWidgetItem("22922005"))

        '''table_widget.setItem(3, 0, QTableWidgetItem("Bilal"))
        table_widget.setItem(3, 1, QTableWidgetItem("bilal.me31scme"))
        table_widget.setItem(3, 2, QTableWidgetItem("2154879"))'''

        vbox.addWidget(table_widget)


        self.setLayout(vbox)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
