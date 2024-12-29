from clinic.controller import Controller
from PyQt6.QtWidgets import QMainWindow, QGridLayout
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class CreateNoteGUI(QMainWindow):
    def __init__(self, parent: 'AppointmentMenuGUI', controller: 'Controller'):
        """
        This window lets user create a new note for the current patient.
        It has a text input for the note and buttons to add the note or go back.
        """
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.setWindowTitle("Create Note")
        self.setFixedSize(200, 100)
        layout = QGridLayout()

        label_note = QLabel("Note")
        self.text_note = QLineEdit()
        self.button_goback = QPushButton("Back")
        self.button_add = QPushButton("Add")

        layout.addWidget(label_note, 0, 0)
        layout.addWidget(self.text_note, 0, 1)
        layout.addWidget(self.button_goback, 1, 0)
        layout.addWidget(self.button_add, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button_goback.clicked.connect(self.goback_button_clicked)
        self.button_add.clicked.connect(self.add_button_clicked)

    def goback_button_clicked(self):
        """
        This function is called when the 'Back' button is clicked.
        It hides the current window and shows the parent window.
        """
        self.hide()
        self.parent.show()

    def add_button_clicked(self):
        """
        This function is called when the 'Add' button is clicked.
        It tries to add the note and shows a success or failure message.
        If no current patient is selected, it shows a warning.
        """
        try:
            new_note = self.text_note.text()
            self.controller.create_note(new_note)
            QMessageBox.information(self, "Success", "Note is created successfully!")
        except:
            QMessageBox.warning(self, "Failure", "Choose the current patient first!")
        finally:
            self.text_note.clear()
