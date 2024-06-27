

class Calculator:
    def __init__(self):
        self._current_E0 = 0
        self._current_E1 = 0

        self.min_e0 = 9999
        self.min_state0 = []

    def get_E(self, n, spins_val, horJ_val, verJ_val):

        spins = [1 if s == 1 else -1 for s in spins_val]
        sum0 = 0

        hi = 0
        for i in range(n * n):
            if (i + 1) % n != 0:
                sum0 += horJ_val[hi] * spins[i] * spins[i+1]
                hi += 1

        vi = 0
        for i in range(n * n):
            if i < (n * n - n):
                sum0 += -1 * verJ_val[vi] * spins[i] * spins[i + n]
                vi += 1

        if sum0 < self.min_e0:
            self.min_e0 = sum0
            self.min_state0 = spins

        print(sum0)

