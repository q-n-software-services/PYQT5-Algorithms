from PyQt5.QtWidgets import QApplication, QLineEdit,QSpacerItem, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget
import sys, calendar, datetime
from PyQt5.QtGui import QFont, QIcon, QPainter, QPen, QBrush, QTextDocument, QPolygon

from PyQt5.QtCore import Qt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QSize, QTime, QTimer, QRect, QRectF, QPoint
import mysql.connector as mc
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 1100, 600)
        self.setWindowTitle("Painter_PyQt5")
        self.setWindowIcon(QIcon("burger.ico"))
        self.donedone()

    def donedone(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        self.lineedit = QLineEdit()
        self.label1 = QLabel("Database Name")
        hbox.addWidget(self.label1)
        hbox.addWidget(self.lineedit)

        vbox.addLayout(hbox)


        hbox2 = QHBoxLayout()
        self.btn1 = QPushButton("Create Database")
        self.btn1.clicked.connect(self.create_database)
        self.btn2 = QPushButton("Connect Database")
        self.btn2.clicked.connect(self.connect_database)
        hbox2.addWidget(self.btn1)
        hbox2.addWidget(self.btn2)

        vbox.addLayout(hbox2)
        self.label2 = QLabel("")

        vbox.addWidget(self.label2)
        self.setLayout(vbox)

    def create_database(self):
        try:
            mydb = mc.connect(
                host="https://demo.phpmyadmin.net/master-config/index.php?route=/server/databases",
                user="root",
                password=""
            )
            cursor = mydb.cursor()
            dbname = self.lineedit.text()
            self.label2.setText("Database {} created".format(dbname))

            cursor.execute("CREATE DATABASE {}".format(dbname))
        except mc.Error as e:
            self.label2.setText("Database creation failed")

    def connect_database(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="Muhammad Mohib"

            )

            self.label2.setText("There is a connection")

        except mc.Error as e:
            self.label2.setText("Error in Connection")












app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
