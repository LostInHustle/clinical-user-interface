from clinic.controller import Controller
from clinic.gui.create_patient_gui import CreatePatientGUI
from clinic.gui.search_patient_gui import SearchPatientGUI
from clinic.gui.choose_patient_gui import ChoosePatientGUI
from clinic.gui.update_patient_gui import UpdatePatientGUI
from clinic.gui.remove_patient_gui import RemovePatientGUI
from clinic.gui.retrieve_patient_gui import RetrievePatientGUI
from clinic.gui.list_patients_gui import ListPatientsGUI
from clinic.gui.appointment_menu_gui import AppointmentMenuGUI
from PyQt6.QtWidgets import QMainWindow, QGridLayout
from PyQt6.QtWidgets import QWidget, QPushButton

class MenuGUI(QMainWindow):
    def __init__(self, parent: 'ClinicGUI', controller: 'Controller'):
        ''' 
        This function is the constructor. It make the main menu window of the system.
        It add buttons for different patient and appointment actions. 
        Buttons are connected to their functions when clicked.
        '''
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.setWindowTitle("SYSTEM MENU")
        self.setFixedSize(300, 350)
        layout = QGridLayout()

        self.button_create = QPushButton("Add new patient")
        self.button_search = QPushButton("Search patient by PHN")
        self.button_retrieve = QPushButton("Retrieve patients by name")
        self.button_choose = QPushButton("Choose current patient")
        self.button_update = QPushButton("Update patient data")
        self.button_remove = QPushButton("Remove patient")
        self.button_list = QPushButton("List all patients")
        self.button_start = QPushButton("Start appointment with patient")
        self.button_logout = QPushButton("Log out")

        layout.addWidget(self.button_create, 0, 0)
        layout.addWidget(self.button_search, 1, 0)
        layout.addWidget(self.button_retrieve, 2, 0)
        layout.addWidget(self.button_choose, 3, 0)
        layout.addWidget(self.button_update, 4, 0)
        layout.addWidget(self.button_remove, 5, 0)
        layout.addWidget(self.button_list, 6, 0)
        layout.addWidget(self.button_start, 7, 0)
        layout.addWidget(self.button_logout, 8, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button_logout.clicked.connect(self.logout_button_clicked)
        self.button_create.clicked.connect(self.create_button_clicked)
        self.button_search.clicked.connect(self.search_button_clicked)
        self.button_choose.clicked.connect(self.choose_button_clicked)
        self.button_update.clicked.connect(self.update_button_clicked)
        self.button_remove.clicked.connect(self.remove_button_clicked)
        self.button_retrieve.clicked.connect(self.retrieve_button_clicked)
        self.button_list.clicked.connect(self.list_button_clicked)
        self.button_start.clicked.connect(self.start_appointment_clicked)

    def logout_button_clicked(self):
        ''' 
        This function is for logout button click. 
        It log out the user, hide the menu window, and show the login window again.
        '''
        self.controller.logout()
        self.hide()
        self.parent.show()

    def create_button_clicked(self):
        ''' 
        This function is for "Add new patient" button click.
        It hide the menu window and show the create patient window.
        '''
        self.hide()
        self.window = CreatePatientGUI(self, self.controller)
        self.window.show()

    def search_button_clicked(self):
        ''' 
        This function is for "Search patient by PHN" button click.
        It hide the menu window and show the search patient window.
        '''
        self.hide()
        self.window = SearchPatientGUI(self, self.controller)
        self.window.show()

    def choose_button_clicked(self):
        ''' 
        This function is for "Choose current patient" button click.
        It hide the menu window and show the choose patient window.
        '''
        self.hide()
        self.window = ChoosePatientGUI(self, self.controller)
        self.window.show()

    def update_button_clicked(self):
        ''' 
        This function is for "Update patient data" button click.
        It hide the menu window and show the update patient window.
        '''
        self.hide()
        self.window = UpdatePatientGUI(self, self.controller)
        self.window.show()

    def remove_button_clicked(self):
        ''' 
        This function is for "Remove patient" button click.
        It hide the menu window and show the remove patient window.
        '''
        self.hide()
        self.window = RemovePatientGUI(self, self.controller)
        self.window.show()

    def retrieve_button_clicked(self):
        ''' 
        This function is for "Retrieve patients by name" button click.
        It hide the menu window and show the retrieve patient window.
        '''
        self.hide()
        self.window = RetrievePatientGUI(self, self.controller)
        self.window.show()

    def list_button_clicked(self):
        ''' 
        This function is for "List all patients" button click.
        It hide the menu window and show the list all patients window.
        '''
        self.hide()
        self.window = ListPatientsGUI(self, self.controller)
        self.window.show()

    def start_appointment_clicked(self):
        ''' 
        This function is for "Start appointment with patient" button click.
        It hide the menu window and show the appointment menu window.
        '''
        self.hide()
        self.window = AppointmentMenuGUI(self, self.controller)
        self.window.show()
