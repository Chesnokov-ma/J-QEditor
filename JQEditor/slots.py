from PyQt6.QtWidgets import QFileDialog, QMessageBox, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QGuiApplication, QClipboard
from PyQt6.QtCore import pyqtSlot
from JQEditor.func import _check_cell_size
from math import sqrt


@pyqtSlot()
def read_button_clicked(self):
    """Кнопка чтения файла"""
    fpath = QFileDialog.getOpenFileName(caption='Чтение файла', filter="Data (*.dat *.txt);;All files (*.*)")[0]
    if fpath != '':
        try:
            self.n = int(sqrt(int(fpath.split('_')[0].replace('cell', '').split('/')[-1])))
            self.read_data(fpath)
        except:
            self.n = _check_cell_size(fpath)
            if self.n:
                self.read_data(fpath)
            else:
                QMessageBox.critical(self, 'Ошибка!', 'Неправильный формат файла!')

        self._update_app()


@pyqtSlot()
def write_button_clicked(self):
    """Кнопка записи файла"""
    if self.is_downloaded:
        try:
            fpath, _ = QFileDialog.getSaveFileName(None, 'Запись файла', '.',  'Dat (*.dat);;Text (*.txt)')
            self.write_data(fpath)
        except:
            pass

        self._update_app()


@pyqtSlot()
def all_up_button_clicked(self):
    """Кнопка все +=1"""
    if self.is_downloaded:
        val = 1
        self.all_down = True
        # self.all_down_button.setText('Все +1')

        self.verJ_val = [val for _ in range(self.n * self.n - self.n)]
        self.horJ_val = [val for _ in range(self.n * self.n - self.n)]
        self._update_app()


@pyqtSlot()
def all_down_button_clicked(self):
    """Кнопка все +=1"""
    if self.is_downloaded:
        val = -1
        self.all_down = True
        # self.all_down_button.setText('Все +1')

        self.verJ_val = [val for _ in range(self.n * self.n - self.n)]
        self.horJ_val = [val for _ in range(self.n * self.n - self.n)]
        self._update_app()


@pyqtSlot()
def invert_clicked(self):
    if self.is_downloaded:
        for i in range(len(self.verJ_val)):
            self.verJ_val[i] *= -1
            self.horJ_val[i] *= -1
        self._update_app()


@pyqtSlot()
def readmfsys_button_clicked(self):
    if self.is_downloaded:
        if self.spins_data.read_mfsys() == 0:
            self.mfsys_is_dowloaded = True
            self.spins_val = self.spins_data.spins_val
            self._update_app()

        elif self.spins_data.read_mfsys() == 1:
            QMessageBox.critical(self, 'Ошибка!', 'Неверный формат данных или размер')


# Ввод данных по спинам ==============================================================
class InputSpinsForm(QWidget):
    def __init__(self, data_array, n):
        super().__init__()
        self.setWindowTitle("Форма ввода данных")
        self.data_array = data_array
        self.size = n * n
        self.input_field = QLineEdit("".join(map(str, data_array)), self)
        self.copy_button = QPushButton("Копировать в буфер", self)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.done_button = QPushButton("Готово", self)
        self.done_button.clicked.connect(self.process_input)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Спины (N = f{self.size})"))
        layout.addWidget(self.input_field)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.done_button)
        self.setLayout(layout)

    def process_input(self):
        input_text = self.input_field.text()

        if len(input_text) == self.size and all(char in "01" for char in input_text):
            self.data_array[:] = [int(char) for char in input_text]
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", f"Строка должна содержать {self.size} символов (только 0 и 1).")

    def copy_to_clipboard(self):
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(self.input_field.text())


@pyqtSlot()
def show_spins_button_clicked(self):
    if self.is_downloaded:
        self.form = InputSpinsForm(self.spins_val, self.n)
        self.form.move
        self.form.show()
    