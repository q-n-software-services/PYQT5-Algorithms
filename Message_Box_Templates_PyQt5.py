from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLCDNumber,QMessageBox, QPushButton, QCalendarWidget, QLabel, QWidget, QTableWidget, QTableWidgetItem
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

        self.create_messageBox()



    def create_messageBox(self):
        hbox = QHBoxLayout()

        btn1 = QPushButton("Warning")
        btn1.clicked.connect(self.warning_message)

        btn2 = QPushButton("Information")
        btn2.clicked.connect(self.information_msg)

        btn3 = QPushButton("About")
        btn3.clicked.connect(self.about_msg)

        btn4 = QPushButton("Yes / No")
        btn4.clicked.connect(self.multi_choice_msgBox)


        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        vbox = QVBoxLayout()

        self.label = QLabel("Text")
        self.label.setFont(QFont("Sanserif", 22))

        vbox.addLayout(hbox)
        vbox.addWidget(self.label)



        self.setLayout(vbox)

    def warning_message(self):
        QMessageBox.warning(self, "Title = Warning", "Message = This is a Warning Message")

    def information_msg(self):
        QMessageBox.information(self, "Title = Information", "Text = This is Information")

    def about_msg(self):
        QMessageBox.about(self, "Title = about", "Text = This is about")

    def multi_choice_msgBox(self):
        message = QMessageBox.question(self, "Choice Message", "Do You Like Python ? ", QMessageBox.Yes |QMessageBox.No)

        if message == QMessageBox.Yes:
            self.label.setText("Yes, I like Python")
        elif message == QMessageBox.No:
            self.label.setText("NO, I don't like Python")











app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
