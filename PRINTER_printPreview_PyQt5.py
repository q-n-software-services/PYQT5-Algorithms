from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout,QTextEdit, QLCDNumber,QMessageBox, QPushButton, QCalendarWidget, QLabel, QWidget, QTableWidget, QTableWidgetItem
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

        btn1 = QPushButton("Print File")
        btn1.clicked.connect(self.Print)


        btn2 = QPushButton("Print Preview")
        btn2.clicked.connect(self.Print_Preview)

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()

        self.text = QTextEdit()


        vbox.addWidget(self.text)
        vbox.addLayout(hbox)

        # velow is code to print a file and can be modified to print all files in a folder

        '''handle = open("C:\\My data\\Text Document.txt", mode='r')
        line = handle.readline()

        while line != "":
            line = handle.readline()
            self.text.append(line)
            #c = c - 1
        btn2.click()'''




        self.setLayout(vbox)

    def Print(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.text.print_(printer)

    def Print_Preview(self):
        printer = QPrinter(QPrinter.HighResolution)
        preview_dialog = QPrintPreviewDialog(printer, self)
        preview_dialog.paintRequested.connect(self.preview)

        preview_dialog.exec_()

    def preview(self, printer):
        self.text.print_(printer)












app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
