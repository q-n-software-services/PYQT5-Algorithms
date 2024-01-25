from PyQt5.QtWidgets import QApplication, QDialog,QComboBox, QFontComboBox, QVBoxLayout, QHBoxLayout,QDial, QTextEdit, QLCDNumber,QMessageBox,QListWidget, QListWidgetItem, QListView, QPushButton, QCalendarWidget, QLabel, QWidget, QTableWidget, QTableWidgetItem
import sys, calendar, datetime
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QSize, QTime, QTimer
import time
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(0, 0, 1350, 750)
        self.setWindowTitle("Drop_Down_List_PyQt5")
        self.setWindowIcon(QIcon("burger.ico"))

        self.create_combo_box()

    def create_combo_box(self):
        vbox = QVBoxLayout()
        self.cbox = QComboBox()

        self.cbox.addItem("Python")
        self.cbox.addItem("Java")
        self.cbox.addItem("JavaScript")
        self.cbox.addItem("SQL")
        self.cbox.addItem("Swift")
        self.cbox.currentIndexChanged.connect(self.hovered)

        self.label = QLabel("")

        vbox.addWidget(self.cbox)
        vbox.addWidget(self.label)

        self.setLayout(vbox)



    def hovered(self):
        text = self.cbox.currentText()
        self.label.setText("" + str(text))
        self.label.setFont(QFont("Sanserif", 48))
        self.label.setStyleSheet("color:green")





app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
