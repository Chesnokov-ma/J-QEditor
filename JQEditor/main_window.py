from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon


class MainWindow(QMainWindow):
    """
    Главное окно приложения
    """

    from .read_write_data import read_data, write_data
    from .slots import read_button_clicked, write_button_clicked, all_down_button_clicked
    from .events import paintEvent, mousePressEvent
    from .draw_chess_board import drawChessBoard
    from .func import read_tmp_cell
    from .create_cell import create_cell
    from .scaler import scale_cell

    n = None    # размер системы
    is_downloaded = False   # загружен ли файл в память?
    all_down = False    # все спины вниз?
    J_full = []     # связи каждый-с-каждым
    verJ_val = []; horJ_val = []    # вертикальные; горизонтальные связи между соседними спинами
    spins = []; ver = []; hor = []
    y_offset = 160  # отступ для корректной отрисовки окна

    secondWindow = None

    def __init__(self, parent=None):
        """
        Инициализация главного окна
        """
        super().__init__(parent)
        self.setWindowTitle('J QEditor')
        self.resize(600, 600 + self.y_offset)
        self.setWindowIcon(QIcon('./resources/icon.png'))

        self.main_widget = QWidget()
        paint_widget = QWidget()
        paint_widget.resize(600, 600)
        main_layout = QVBoxLayout()
        main_layout.addWidget(paint_widget)
        read_button = QPushButton('Выбрать файл')
        write_button = QPushButton('Записать в файл')
        self.all_down_button = QPushButton('Все -1')
        self.create_button = QPushButton('Создать систему')
        self.scale_button = QPushButton('Масштабировать систему')

        # добавить кнопки
        main_layout.addWidget(read_button)
        main_layout.addWidget(self.all_down_button)
        main_layout.addWidget(write_button)
        main_layout.addWidget(self.create_button)
        main_layout.addWidget(self.scale_button)

        # установить main_widget как центральный виджет
        self.main_widget.setLayout(main_layout)
        self.setCentralWidget(self.main_widget)

        # slots (connect обработки нажатия кнопок)
        read_button.clicked.connect(self.read_button_clicked)
        write_button.clicked.connect(self.write_button_clicked)
        self.all_down_button.clicked.connect(self.all_down_button_clicked)
        self.create_button.clicked.connect(self.create_cell)
        self.scale_button.clicked.connect(self.scale_cell)

