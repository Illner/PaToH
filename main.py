from patoh_initialize_parameters import PatohInitializeParameters
from patoh_data import PatohData

import os
import ctypes
from pathlib import Path

xpins = [0, 5, 7, 11, 13, 15, 19, 21, 25, 27, 29, 31]
pins = [2, 3, 5, 6, 9, 0, 1, 0, 1, 2, 3, 1, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 10, 11, 8, 9, 9, 11, 2, 5]

cwghts = [1] * 12
nwghts = [1] * 11

lib_path: Path = Path(os.path.join(os.getcwd(), "Linux", "libpatoh.so"))

patoh_data = PatohData()
patoh_data._c = 12
patoh_data._n = 11
patoh_data.xpins = xpins
patoh_data.pins = pins
patoh_data.cwghts = cwghts
patoh_data.nwghts = nwghts

patoh_data._exportArrays()

clib = ctypes.cdll.LoadLibrary(str(lib_path))

PATOH_InitializeParameters = clib.Patoh_Initialize_Parameters
PATOH_InitializeParameters.argtypes = (ctypes.POINTER(PatohInitializeParameters), ctypes.c_int, ctypes.c_int)
PATOH_checkUserParameters = clib.Patoh_Check_User_Parameters
PATOH_checkUserParameters.argtypes = (ctypes.POINTER(PatohInitializeParameters), ctypes.c_int)
PATOH_Alloc = clib.Patoh_Alloc
PATOH_Alloc.argtypes = (ctypes.POINTER(PatohInitializeParameters), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p,ctypes.c_void_p, ctypes.c_void_p)
PATOH_Part = clib.Patoh_Part
PATOH_Part.argtypes = (ctypes.POINTER(PatohInitializeParameters), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p,ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
PATOH_Free = clib.Patoh_Free

# initializeParameters
patoh_data.params = PatohInitializeParameters()
patoh_data.params._k = 2
patoh_data.params.seed = -1
ok = PATOH_InitializeParameters(ctypes.byref(patoh_data.params), 1, 0)
print(f"PATOH_InitializeParameters: {ok}")

# checkUserParameters
ok = PATOH_checkUserParameters(ctypes.byref(patoh_data.params), 1)
print(f"PATOH_checkUserParameters: {ok}")

# alloc
ok = PATOH_Alloc(ctypes.byref(patoh_data.params), patoh_data._c, patoh_data._n, patoh_data._nconst,
                 patoh_data._cwghts.ctypes, patoh_data._nwghts.ctypes, patoh_data._xpins.ctypes,
                 patoh_data._pins.ctypes)
print(f"PATOH_Alloc: {ok}")

# part
cut_val = ctypes.c_int(patoh_data.cut)
cut_addr = ctypes.addressof(cut_val)

ok = PATOH_Part(ctypes.byref(patoh_data.params), patoh_data._c, patoh_data._n, patoh_data._nconst, patoh_data.useFixCells, patoh_data._cwghts.ctypes, patoh_data._nwghts.ctypes, patoh_data._xpins.ctypes, patoh_data._pins.ctypes, patoh_data._targetweights.ctypes, patoh_data._partvec.ctypes, patoh_data._partweights.ctypes, cut_addr)
print(f"PATOH_Part: {ok}")

print(f"patoh_data.cut: {patoh_data.cut}")
print(f"patoh_data.cut_val: {cut_val}")
print(f"patoh_data._partvec: {patoh_data._partvec}")
print(f"patoh_data._partweights: {patoh_data._partweights}")

for i in range(patoh_data._c):
    print(patoh_data._partvec[i])

# free
ok = PATOH_Free()
print(f"PATOH_Free: {ok}")

del patoh_data
