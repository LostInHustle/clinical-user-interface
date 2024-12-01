from clinic.note import *
from clinic.controller import *
from PyQt6.QtCore import Qt, QAbstractTableModel

class NoteTableModel(QAbstractTableModel):
    """
    This class represents a table model for displaying notes in a QTableView.
    It allows retrieval and listing of notes, including filtering by a keyword.
    """
    def __init__(self, controller: 'Controller'):
        super().__init__()
        self.controller = controller
        self.keyword = ''
        self._data = []

    def refresh_data(self):
        """
        Refreshes the data based on the current keyword.
        Retrieves notes from the controller based on the keyword and updates the table data.
        """
        self._data = []
        notes = self.controller.retrieve_notes(self.keyword)
        if (self.keyword == '') or (not notes):
            raise Exception()
        for note in notes:
            single_data = [note.code, note.text]
            self._data.append(single_data)
        self.layoutChanged.emit()

    def list_data(self):
        """
        Lists all notes in reverse order.
        Retrieves all notes from the controller and populates the table with their data.
        """
        self._data = []
        notes = self.controller.list_notes()
        for note in notes:
            single_data = [note.code, note.text]
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
        Handles formatting for different data types (string, int, etc.).
        """
        value = self._data[index.row()][index.column()]
        if role == Qt.ItemDataRole.DisplayRole:
            if isinstance(value, int):
                return "%d" % value
            if isinstance(value, str):
                return '%s' % value
            return value
        if role == Qt.ItemDataRole.TextAlignmentRole:
            if isinstance(value, int):
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
        headers = ['Code', 'Description']
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return '%s' % headers[section]
        return super().headerData(section, orientation, role)