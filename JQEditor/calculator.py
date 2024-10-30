from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton


class Calculator:
    current_E0 = 0
    current_size = 0
    cur_n = 0
    current_Jsum = 0
    current_P = 0
    current_fp_p = 0
    current_fp_m = 0
    current_fp_sum = 0

    jmax = 0

    def __init__(self):
        self.min_e0 = 9999
        self.min_state0 = []

        self.info_E0 = QLabel(f'E0 = {self.current_E0}')
        self.info_size = QLabel(f'N = {self.current_size}')
        self.info_Jsum = QLabel(f'Jsum = {self.current_Jsum}')
        self.info_P = QLabel(f'P = {self.current_P}')
        self.info_fp_p = QLabel(f'Fp plus (+3 -1) = {self.current_fp_p}')
        self.info_fp_m = QLabel(f'Fp min (+1 -3) = {self.current_fp_m}')
        self.info_fp_sum = QLabel(f'Fp sum = {self.current_fp_sum}')
        self.info_jmax = QLabel(f'J max = {self.jmax}')

    def get_E(self, n, spins_val, horJ_val, verJ_val):

        spins = [1 if s == 1 else -1 for s in spins_val]
        sum0 = 0

        hi = 0
        for i in range(n * n):
            if (i + 1) % n != 0:
                sum0 += -1 * horJ_val[hi] * spins[i] * spins[i + 1]
                hi += 1

        vi = 0
        for i in range(n * n):
            if i < (n * n - n):
                sum0 += -1 * verJ_val[vi] * spins[i] * spins[i + n]
                vi += 1

        if sum0 < self.min_e0:
            self.min_e0 = sum0
            self.min_state0 = spins

        self.current_E0 = sum0
        self.cur_n = n
        self.current_size = self.cur_n ** 2

    def get_fp_p(self, n, horJ_val, verJ_val):
        """
        Расчет количества фрустрированных плакетов
        """
        # Разбивка по крестам ( 4 связи )
        crosses = [[[] for i in range(n)] for j in range(n)]
        crosses_sum = [[[] for i in range(n)] for j in range(n)]

        # Горизонтальные связи (пропуск граничных спинов)
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                crosses[i][j].append(horJ_val[i * (n - 1) + j - 1])
                crosses[i][j].append(horJ_val[i * (n - 1) + j])

        # Вертикальные связи
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                crosses[i][j].append(verJ_val[(i - 1) * n + j])
                crosses[i][j].append(verJ_val[i * n + j])

        # Расчет сумм и количества фрустрированных плакетов
        plus3_min1 = 0
        min3_plus1 = 0

        for i in range(n - 1):
            for j in range(n - 1):
                crosses_sum[i][j] = sum(crosses[i][j])

                plus3_min1 += 1 if crosses_sum[i][j] == 2 else 0
                min3_plus1 += 1 if crosses_sum[i][j] == -2 else 0

        # print(f'{plus3_min1}\t{min3_plus1}\t{plus3_min1+min3_plus1}')
        self.current_fp_p = plus3_min1
        self.current_fp_m = min3_plus1
        self.current_fp_sum = plus3_min1 + min3_plus1

    def get_Jsum_P(self, n,  horJ_val, verJ_val):
        sumJ = 0
        J_max = n * n - n

        for j in horJ_val:
            sumJ += j
        for j in verJ_val:
            sumJ += j

        self.current_Jsum = sumJ
        self.current_P = (self.current_Jsum - J_max) / -J_max / 2
        self.jmax = J_max

    def __make_stat_panel(self):

        widget = QWidget()
        layout = QHBoxLayout()
        widget.setLayout(layout)
        widget.setMaximumHeight(80)

        left_layout = QVBoxLayout()
        mid_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        layout.addLayout(left_layout)
        layout.addLayout(mid_layout)
        layout.addLayout(right_layout)

        labels = [
            self.info_E0,
            self.info_size
        ]

        labels1 = [
            self.info_Jsum,
            self.info_jmax,
            self.info_P,
        ]

        labels2 = [
            self.info_fp_sum,
            self.info_fp_p,
            self.info_fp_m
        ]

        for label in labels:
            left_layout.addWidget(label)
        for label in labels1:
            mid_layout.addWidget(label)
        for label in labels2:
            right_layout.addWidget(label)

        return widget

    def update_info(self, shown):
        if shown:
            self.info_E0.setText(f'E0 = {self.current_E0}')
            self.info_size.setText(f'N = {self.current_size} ({self.cur_n} x {self.cur_n})')
            self.info_Jsum.setText(f'Jsum = {self.current_Jsum}')
            self.info_P.setText('P = {:.2f}'.format(self.current_P))
            self.info_fp_p.setText(f'Fp_plus (+3 -1) = {self.current_fp_p}')
            self.info_fp_m.setText(f'Fp_min (+1 -3) = {self.current_fp_m}')
            self.info_fp_sum.setText(f'Fp_sum = {self.current_fp_sum}')
            self.info_jmax.setText(f'J max = {self.jmax}')
        else:
            self.info_E0.setText('')
            self.info_size.setText('')
            self.info_Jsum.setText('')
            self.info_P.setText('')
            self.info_fp_p.setText('')
            self.info_fp_m.setText('')
            self.info_fp_sum.setText('')
            self.info_jmax.setText('')

    @property
    def stat_widget(self):
        return self.__make_stat_panel()
