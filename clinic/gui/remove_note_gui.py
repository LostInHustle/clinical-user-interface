from clinic.controller import Controller
from clinic.exception.no_current_patient_exception import NoCurrentPatientException
from PyQt6.QtWidgets import QMainWindow, QGridLayout
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class RemoveNoteGUI(QMainWindow):
    def __init__(self, parent: 'AppointmentMenuGUI', controller: 'Controller'):
        """
        This window lets the user remove a note by entering its code.
        It has a text input for the code and a button to remove the note.
        """
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.setWindowTitle("REMOVE NOTE")
        self.setFixedWidth(275)
        self.setFixedHeight(100)
        layout = QGridLayout()

        self.label_code = QLabel("Enter code")
        self.text_code = QLineEdit()
        self.button_goback = QPushButton("Back")
        self.button_remove = QPushButton("Remove Note")

        layout.addWidget(self.label_code, 0, 0)
        layout.addWidget(self.text_code, 0, 1)
        layout.addWidget(self.button_goback, 1, 0)
        layout.addWidget(self.button_remove, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button_goback.clicked.connect(self.goback_button_clicked)
        self.button_remove.clicked.connect(self.remove_button_clicked)

    def goback_button_clicked(self):
        """
        This function is called when the 'Back' button is clicked.
        It hides the current window and shows the parent window.
        """
        self.hide()
        self.parent.show()

    def remove_button_clicked(self):
        """
        This function is called when the 'Remove Note' button is clicked.
        It tries to remove the note by the code entered by the user.
        If the note is not found or an invalid code is entered, it shows an error message.
        """
        try:
            code = int(self.text_code.text())
            if self.controller.delete_note(code):
                QMessageBox.information(self, "Success", "The note is deleted!")
            else:
                QMessageBox.warning(self, "Failure", "Cannot find the note!")
        except ValueError:
            QMessageBox.warning(self, "Failure", "Type an integer first!")
        except NoCurrentPatientException:
            QMessageBox.warning(self, "Failure", "Choose the current patient first!")
