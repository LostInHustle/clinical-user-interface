from clinic.controller import Controller
from clinic.gui.patient_table_model import PatientTableModel
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QVBoxLayout, QTableView
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class RetrievePatientGUI(QMainWindow):
    def __init__(self, parent: 'MenuGUI', controller: 'Controller'):
        """
        This is the constructor. It creates the window for retrieving patients.
        It has a table to show patients and input field for searching by keyword.
        There are buttons for retrieve, clear, and back actions.
        """
        super().__init__()
        self.parent = parent
        self.controller = controller

        self.setWindowTitle("Retrieve Patients")
        self.resize(600, 400)

        self.patient_table = QTableView()
        self.patient_model = PatientTableModel(self.controller)
        self.patient_table.setModel(self.patient_model)

        self.retrieve_label = QLabel("Enter Keyword")
        self.text_keyword = QLineEdit()
        self.retrieve_button = QPushButton("Retrieve")
        self.back_button = QPushButton("Back")
        self.clear_button = QPushButton("Clear")

        self.retrieve_button.clicked.connect(self.retrieve_button_clicked)
        self.clear_button.clicked.connect(self.clear_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)

        layout = QVBoxLayout()
        sub_layout = QGridLayout()
        layout.addWidget(self.patient_table)
        sub_layout.addWidget(self.retrieve_label, 0, 0)
        sub_layout.addWidget(self.text_keyword, 0, 1)
        sub_layout.addWidget(self.back_button, 1, 0)
        sub_layout.addWidget(self.retrieve_button, 1, 1)
        sub_layout.addWidget(self.clear_button, 1, 2)
        layout.addLayout(sub_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def retrieve_button_clicked(self):
        """
        This function is called when the retrieve button is clicked.
        It takes the keyword, searches for matching patients and shows them in the table.
        If no patients are found, it shows a warning message.
        """
        try:
            text_keyword = self.text_keyword.text().strip()
            self.patient_model.keyword = text_keyword
            self.patient_model.refresh_data()
            self.patient_table.setColumnWidth(0, 100)
            self.patient_table.setColumnWidth(1, 100)
            self.patient_table.setColumnWidth(2, 100)
            self.patient_table.setColumnWidth(3, 150)
            self.patient_table.setColumnWidth(4, 200)
            self.patient_table.setColumnWidth(5, 300)
            self.text_keyword.setEnabled(False)
            self.retrieve_button.setEnabled(False)
        except:
            QMessageBox.warning(self, "Failure", "There is no matching patient!")

    def clear_button_clicked(self):
        """
        This function is called when the clear button is clicked.
        It resets the model, clears the keyword input, and enables the search button again.
        """
        self.patient_model.reset()
        self.text_keyword.clear()
        self.text_keyword.setEnabled(True)
        self.retrieve_button.setEnabled(True)

    def back_button_clicked(self):
        """
        This function is called when the back button is clicked.
        It hides the current window and shows the parent window again.
        """
        self.hide()
        self.parent.show()