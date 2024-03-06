from PyQt6.QtCore import pyqtSlot
from JQEditor.scaler.scale_cell_input_window import ScaleCellInputWindow


@pyqtSlot()
def scale_cell(self):
    if self.is_downloaded:
        self.secondWindow = ScaleCellInputWindow(self)
        self.secondWindow.show()
