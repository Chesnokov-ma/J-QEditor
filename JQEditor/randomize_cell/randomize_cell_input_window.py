from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QCheckBox
from PyQt6.QtGui import QIntValidator


class RandomizeCellInputWindow(QMainWindow):
    from .randomize_cell import _randomize_cell

    def __init__(self, parent=None):
        """Переворот случайных спинов"""
        super().__init__(parent)

        self.setWindowTitle("Случайные спины")
        self.inputLine = QLineEdit(self)
        self.button = QPushButton("Начать", self)
        self.inputLine.setPlaceholderText("Количество итераций")
        self.button.clicked.connect(self._randomize_cell)

        # валидатор для QLineEdit
        self.validator = QIntValidator(1, 999999, self)
        self.inputLine.setValidator(self.validator)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.inputLine)

        self.layout.addWidget(self.button)

        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)