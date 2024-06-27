

class SpinData:

    from .default import make_default_Ising
    from .mfsys_read import read_mfsys

    def __init__(self):
        self._current_spins_val = []
        self._points = []

    @property
    def spins_val(self):
        return self._current_spins_val

    @property
    def points(self):
        return self._points
