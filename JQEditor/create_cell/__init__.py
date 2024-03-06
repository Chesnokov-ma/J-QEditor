from PyQt6.QtCore import pyqtSlot
from JQEditor.create_cell.create_cell_input_window import CreateCellInputWindow


@pyqtSlot()
def create_cell(self):
    self.secondWindow = CreateCellInputWindow(self)
    self.secondWindow.show()