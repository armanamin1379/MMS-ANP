from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont


import sys
app = QtWidgets.QApplication(sys.argv)   

screen = app.primaryScreen()
size = screen.size()
class Matrix_wnw(object):
    def setupUi(self, MainWindow):

        screen_width = size.width()
        screen_height = size.height()


        width = int(screen_width * 0.651)  
        height = int(screen_height * 0.439)  

        MainWindow.resize(width, height)

        x = (screen_width - width) // 2  # مرکز پنجره روی محور افقی
        y = (screen_height - height) // 2  # مرکز پنجره روی محور عمودی


        MainWindow.move(x, y)

        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(QFont.Bold)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.final_lw = QtWidgets.QListWidget(self.centralwidget)
        
        self.final_lw.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")
        self.final_lw.setObjectName("final_lw")
        self.calculate_btn = QtWidgets.QPushButton(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(int(height * 0.025))
        font.setBold(True)
        font.setWeight(QFont.Bold)
        self.calculate_btn.setFont(font)
        self.calculate_btn.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")
        self.calculate_btn.setObjectName("calculate_btn")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(int(height * 0.025))
        font.setBold(True)
        font.setWeight(QFont.Bold)
        self.back_btn.setFont(font)
        self.final_lw.setFont(font)
        self.back_btn.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")
        self.back_btn.setObjectName("back_btn")
        self.matrix_tw = QtWidgets.QTableWidget(self.centralwidget)
        
        self.matrix_tw.setObjectName("tableWidget")
        self.matrix_tw.setColumnCount(6)
        self.matrix_tw.setRowCount(11)
        self.matrix_tw.setStyleSheet("QTableWidget::item::last-child {background-color: #32CC99; border: 0px; padding: 5px;} QHeaderView::section { color:white; background-color:#232326; } ")
        # self.matrix_tw.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.matrix_tw.setAlternatingRowColors(True)
        self.matrix_tw.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.matrix_tw.setShowGrid(True)
        self.matrix_tw.setGridStyle(QtCore.Qt.SolidLine)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.matrix_tw.setHorizontalHeaderItem(5, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.matrix_tw.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        for i in range(1, 11):
            self.technical_tw = QtWidgets.QComboBox()
            self.technical_tw.setStyleSheet("background-color: #20B2AA;")
            for j in range(1, 11):
                self.technical_tw.addItem(str(j))

            self.matrix_tw.setCellWidget(i, 2, self.technical_tw)


        self.final_lw.setGeometry(int(screen_width * 0.494), int(screen_height * 0.009), int(screen_width * 0.136), int(screen_height * 0.233))
        self.calculate_btn.setGeometry(int(screen_width * 0.575), int(screen_height * 0.287), int(screen_width * 0.05), int(screen_height * 0.04))
        self.back_btn.setGeometry(int(screen_width * 0.494), int(screen_height * 0.287), int(screen_width * 0.05), int(screen_height * 0.04))
        self.matrix_tw.setGeometry(int(screen_width * 0.010), int(screen_height * 0.010), int(screen_width * 0.469), int(screen_height * 0.407))

        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculate_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calculate_btn.setText(_translate("MainWindow", "Calculate"))
        self.back_btn.setText(_translate("MainWindow", "Back"))
        # method = ["Open Pit","Block Caving","Sublevel Stoping","Sublevel Caving","Long Wall Mining","Room And Pillar","Shrinkage Stoping","Cut And Fill","Top Slicing","Square Set Stoping"]
        item = self.matrix_tw.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Weight"))
        item = self.matrix_tw.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Open Pit"))
        item = self.matrix_tw.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Block Caving"))
        item = self.matrix_tw.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sublevel Stoping"))
        item = self.matrix_tw.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Sublevel Caving"))
        item = self.matrix_tw.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Long Wall Mining"))
        item = self.matrix_tw.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Room And Pillar"))
        item = self.matrix_tw.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Shrinkage Stoping"))
        item = self.matrix_tw.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Cut And Fill"))
        item = self.matrix_tw.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Top Slicing"))
        item = self.matrix_tw.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Square Set Stoping"))
        item = self.matrix_tw.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Rock Mechanic"))
        item = self.matrix_tw.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Geometry"))
        item = self.matrix_tw.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Technical"))
        item = self.matrix_tw.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Geology"))
        item = self.matrix_tw.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Economic"))
        item = self.matrix_tw.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Enviromental"))


if __name__ == "__main__":
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Matrix_wnw()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
