from clinic.controller import Controller
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QWidget, QLabel
from PyQt6.QtWidgets import QLineEdit, QPushButton, QMessageBox

class CreatePatientGUI(QMainWindow):
    def __init__(self, parent: 'MenuGUI', controller: 'Controller'):
        '''
        This function is the constructor. It creates the window for adding a new patient.
        It also adds input fields for the patient's information and buttons to add the patient or go back.
        '''
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.setWindowTitle("Create Patient")
        layout = QGridLayout()

        label_phn = QLabel("Phn")
        self.text_phn = QLineEdit()
        label_name = QLabel("Name")
        self.text_name = QLineEdit()
        lable_birthdate = QLabel("Birthdate")
        self.text_birthdate = QLineEdit()
        label_phone = QLabel("Phone")
        self.text_phone = QLineEdit()
        lable_email = QLabel("Email")
        self.text_email = QLineEdit()
        label_address = QLabel("Address")
        self.text_address = QLineEdit()

        self.button_goback = QPushButton("Back")
        self.button_add = QPushButton("Add")

        layout.addWidget(label_phn, 0, 0)
        layout.addWidget(self.text_phn, 0, 1)
        layout.addWidget(label_name, 1, 0)
        layout.addWidget(self.text_name, 1, 1)
        layout.addWidget(lable_birthdate, 2, 0)
        layout.addWidget(self.text_birthdate, 2, 1)
        layout.addWidget(label_phone, 3, 0)
        layout.addWidget(self.text_phone, 3, 1)
        layout.addWidget(lable_email, 4, 0)
        layout.addWidget(self.text_email, 4, 1)
        layout.addWidget(label_address, 5, 0)
        layout.addWidget(self.text_address, 5, 1)
        layout.addWidget(self.button_goback, 6, 0)
        layout.addWidget(self.button_add, 6, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button_goback.clicked.connect(self.goback_button_clicked)
        self.button_add.clicked.connect(self.add_button_clicked)

    def goback_button_clicked(self):
        '''
        This function is for the "Back" button click.
        It hides the current window and shows the main menu window.
        '''
        self.hide()
        self.parent.show()

    def add_button_clicked(self):
        '''
        This function is for the "Add" button click.
        It gets the patient's information from input fields and tries to add the patient to the system.
        If the operation is successful, it shows a success message.
        If the operation fails, it shows a warning message.
        Finally, it clears all input fields for new input.
        '''
        try:
            phn = int(self.text_phn.text())
            name = self.text_name.text()
            birthdate = self.text_birthdate.text()
            phone = self.text_phone.text()
            email = self.text_email.text()
            address = self.text_address.text()
            self.controller.create_patient(phn, name, birthdate, phone, email, address)
            QMessageBox.information(self, "Success", "Patient is added successfully!")
        except:
            QMessageBox.warning(self, "Failure", "The operation is invalid...")
        finally:
            self.text_phn.clear()
            self.text_name.clear()
            self.text_birthdate.clear()
            self.text_phone.clear()
            self.text_email.clear()
            self.text_address.clear()