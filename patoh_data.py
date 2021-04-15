import numpy as np


class PatohData:
    def __init__(self):
        self._c = None
        self._n = None
        self._nconst = 1
        self.cwghts = []
        self.nwghts = []
        self.xpins = []
        self.pins = []
        self.partvec = []
        self.useFixCells = 0  # 0 assumes no partitions assigned
        self.cut = 0
        self.targetweights = []
        self.partweights = []

        self.params = None

        # exported arrays
        self._cwghts = None
        self._nwghts = None
        self._xpins = None
        self._pins = None
        self._partvec = None

        self._targetweights = None
        self._partweights = None

    def _exportArrays(self):
        self._cwghts = np.array(self.cwghts)
        self._nwghts = np.array(self.nwghts)
        self._xpins = np.array(self.xpins)
        self._pins = np.array(self.pins)
        self._partvec = np.array(self.partvec)

        self._targetweights = np.ndarray(shape=[2], dtype=np.float32)
        self._partweights = np.ndarray(shape=[self._c], dtype=np.int32)
