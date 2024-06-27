from math import sqrt


def _read_tmp_cell(self, n, filename):
    self.n = n
    self.read_data(filename, True)


def _check_cell_size(file_path):
    line_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line == '\n':
                break
            else:
                line_count += 1

    n = sqrt(line_count)
    return int(n) if n.is_integer() else None


def _set_numbers(self):
    self.numbers_drown = True
    self.update()


def _clear_numbers(self):
    self.numbers_drown = False
    self.update()

