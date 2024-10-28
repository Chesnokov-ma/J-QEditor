from PyQt6.QtGui import QAction
import sys


def create_menu(self):
    file_menu = self.menuBar().addMenu("&Файл")
    action_menu = self.menuBar().addMenu("&Действие")
    design_menu = self.menuBar().addMenu("&Вид")
    calc_menu = self.menuBar().addMenu("&Калькулятор")
    help_menu = self.menuBar().addMenu("&Справка")

    # Файл - Новый
    new_action = QAction("&Новый", self)
    new_action.setShortcut("Ctrl+N")
    new_action.triggered.connect(self.create_cell)
    file_menu.addAction(new_action)

    # Файл - Открыть
    open_action = QAction("&Открыть", self)
    open_action.setShortcut("Ctrl+O")
    open_action.triggered.connect(self.read_button_clicked)
    file_menu.addAction(open_action)

    # Файл - Загрузить спины
    spin_action = QAction("&Загрузить спины", self)
    # open_action.setShortcut("Ctrl+O")
    spin_action.triggered.connect(self.readmfsys_button_clicked)
    file_menu.addAction(spin_action)

    # Файл - Сохранить как
    save_action = QAction("&Сохранить как", self)
    save_action.setShortcut("Ctrl+S")
    save_action.triggered.connect(self.write_button_clicked)
    file_menu.addAction(save_action)

    file_menu.addSeparator()

    # Файл - Выйти
    exit_action = QAction("&Выйти", self)
    exit_action.triggered.connect(lambda: sys.exit())
    file_menu.addAction(exit_action)

    # Действие - Все +-1
    all_up = QAction("&Все +1", self)
    all_down = QAction("&Все -1", self)
    all_up.triggered.connect(self.all_up_button_clicked)
    all_down.triggered.connect(self.all_down_button_clicked)
    action_menu.addAction(all_up)
    action_menu.addAction(all_down)

    invert = QAction("&Инвертировать", self)
    invert.setShortcut("Ctrl+I")
    invert.triggered.connect(self.invert_clicked)
    action_menu.addAction(invert)

    action_menu.addSeparator()

    # Действие - Масштабировать
    scale_action = QAction("&Масштабировать", self)
    scale_action.setShortcut("Ctrl+M")
    scale_action.triggered.connect(self.scale_cell)
    action_menu.addAction(scale_action)

    # Действие - Переворот
    random_action = QAction("&Перевернуть случайные спины", self)
    random_action.setShortcut("R")
    random_action.triggered.connect(self.randomize_cell)
    action_menu.addAction(random_action)
    action_menu.addSeparator()

    # Действие - Скриншот
    screenshot_action = QAction("&Скриншот", self)
    action_menu.addAction(screenshot_action)
    screenshot_action.triggered.connect(self._save_qimage)

    # Действие - Модель (matplotlib grid)
    # plt_model0_action = QAction("&Модель (matplotlib grid)", self)
    # action_menu.addAction(plt_model0_action)
    # plt_model0_action.triggered.connect(self._run_model0)

    # Вид
    numbers_drawn_action = QAction("&Все подписи", self)
    numbers_not_drawn_action = QAction("&Подписи отсутствуют", self)
    only_spins_drawn_action = QAction("&Только спины", self)
    only_j_drawn_action = QAction("&Только связи (+-J)", self)

    default_background = QAction("&Стандартный фон", self)
    white_background = QAction("&Белый фон", self)
    gray_background = QAction("&Серый фон", self)

    numbers_drawn_action.triggered.connect(self._set_numbers)
    numbers_not_drawn_action.triggered.connect(self._clear_numbers)
    only_spins_drawn_action.triggered.connect(self._only_spins)
    only_j_drawn_action.triggered.connect(self._only_j)

    default_background.triggered.connect(self._background_color_0)
    white_background.triggered.connect(self._background_color_1)
    gray_background.triggered.connect(self._background_color_2)

    design_menu.addAction(numbers_drawn_action)
    design_menu.addAction(numbers_not_drawn_action)
    design_menu.addAction(only_spins_drawn_action)
    design_menu.addAction(only_j_drawn_action)

    design_menu.addSeparator()

    design_menu.addAction(default_background)
    design_menu.addAction(white_background)
    design_menu.addAction(gray_background)

    # Калькулятор
    # calc_shown = QAction("&Включен", self)
    # calc_not_shown = QAction("&Выключен", self)

    # calc_shown.triggered.connect(self._calc_shown)
    # calc_not_shown.triggered.connect(self._calc_not_shown)

    # calc_menu.addAction(calc_shown)
    # calc_menu.addAction(calc_not_shown)

    # Справка
    help_1 = QAction("&Масштабирование", self)
    help_2 = QAction("&Случайные спины", self)
    help_3 = QAction("&О программе", self)

    help_menu.addAction(help_1)
    help_menu.addAction(help_2)
    help_menu.addSeparator()
    help_menu.addAction(help_3)




