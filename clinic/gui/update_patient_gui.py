from clinic.controller import Controller
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QWidget, QLabel
from PyQt6.QtWidgets import QLineEdit, QPushButton, QMessageBox

class UpdatePatientGUI(QMainWindow):
    def __init__(self, parent: 'MenuGUI', controller: 'Controller'):
        '''
        Constructor that initializes the Update Patient GUI.
        It allows the user to search for a patient by PHN (Personal Health Number) and update their details.
        '''
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.setWindowTitle("UPDATE PATIENT")
        layout = QGridLayout()

        label_phn = QLabel("New Phn")
        self.text_phn = QLineEdit()
        label_name = QLabel("New Name")
        self.text_name = QLineEdit()
        lable_birthdate = QLabel("New Birthdate")
        self.text_birthdate = QLineEdit()
        label_phone = QLabel("New Phone")
        self.text_phone = QLineEdit()
        lable_email = QLabel("New Email")
        self.text_email = QLineEdit()
        label_address = QLabel("New Address")
        self.text_address = QLineEdit()

        label_name_key = QLabel("Current Phn")
        self.text_key = QLineEdit()

        self.button_search = QPushButton("Search")
        self.button_goback = QPushButton("Back")
        self.button_update = QPushButton("Update")

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
        layout.addWidget(label_name_key, 6, 0)
        layout.addWidget(self.text_key, 6, 1)
        layout.addWidget(self.button_search, 7, 1)
        layout.addWidget(self.button_goback, 8, 0)
        layout.addWidget(self.button_update, 8, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.button_goback.clicked.connect(self.goback_button_clicked)
        self.button_search.clicked.connect(self.search_button_clicked)
        self.button_update.clicked.connect(self.update_button_clicked)

        self.button_update.setEnabled(False)
        self.text_phn.setEnabled(False)
        self.text_name.setEnabled(False)
        self.text_birthdate.setEnabled(False)
        self.text_phone.setEnabled(False)
        self.text_email.setEnabled(False)
        self.text_address.setEnabled(False)

        self.text_key.textChanged.connect(self.text_key_changed)

    def goback_button_clicked(self):
        '''
        This function is called when the "Back" button is clicked.
        It hides the Update Patient GUI and shows the main menu.
        '''
        self.hide()
        self.parent.show()

    def text_key_changed(self):
        '''
        This function is called when the text in the PHN input changes.
        It disables the update button and input fields until a valid patient is searched.
        '''
        self.button_update.setEnabled(False)
        self.text_phn.setEnabled(False)
        self.text_name.setEnabled(False)
        self.text_birthdate.setEnabled(False)
        self.text_phone.setEnabled(False)
        self.text_email.setEnabled(False)
        self.text_address.setEnabled(False)

    def search_button_clicked(self):
        '''
        This function is called when the "Search" button is clicked.
        It searches for a patient using the given PHN.
        If the patient is found, it populates the input fields with their information and enables them for editing.
        '''
        try:
            key = int(self.text_key.text())
            patient = self.controller.search_patient(key)
            
            self.text_phn.setText(str(patient.phn))
            self.text_name.setText(patient.name)
            self.text_birthdate.setText(patient.birth_date)
            self.text_phone.setText(patient.phone)
            self.text_email.setText(patient.email)
            self.text_address.setText(patient.address)

            self.button_update.setEnabled(True)
            self.text_phn.setEnabled(True)
            self.text_name.setEnabled(True)
            self.text_birthdate.setEnabled(True)
            self.text_phone.setEnabled(True)
            self.text_email.setEnabled(True)
            self.text_address.setEnabled(True)
        except:
            QMessageBox.warning(self, "Failure", "Patient not found")

    def update_button_clicked(self):
        '''
        This function is called when the "Update" button is clicked.
        It updates the patient's information with the new details entered by the user.
        If successful, it shows a success message. If not, it shows a failure message.
        '''
        try:
            key = int(self.text_key.text())
            new_phn = int(self.text_phn.text())
            new_name = self.text_name.text()
            new_birthdate = self.text_birthdate.text()
            new_phone = self.text_phone.text()
            new_email = self.text_email.text()
            new_address = self.text_address.text()

            self.controller.update_patient(key, new_phn, new_name, new_birthdate, new_phone, new_email, new_address)
            QMessageBox.information(self, "Success", "The patient's info is updated!")
        except:
            QMessageBox.warning(self, "Failure", "Cannot update the current patient or update the patient using others' PHN.")
        finally:
            self.text_key.clear()
            self.text_phn.clear()
            self.text_name.clear()
            self.text_birthdate.clear()
            self.text_phone.clear()
            self.text_email.clear()
            self.text_address.clear()