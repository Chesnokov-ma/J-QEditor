from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QIntValidator


class CreateCellInputWindow(QMainWindow):
    from .create_cell import _create_cell

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Новая система")
        self.inputLine = QLineEdit(self)
        self.inputLine.setPlaceholderText("Введите n")
        self.button = QPushButton("Создать решетку", self)
        self.button.setFocus()
        self.button.clicked.connect(self._create_cell)

        # валидатор для QLineEdit
        self.validator = QIntValidator(1, 99, self)
        self.inputLine.setValidator(self.validator)
        self.inputLine.setText(f'{10}')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.inputLine)
        self.layout.addWidget(self.button)

        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)