from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QDialog, QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QApplication
from PyQt5.QtGui import QFont, QIcon, QPen
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtCore import Qt, QPointF
import sys

class mylog(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Line Chart ")
        self.setWindowIcon(QIcon("burger.ico"))
        self.setStyleSheet("background-color:green")

        series = QPieSeries()
        series.setHoleSize(0.40)

        series.append("Protein 4.3%", 4.3)

        my_slice = series.append("Fat 15.6", 15.6)
        '''my_slice.setExploded(True)
        my_slice.setLabelVisible(True)'''

        series.append("Others 30%", 30)
        series.append("Carbs 57%", 57)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Donut Chart")
        chart.setTheme(QChart.ChartThemeBlueCerulean)

        chartview = QChartView(chart)

        vbox = QVBoxLayout()
        vbox.addWidget(chartview)

        self.setLayout(vbox)




app = QApplication(sys.argv)
window = mylog()
window.show()
sys.exit(app.exec_())