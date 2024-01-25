from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QDialog, QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QApplication
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis
import sys

class mylog(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Percent Bar Chart ")
        self.setWindowIcon(QIcon("burger.ico"))


        self.setStyleSheet("background-color:green")

        # names of contributions in a single bar
        set1 = QBarSet("Mohib")
        set2 = QBarSet("Hassaan")
        set3 = QBarSet("Ahmad")
        set4 = QBarSet("Maaz")
        set5 = QBarSet("Muzammil")

        # relative or discrete data of each contribution to that bar / set
        set1 << 1 << 2 << 3 << 4 << 5 << 6
        set2 << 5 << 0 << 0 << 4 << 0 << 7
        set3 << 3 << 5 << 8 << 13 << 8 << 5
        set4 << 5 << 6 << 7 << 3 << 4 << 5
        set5 << 9 << 7 << 5 << 3 << 1 << 2

        series = QPercentBarSeries()
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)
        series.append(set5)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Bar-Chart Percent")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # X-axis labels     
        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        chartview = QChartView(chart)
        vbox = QVBoxLayout()
        vbox.addWidget(chartview)

        self.setLayout(vbox)









app = QApplication(sys.argv)
window = mylog()
window.show()
sys.exit(app.exec_())