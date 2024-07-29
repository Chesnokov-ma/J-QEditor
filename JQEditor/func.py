from JQEditor.JQ_plt.model0 import draw_model0
from math import sqrt


def _update_app(self):
    self.update_info(self.calc_shown)
    self.update()


def update_info(self, show):
    if show:
        self.calc.get_E(self.n, self.spins_data.spins_val, self.horJ_val, self.verJ_val)
        self.calc.get_Jsum_P(self.n, self.horJ_val, self.verJ_val)
        self.calc.get_fp_p(self.n, self.horJ_val, self.verJ_val)
    self.calc.update_info(show)


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
    if self.is_downloaded:
        self.numbers_drown = True
        self.spins_drown = True
        self._update_app()


def _clear_numbers(self):
    if self.is_downloaded:
        self.numbers_drown = False
        self.spins_drown = False
        self._update_app()


def _only_spins(self):
    if self.is_downloaded:
        self.numbers_drown = False
        self.spins_drown = True
        self._update_app()


def _only_j(self):
    if self.is_downloaded:
        self.numbers_drown = True
        self.spins_drown = False
        self._update_app()


def _background_color_0(self):
    if self.is_downloaded:
        self.background_color = 0
        self._update_app()


def _background_color_1(self):
    if self.is_downloaded:
        self.background_color = 1
        self._update_app()


def _background_color_2(self):
    if self.is_downloaded:
        self.background_color = 2
        self._update_app()


def _calc_shown(self):
    if self.is_downloaded:
        self.calc_shown = True


def _calc_not_shown(self):
    if self.is_downloaded:
        self.calc_shown = False


def _save_qimage(self):
    if self.is_downloaded:
        self.saveChessBoard(self.qp)


def _run_model0(self):
    if self.is_downloaded:
        draw_model0(self.n, self.horJ_val, self.verJ_val)
