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
        self.targetweights = [0.5, 0.5]
        self.partweights = [0, 0]

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
        self._cwghts = np.array(self.cwghts, dtype=np.int32)
        self._nwghts = np.array(self.nwghts, dtype=np.int32)
        self._xpins = np.array(self.xpins, dtype=np.int32)
        self._pins = np.array(self.pins, dtype=np.int32)
        self._partvec = np.array(self.partvec, dtype=np.int32)

        self._targetweights = np.array(self.targetweights, dtype=np.float32)
        self._partweights = np.array(self.partweights, dtype=np.int32)
