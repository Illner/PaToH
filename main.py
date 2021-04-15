from patoh_initialize_parameters import PatohInitializeParameters
from patoh_data import PatohData

import os
import ctypes
from pathlib import Path

lib_path: Path = Path(os.path.join(os.getcwd(), "Linux", "libpatoh.so"))

xpins = [0, 5, 7, 11, 13, 15, 19, 21, 25, 27, 29, 31]
pins = [2, 3, 5, 6, 9, 0, 1, 0, 1, 2, 3, 1, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 10, 11, 8, 11, 8, 10, 2, 5]

cwghts = [1] * 12
nwghts = [1] * 11

patoh_data: PatohData = PatohData(number_of_nodes=12, number_of_hyperedges=11,
                                  node_weight_list=cwghts, hyperedge_weight_list=nwghts,
                                  xpins=xpins, pins=pins)

clib = ctypes.cdll.LoadLibrary(str(lib_path))

PATOH_InitializeParameters = clib.Patoh_Initialize_Parameters
PATOH_InitializeParameters.argtypes = (ctypes.POINTER(PatohInitializeParameters), ctypes.c_int, ctypes.c_int)
PATOH_Alloc = clib.Patoh_Alloc
PATOH_Alloc.argtypes = (ctypes.POINTER(PatohInitializeParameters), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p,ctypes.c_void_p, ctypes.c_void_p)
PATOH_Part = clib.Patoh_Part
PATOH_Part.argtypes = (ctypes.POINTER(PatohInitializeParameters), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p,ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
PATOH_Free = clib.Patoh_Free

# PATOH_InitializeParameters
ok = PATOH_InitializeParameters(patoh_data.params_ref(), 2, 1)
print(f"PATOH_InitializeParameters: {ok}")

# PATOH_Alloc
ok = PATOH_Alloc(patoh_data.params_ref(), patoh_data.c, patoh_data.n, patoh_data.nconst,
                 patoh_data.cwghts_ctypes(), patoh_data.nwghts_ctypes(),
                 patoh_data.xpins_ctypes(), patoh_data.pins_ctypes())
print(f"PATOH_Alloc: {ok}")

# PATOH_Part
ok = PATOH_Part(patoh_data.params_ref(), patoh_data.c, patoh_data.n, patoh_data.nconst, patoh_data.useFixCells,
                patoh_data.cwghts_ctypes(), patoh_data.nwghts_ctypes(),
                patoh_data.xpins_ctypes(), patoh_data.pins_ctypes(),
                patoh_data.targetweights_ctypes(), patoh_data.partvec_ctypes(), patoh_data.partweights_ctypes(), patoh_data.cut_addr())
print(f"PATOH_Part: {ok}")

print(f"patoh_data.cut: {patoh_data.partvec()}")

# PATOH_Free
ok = PATOH_Free()
print(f"PATOH_Free: {ok}")

del patoh_data
