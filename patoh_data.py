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

    def exportArrayToNumpyArray(array, dtype=np.int32):
        ''' Converts an array list to a numpy array '''
        if (array is None) or (isinstance(array, list) == False):
            array = []
        return np.asanyarray(array, dtype=dtype)

    def _exportArrays(self):
        self._cwghts = self.exportArrayToNumpyArray(self.cwghts)
        self._nwghts = self.exportArrayToNumpyArray(self.nwghts)
        self._xpins = self.exportArrayToNumpyArray(self.xpins)
        self._pins = self.exportArrayToNumpyArray(self.pins)
        self._partvec = self.exportArrayToNumpyArray(self.partvec)

        self._targetweights = self.exportArrayToNumpyArray(self.targetweights, dtype=np.float32)
        self._partweights = self.exportArrayToNumpyArray(self.partweights)
