from clinic.controller import Controller
from clinic.gui.patient_table_model import PatientTableModel
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QVBoxLayout, QTableView
from PyQt6.QtWidgets import QWidget, QPushButton

class ListPatientsGUI(QMainWindow):
    def __init__(self, parent: 'MenuGUI', controller: 'Controller'):
        """
        This constructor creates the window that shows all patients.
        It has a table that displays the patient list and a back button.
        """
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.setWindowTitle("List Patients")
        self.resize(600, 400)

        self.patient_table = QTableView()
        self.patient_model = PatientTableModel(self.controller)
        self.patient_table.setModel(self.patient_model)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.back_button_clicked)
        
        layout = QVBoxLayout()
        sub_layout = QGridLayout()
        sub_layout.addWidget(self.back_button, 0, 0)
        layout.addWidget(self.patient_table)
        layout.addLayout(sub_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.patient_model.list_data()
        self.patient_table.setColumnWidth(0, 100)
        self.patient_table.setColumnWidth(1, 100)
        self.patient_table.setColumnWidth(2, 100)
        self.patient_table.setColumnWidth(3, 150)
        self.patient_table.setColumnWidth(4, 200)
        self.patient_table.setColumnWidth(5, 300)

    def back_button_clicked(self):
        """
        This function is called when the back button is clicked.
        It hides the current window and shows the parent window.
        """
        self.hide()
        self.parent.show()