from PyQt6.QtWidgets import QMessageBox
from os import path, mkdir


def _scale_cell(self):
    """Масштабировать решетку"""
    if self.inputLine.text() == '':
        return

    scale = int(self.inputLine.text())
    if (scale < 2) or (scale > 20):
        QMessageBox.critical(self, 'Ошибка!',
                             'Увеличение масштаба должно быть в пределах от 2 до 20.')
        return

    n = self.parent().n
    N = n * scale  # размер увеличенной решетки

    # угловые значения
    if self.inputLine_bh.text() == '' or self.inputLine_bv.text() == '':
        return

    try:
        border_v_val = int(self.inputLine_bv.text())
        border_h_val = int(self.inputLine_bh.text())

        if border_v_val != -1:
            if border_v_val != 1:
                raise

        if border_h_val != -1:
            if border_h_val != 1:
                raise

    except:
        QMessageBox.critical(self, 'Ошибка!',
                             'Разрешенные угловые значения: 1 и -1')
        return

    verJ_val_scaled = []
    horJ_val_scaled = []

    # 1. Горизонтальные связи
    row = 0
    skip = 0
    for i in range(scale):  # масштабирование по вертикали
        row = 0
        for j in range(n):  # масштабирование по горизонтали
            for _ in range(scale):
                for h in range(n - 1):  # повторять ряд
                    # print(self.parent().horJ_val[row + h], end=' ')  # первые n-1 значений в ряду
                    horJ_val_scaled.append(self.parent().horJ_val[row + h])

                # угловые значения
                if skip != (scale - 1):
                    # print(border_h_val, end='    ')
                    horJ_val_scaled.append(border_v_val)
                    skip += 1
                else:
                    # print()
                    skip = 0

            row += (n - 1)  # перейти на другой ряд
        print()

    # 2. Вертикальные связи
    row = 0
    skip = 0
    for i in range(scale):  # масштабирование по горизонтали
        row = 0
        for j in range(n - 1):  # масштабирование по вертикали
            for _ in range(scale):
                for v in range(n):
                    # print(self.parent().verJ_val[row + v], end=' ')
                    verJ_val_scaled.append(self.parent().verJ_val[row + v])
                # print('    ', end='')
            # print()
            row += n

        if skip != (scale - 1):
            for _ in range(scale):
                for v in range(n):
                    # print(border_v_val, end=' ')
                    verJ_val_scaled.append(border_h_val)
                # print('    ', end='')
            # print()
            skip += 1
        else:
            skip = 0
        # print()

    # 3. Запись в файл масштабированной решетки
    if not path.exists('./scaled/'):
        mkdir('./scaled/')

    # Например, для решетки из 9 спинов (N)
    # 81 знаков по вертикали, 81 по горизонтали
    # 9 * 9 * 9 * 9 -> размер J_full_scaled
    J_full_scaled = [0 for _ in range(N ** 4)]

    k = 1
    for i in range(N):
        for j in range(N - 1):
            J_full_scaled[k] = horJ_val_scaled[i * (N - 1) + j]
            k += N * N + 1
        k += N * N + 1

    k = N
    for i in range(N - 1):
        for j in range(N):
            J_full_scaled[k] = verJ_val_scaled[i * N + j]
            k += N * N + 1

    with open(f'./scaled/cell{N * N}_scaled.dat', 'w') as f:
        symbols = 0
        for j in J_full_scaled:
            f.write(f'{j} ')
            symbols += 1
            if symbols == N * N:
                f.write('\n')
                symbols = 0

    # 4. Закрыть окно
    self.close()
