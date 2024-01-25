from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout,QTextEdit, QLCDNumber,QMessageBox,QListWidget, QListWidgetItem, QListView, QPushButton, QCalendarWidget, QLabel, QWidget, QTableWidget, QTableWidgetItem
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

        self.create_list_widget()

    def create_list_widget(self):
        vbox = QVBoxLayout()

        self.list_widget = QListWidget()

        self.list_widget.insertItem(0, "PYTHON")
        self.list_widget.insertItem(1, "JAVASCRIPT")
        self.list_widget.insertItem(2, "SQL")
        self.list_widget.insertItem(3, "SWIFT")
        self.list_widget.insertItem(4, "JAVA")
        self.list_widget.clicked.connect(self.item_clicked)

        self.list_widget.setStyleSheet("background-color:pink")
        self.list_widget.setFont(QFont("Sanserif", 14))

        self.label = QLabel("")
        self.label.setFont(QFont("sanserif", 15))
        self.label.setStyleSheet("background-color:yellow")

        vbox.addWidget(self.list_widget)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def item_clicked(self):
        item = self.list_widget.currentItem()
        self.label.setText("You have selected:\t" + str(item.text()))







app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
