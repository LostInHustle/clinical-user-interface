from clinic.controller import Controller
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QWidget, QLabel
from PyQt6.QtWidgets import QLineEdit, QPushButton, QMessageBox

class ChoosePatientGUI(QMainWindow):
    def __init__(self, parent: 'MenuGUI', controller: 'Controller'):
        '''
        This function is the constructor. It creates the window for selecting the current patient.
        It shows the current patient and allows the user to set a new current patient or unset the current one.
        '''
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.setWindowTitle("SELECT CURRENT PATIENT")
        layout = QGridLayout()

        label_current = QLabel("Current Patient")
        self.text_current = QLineEdit()
        label_new_current = QLabel("New Current Patient")
        self.text_new_current = QLineEdit()
        self.button_set = QPushButton("Set")
        self.button_unset = QPushButton("Unset")
        self.button_goback = QPushButton("Back")

        layout.addWidget(label_current, 0, 0)
        layout.addWidget(self.text_current, 0, 1)
        layout.addWidget(label_new_current, 1, 0)
        layout.addWidget(self.text_new_current, 1, 1)
        layout.addWidget(self.button_goback, 2, 0)
        layout.addWidget(self.button_set, 2, 1)
        layout.addWidget(self.button_unset, 2, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.text_current.setEnabled(False)

        if self.controller.current_patient:
            self.text_current.setText(str(self.controller.current_patient.phn))
        else:
            self.text_current.setText("N/A")

        self.button_goback.clicked.connect(self.goback_button_clicked)
        self.button_set.clicked.connect(self.set_button_clicked)
        self.button_unset.clicked.connect(self.unset_button_clicked)

    def set_button_clicked(self):
        '''
        This function is for the "Set" button click.
        It takes the new patient PHN, sets it as the current patient,
        updates the current patient display, and clears the input field.
        If the input is invalid, it shows a warning message.
        '''
        try:
            new_current_patient = int(self.text_new_current.text())
            self.controller.set_current_patient(new_current_patient)
            self.text_current.setText(str(self.controller.current_patient.phn))
            self.text_new_current.clear()
        except:
            QMessageBox.warning(self, "Warning", "Invalid input!!!")

    def goback_button_clicked(self):
        '''
        This function is for the "Back" button click.
        It hides the current window and shows the main menu window.
        '''
        self.hide()
        self.parent.show()

    def unset_button_clicked(self):
        '''
        This function is for the "Unset" button click.
        It removes the current patient from the system and shows "N/A".
        If no current patient exists, it shows a warning message.
        '''
        try:
            self.controller.unset_current_patient()
            self.text_current.setText("N/A")
            self.text_new_current.clear()
        except:
            QMessageBox.warning(self, "Failure", "There is no current patient!")