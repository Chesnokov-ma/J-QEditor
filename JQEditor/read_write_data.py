from os import path, remove


def read_data(self, file_name, del_input_file=False):
    """Прочитать решетку из файла"""
    self.verJ_val = [0 for _ in range(self.n * self.n - self.n)]
    self.horJ_val = [0 for _ in range(self.n * self.n - self.n)]

    self.J_full = []

    with open(file_name, 'r') as f:
        for line in f:
            for elem in line.replace('\n', '').split(' '):
                if elem:
                    self.J_full.append(int(elem))

    k = 1
    for i in range(self.n):
        for j in range(self.n - 1):
            self.horJ_val[i * (self.n - 1) + j] = self.J_full[k]
            k += self.n * self.n + 1
        k += self.n * self.n + 1

    k = self.n
    for i in range(self.n - 1):
        for j in range(self.n):
            self.verJ_val[i * self.n + j] = self.J_full[k]
            k += self.n * self.n + 1

    # удалить временный файл с пустой решеткой
    if del_input_file:
        if path.exists(file_name):
            remove(file_name)

    self.is_downloaded = True
    self.mfsys_is_dowloaded = False

    # Задать единичное пространство между спинами
    self.spins_data.make_default_Ising(self.n)
    self.spins_val = self.spins_data.spins_val

    # обновить внешний вид приложения
    self._update_app()


def write_data(self, file_name):
    """Запись в файл (то же что и read_data(), только наоборот)"""
    k = 1
    for i in range(self.n):
        for j in range(self.n - 1):
            self.J_full[k] = self.horJ_val[i * (self.n - 1) + j]
            k += self.n * self.n + 1
        k += self.n * self.n + 1

    k = self.n
    for i in range(self.n - 1):
        for j in range(self.n):
            self.J_full[k] = self.verJ_val[i * self.n + j]
            k += self.n * self.n + 1

    with open(file_name, 'w') as f:
        symbols = 0
        for j in self.J_full:
            f.write(f'{j} ')
            symbols += 1
            if symbols == self.n * self.n:
                f.write('\n')
                symbols = 0