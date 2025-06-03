from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidgetItem

from os import path
import numpy as np
import sqlite3
import page, matrix
import sys




app = QApplication(sys.argv)

#    ROCK MECK  GEOMETRY  TECh  GEOLOGY  ECONOMIC  ENV
W = [3.67     , 2.92    , 1.71,   0.73  , 0.49   , 0.45]

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = page.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        conn = sqlite3.connect(path.dirname(__file__) + "/data.db")


        cur=conn.cursor()
        cur.execute("SELECT DISTINCT shape from methods ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.shape_cb.addItem(i[0])

        cur.execute("SELECT DISTINCT depth from methods ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.depth_cb.addItem(i[0])

        cur.execute("SELECT DISTINCT thickness from methods ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.thickness_cb.addItem(i[0])

        cur.execute("SELECT DISTINCT dip from methods ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.dip_cb.addItem(i[0])

        cur.execute("SELECT DISTINCT strengthofore from methods ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.strength_of_ore_cb.addItem(i[0])

        cur.execute("SELECT DISTINCT strengthofcountryrock from methods ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.strength_of_country_rock_cb.addItem(i[0])

        cur.execute("SELECT DISTINCT oretype from weights ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.ore_type_cb.addItem(i[0])


        cur.execute("SELECT DISTINCT distribution from geology ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.distribution_cb.addItem(i[0])
        

        conn.close()

        self.ui.shape_cb.currentTextChanged.connect(lambda : self.change_shape())
        self.ui.thickness_cb.currentTextChanged.connect(lambda : self.change_thickness())
        self.ui.apply_btn.clicked.connect(self.apply)
        
    def change_shape(self):
        shape = self.ui.shape_cb.currentText()
        conn = sqlite3.connect(path.dirname(__file__) + "/data.db")
        cur=conn.cursor()
        self.ui.thickness_cb.clear()
        sql = "SELECT DISTINCT thickness from methods WHERE shape= ?"
        val = (shape,)
        cur.execute(sql, val)
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.thickness_cb.addItem(i[0])

        thickness = self.ui.thickness_cb.currentText()
        self.ui.dip_cb.clear()
        sql = "SELECT DISTINCT dip from methods WHERE shape= ? and thickness= ?"
        val = (shape, thickness)
        cur.execute(sql, val)
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.dip_cb.addItem(i[0])

        conn.close()

    def change_thickness(self):
        shape = self.ui.shape_cb.currentText()
        conn = sqlite3.connect(path.dirname(__file__) + "/data.db")
        cur=conn.cursor()

        thickness = self.ui.thickness_cb.currentText()
        self.ui.dip_cb.clear()
        sql = "SELECT DISTINCT dip from methods WHERE shape= ? and thickness= ?"
        val = (shape, thickness)
        cur.execute(sql, val)
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.dip_cb.addItem(i[0])

        conn.close()

    def apply(self):
        shape = self.ui.shape_cb.currentText()
        depth = self.ui.depth_cb.currentText()
        thickness = self.ui.thickness_cb.currentText()
        dip = self.ui.dip_cb.currentText()
        ore_type = self.ui.ore_type_cb.currentText()
        distribution = self.ui.distribution_cb.currentText()
        strength_of_country_rock= self.ui.strength_of_country_rock_cb.currentText()
        strength_of_ore = self.ui.strength_of_ore_cb.currentText()
        
        
        if thickness == "Very Narrow":
            thickness = "VN"

        elif thickness == "Very Thick":
            thickness = "VT"
        
        else:
            thickness = thickness[0]

        print(path.dirname(__file__) + "/pictures/{}-{}-{}-{}.png".format(shape[0], depth[0], thickness, dip[0] ) )

        self.ui.pic_lbl.setPixmap(QtGui.QPixmap(path.dirname(__file__) + "/pictures/{}-{}-{}-{}.png".format(shape[0], depth[0], thickness, dip[0] )))

        self.ui.next_btn.setHidden(False)
        thickness = self.ui.thickness_cb.currentText()
        self.ui.next_btn.clicked.connect(lambda : self.next(ore_type, strength_of_country_rock, strength_of_ore, shape, dip, depth, thickness, distribution))
        
    def next(self, ore_type, strength_of_country_rock, strength_of_ore, shape, dip, depth, thickness, distribution):
        self.ui = matrix.Matrix_wnw()
        self.ui.setupUi(self)

        conn = sqlite3.connect(path.dirname(__file__) + "/data.db")
        cur=conn.cursor()

        sql = "SELECT * from weights WHERE oretype= ? "
        val = (ore_type,)
        cur.execute(sql, val)
        myresult = cur.fetchall()
        counter = 0
        myresult = [i for i in myresult]
        for i in myresult:
            for j in i :
                if counter not in [0, 7]:
                    item = QTableWidgetItem(str(j))
                    item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.ui.matrix_tw.setItem(0, counter - 1 , item)
                counter += 1

        methods = ["Open Pit","Block Caving","Sublevel Stoping","Sublevel Caving","Long Wall Mining","Room And Pillar","Shrinkage Stoping","Cut And Fill","Top Slicing","Square Set Stoping"]
        for method in methods:
            ind_method = methods.index(method)
            # if (method in result) :
            if strength_of_country_rock == "Destructible":
                strength_of_country_rock = "Weak"
            sql = "SELECT rockmechanics from rockmechanics WHERE method= ? AND strengthofcountryrock= ? AND strengthofore= ?  "
            val = (method, strength_of_country_rock, strength_of_ore )
            cur.execute(sql, val)
            myresult = cur.fetchall()
            weight = [i[0] for i in myresult]
            item = QTableWidgetItem(str(weight[0]))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.ui.matrix_tw.setItem(ind_method + 1, 0 , item)

            sql = "SELECT weight from geometry WHERE method= ? AND shape= ? AND dip= ? AND Thickness= ? AND depth= ?"
            val = (method, shape , dip, thickness, depth )
            cur.execute(sql, val)
            myresult = cur.fetchall()
            weight = [i[0] for i in myresult]
            item = QTableWidgetItem(str(weight[0]))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.ui.matrix_tw.setItem(ind_method + 1, 1 , item)

            sql = "SELECT weight from geology WHERE method= ? AND distribution= ? "
            val = (method, distribution )
            cur.execute(sql, val)
            myresult = cur.fetchall()
            weight = [i[0] for i in myresult]
            item = QTableWidgetItem(str(weight[0]))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.ui.matrix_tw.setItem(ind_method + 1, 3 , item)

            sql = "SELECT weight from economic WHERE method= ? "
            val = (method, )
            cur.execute(sql, val)
            myresult = cur.fetchall()
            weight = [i[0] for i in myresult]
            item = QTableWidgetItem(str(weight[0]))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.ui.matrix_tw.setItem(ind_method + 1, 4 , item)

            sql = "SELECT weight from enviroment WHERE method= ? "
            val = (method, )
            cur.execute(sql, val)
            myresult = cur.fetchall()
            weight = [i[0] for i in myresult]
            item = QTableWidgetItem(str(weight[0]))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.ui.matrix_tw.setItem(ind_method + 1, 5 , item)

        conn.close()

        if strength_of_country_rock == "Weak" :
                strength_of_country_rock = "Destructible"

        self.ui.back_btn.clicked.connect(lambda : self.back(ore_type, strength_of_country_rock, strength_of_ore, shape, dip, depth, thickness, distribution))
        self.ui.calculate_btn.clicked.connect(self.calculate)

    def back(self, ore_type, strength_of_country_rock, strength_of_ore, shape, dip, depth, thickness, distribution):
        self.close()
        self.__init__()

        self.ui.ore_type_cb.setCurrentText(ore_type)
        self.ui.strength_of_country_rock_cb.setCurrentText(strength_of_country_rock)
        self.ui.strength_of_ore_cb.setCurrentText(strength_of_ore)
        self.ui.shape_cb.setCurrentText(shape)
        self.ui.dip_cb.setCurrentText(dip)
        self.ui.depth_cb.setCurrentText(depth)
        self.ui.thickness_cb.setCurrentText(thickness)
        self.ui.distribution_cb.setCurrentText(distribution)

    def calculate(self):
        self.ui.final_lw.clear()
        normed_matrix =  [[0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],]
        
        matrix =  [[0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],
                        [0  , 0  , 0  , 0  , 0, 0  ],]
        
        
        normed_w = [[0  , 0  , 0  , 0  , 0, 0  ],]
        
        for row in range(11):
            for column in range(6):
                if row == 0 :
                    normed_w[row][column] = float(self.ui.matrix_tw.item(row, column).text())

                elif column == 2:
                    matrix[row - 1][column] =  int(self.ui.matrix_tw.cellWidget(row, column).currentText())
                   

                else:
                    try:
                        if float(self.ui.matrix_tw.item(row, column).text()) > 0 :
                            matrix[row - 1][column] = float(self.ui.matrix_tw.item(row, column).text())

                        else:
                            matrix[row - 1][column] = 0

                    except AttributeError or ValueError:
                        matrix[row - 1][column] = 1


        normed_w = np.array(normed_w) 
        sum_w = sum(normed_w[0])
        for i in range(6):
                normed_w[0][i] = (normed_w[0][i]) / (sum_w)
        
        
        matrix = np.array(matrix) 
        # print(matrix)
        matrix = matrix.transpose() 
        
        for row in range(6):
            for column in range(10):
                normed_matrix[column][row] = (matrix[row][column]) / (sum(matrix[row]))

        normed_matrix = np.array(normed_matrix) 
        # print(normed_matrix)

        n = 17

        supermatix = [list(0 for j in range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]
        result = normed_matrix
        result = np.array(result) 

    
        for i in range(1, 7):
            supermatix[i][0] = normed_w[0][i - 1]



        for i in range(7, 17):
            for j in range(1, 7):
                supermatix[i][j] = result[i - 7][j - 1]

        for i in range(7, 17):
            for j in range(7, 17):
                if i == j:
                    supermatix[i][j] = 1

        supermatix = np.array(supermatix) 
        result = np.dot(supermatix ,supermatix )
        
        


 
        method = ["Open Pit","Block Caving","Sublevel Stoping","Sublevel Caving","Long Wall Mining","Room And Pillar","Shrinkage Stoping","Cut And Fill","Top Slicing","Square Set Stoping"]
        


        best_methods = [result[i + 7][0] for i in range(10)]
        best_methods.sort(reverse=True)
        
        for i in range(5):
            for j in range(10):
                if best_methods[i] == result[j + 7][0]:
                    self.ui.final_lw.addItem("{} - {} : {}".format(i + 1, method[j], round(best_methods[i], 3 )))
            














w = MainWindow()
w.show()
app.exec()