from clinic.controller import Controller
from clinic.gui.note_table_model import NoteTableModel
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QVBoxLayout, QTableView
from PyQt6.QtWidgets import QWidget, QPushButton

class ListNotesGUI(QMainWindow):
    def __init__(self, parent: 'AppointmentMenuGUI', controller: 'Controller'):
        """
        This window lists all notes for the current patient.
        It displays a table of notes and has a button to go back to the previous window.
        """
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.setWindowTitle("List Notes")
        self.resize(600, 400)

        self.note_table = QTableView()
        self.note_model = NoteTableModel(self.controller)
        self.note_table.setModel(self.note_model)
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.back_button_clicked)
        
        layout = QVBoxLayout()
        sub_layout = QGridLayout()
        sub_layout.addWidget(self.back_button, 0, 0)
        layout.addWidget(self.note_table)
        layout.addLayout(sub_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.note_model.list_data()
        self.note_table.setColumnWidth(0, 100)
        self.note_table.setColumnWidth(1, 400)

    def back_button_clicked(self):
        """
        This function is called when the 'Back' button is clicked.
        It hides the current window and shows the parent window.
        """
        self.hide()
        self.parent.show()