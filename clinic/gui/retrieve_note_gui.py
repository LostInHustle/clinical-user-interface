from clinic.controller import Controller
from clinic.exception.no_current_patient_exception import NoCurrentPatientException
from clinic.gui.note_table_model import NoteTableModel
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QVBoxLayout, QTableView
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class RetrieveNoteGUI(QMainWindow):
    def __init__(self, parent: 'AppointmentMenuGUI', controller: 'Controller'):
        """
        This window allows the user to retrieve notes based on text input.
        It displays a table of notes matching the keyword and has buttons for retrieving,
        clearing the search, and going back to the previous window.
        """
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.setWindowTitle("Retrieve Notes")
        self.setFixedWidth(600)
        self.setFixedHeight(400)

        self.note_table = QTableView()
        self.note_model = NoteTableModel(self.controller)
        self.note_table.setModel(self.note_model)

        self.retrieve_label = QLabel("Enter Text")
        self.retrieve_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_note_number = QLineEdit()
        self.retrieve_button = QPushButton("Retrieve")
        self.back_button = QPushButton("Back")
        self.clear_button = QPushButton("Clear")

        self.retrieve_button.clicked.connect(self.retrieve_button_clicked)
        self.clear_button.clicked.connect(self.clear_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)

        layout = QVBoxLayout()
        sub_layout = QGridLayout()
        layout.addWidget(self.note_table)
        sub_layout.addWidget(self.retrieve_label, 0, 0)
        sub_layout.addWidget(self.text_note_number, 0, 1)
        sub_layout.addWidget(self.back_button, 1, 0)
        sub_layout.addWidget(self.retrieve_button, 1, 1)
        sub_layout.addWidget(self.clear_button, 1, 2)
        layout.addLayout(sub_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def retrieve_button_clicked(self):
        """
        This function is called when the 'Retrieve' button is clicked.
        It tries to find notes matching the text entered by the user.
        If no notes are found or if there is no current patient, it shows an error message.
        """
        try:
            text_note_number = self.text_note_number.text().strip()
            self.note_model.keyword = text_note_number
            self.note_model.refresh_data()
            self.note_table.setColumnWidth(0, 100)
            self.note_table.setColumnWidth(1, 400)
            self.text_note_number.setEnabled(False)
            self.retrieve_button.setEnabled(False)
        except NoCurrentPatientException:
            QMessageBox.warning(self, "Failure", "Can not find the current patient!")
        except:
            QMessageBox.warning(self, "Failure", "There is no matching note!")

    def clear_button_clicked(self):
        """
        This function is called when the 'Clear' button is clicked.
        It resets the search and clears the input text.
        """
        self.note_model.reset()
        self.text_note_number.clear()
        self.text_note_number.setEnabled(True)
        self.retrieve_button.setEnabled(True)

    def back_button_clicked(self):
        """
        This function is called when the 'Back' button is clicked.
        It hides the current window and shows the parent window.
        """
        self.hide()
        self.parent.show()
