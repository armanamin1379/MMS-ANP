from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
import sys

# Create the QApplication object needed to run any PyQt application
app = QtWidgets.QApplication(sys.argv)

# Get screen dimensions for responsive sizing
screen = app.primaryScreen()
size = screen.size()

# Define the UI class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Calculate main window dimensions relative to screen size
        screen_width = size.width()
        screen_height = size.height()
        width = int(screen_width * 0.45)
        height = int(screen_height * 0.324)

        # Set main window size and font
        MainWindow.resize(width, height)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)

        # Central widget for the main window
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # --- Apply Button ---
        self.apply_btn = QtWidgets.QPushButton(self.centralwidget)
        window_width = MainWindow.width()
        window_height = MainWindow.height()

        # Calculate button geometry relative to window size
        btn_x = int(window_width * 0.036)
        btn_y = int(window_height * 0.743)
        btn_w = int(window_width * 0.0857)
        btn_h = int(window_height * 0.0886)
        self.apply_btn.setGeometry(QtCore.QRect(btn_x, btn_y, btn_w, btn_h))

        # Set font and style for Apply button
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(int(height * 0.032))
        font.setBold(True)
        font.setWeight(QFont.Bold)
        self.apply_btn.setFont(font)
        self.apply_btn.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")
        self.apply_btn.setObjectName("apply_btn")

        # --- ComboBoxes for inputs ---
        self.depth_cb = QtWidgets.QComboBox(self.centralwidget)
        self.depth_cb.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")

        self.ore_type_cb = QtWidgets.QComboBox(self.centralwidget)
        self.ore_type_cb.setFont(font)
        self.ore_type_cb.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")

        self.dip_cb = QtWidgets.QComboBox(self.centralwidget)
        self.dip_cb.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")

        self.strength_of_ore_cb = QtWidgets.QComboBox(self.centralwidget)
        self.strength_of_ore_cb.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")

        self.strength_of_country_rock_cb = QtWidgets.QComboBox(self.centralwidget)
        self.strength_of_country_rock_cb.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")

        self.distribution_cb = QtWidgets.QComboBox(self.centralwidget)
        self.distribution_cb.setFont(font)
        self.distribution_cb.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")

        self.thickness_cb = QtWidgets.QComboBox(self.centralwidget)
        self.thickness_cb.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")

        self.shape_cb = QtWidgets.QComboBox(self.centralwidget)
        self.shape_cb.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")

        # --- Labels for each input ---
        def create_label(name):
            label = QtWidgets.QLabel(self.centralwidget)
            label.setFont(font)
            label.setLayoutDirection(QtCore.Qt.LeftToRight)
            label.setAlignment(QtCore.Qt.AlignLeft)
            label.setObjectName(name)
            return label

        self.strength_of_country_rock_lb = create_label("strength_of_country_rock_lb")
        self.distribution_lb = create_label("distribution_lb")
        self.dip_lb = create_label("dip_lb")
        self.depth_lb = create_label("depth_lb")
        self.shape_lb = create_label("shape_lb")
        self.strength_of_ore_lb = create_label("strength_of_ore_lb")
        self.thickness_lb = create_label("thickness_lb")
        self.ore_type_lb = create_label("ore_type_lb")

        # --- Image Label ---
        self.pic_lbl = QtWidgets.QLabel(self.centralwidget)
        self.pic_lbl.setAutoFillBackground(True)
        self.pic_lbl.setText("")
        self.pic_lbl.setTextFormat(QtCore.Qt.PlainText)
        self.pic_lbl.setPixmap(QtGui.QPixmap(""))  # Placeholder for image
        self.pic_lbl.setScaledContents(True)
        self.pic_lbl.setObjectName("label")

        # --- Next Button ---
        self.next_btn = QtWidgets.QPushButton(self.centralwidget)
        btn2_x = int(MainWindow.width() * 0.329)
        btn2_y = int(MainWindow.height() * 0.743)
        btn2_w = int(MainWindow.width() * 0.0857)
        btn2_h = int(MainWindow.height() * 0.0886)
        self.next_btn.setGeometry(QtCore.QRect(btn2_x, btn2_y, btn2_w, btn2_h))

        self.next_btn.setHidden(True)
        self.next_btn.setFont(font)
        self.next_btn.setStyleSheet("background-color: #32CC99; border-radius:5px ; color:white;")
        self.next_btn.setObjectName("next_btn")

        # --- Set Fonts and Cursor for ComboBoxes ---
        for cb in [
            self.shape_cb, self.depth_cb, self.thickness_cb, self.dip_cb,
            self.strength_of_country_rock_cb, self.strength_of_ore_cb,
            self.distribution_cb, self.ore_type_cb
        ]:
            cb.setFont(font)
            cb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # --- Set Geometry for all ComboBoxes ---
        w = MainWindow.width()
        h = MainWindow.height()
        self.depth_cb.setGeometry(int(w*0.036), int(h*0.257), int(w*0.25), int(h*0.085))
        self.ore_type_cb.setGeometry(int(w*0.036), int(h*0.6), int(w*0.25), int(h*0.085))
        self.dip_cb.setGeometry(int(w*0.329), int(h*0.091), int(w*0.25), int(h*0.085))
        self.strength_of_ore_cb.setGeometry(int(w*0.329), int(h*0.257), int(w*0.25), int(h*0.085))
        self.strength_of_country_rock_cb.setGeometry(int(w*0.329), int(h*0.431), int(w*0.25), int(h*0.085))
        self.distribution_cb.setGeometry(int(w*0.329), int(h*0.6), int(w*0.25), int(h*0.085))
        self.thickness_cb.setGeometry(int(w*0.036), int(h*0.428), int(w*0.25), int(h*0.085))
        self.shape_cb.setGeometry(int(w*0.036), int(h*0.091), int(w*0.25), int(h*0.085))

        # --- Set Geometry for all Labels ---
        self.strength_of_country_rock_lb.setGeometry(int(w*0.329), int(h*0.343), int(w*0.9), int(h*0.085))
        self.distribution_lb.setGeometry(int(w*0.329), int(h*0.515), int(w*0.3), int(h*0.085))
        self.dip_lb.setGeometry(int(w*0.329), int(h*0.011), int(w*0.143), int(h*0.085))
        self.depth_lb.setGeometry(int(w*0.036), int(h*0.175), int(w*0.2), int(h*0.085))
        self.shape_lb.setGeometry(int(w*0.036), int(h*0.0085), int(w*0.2), int(h*0.085))
        self.strength_of_ore_lb.setGeometry(int(w*0.329), int(h*0.175), int(w*0.214), int(h*0.085))
        self.thickness_lb.setGeometry(int(w*0.036), int(h*0.343), int(w*0.2), int(h*0.085))
        self.ore_type_lb.setGeometry(int(w*0.036), int(h*0.514), int(w*0.2), int(h*0.085))

        # --- Set Geometry for Image ---
        self.pic_lbl.setGeometry(int(w*0.625), int(h*0.085), int(w*0.350), int(h*0.700))

        # Set button cursors
        self.next_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.apply_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Setup window translations (UI text)
        self.retranslateUi(MainWindow)

        # Auto-connect slots to signals
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.apply_btn.setText(_translate("MainWindow", "Apply"))
        self.strength_of_country_rock_lb.setText(_translate("MainWindow", "Strength Of Country Rock"))
        self.dip_lb.setText(_translate("MainWindow", "Dip"))
        self.distribution_lb.setText(_translate("MainWindow", "Ore Grade Distribution"))
        self.depth_lb.setText(_translate("MainWindow", "Depth"))
        self.shape_lb.setText(_translate("MainWindow", "Orebody Shape"))
        self.strength_of_ore_lb.setText(_translate("MainWindow", "Strength Of Ore"))
        self.thickness_lb.setText(_translate("MainWindow", "Thickness"))
        self.ore_type_lb.setText(_translate("MainWindow", "Ore Type"))
        self.next_btn.setText(_translate("MainWindow", "Next"))

# Main execution block
if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
