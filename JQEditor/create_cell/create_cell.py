from PyQt6.QtWidgets import QMessageBox


def _create_cell(self):
    """Создать пустую решетку """
    if self.inputLine.text() == '':
        return

    n = int(self.inputLine.text())
    if (n < 2) or (n > 25):
        QMessageBox.critical(self, 'Ошибка!',
                             'Размер решетки (количество спинов - по вертикали или горизонтали)'
                             ' должен быть в пределах от 2 до 25.')
        return

    else:
        w, h = n * n, n * n
        matrix = [[0 for x in range(w)] for y in range(h)]

        matrix[0][1] = 1
        matrix[0][n] = 1

        matrix[1][0] = 1
        matrix[n][0] = 1

        for i in range(w - 1):
            matrix[i][1 + i] = 1
            matrix[1 + i][i] = 1

        for i in range(w - n):
            matrix[i][n + i] = 1
            matrix[n + i][i] = 1

        filename = f'cell{n * n}_tmp'
        with open(filename, 'w') as f:
            for i in range(h):
                for j in range(w):
                    f.write(f'{matrix[i][j]} ')
                f.write('\n')

        self.parent().read_tmp_cell(n, filename)
        self.close()
