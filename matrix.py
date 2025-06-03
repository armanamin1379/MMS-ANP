from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

import sys
app = QtWidgets.QApplication(sys.argv)

# Get screen size for responsive UI
screen = app.primaryScreen()
size = screen.size()

class Matrix_wnw(object):
    def setupUi(self, MainWindow):
        screen_width = size.width()
        screen_height = size.height()

        # Calculate window size as a percentage of screen
        width = int(screen_width * 0.651)
        height = int(screen_height * 0.439)

        # Resize and center the window
        MainWindow.resize(width, height)
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        MainWindow.move(x, y)

        # Set base font for the window
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(QFont.Bold)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)

        # Central widget setup
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Final result list widget
        self.final_lw = QtWidgets.QListWidget(self.centralwidget)
        self.final_lw.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")
        self.final_lw.setObjectName("final_lw")

        # Calculate button
        self.calculate_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(int(height * 0.025))
        font.setBold(True)
        font.setWeight(QFont.Bold)
        self.calculate_btn.setFont(font)
        self.calculate_btn.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")
        self.calculate_btn.setObjectName("calculate_btn")

        # Back button
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setFont(font)
        self.final_lw.setFont(font)
        self.back_btn.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")
        self.back_btn.setObjectName("back_btn")

        # Matrix table widget setup
        self.matrix_tw = QtWidgets.QTableWidget(self.centralwidget)
        self.matrix_tw.setObjectName("tableWidget")
        self.matrix_tw.setColumnCount(6)
        self.matrix_tw.setRowCount(11)
        self.matrix_tw.setStyleSheet("QTableWidget::item::last-child {background-color: #32CC99; border: 0px; padding: 5px;} QHeaderView::section { color:white; background-color:#232326; } ")
        self.matrix_tw.setAlternatingRowColors(True)
        self.matrix_tw.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.matrix_tw.setShowGrid(True)
        self.matrix_tw.setGridStyle(QtCore.Qt.SolidLine)

        # Set vertical and horizontal header items
        for i in range(11):
            self.matrix_tw.setVerticalHeaderItem(i, QtWidgets.QTableWidgetItem())
        for j in range(6):
            self.matrix_tw.setHorizontalHeaderItem(j, QtWidgets.QTableWidgetItem())

        MainWindow.setCentralWidget(self.centralwidget)

        # Set cursor type for table
        self.matrix_tw.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Add combo boxes to "Technical" column
        for i in range(1, 11):
            combo_box = QtWidgets.QComboBox()
            combo_box.setStyleSheet("background-color: #20B2AA;")
            for j in range(1, 11):
                combo_box.addItem(str(j))
            self.matrix_tw.setCellWidget(i, 2, combo_box)

        # Set geometry for widgets
        self.final_lw.setGeometry(int(screen_width * 0.494), int(screen_height * 0.009), int(screen_width * 0.136), int(screen_height * 0.233))
        self.calculate_btn.setGeometry(int(screen_width * 0.575), int(screen_height * 0.287), int(screen_width * 0.05), int(screen_height * 0.04))
        self.back_btn.setGeometry(int(screen_width * 0.494), int(screen_height * 0.287), int(screen_width * 0.05), int(screen_height * 0.04))
        self.matrix_tw.setGeometry(int(screen_width * 0.010), int(screen_height * 0.010), int(screen_width * 0.469), int(screen_height * 0.407))

        # Set cursor for buttons
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculate_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Apply translations and labels
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calculate_btn.setText(_translate("MainWindow", "Calculate"))
        self.back_btn.setText(_translate("MainWindow", "Back"))

        # Set vertical header labels for mining methods
        vertical_labels = ["Weight", "Open Pit", "Block Caving", "Sublevel Stoping", "Sublevel Caving",
                           "Long Wall Mining", "Room And Pillar", "Shrinkage Stoping", "Cut And Fill",
                           "Top Slicing", "Square Set Stoping"]
        for i, label in enumerate(vertical_labels):
            self.matrix_tw.verticalHeaderItem(i).setText(_translate("MainWindow", label))

        # Set horizontal header labels for criteria
        horizontal_labels = ["Rock Mechanic", "Geometry", "Technical", "Geology", "Economic", "Enviromental"]
        for i, label in enumerate(horizontal_labels):
            self.matrix_tw.horizontalHeaderItem(i).setText(_translate("MainWindow", label))


if __name__ == "__main__":
    # Launch the application
    MainWindow = QtWidgets.QMainWindow()
    ui = Matrix_wnw()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
