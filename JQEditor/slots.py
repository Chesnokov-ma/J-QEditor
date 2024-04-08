from PyQt6.QtWidgets import QFileDialog, QMessageBox
from PyQt6.QtCore import pyqtSlot
from JQEditor.func import _check_cell_size
from math import sqrt


@pyqtSlot()
def read_button_clicked(self):
    """Кнопка чтения файла"""
    fpath = QFileDialog.getOpenFileName(caption='Чтение файла', filter="Data (*.dat *.txt);;All files (*.*)")[0]
    if fpath:
        try:
            self.n = int(sqrt(int(fpath.split('_')[0].replace('cell', '').split('/')[-1])))
            self.read_data(fpath)
        except:
            self.n = _check_cell_size(fpath)
            if self.n:
                self.read_data(fpath)
            else:
                QMessageBox.critical(self, 'Ошибка!', 'Неправильный формат файла!')


@pyqtSlot()
def write_button_clicked(self):
    """Кнопка записи файла"""
    if self.is_downloaded:
        try:
            fpath, _ = QFileDialog.getSaveFileName(None, 'Запись файла', '.',  'Dat (*.dat);;Text (*.txt)')
            self.write_data(fpath)
        except:
            pass


@pyqtSlot()
def all_up_button_clicked(self):
    """Кнопка все +=1"""
    if self.is_downloaded:
        val = 1
        self.all_down = True
        # self.all_down_button.setText('Все +1')

        self.verJ_val = [val for _ in range(self.n * self.n - self.n)]
        self.horJ_val = [val for _ in range(self.n * self.n - self.n)]
        self.update()


@pyqtSlot()
def all_down_button_clicked(self):
    """Кнопка все +=1"""
    if self.is_downloaded:
        val = -1
        self.all_down = True
        # self.all_down_button.setText('Все +1')

        self.verJ_val = [val for _ in range(self.n * self.n - self.n)]
        self.horJ_val = [val for _ in range(self.n * self.n - self.n)]
        self.update()


@pyqtSlot()
def invert_clicked(self):
    if self.is_downloaded:
        for i in range(len(self.verJ_val)):
            self.verJ_val[i] *= -1
            self.horJ_val[i] *= -1
        self.update()