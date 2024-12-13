from clinic.patient import *
from clinic.controller import *
from PyQt6.QtCore import Qt, QAbstractTableModel

class PatientTableModel(QAbstractTableModel):
    """
    This class provides the model for displaying patient data in a table.
    It fetches patient data from the controller and allows interaction with it.
    Supports patient retrieval based on a keyword and listing all patients.
    """
    def __init__(self, controller: 'Controller'):
        super().__init__()
        self.controller = controller
        self.keyword = ''
        self._data = []

    def refresh_data(self):
        """
        Refreshes the data based on the current keyword.
        Fetches patients from the controller based on the keyword and updates the table data.
        """
        self._data = []
        patients = self.controller.retrieve_patients(self.keyword)
        if (self.keyword == '') or (not patients):
            raise Exception()
        for patient in patients:
            single_data = [patient.phn, patient.name, patient.birth_date, patient.phone, patient.email, patient.address]
            self._data.append(single_data)
        self.layoutChanged.emit()

    def list_data(self):
        """
        Lists all patients.
        Fetches all patients from the controller and populates the table with their data.
        """
        self._data = []
        patients = self.controller.list_patients()
        for patient in patients:
            single_data = [patient.phn, patient.name, patient.birth_date, patient.phone, patient.email, patient.address]
            self._data.append(single_data)
        self.layoutChanged.emit()

    def reset(self):
        """
        Resets the table data.
        Clears the data and refreshes the layout.
        """
        self._data = []
        self.layoutChanged.emit()

    def data(self, index, role):
        """
        Returns the data to display for a specific cell in the table.
        Handles formatting for different data types (string, float, etc.).
        """
        value = self._data[index.row()][index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
            if isinstance(value, float):
                return "%.2f" % value
            if isinstance(value, str):
                return '%s' % value
            return value
        if role == Qt.ItemDataRole.TextAlignmentRole:
            if isinstance(value, int) or isinstance(value, float):
                return Qt.AlignmentFlag.AlignVCenter + Qt.AlignmentFlag.AlignRight

    def rowCount(self, index):
        """
        Returns the number of rows in the table.
        """
        return len(self._data)

    def columnCount(self, index):
        """
        Returns the number of columns in the table.
        """
        if self._data:
            return len(self._data[0])
        else:
            return 0

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        """
        Returns the header data for the table.
        Provides column names for the table's headers.
        """
        headers = ['Phn', 'Name', 'Birthdate', 'Phone', 'Email', 'Address']
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return '%s' % headers[section]
        return super().headerData(section, orientation, role)