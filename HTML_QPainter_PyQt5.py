from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QDialog,QComboBox,QSlider, QFontComboBox, QVBoxLayout, QHBoxLayout,QDial, QTextEdit, QLCDNumber,QMessageBox,QListWidget, QListWidgetItem, QListView, QPushButton, QCalendarWidget, QLabel, QWidget, QTableWidget, QTableWidgetItem
import sys, calendar, datetime
from PyQt5.QtGui import QFont, QIcon, QPainter, QPen, QBrush, QTextDocument

from PyQt5.QtCore import Qt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QSize, QTime, QTimer, QRect, QRectF
import time
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 1100, 600)
        self.setWindowTitle("Painter_PyQt5")
        self.setWindowIcon(QIcon("burger.ico"))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 12, Qt.SolidLine))

        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        document = QTextDocument()

        rect2 = QRectF(0, 0, 500, 500)
        document.setTextWidth(rect2.width())

        document.setHtml("<b>MUHAMMAD Mohib</b><i>Programming</i>"
                         "<font size='12' color='green'>This is a Test TEXT</font>")

        document.drawContents(painter, rect2)










app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
