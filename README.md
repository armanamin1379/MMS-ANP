# MMS-ANP: A Decision Support Tool for Mining Method Selection

This repository contains the source code and implementation for the software tool developed in the paper:

**"A Decision Support System and Software Tool (MMS-ANP) for Mining Method Selection based on Analytic Network Process"**

The tool supports mining engineers and decision-makers in selecting the most appropriate mining method based on user-defined input and the Analytic Network Process (ANP). The algorithm uses matrix-based decision modeling and NumPy for calculations.

---

## 📌 Features

- Manual input of decision criteria and alternatives by the user
- Dynamic matrix construction and analysis
- ANP-based ranking and recommendation of the top 5 mining methods
- GUI-based interface built using PyQt5
- Includes sample data in a pre-configured SQLite database (`data.db`)
- Includes example screenshots in the `pictures/` folder

---

## 🛠 Requirements

- **Operating System**: Windows 64-bit
- **Python version**: 3.7.0
- **Required packages**: Listed in `requirements.txt`

To install the required packages:

```bash
pip install -r requirements.txt
```

💡 *Using a virtual environment is recommended to avoid version conflicts:*

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 How to Run

1. Clone or download the entire repository.
2. Make sure Python 3.7.0 and required libraries are installed.
3. Run the main file:

```bash
python method.py
```

Alternatively, you can double-click on `method.py` in Windows (if Python is properly associated with `.py` files).

---

## ✅ Quick Test

To verify the installation:

1. Launch `method.py`
2. Enter sample values manually in the GUI
3. Confirm that a list of 5 ranked mining methods is returned

---

## 📁 Repository Structure

```
├── method.py         # Main script to run the software
├── page.py           # GUI components and windows
├── matrix.py         # Matrix generation and calculation logic
├── data.db           # Sample SQLite3 database
├── pictures/         # Folder containing illustrative images/screenshots
├── requirements.txt  # Python package dependencies
└── README.md         # This file
```

---

## 📄 License

This software is released for academic and research use. You may adapt or extend it with appropriate credit. For licensing, please consult the authors.

---

## 📬 Contact

For questions or collaboration, please contact the corresponding author listed in the original publication.
