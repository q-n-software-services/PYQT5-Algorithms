from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QDialog, QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QApplication
from PyQt5.QtGui import QFont, QIcon, QPen
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import Qt, QPointF
import sys

class mylog(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Line Chart ")
        self.setWindowIcon(QIcon("burger.ico"))
        self.setStyleSheet("background-color:green")

        series = QLineSeries()
        series.append(-5, 25)
        series.append(-4, 16)
        series.append(-3, 9)
        series.append(-2, 4)
        series.append(-1, 1)
        series.append(0, 0)
        series.append(1, 1)
        series.append(2, 4)
        series.append(3, 9)
        series.append(4, 16)
        series.append(5, 25)

        # series << QPointF(11, 1) << QPointF(13, 3) << QPointF(17, 6) << QPointF(18, 3) << QPointF(20, 22)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Line Chart")

        chartview = QChartView(chart)

        vbox = QVBoxLayout()
        vbox.addWidget(chartview)

        self.setLayout(vbox)




app = QApplication(sys.argv)
window = mylog()
window.show()
sys.exit(app.exec_())