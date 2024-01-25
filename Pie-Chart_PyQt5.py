from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QDialog, QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QApplication
from PyQt5.QtGui import QFont, QIcon, QPen
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtCore import Qt
import sys

class mylog(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Pie Chart ")
        self.setWindowIcon(QIcon("burger.ico"))
        self.setStyleSheet("background-color:green")

        series = QPieSeries()
        series.append("Apple", 80)
        series.append("Banana", 70)
        series.append("Pear", 50)
        series.append("Melon", 80)
        series.append("Water Melon", 30)

        my_slice1 = series.slices()[0]
        my_slice1.setExploded(True)
        my_slice1.setLabelVisible(True)
        my_slice1.setPen(QPen(Qt.red, 4))
        my_slice1.setBrush(Qt.yellow)

        '''my_slice2 = series.slices()[1]
        my_slice2.setExploded(True)
        my_slice2.setLabelVisible(True)

        my_slice3 = series.slices()[2]
        my_slice3.setExploded(True)
        my_slice3.setLabelVisible(True)

        my_slice4 = series.slices()[3]
        my_slice4.setExploded(True)
        my_slice4.setLabelVisible(True)

        my_slice5 = series.slices()[4]
        my_slice5.setExploded(True)
        my_slice5.setLabelVisible(True)'''


        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Fruits Pie Chart")

        chartview = QChartView(chart)

        vbox = QVBoxLayout()
        vbox.addWidget(chartview)

        self.setLayout(vbox)




app = QApplication(sys.argv)
window = mylog()
window.show()
sys.exit(app.exec_())