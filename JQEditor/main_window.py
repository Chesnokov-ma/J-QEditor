from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon

from JQEditor.spins_module import SpinData
from JQEditor.calculator import Calculator

class MainWindow(QMainWindow):
    """
    Главное окно приложения
    """

    from .read_write_data import read_data, write_data
    from .slots import read_button_clicked, write_button_clicked, all_down_button_clicked, \
        all_up_button_clicked, invert_clicked, readmfsys_button_clicked
    from .events import paintEvent, mousePressEvent
    from .draw_chess_board import drawChessBoard
    from .func import _read_tmp_cell, _set_numbers, _clear_numbers
    from .create_cell import create_cell
    from .scaler import scale_cell
    from .randomize_cell import randomize_cell
    from .form_menu import create_menu


    n = None    # размер системы
    is_downloaded = False   # загружен ли файл в память
    mfsys_is_downloaded = False
    numbers_drown = True

    all_down = False    # все спины вниз
    J_full = []     # связи каждый-с-каждым
    verJ_val = []; horJ_val = []    # вертикальные; горизонтальные связи между соседними спинами
    spins = []; ver = []; hor = []  # прямоугольники для обработки нажатий
    spins_val = []

    x_offset = 0
    y_offset = 120  # отступ для корректной отрисовки окна

    secondWindow = None

    def __init__(self, parent=None):
        """
        Инициализация главного окна
        """
        super().__init__(parent)
        self.setWindowTitle('J QEditor')
        self.resize(600 + self.x_offset, 620 + self.y_offset)
        self.setWindowIcon(QIcon('./resources/icon.png'))
        self.create_menu()

        self.spins_data = SpinData()
        self.calc = Calculator()

        self.main_widget = QWidget()
        paint_widget = QWidget()
        paint_widget.resize(600, 100)
        main_layout = QVBoxLayout()
        main_layout.addWidget(paint_widget)

        # read_button = QPushButton('Выбрать файл')
        # write_button = QPushButton('Записать в файл')
        # self.all_down_button = QPushButton('Все -1')
        self.create_button = QPushButton('Создать систему')
        self.scale_button = QPushButton('Масштабировать систему')
        self.randomize_button = QPushButton('Перевернуть случайные спины')

        # добавить кнопки
        # main_layout.addWidget(self.create_button)
        # main_layout.addWidget(self.scale_button)
        # main_layout.addWidget(self.randomize_button)

        # установить main_widget как центральный виджет
        # main_layout.setContentsMargins(0, 20, 0, 0)
        self.main_widget.setLayout(main_layout)
        self.setCentralWidget(self.main_widget)

        # slots (connect обработки нажатия кнопок)
        # read_button.clicked.connect(self.read_button_clicked)
        # write_button.clicked.connect(self.write_button_clicked)
        # self.all_down_button.clicked.connect(self.all_down_button_clicked)
        self.create_button.clicked.connect(self.create_cell)
        self.scale_button.clicked.connect(self.scale_cell)
        self.randomize_button.clicked.connect(self.randomize_cell)

