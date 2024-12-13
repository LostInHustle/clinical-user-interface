import sys
from clinic.controller import *
from clinic.gui.menu_gui import MenuGUI
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class ClinicGUI(QMainWindow):
    def __init__(self):
        '''
        This function is the constructor. It create main window of the clinic system.
        It also make the layout, input box for username and password, and buttons for login and quit.
        It connects buttons to their functions when clicked.
        '''
        super().__init__()
        self.controller = Controller(autosave = True)
        self.setWindowTitle("MEDICAL CLINIC SYSTEM")
        layout = QGridLayout()

        label_username = QLabel("Username")
        self.text_username = QLineEdit()
        label_password = QLabel("Password")
        self.text_password = QLineEdit()
        self.text_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.button_login = QPushButton("Login")
        self.button_quit = QPushButton("Quit")

        layout.addWidget(label_username, 0, 0)
        layout.addWidget(self.text_username, 0, 1)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.text_password, 1, 1)
        layout.addWidget(self.button_quit, 2, 0)
        layout.addWidget(self.button_login, 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button_login.clicked.connect(self.login_button_clicked)
        self.button_quit.clicked.connect(self.quit_button_clicked)

    def login_button_clicked(self):
        ''' 
        This function is for login button click.
        It takes the username and password from input boxes, then try to login using controller.
        If login is successful, it hide the current window and open the main menu.
        If login fails, it show a warning message box to user.
        After that, it clear the username and password input boxes.
        '''
        usrName = self.text_username.text().strip()
        passWord = self.text_password.text().strip()

        try:     
            if (self.controller.login(usrName, passWord)):
                self.hide()
                self.window = MenuGUI(self, self.controller)
                self.window.show()
        except:
            QMessageBox.warning(self, "Login Failed", "Wrong username or password...")

        self.text_username.clear()
        self.text_password.clear()

    def quit_button_clicked(self):
        ''' 
        This function is for quit button click.
        When clicked, it close the application.
        '''
        QApplication.quit()

def main():
    ''' 
    This function start the application.
    It create the main window of the clinic system and show it.
    Then, it run the application until the user close it.
    '''
    app = QApplication(sys.argv)
    window = ClinicGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()