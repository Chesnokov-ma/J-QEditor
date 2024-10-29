from PyQt6.QtWidgets import QMessageBox, QFileDialog
from os import path, mkdir
import time
import random


def _randomize_cell(self):

    # чтение данных формы и проверка
    if self.inputLine.text() == '':
        return

    iter_times = int(self.inputLine.text())
    if (iter_times <= 0) or (iter_times > 100000):
        QMessageBox.critical(self, 'Ошибка!',
                             'Количество итераций должно быть > 0 и < 100000.')
        return

    self.close()
    n = self.parent().n

    random_spins = []
    for i in range(iter_times):
        current_spin = random.randint(0, n * n - 1)
        random_spins.append(current_spin)

        # 1. Найти 2 соседних спина по горизонтали
        left_j = None
        if current_spin % n != 0:
            left_j = 0
            for j in range(current_spin):
                if j % n != 0:
                    left_j += 1

        right_j = None
        if (current_spin + 1) % n != 0:
            right_j = 0
            for j in range(current_spin):
                if (j + 1) % n != 0:
                    right_j += 1

        # print(f'{current_spin}\t{left_j}\t{right_j}')

        # 2. Найти 2 соседних спина по вертикали
        top_j = None
        if current_spin >= n:
            top_j = 0
            for j in range(current_spin):
                if j >= n:
                    top_j += 1

        bot_j = None
        if current_spin < (n * n - n):
            bot_j = 0
            for j in range(current_spin):
                if j < (n * n - n):
                    bot_j += 1

        # print(f'{current_spin}\t{top_j}\t{bot_j}\n')

        # 3. Перевернуть спины
        for j in (left_j, right_j):
            if j:
                self.parent().horJ_val[j] *= -1

        for j in (top_j, bot_j):
            if j:
                self.parent().verJ_val[j] *= -1

        # print(current_spin)

        # обновить информацию о системе
        self.parent().update_info(True)


    # записать результат
    # fpath, _ = QFileDialog.getSaveFileName(None, 'Запись файла', f'./cell{n * n}_rand.dat', 'Dat (*.dat);;Text (*.txt)')
    # if fpath:

        # self.parent().write_data(fpath)
        #
        # # записать случайные спины
        # spins_fpath = f"{'/'.join(fpath.split('/')[:-1])}/spins{n * n}_{len(random_spins)}rand.txt"
        # with open(spins_fpath, 'w') as f:
        #     for spin in random_spins:
        #         f.write(f'{spin}, ')
