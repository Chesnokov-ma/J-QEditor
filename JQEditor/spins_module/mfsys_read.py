from PyQt6.QtWidgets import QFileDialog
from math import sqrt


def read_mfsys(self):
    fpath = QFileDialog.getOpenFileName(caption='Чтение файла', filter="Data (*.mfsys);;All files (*.*)")[0]

    try:
        with open(fpath, 'r') as f:
            read_info = f.readlines()
    except FileNotFoundError:
        return

    try:
        n = sqrt(int(read_info[4].replace('size=', '').replace('\n', '')))
        if n != self.real_n:
            raise TypeError
    except TypeError:
        return 1

    self._current_spins_val = [int(s) for s in read_info[7].replace('state=', '').replace('\n', '')]
    self._min_state = [int(s) for s in read_info[8].replace('minstate=', '').replace('\n', '')]
    self._max_state = [int(s) for s in read_info[9].replace('maxstate=', '').replace('\n', '')]

    self._points = []
    for i in range(14, 9999):
        sp = read_info[i].split('\t')
        self._points.append((sp[1], sp[2]))
        if '[' in read_info[i + 1]:
            break

    return 0