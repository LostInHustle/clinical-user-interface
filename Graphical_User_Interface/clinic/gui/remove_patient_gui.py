from clinic.controller import Controller
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QWidget, QLabel
from PyQt6.QtWidgets import QLineEdit, QPushButton, QMessageBox

class RemovePatientGUI(QMainWindow):
    def __init__(self, parent: 'MenuGUI', controller: 'Controller'):
        """
        This is the constructor. It makes the window for removing patient.
        It has one input for the PHN (Personal Health Number) and two buttons.
        """
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.setWindowTitle("REMOVE PATIENT")
        layout = QGridLayout()
        self.label_phn = QLabel("Enter Phn")
        self.text_phn = QLineEdit()

        self.button_goback = QPushButton("Back")
        self.button_remove = QPushButton("Remove Patient")

        layout.addWidget(self.label_phn, 0, 0)
        layout.addWidget(self.text_phn, 0, 1)
        layout.addWidget(self.button_goback, 1, 0)
        layout.addWidget(self.button_remove, 1, 1)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button_goback.clicked.connect(self.goback_button_clicked)
        self.button_remove.clicked.connect(self.remove_button_clicked)

    def goback_button_clicked(self):
        """
        This function runs when Back button is clicked.
        It closes the remove patient window and shows the main menu again.
        """
        self.hide()
        self.parent.show()

    def remove_button_clicked(self):
        """
        This function runs when Remove Patient button is clicked.
        It tries to remove the patient with the PHN entered.
        If the patient is removed, it shows a success message.
        For other cases, it shows a warning message.
        """
        try:
            phn = int(self.text_phn.text())
            self.controller.delete_patient(phn)
            QMessageBox.information(self, "Success", "The patient is deleted")
        except:
            QMessageBox.warning(self, "Failure", "Cannot delete the patient...")