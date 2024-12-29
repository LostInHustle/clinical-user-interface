from clinic.controller import Controller
from clinic.gui.create_note_gui import CreateNoteGUI
from clinic.gui.update_note_gui import UpdateNoteGUI
from clinic.gui.remove_note_gui import RemoveNoteGUI
from clinic.gui.retrieve_note_gui import RetrieveNoteGUI
from clinic.gui.list_notes_gui import ListNotesGUI
from PyQt6.QtWidgets import QMainWindow, QGridLayout
from PyQt6.QtWidgets import QWidget, QPushButton, QMessageBox

class AppointmentMenuGUI(QMainWindow):
    def __init__(self, parent: 'MenuGUI', controller: 'Controller'):
        """
        This is the Appointment Menu screen.
        It has buttons for adding, updating, removing, retrieving, 
        and listing appointment notes. Also, a back button to return 
        to the previous menu.
        """
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.setWindowTitle("APPOINTMENT MENU")
        self.setFixedSize(250, 275)
        layout = QGridLayout()

        self.button_create = QPushButton("Add new note")
        self.button_retrieve = QPushButton("Retrieve notes by key")
        self.button_update = QPushButton("Update note")
        self.button_remove = QPushButton("Remove note")
        self.button_list = QPushButton("List all notes")
        self.button_goback = QPushButton("Back")

        layout.addWidget(self.button_create, 0, 0)
        layout.addWidget(self.button_retrieve, 1, 0)
        layout.addWidget(self.button_update, 2, 0)
        layout.addWidget(self.button_remove, 3, 0)
        layout.addWidget(self.button_list, 4, 0)
        layout.addWidget(self.button_goback, 5, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button_create.clicked.connect(self.create_button_clicked)
        self.button_update.clicked.connect(self.update_button_clicked)
        self.button_remove.clicked.connect(self.remove_button_clicked)
        self.button_retrieve.clicked.connect(self.retrieve_button_clicked)
        self.button_list.clicked.connect(self.list_button_clicked)
        self.button_goback.clicked.connect(self.goback_button_clicked)

    def goback_button_clicked(self):
        """
        This function is called when the 'Back' button is clicked.
        It hides the current window and shows the parent window.
        """
        self.hide()
        self.parent.show()

    def create_button_clicked(self):
        """
        This function is called when the 'Add new note' button is clicked.
        It hides the current window and shows the CreateNoteGUI window.
        """
        self.hide()
        self.window = CreateNoteGUI(self, self.controller)
        self.window.show()

    def update_button_clicked(self):
        """
        This function is called when the 'Update note' button is clicked.
        It hides the current window and shows the UpdateNoteGUI window.
        """
        self.hide()
        self.window = UpdateNoteGUI(self, self.controller)
        self.window.show()

    def remove_button_clicked(self):
        """
        This function is called when the 'Remove note' button is clicked.
        It hides the current window and shows the RemoveNoteGUI window.
        """
        self.hide()
        self.window = RemoveNoteGUI(self, self.controller)
        self.window.show()

    def retrieve_button_clicked(self):
        """
        This function is called when the 'Retrieve notes by key' button is clicked.
        It hides the current window and shows the RetrieveNoteGUI window.
        """
        self.hide()
        self.window = RetrieveNoteGUI(self, self.controller)
        self.window.show()

    def list_button_clicked(self):
        """
        This function is called when the 'List all notes' button is clicked.
        It hides the current window and shows the ListNotesGUI window.
        If the current patient is not found, it shows a warning message.
        """
        self.hide()
        try:
            self.window = ListNotesGUI(self, self.controller)
            self.window.show()
        except:
            QMessageBox.warning(self, "Failure", "Can not find the current patient!")
            self.show()
