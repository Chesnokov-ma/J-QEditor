from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt6.QtGui import QIntValidator


class ScaleCellInputWindow(QMainWindow):
    from .scale_cell import _scale_cell

    def __init__(self, parent=None):
        """Масштабирование решетки"""
        super().__init__(parent)

        self.setWindowTitle("Новая система")
        self.inputLine = QLineEdit(self)
        self.inputLine_bh = QLineEdit(self)
        self.inputLine_bv = QLineEdit(self)
        self.text_bh = QLabel(self)
        self.text_bv = QLabel(self)
        self.inputLine.setPlaceholderText("Во сколько раз увеличить решетку?")

        self.button = QPushButton("Масштабировать решетку", self)
        self.button.clicked.connect(self._scale_cell)

        # валидатор для QLineEdit
        self.validator = QIntValidator(1, 99, self)
        self.inputLine.setValidator(self.validator)
        self.text_bh.setText('Горизонтальные угловые значения')
        self.text_bv.setText('Вертикальные угловые значения')
        self.inputLine_bh.setText('1')
        self.inputLine_bv.setText('1')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.inputLine)
        self.layout.addWidget(self.text_bh)
        self.layout.addWidget(self.inputLine_bh)
        self.layout.addWidget(self.text_bv)
        self.layout.addWidget(self.inputLine_bv)
        self.layout.addWidget(self.button)

        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)