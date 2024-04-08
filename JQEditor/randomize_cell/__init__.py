from PyQt6.QtCore import pyqtSlot
from JQEditor.randomize_cell.randomize_cell_input_window import RandomizeCellInputWindow


@pyqtSlot()
def randomize_cell(self):
    if self.is_downloaded:
        self.secondWindow = RandomizeCellInputWindow(self)
        self.secondWindow.show()