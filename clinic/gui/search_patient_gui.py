from clinic.controller import Controller
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QWidget, QLabel
from PyQt6.QtWidgets import QLineEdit, QPushButton, QMessageBox

class SearchPatientGUI(QMainWindow):
    def __init__(self, parent: 'MenuGUI', controller: 'Controller'):
        '''
        This function is the constructor. It creates the window for searching a patient.
        It adds an input field for the search key and displays the patient information if found.
        '''
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.setWindowTitle("SEARCH FOR PATIENT")
        self.setFixedSize(250, 275)
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

        label_name_key = QLabel("Key")
        self.text_key = QLineEdit()

        self.button_goback = QPushButton("Back")
        self.button_search = QPushButton("Search")

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
        layout.addWidget(self.button_goback, 7, 0)
        layout.addWidget(self.button_search, 7, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.text_phn.setEnabled(False)
        self.text_name.setEnabled(False)
        self.text_birthdate.setEnabled(False)
        self.text_phone.setEnabled(False)
        self.text_email.setEnabled(False)
        self.text_address.setEnabled(False)

        self.button_goback.clicked.connect(self.goback_button_clicked)
        self.button_search.clicked.connect(self.search_button_clicked)

    def goback_button_clicked(self):
        '''
        This function is for the "Back" button click.
        It hides the current window and shows the main menu window.
        '''
        self.hide()
        self.parent.show()

    def search_button_clicked(self):
        '''
        This function is for the "Search" button click.
        It takes the key input, searches for the patient in the system, 
        and fills the fields with the patient's information if found.
        If the patient is not found, it shows a warning message.
        Finally, it clears the search key field.
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
        except:
            QMessageBox.warning(self, "Failure", "The patient is not found...")
        finally:
            self.text_key.clear()
