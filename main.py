from patoh_initialize_parameters import PatohInitializeParameters
from patoh_data import PatohData

import os
import ctypes
from pathlib import Path

xpins = [0, 5, 7, 11, 13, 15, 19, 21, 25, 27, 29, 31]
pins = [2, 3, 5, 6, 9, 0, 1, 0, 1, 2, 3, 1, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 10, 11, 8, 9, 9, 11, 2, 5]

cwghts = [1]*12
nwghts = [1]*11

lib_path: Path = Path(os.path.join(os.getcwd(), "Linux", "libpatoh.so"))

patoh_data = PatohData()
patoh_data._c = 12
patoh_data._n = 11
patoh_data.xpins = xpins
patoh_data.pins = pins
patoh_data.cwghts = cwghts
patoh_data.nwghts = nwghts

clib = ctypes.cdll.LoadLibrary(str(lib_path))

PATOH_InitializeParameters = clib.Patoh_Initialize_Parameters
PATOH_InitializeParameters.argtypes = (ctypes.POINTER(PatohInitializeParameters), ctypes.c_int, ctypes.c_int)
PATOH_checkUserParameters = clib.Patoh_Check_User_Parameters
PATOH_checkUserParameters.argtypes = (ctypes.POINTER(PatohInitializeParameters), ctypes.c_int)
PATOH_Alloc = clib.Patoh_Alloc
PATOH_Alloc.argtypes = (ctypes.POINTER(PatohInitializeParameters), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
PATOH_Part = clib.Patoh_Part
PATOH_Part.argtypes = (ctypes.POINTER(PatohInitializeParameters), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
PATOH_Free = clib.Patoh_Free

patoh_data.params = PatohInitializeParameters()
patoh_data.params._k = 2
ok = PATOH_InitializeParameters(ctypes.byref(patoh_data.params), 1, 0)
print(f"PATOH_InitializeParameters: {ok}")

ok = PATOH_checkUserParameters(ctypes.byref(patoh_data.params), 1)
print(f"PATOH_checkUserParameters: {ok}")
