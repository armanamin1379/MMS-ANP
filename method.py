# Import necessary PyQt5 classes for GUI
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

# Import standard and external libraries
from os import path
import numpy as np
import sqlite3
import page, matrix  # Custom modules for GUI layout and calculations
import sys

# Initialize the Qt Application
app = QApplication(sys.argv)

# Define the main window class
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        # Load the UI design from page.py
        self.ui = page.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()  # Display the GUI window

        # Connect to the local SQLite3 database (data.db)
        conn = sqlite3.connect(path.dirname(__file__) + "/data.db")
        cur = conn.cursor()

        # Populate combo box with unique values from 'shape' column in 'methods' table
        cur.execute("SELECT DISTINCT shape from methods ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.shape_cb.addItem(i[0])

        # Populate combo box with values from 'depth' column
        cur.execute("SELECT DISTINCT depth from methods ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.depth_cb.addItem(i[0])

        # Populate combo box with values from 'thickness' column
        cur.execute("SELECT DISTINCT thickness from methods ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.thickness_cb.addItem(i[0])

        # Populate combo box with values from 'dip' column
        cur.execute("SELECT DISTINCT dip from methods ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.dip_cb.addItem(i[0])

        # Populate combo box with values from 'strengthofore' column
        cur.execute("SELECT DISTINCT strengthofore from methods ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.strength_of_ore_cb.addItem(i[0])

        # Populate combo box with values from 'strengthofcountryrock' column
        cur.execute("SELECT DISTINCT strengthofcountryrock from methods ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.strength_of_country_rock_cb.addItem(i[0])

        # Populate combo box with ore types from 'weights' table
        cur.execute("SELECT DISTINCT oretype from weights ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.ore_type_cb.addItem(i[0])

        # Populate combo box with geological distribution types
        cur.execute("SELECT DISTINCT distribution from geology ")
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.distribution_cb.addItem(i[0])

        # Close the database connection after loading data
        conn.close()

        # Connect dropdown changes and button clicks to methods
        self.ui.shape_cb.currentTextChanged.connect(lambda: self.change_shape())
        self.ui.thickness_cb.currentTextChanged.connect(lambda: self.change_thickness())
        self.ui.apply_btn.clicked.connect(self.apply)  # Connect the 'Apply' button to apply logic

        
    def change_shape(self):
        """
        Updates the 'thickness' and 'dip' combo boxes based on the selected 'shape'.
        This ensures that only valid combinations of shape → thickness → dip are selectable.
        """
        shape = self.ui.shape_cb.currentText()

        # Connect to database to fetch thickness options for selected shape
        conn = sqlite3.connect(path.dirname(__file__) + "/data.db")
        cur = conn.cursor()

        # Clear current thickness options
        self.ui.thickness_cb.clear()

        # Fetch thickness values where shape matches
        sql = "SELECT DISTINCT thickness from methods WHERE shape= ?"
        val = (shape,)
        cur.execute(sql, val)
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.thickness_cb.addItem(i[0])

        # Auto-update dip combo box based on first thickness option
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
        """
        Updates the 'dip' combo box when the user selects a new thickness value.
        Depends on the currently selected shape.
        """
        shape = self.ui.shape_cb.currentText()
        thickness = self.ui.thickness_cb.currentText()

        # Connect to DB and fetch dip options for shape+thickness
        conn = sqlite3.connect(path.dirname(__file__) + "/data.db")
        cur = conn.cursor()
        self.ui.dip_cb.clear()

        sql = "SELECT DISTINCT dip from methods WHERE shape= ? and thickness= ?"
        val = (shape, thickness)
        cur.execute(sql, val)
        myresult = cur.fetchall()
        for i in myresult:
            self.ui.dip_cb.addItem(i[0])

        conn.close()

    def apply(self):
        """
        Gathers all user-selected inputs and updates the image preview
        based on current parameters. Prepares for the next step in analysis.
        """
        # Read all selected parameters from combo boxes
        shape = self.ui.shape_cb.currentText()
        depth = self.ui.depth_cb.currentText()
        thickness = self.ui.thickness_cb.currentText()
        dip = self.ui.dip_cb.currentText()
        ore_type = self.ui.ore_type_cb.currentText()
        distribution = self.ui.distribution_cb.currentText()
        strength_of_country_rock = self.ui.strength_of_country_rock_cb.currentText()
        strength_of_ore = self.ui.strength_of_ore_cb.currentText()

        # Normalize thickness to short code used in image filenames
        if thickness == "Very Narrow":
            thickness = "VN"
        elif thickness == "Very Thick":
            thickness = "VT"
        else:
            thickness = thickness[0]  # Use first character (e.g. 'N' for Narrow)

        # Load and display corresponding image from the 'pictures' folder
        image_path = path.dirname(__file__) + "/pictures/{}-{}-{}-{}.png".format(
            shape[0], depth[0], thickness, dip[0]
        )
        print(image_path)  # For debugging
        self.ui.pic_lbl.setPixmap(QtGui.QPixmap(image_path))

        # Show the 'Next' button and connect its click to the next step
        self.ui.next_btn.setHidden(False)

        # Re-fetch full thickness (for passing to next step)
        thickness = self.ui.thickness_cb.currentText()

        # Connect the next button to the 'next' function with all parameters
        self.ui.next_btn.clicked.connect(lambda: self.next(
            ore_type, strength_of_country_rock, strength_of_ore,
            shape, dip, depth, thickness, distribution
        ))

        
    def next(self, ore_type, strength_of_country_rock, strength_of_ore, shape, dip, depth, thickness, distribution):
        """
        This method loads the second UI page (matrix view), retrieves corresponding weights from the database
        based on user selections, and populates the decision matrix for further processing (ANP calculation).
        """

        # Load and initialize the matrix UI
        self.ui = matrix.Matrix_wnw()
        self.ui.setupUi(self)

        # Connect to local SQLite database
        conn = sqlite3.connect(path.dirname(__file__) + "/data.db")
        cur = conn.cursor()

        # === Fill weights from 'weights' table based on ore type ===
        sql = "SELECT * from weights WHERE oretype= ? "
        val = (ore_type,)
        cur.execute(sql, val)
        myresult = cur.fetchall()

        counter = 0
        myresult = [i for i in myresult]  # Convert to list of tuples
        for i in myresult:
            for j in i:
                if counter not in [0, 7]:  # Skip non-matrix fields (likely ID or label)
                    item = QTableWidgetItem(str(j))
                    item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.ui.matrix_tw.setItem(0, counter - 1, item)
                counter += 1

        # === Define mining methods considered ===
        methods = [
            "Open Pit", "Block Caving", "Sublevel Stoping", "Sublevel Caving", "Long Wall Mining",
            "Room And Pillar", "Shrinkage Stoping", "Cut And Fill", "Top Slicing", "Square Set Stoping"
        ]

        # === Loop over methods and populate matrix rows for each ===
        for method in methods:
            ind_method = methods.index(method)

            # Normalize country rock strength (unify terminology)
            if strength_of_country_rock == "Destructible":
                strength_of_country_rock = "Weak"

            # 1. Rock mechanics weight
            sql = "SELECT rockmechanics from rockmechanics WHERE method= ? AND strengthofcountryrock= ? AND strengthofore= ?"
            val = (method, strength_of_country_rock, strength_of_ore)
            cur.execute(sql, val)
            weight = [i[0] for i in cur.fetchall()]
            item = QTableWidgetItem(str(weight[0]))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.ui.matrix_tw.setItem(ind_method + 1, 0, item)

            # 2. Geometry weight
            sql = "SELECT weight from geometry WHERE method= ? AND shape= ? AND dip= ? AND Thickness= ? AND depth= ?"
            val = (method, shape, dip, thickness, depth)
            cur.execute(sql, val)
            weight = [i[0] for i in cur.fetchall()]
            item = QTableWidgetItem(str(weight[0]))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.ui.matrix_tw.setItem(ind_method + 1, 1, item)

            # 3. Geology weight
            sql = "SELECT weight from geology WHERE method= ? AND distribution= ?"
            val = (method, distribution)
            cur.execute(sql, val)
            weight = [i[0] for i in cur.fetchall()]
            item = QTableWidgetItem(str(weight[0]))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.ui.matrix_tw.setItem(ind_method + 1, 3, item)

            # 4. Economic weight
            sql = "SELECT weight from economic WHERE method= ?"
            val = (method,)
            cur.execute(sql, val)
            weight = [i[0] for i in cur.fetchall()]
            item = QTableWidgetItem(str(weight[0]))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.ui.matrix_tw.setItem(ind_method + 1, 4, item)

            # 5. Environmental weight
            sql = "SELECT weight from enviroment WHERE method= ?"
            val = (method,)
            cur.execute(sql, val)
            weight = [i[0] for i in cur.fetchall()]
            item = QTableWidgetItem(str(weight[0]))
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.ui.matrix_tw.setItem(ind_method + 1, 5, item)

        # Close the DB connection after all data is loaded
        conn.close()

        # Restore original label if needed for passing to back()
        if strength_of_country_rock == "Weak":
            strength_of_country_rock = "Destructible"

        # Connect button actions
        self.ui.back_btn.clicked.connect(lambda: self.back(
            ore_type, strength_of_country_rock, strength_of_ore,
            shape, dip, depth, thickness, distribution
        ))
        self.ui.calculate_btn.clicked.connect(self.calculate)


    def back(self, ore_type, strength_of_country_rock, strength_of_ore, shape, dip, depth, thickness, distribution):
        """
        Reverts the interface back to the main selection window with all previously selected parameters restored.
        Useful when the user navigates backward from the matrix evaluation screen to modify inputs.
        """

        # Close the current matrix window
        self.close()

        # Reinitialize the main window and UI
        self.__init__()

        # Restore user selections to the corresponding combo boxes
        self.ui.ore_type_cb.setCurrentText(ore_type)
        self.ui.strength_of_country_rock_cb.setCurrentText(strength_of_country_rock)
        self.ui.strength_of_ore_cb.setCurrentText(strength_of_ore)
        self.ui.shape_cb.setCurrentText(shape)
        self.ui.dip_cb.setCurrentText(dip)
        self.ui.depth_cb.setCurrentText(depth)
        self.ui.thickness_cb.setCurrentText(thickness)
        self.ui.distribution_cb.setCurrentText(distribution)


    def calculate(self):
        """
        Performs Analytic Network Process (ANP) calculation based on matrix input.
        This method:
            - Reads user-entered weights and scores
            - Normalizes the data
            - Builds the supermatrix
            - Computes influence propagation (via supermatrix multiplication)
            - Displays top 5 recommended mining methods.
        """

        # Clear previous results from the result list widget
        self.ui.final_lw.clear()

        # Initialize empty matrices (10 methods × 6 criteria)
        normed_matrix = [[0 for _ in range(6)] for _ in range(10)]
        matrix = [[0 for _ in range(6)] for _ in range(10)]

        # Weight row (1 row × 6 columns)
        normed_w = [[0 for _ in range(6)]]

        # === Populate weight row and input matrix ===
        for row in range(11):  # Includes weights (row 0) and 10 methods (rows 1-10)
            for column in range(6):
                if row == 0:
                    # Top row contains the weights for each criterion
                    normed_w[0][column] = float(self.ui.matrix_tw.item(row, column).text())
                elif column == 2:
                    # Column 2 is expected to be a dropdown selection (e.g., score as integer)
                    matrix[row - 1][column] = int(self.ui.matrix_tw.cellWidget(row, column).currentText())
                else:
                    # Other columns are numerical scores
                    try:
                        value = float(self.ui.matrix_tw.item(row, column).text())
                        matrix[row - 1][column] = value if value > 0 else 0
                    except (AttributeError, ValueError):
                        # If invalid or missing, assume a neutral/default score
                        matrix[row - 1][column] = 1

        # === Normalize weight vector ===
        normed_w = np.array(normed_w)
        sum_w = sum(normed_w[0])
        for i in range(6):
            normed_w[0][i] /= sum_w

        # Convert to NumPy array for matrix operations
        matrix = np.array(matrix).T  # Transpose to column-wise criterion

        # === Normalize each criterion column ===
        for row in range(6):
            col_sum = sum(matrix[row])
            for column in range(10):
                normed_matrix[column][row] = matrix[row][column] / col_sum if col_sum != 0 else 0

        normed_matrix = np.array(normed_matrix)

        # === Create Supermatrix (17x17) ===
        n = 17
        supermatix = [[0 for _ in range(n)] for _ in range(n)]

        # Insert normalized weights (from criteria to goal)
        for i in range(1, 7):  # Indices 1–6 are criteria
            supermatix[i][0] = normed_w[0][i - 1]

        # Insert normalized decision matrix (alternatives to criteria)
        for i in range(7, 17):  # Rows 7–16 represent 10 alternatives
            for j in range(1, 7):
                supermatix[i][j] = normed_matrix[i - 7][j - 1]

        # Identity submatrix for alternatives (self-loop)
        for i in range(7, 17):
            supermatix[i][i] = 1

        supermatix = np.array(supermatix)

        # === Multiply supermatrix to simulate influence propagation ===
        result = np.dot(supermatix, supermatix)

        # === Rank methods by their overall influence score ===
        methods = [
            "Open Pit", "Block Caving", "Sublevel Stoping", "Sublevel Caving",
            "Long Wall Mining", "Room And Pillar", "Shrinkage Stoping",
            "Cut And Fill", "Top Slicing", "Square Set Stoping"
        ]

        # Extract scores for alternatives (rows 7–16, column 0)
        best_methods = [result[i + 7][0] for i in range(10)]
        sorted_scores = sorted(best_methods, reverse=True)

        # Display top 5 methods in the result list
        for i in range(5):
            for j in range(10):
                if sorted_scores[i] == result[j + 7][0]:
                    self.ui.final_lw.addItem(f"{i + 1} - {methods[j]} : {round(sorted_scores[i], 3)}")

            
# Create an instance of the MainWindow class, which contains the GUI and application logic
w = MainWindow()

# Show the main application window
w.show()

# Start the application's event loop to keep the GUI running
app.exec()
