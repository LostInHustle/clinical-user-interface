from clinic.controller import Controller
from clinic.exception.no_current_patient_exception import NoCurrentPatientException
from PyQt6.QtWidgets import QMainWindow, QGridLayout
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class UpdateNoteGUI(QMainWindow):
    def __init__(self, parent: 'AppointmentMenuGUI', controller: 'Controller'):
        """
        This window lets the user search for a note by keycode and update it.
        It has a text input for the note and a button to search and update.
        """
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.setWindowTitle("UPDATE NOTE")
        self.setFixedSize(300, 150)
        layout = QGridLayout()

        self.label_note = QLabel("Note Obtained")
        self.text_note = QLineEdit()
        self.keycode = QLabel("Keycode")
        self.text_keycode = QLineEdit()

        self.button_search = QPushButton("Search")
        self.button_goback = QPushButton("Back")
        self.button_update = QPushButton("Update")

        layout.addWidget(self.label_note, 0, 0)
        layout.addWidget(self.text_note, 0, 1, 1, 2)
        layout.addWidget(self.keycode, 1, 0)
        layout.addWidget(self.text_keycode, 1, 1, 1, 2)
        layout.addWidget(self.button_goback, 2, 0)
        layout.addWidget(self.button_update, 2, 1)
        layout.addWidget(self.button_search, 2, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button_goback.clicked.connect(self.goback_button_clicked)
        self.button_search.clicked.connect(self.search_button_clicked)
        self.button_update.clicked.connect(self.update_button_clicked)

        self.text_note.setEnabled(False)
        self.button_update.setEnabled(False)
        self.text_keycode.textChanged.connect(self.text_keycode_changed)

    def goback_button_clicked(self):
        """
        This function is called when the 'Back' button is clicked.
        It hides the current window and shows the parent window.
        """
        self.hide()
        self.parent.show()

    def search_button_clicked(self):
        """
        This function is called when the 'Search' button is clicked.
        It tries to search the note by keycode, and if found, shows the note text for editing.
        If no note or invalid keycode is found, it shows an error message.
        """
        try:
            code = int(self.text_keycode.text().strip())
            note_obtained = self.controller.search_note(code)
            if not note_obtained:
                raise Exception()
            self.text_note.setText(f'{note_obtained.text}')
            self.text_note.setEnabled(True)
            self.button_update.setEnabled(True)
        except ValueError:
            QMessageBox.warning(self, "Warning", "Please enter a valid integer!")
        except NoCurrentPatientException:
            QMessageBox.warning(self, "Warning", "There is no current patient!")
        except:
            QMessageBox.warning(self, "Warning", "There is no matching note!")

    def update_button_clicked(self):
        """
        This function is called when the 'Update' button is clicked.
        It updates the note with the new text entered by the user.
        If no current patient is selected, it shows a warning.
        """
        try:
            code = int(self.text_keycode.text().strip())
            new_note = self.text_note.text().strip()
            self.controller.update_note(code, new_note)
            QMessageBox.information(self, "Success", "The note is updated!")
            self.text_note.clear()
            self.text_keycode.clear()
        except NoCurrentPatientException:
            QMessageBox.warning(self, "Warning", "There is no current patient!")

    def text_keycode_changed(self):
        """
        This function disables the note text field and update button until a keycode is entered.
        """
        self.text_note.setEnabled(False)
        self.button_update.setEnabled(False)
