import ctypes


class PatohInitializeParameters(ctypes.Structure):

    _fields_ = [
        ("_k", ctypes.c_int),
        ("seed", ctypes.c_int)
    ]
