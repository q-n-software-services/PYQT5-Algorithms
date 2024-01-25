from PyQt5.QtWidgets import QApplication, QDialog,QComboBox,QSlider, QFontComboBox, QVBoxLayout, QHBoxLayout,QDial, QTextEdit, QLCDNumber,QMessageBox,QListWidget, QListWidgetItem, QListView, QPushButton, QCalendarWidget, QLabel, QWidget, QTableWidget, QTableWidgetItem
import sys, calendar, datetime
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QSize, QTime, QTimer
import time
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle("Drop_Down_List_PyQt5")
        self.setWindowIcon(QIcon("burger.ico"))

        hbox = QHBoxLayout()

        self.slider = QSlider()

        self.slider.setOrientation(Qt.Horizontal)
        # self.slider.setStyleSheet("background-color:blue")
        self.setStyleSheet("background-color:rgb(85, 255, 255)")
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(12)
        self.slider.setMaximum(92)
        self.slider.valueChanged.connect(self.movers)

        self.label = QLabel("Hello")
        self.label.setFont(QFont("Sanserif", 22))
        self.label.setStyleSheet("color:red")

        hbox.addWidget(self.label)
        hbox.addWidget(self.slider)

        self.setLayout(hbox)

    def movers(self):
        text = self.slider.value()
        self.label.setText(str(text))




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
