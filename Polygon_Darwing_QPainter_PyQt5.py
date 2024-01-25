from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QDialog,QComboBox,QSlider, QFontComboBox, QVBoxLayout, QHBoxLayout,QDial, QTextEdit, QLCDNumber,QMessageBox,QListWidget, QListWidgetItem, QListView, QPushButton, QCalendarWidget, QLabel, QWidget, QTableWidget, QTableWidgetItem
import sys, calendar, datetime
from PyQt5.QtGui import QFont, QIcon, QPainter, QPen, QBrush, QTextDocument, QPolygon

from PyQt5.QtCore import Qt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QSize, QTime, QTimer, QRect, QRectF, QPoint
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
        painter.setPen(QPen(Qt.green, 5, Qt.SolidLine))

        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        for i in range(4):
            x = (100 * i) - 100 + (170 * i)
            y = 50

            points = QPolygon([
                QPoint(250 + x, 50 + y),
                QPoint(300 + x, 150 + y),
                QPoint(400 + x, 150 + y),
                QPoint(320 + x, 200 + y),
                QPoint(350 + x, 300 + y),
                QPoint(250 + x, 240 + y),
                QPoint(150 + x, 300 + y),
                QPoint(180 + x, 200 + y),
                QPoint(100 + x, 150 + y),
                QPoint(200 + x, 150 + y)
            ])

            painter.drawPolygon(points)










app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
