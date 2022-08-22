# -*- encoding: utf8 -*-
# ------------------------------------------------------------------------------
# rlapi.py
# Created on 13/08/2022
#
# The MIT License
#
#
# Copyright 2022 Jorge A. Gomes
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ------------------------------------------------------------------------------

# region IMPORTS
import ctypes
import json
import re

# endregion (imports)
# ---------------------------------------------------------
# region EXPORTS


__all__ = [
    'generate_wrapper',
]


# endregion (exports)
# ---------------------------------------------------------
# region CONSTANTS & ENUMS

LIB_LOADER = '''
import sys
import re
import os
import platform
import ctypes
from enum import IntEnum
from ctypes import (
    CDLL, wintypes,
    c_bool, c_char, c_byte, c_short, c_long, c_ubyte, c_ushort, c_ulong, c_ulong, c_float, c_double, c_char_p, c_void_p,
    Structure, POINTER, CFUNCTYPE, byref, cast
) 


__all__ = [
    '{lib_name}',
    'Bool',
    'BoolPtr',
    'Byte',
    'BytePtr',
    'Char',
    'CharPtr',
    'Short',
    'ShortPtr',
    'Int',
    'IntPtr',
    'Long',
    'LongPtr',
    'UByte',
    'UBytePtr',
    'UShort',
    'UShortPtr',
    'UInt',
    'UIntPtr',
    'ULong',
    'ULongPtr',
    'Float',
    'FloatPtr',
    'Double',
    'DoublePtr',
    'VoidPtr',
    'VoidPtrPtr',
{exports}
]

# region LIBRARY LOADING

# region CDLLEX

DONT_RESOLVE_DLL_REFERENCES = 0x00000001
LOAD_LIBRARY_AS_DATAFILE = 0x00000002
LOAD_WITH_ALTERED_SEARCH_PATH = 0x00000008
LOAD_IGNORE_CODE_AUTHZ_LEVEL = 0x00000010  # NT 6.1
LOAD_LIBRARY_AS_IMAGE_RESOURCE = 0x00000020  # NT 6.0
LOAD_LIBRARY_AS_DATAFILE_EXCLUSIVE = 0x00000040  # NT 6.0

# These cannot be combined with LOAD_WITH_ALTERED_SEARCH_PATH.
# Install update KB2533623 for NT 6.0 & 6.1.
LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR = 0x00000100
LOAD_LIBRARY_SEARCH_APPLICATION_DIR = 0x00000200
LOAD_LIBRARY_SEARCH_USER_DIRS = 0x00000400
LOAD_LIBRARY_SEARCH_SYSTEM32 = 0x00000800
LOAD_LIBRARY_SEARCH_DEFAULT_DIRS = 0x00001000

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)


def check_bool(result, func, args):
    if not result:
        raise ctypes.WinError(ctypes.get_last_error())
    return args


kernel32.LoadLibraryExW.errcheck = check_bool
kernel32.LoadLibraryExW.restype = wintypes.HMODULE
kernel32.LoadLibraryExW.argtypes = (wintypes.LPCWSTR,
                                    wintypes.HANDLE,
                                    wintypes.DWORD)


class CDLLEx(ctypes.CDLL):
    def __init__(self, name, mode=0, handle=None,
                 use_errno=True, use_last_error=False):
        if handle is None:
            handle = kernel32.LoadLibraryExW(name, None, mode)
        super(CDLLEx, self).__init__(name, mode, handle,
                                     use_errno, use_last_error)


class WinDLLEx(ctypes.WinDLL):
    def __init__(self, name, mode=0, handle=None,
                 use_errno=False, use_last_error=True):
        if handle is None:
            handle = kernel32.LoadLibraryExW(name, None, mode)
        super(WinDLLEx, self).__init__(name, mode, handle,
                                       use_errno, use_last_error)


# endregion (cdllex)


_lib_fname = {{
    'win32': 'raylib.dll',
    'linux': 'libraylib.so.3.7.0',
    'darwin': 'libraylib.3.7.0.dylib'
}}

_lib_platform = sys.platform

if _lib_platform == 'win32':
    _bitness = platform.architecture()[0]
else:
    _bitness = '64bit' if sys.maxsize > 2 ** 32 else '32bit'

_lib_fname_abspath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', _bitness, _lib_fname[_lib_platform])
_lib_fname_abspath = os.path.normcase(os.path.normpath(_lib_fname_abspath))

print(
    """Library loading info:
    platform: {{}}
    bitness: {{}}
    absolute path: {{}}
    exists: {{}}
    is file: {{}}
    """.format(
        _lib_platform,
        _bitness,
        _lib_fname_abspath,
        'yes' if os.path.exists(_lib_fname_abspath) else 'no',
        'yes' if os.path.isfile(_lib_fname_abspath) else 'no'
    )
)

{lib_name} = None
if _lib_platform == 'win32':

    try:
        {lib_name} = CDLLEx(_lib_fname_abspath, LOAD_WITH_ALTERED_SEARCH_PATH)
    except OSError:
        print("Unable to load {{}}.".format(_lib_fname[_lib_platform]))
        {lib_name} = None
else:
    {lib_name} = CDLL(_lib_fname_abspath)

if {lib_name} is None:
    print("Failed to load shared library.")
    exit()
else:
    print("Shared library loaded succesfully.", {lib_name})

# Vector component swizzling helppers
_VEC2_GET_SWZL = re.compile(r'[xy]{{,4}}')
_VEC3_GET_SWZL = re.compile(r'[xyz]{{,4}}')
_VEC4_GET_SWZL = re.compile(r'[xyzw]{{,4}}')
_RGBA_GET_SWZL = re.compile(r'[rgba]{{4}}')

_VEC2_SET_SWZL = re.compile(r'[xy]{{,2}}')
_VEC3_SET_SWZL = re.compile(r'[xyz]{{,3}}')
_VEC4_SET_SWZL = re.compile(r'[xyzw]{{,4}}')
_RGBA_SET_SWZL = re.compile(r'[rgba]{{1,4}}')

_number = (int, float)

# region FUNCTIONS


def _classname(obj):
    return obj.__class__.__name__


def _clsname(obj):
    return obj.__class__.__name__


def is_number(obj):
    return isinstance(obj, _number)


def is_component(value):
    return isinstance(value, int) and 0 <= value <= 255


def _clamp_rgba(*args):
    return tuple(value & 255 for value in args)


def _str_in(value):
    return value.encode('utf-8', 'ignore') if isinstance(value, str) else value


def _str_in2(values):
    return _arr(CharPtr, tuple(_str_in(value) for value in values))


def _str_out(value):
    return value.decode('utf-8', 'ignore') if isinstance(value, bytes) else value


def _arr(typ, data):
    return (typ * len(data))(*data)


def _arr2(typ, data):
    arr = typ * len(data[0])
    return (arr * len(data))(*data)

# region TYPE CAST FUNCS


def _float(value):
    return float(value)


def _int(value, ranged=None):
    if ranged:
        return max(ranged[0], min(int(value), ranged[1]))
    return int(value)


def _vec2(seq):
    if isinstance(seq, Vector2):
        return seq
    x, y = seq
    return Vector2(_float(x), _float(y))


def _vec3(seq):
    if isinstance(seq, Vector3):
        return seq
    x, y, z = seq
    return Vector3(float(x), float(y), float(z))


def _vec4(seq):
    if isinstance(seq, Vector4):
        return seq
    x, y, z, w = seq
    return Vector4(float(x), float(y), float(z), float(w))


def _rect(seq):
    if isinstance(seq, Rectangle):
        return seq
    x, y, w, h = seq
    return Rectangle(float(x), float(y), float(w), float(h))


def _color(seq):
    if isinstance(seq, Color):
        return seq
    r, g, b, q = seq
    rng = 0, 255
    return Color(_int(r, rng), _int(r, rng), _int(b, rng), _int(q, rng))

# endregion (type cast funcs)

# endregion (functions)

'''

NL = '\n'
ND = '    '
REGEX_TYPE_RULE = re.compile(r"\.\.\.|(const\s+)?(unsigned\s+)?(\w+)\s*(\[(\d+)]|\*+)?")
REGEX_COLOR_RULE = re.compile(r"CLITERAL\((\w+)\)\{ (\d+), (\d+), (\d+), (\d+) }")

ALL_TYPES = {
    '??': 0,
    'AudioCallback': 0,
    'AudioStream': 0,
    'BoneInfo *': 0,
    'BoundingBox': 0,
    'Camera *': 0,
    'Camera': 0,
    'Camera2D': 0,
    'Camera3D': 0,
    'Color *': 0,
    'Color': 0,
    'FilePathList': 0,
    'Font': 0,
    'GlyphInfo *': 0,
    'GlyphInfo': 0,
    'Image *': 0,
    'Image': 0,
    'LoadFileDataCallback': 0,
    'LoadFileTextCallback': 0,
    'Material *': 0,
    'Material': 0,
    'MaterialMap *': 0,
    'Matrix': 0,
    'Matrix[2]': 0,
    'Mesh *': 0,
    'Mesh': 0,
    'Model *': 0,
    'Model': 0,
    'ModelAnimation *': 0,
    'ModelAnimation': 0,
    'Music': 0,
    'NPatchInfo': 0,
    'Quaternion': 0,
    'Ray': 0,
    'RayCollision': 0,
    'Rectangle *': 0,
    'Rectangle **': 0,
    'Rectangle': 0,
    'RenderTexture2D': 0,
    'SaveFileDataCallback': 0,
    'SaveFileTextCallback': 0,
    'Shader': 0,
    'Sound': 0,
    'Texture': 0,
    'Texture2D *': 0,
    'Texture2D': 0,
    'TextureCubemap': 0,
    'TraceLogCallback': 0,
    'Transform *': 0,
    'Transform **': 0,
    'Vector2 *': 0,
    'Vector2': 0,
    'Vector3 *': 0,
    'Vector3': 0,
    'Vector4': 0,
    'VrDeviceInfo': 0,
    'VrStereoConfig': 0,
    'Wave *': 0,
    'Wave': 0,
    'bool': 0,
    'char *': 0,
    'char **': 0,
    'char': 0,
    'char[32]': 0,
    'const GlyphInfo *': 0,
    'const Matrix *': 0,
    'const char *': 0,
    'const char **': 0,
    'const int *': 0,
    'const unsigned char *': 0,
    'const void *': 0,
    'double': 0,
    'float *': 0,
    'float': 0,
    'float[2]': 0,
    'float[4]': 0,
    'int *': 0,
    'int': 0,
    'long': 0,
    'rAudioBuffer *': 0,
    'rAudioProcessor *': 0,
    'unsigned char *': 0,
    'unsigned char': 0,
    'unsigned int *': 0,
    'unsigned int': 0,
    'unsigned short *': 0,
    'va_list': 0,
    'void *': 0,
    'void': 0,
}

ALL_NAMES = []

PRIMITIVE_TYPES = {
    'Bool': ctypes.c_bool,
    'Byte': ctypes.c_byte,
    'Char': ctypes.c_char,
    'Short': ctypes.c_short,
    'Int': ctypes.c_int,
    'Long': ctypes.c_long,
    'UByte': ctypes.c_ubyte,
    'UShort': ctypes.c_ushort,
    'UInt': ctypes.c_uint,
    'ULong': ctypes.c_ulong,
    'Float': ctypes.c_float,
    'Double': ctypes.c_double,
    'VoidPtr': ctypes.c_void_p,
    'CharPtr': ctypes.c_char_p,
}

STRUCT_TYPES = []

C_TO_PRIMITIVE = {
    '...': "VoidPtr",
    'va_list': "VoidPtr",
    'void': "None",
    'void*': "VoidPtr",
    'bool': "Bool",
    'char': "Char",
    'byte': "Byte",
    'short': "Short",
    'int': "Int",
    'long': "Long",
    'unsigned char': "UByte",
    'unsigned byte': "UByte",
    'unsigned short': "UShort",
    'unsigned int': "UInt",
    'unsigned long': "ULong",
    'float': "Float",
    'double': "Double",
}

C_TO_ZERO = {
    '...': None,
    'va_list': None,
    'void': 0,
    'void*': None,
    'bool': 0,
    'char': 0,
    'byte': 0,
    'short': 0,
    'int': 0,
    'long': 0,
    'unsigned char': 0,
    'unsigned byte': 0,
    'unsigned short': 0,
    'unsigned int': 0,
    'unsigned long': 0,
    'float': 0.0,
    'double': 0.0,
}

C_TO_PY = {
    '...': "bytes",
    'va_list': "bytes",
    'void': "bytes",
    'bool': "bool",
    'char': "int",
    'byte': "int",
    'short': "int",
    'int': "int",
    'long': "int",
    'unsigned char': "int",
    'unsigned byte': "int",
    'unsigned short': "int",
    'unsigned int': "int",
    'unsigned long': "int",
    'float': "float",
    'double': "float",
}

VEC2_SWIZZLE_METHODS = """
    def __len__(self):
        return 2

    def __getitem__(self, key):
        return (self.x, self.y).__getitem__(key)

    def __getattr__(self, attr):
        m = _VEC2_GET_SWZL.match(attr)
        if not m:
            raise AttributeError("{} object does not have attribute '{}'.".format(_classname(self), attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _VEC2_SET_SWZL.match(attr)
        if not m:
            raise AttributeError("{} object does not have attribute '{}'.".format(_classname(self), attr))
        if len(attr) == 1:
            super(Vector2, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                super(Vector2, self).__setattr__(ch, float(value[i]))

    def todict(self):
        '''Returns a dict mapping this Vector2's components'''
        return {'x': self.x, 'y': self.y}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Vector2's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))
"""

VEC3_SWIZZLE_METHODS = """
    def __len__(self):
        return 3

    def __getitem__(self, key):
        return (self.x, self.y, self.z).__getitem__(key)

    def __getattr__(self, attr):
        m = _VEC3_GET_SWZL.match(attr)
        if not m:
            raise AttributeError("{} object does not have attribute '{}'.".format(_classname(self), attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _VEC3_SET_SWZL.match(attr)
        if not m:
            raise AttributeError("{} object does not have attribute '{}'.".format(_classname(self), attr))
        if len(attr) == 1:
            super(Vector3, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                super(Vector3, self).__setattr__(ch, float(value[i]))

    def todict(self):
        '''Returns a dict mapping this Vector3's components'''
        return {'x': self.x, 'y': self.y, 'z': self.z}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Vector3's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))
        self.z = float(d.get('z', self.z))
"""

VEC4_SWIZZLE_METHODS = """
    def __len__(self):
        return 4

    def __getitem__(self, key):
        return (self.x, self.y. self.z, self.w).__getitem__(key)

    def __getattr__(self, attr):
        m = _VEC4_GET_SWZL.match(attr)
        if not m:
            raise AttributeError("{} object does not have attribute '{}'.".format(_classname(self), attr))
        cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _VEC4_GET_SWZL.match(attr)
        if not m:
            raise AttributeError("{} object does not have attribute '{}'.".format(_classname(self), attr))
        if len(attr) == 1:
            super(Vector4, self).__setattr__(attr, float(value))
        else:
            for i, ch in enumerate(attr):
                super(Vector4, self).__setattr__(ch, float(value[i]))

    def todict(self):
        '''Returns a dict mapping this Vector4's components'''
        return {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Vector4's components'''
        self.x = float(d.get('x', self.x))
        self.y = float(d.get('y', self.y))
        self.z = float(d.get('z', self.z))
        self.w = float(d.get('w', self.w))
"""

RGBA_SWIZZLE_METHODS = """
    def __len__(self):
        return 4

    def __getitem__(self, key):
        return (self.r, self.g, self.b, self.a).__getitem__(key)

    def __getattr__(self, attr):
        m = _RGBA_GET_SWZL.match(attr)
        if not m:
            raise AttributeError("{} object does not have attribute '{}'.".format(_classname(self), attr))
        cls = {1: int, 4: Color}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr, value):
        m = _RGBA_SET_SWZL.match(attr)
        if not m:
            raise AttributeError("{} object does not have attribute '{}'.".format(_classname(self), attr))
        if len(attr) == 1:
            super(Color, self).__setattr__(attr, int(value))
        else:
            for i, ch in enumerate(attr):
                super(Color, self).__setattr__(ch, int(value[i]))

    def todict(self):
        '''Returns a dict mapping this Color's components'''
        return {'r': self.r, 'g': self.g, 'b': self.b, 'a': self.a}

    def fromdict(self, d):
        '''Apply the mapping `d` to this Color's components'''
        self.r = int(d.get('r', self.r))
        self.g = int(d.get('g', self.g))
        self.b = int(d.get('b', self.b))
        self.a = int(d.get('a', self.a))
"""

WRAPPER = """
def _wrap(api, argtypes, restype):
    api.argtypes = argtypes
    api.restype = restype
"""
API_NAME = 'rlapi'

TEMPLATE_BASE_STRUCT = """
class {name}(Structure):
    '''{description}'''
    {field_map}
    @classmethod
    def array_of(cls, {py_name}_sequence):
        '''Creates and returns an array of {name}s'''
        arr = cls * len({py_name}_sequence)
        return arr(*{py_name}_sequence)

    @classmethod
    def zero(cls):
        '''Creates and returns a zero initialized {name}'''
        return cls({none_args})

    def __init__(self, {init_params}):
{init_docstring}
        super({name}, self).__init__({init_fields})

    def __str__(self):
        return "[{name} at {{}}]".format(id(self))

    @property
    def byref(self):
        '''Gets a reference to this {name} instance'''
        return byref(self)
{extra_impl}

# Pointer type to {name}s
{name}Ptr = POINTER({name})
{alias}

"""

TEMPLATE_FUNCTION = """

def {py_name}({param_list}){r_type}:
{description}{before}
    {result}{lib_name}.{c_name}({arg_list}){after}
"""

# endregion (constants)
# ---------------------------------------------------------
# region CLASSES


class TypeTable:

    def __init__(self):
        self._table = {}
        self._types = {}

    def add_info(self, t_info):
        if t_info.key not in self._table:
            self._table[t_info.key] = t_info

    def get_info(self, key, default):
        return self._table.get(key, default)

    def add_type(self, name, d_type):
        if name not in self._types:
            self._types[name] = d_type

    def get_type(self, name, default):
        return self._types.get(name, default)


class TypeInfo:

    def __init__(self, name, const=False, unsigned=False, length=None, pointer=None):
        self.name = name
        self.const = const
        self.unsigned = unsigned
        self.length = length
        self.pointer = pointer

        self._c_type = None
        self._py_type = None
        fulltype = self.rl_type
        if fulltype == 'None':
            raise ValueError()
        if fulltype not in ALL_TYPES:
            ALL_TYPES[fulltype] = 0
        else:
            ALL_TYPES[fulltype] += 1

    def __str__(self):
        return self.key

    @property
    def key(self):
        return ' '.join([str(i)
                         for i in (self.const, self.unsigned, self.name, self.length, self.pointer)
                         if i is not None])

    @property
    def zero(self):
        if self.name in C_TO_ZERO:
            if self.pointer or self.length:
                return "None"
            return f'{C_TO_ZERO.get(self.name)}'
        else:
            return f"{self.name}.zero()"

    @property
    def rl_type(self):
        return "{}{}{}".format(
            'const ' if self.const else '',
            self.name,
            (' ' + '*' * self.pointer) if self.pointer else ('[{}]'.format(self.length) if self.length else '')
        )

    def arg(self, value, before, after):
        if self.name == '...':
            return '*args'
        if self.name in C_TO_PY:
            if not (self.pointer or self.length):
                return f"{C_TO_PY.get(self.name)}({value})"
            elif self.pointer:
                if self.name in 'unsigned char':
                    return f"_str_in({value})"
                else:
                    before.append(f"{value}_ref = cast({value}, {self.as_c_type()})")
                    # after.append(f"{value}_ref.contents.value")
                return f"{value}_ref"
            elif self.length:
                return f"_array({self.as_c_type()}, {value})"
        return f"{value}"

    def as_c_type(self):
        sub = False
        if self.name in C_TO_PRIMITIVE:
            c_type = C_TO_PRIMITIVE.get(self.name)
            if self.pointer:
                if c_type == 'None':
                    c_type = 'Void'
                c_type = f"{c_type}Ptr"
                sub = True

        elif self.name in STRUCT_TYPES:
            c_type = self.name
            if self.pointer:
                c_type = f"{c_type}Ptr"
                sub = True
        elif self.name == '...':
            c_type = 'VoidPtr'
            sub = True
        else:
            c_type = 'VoidPtr'
            sub = True
        if self.pointer:
            for _ in range(self.pointer - (1 if sub else 0)):
                c_type = "POINTER({})".format(c_type)
        elif self.length:
            c_type = "{} * {}".format(c_type, self.length)
        return c_type

    def as_py_type(self):
        sub = False
        if self.name in C_TO_PRIMITIVE:
            py_type = C_TO_PY.get(self.name)
            if self.name == 'void':
                if self.pointer:
                    py_type = 'bytes'
                    sub = True
                else:
                    py_type = 'None'
            if self.name in 'unsigned char' and (self.pointer or self.length):
                py_type = 'bytes'
                sub = True
        elif self.name in STRUCT_TYPES:
            py_type = self.name
            if self.pointer:
                py_type = "{}Ptr".format(py_type)
                sub = True
        elif self.name == '...':
            py_type = 'bytes'
            sub = True
        else:
            py_type = 'bytes'
            sub = True

        if self.pointer:
            for _ in range(self.pointer - (1 if sub else 0)):
                py_type = "Sequence[{}]".format(py_type)

        elif self.length:
            py_type = "Sequence[{}]".format(py_type)

        if py_type == "NonePtr":
            raise ValueError('Oh no!')
        return py_type


class ParamInfo:

    def __init__(self, name, t_info, doc=""):
        self.name = name
        self.t_info = t_info
        self.doc = doc

    @property
    def py_name(self):
        return snakefy(self.name)

    @property
    def py_param(self):
        star = '*' if self.t_info.name == '...' else ''
        default = ''
        return f"{star}{self.py_name}{default}"

    def docstring(self, lv):
        return f"{ND * lv}:param {self.t_info.as_py_type()} {self.py_name}: `{self.t_info.rl_type}` in C raylib\n"


class FuncInfo:

    def __init__(self, name, p_info, r_info, doc=""):
        self.name = name
        self.p_info = p_info
        self.r_info = r_info
        self.doc = doc

    @property
    def py_name(self):
        return snakefy(self.name)

    def prototype(self, lib_name, prototyper):
        argtypes = ', '.join([p.t_info.as_c_type() for p in self.p_info])
        restype = self.r_info.as_c_type() if self.r_info else "None"
        return f"{prototyper}({lib_name}.{self.name}, [{argtypes}], {restype})\n"

    def ret(self, result, after):
        rtype = self.r_info.as_py_type()
        resval = ''
        retval = ''
        if rtype != "None":
            resval = f'{result} = '
            retval = f'return {result}'
            if after:
                retval += ', ' + ', '.join(after)
        elif after:
            retval = 'return ' + ', '.join(after)
        return resval, retval

    def wrap(self):
        # ALL_NAMES.append(self.py_name)
        ret = 'None (`void` in C raylib)'
        if self.r_info:
            ret = f"{self.r_info.as_py_type()} (`{self.r_info.rl_type}` in C raylib)"
        docstring = ''.join([
            f"{ND}'''{self.doc}\n\n",
            f"{ND}Raylib's C API: {self.name}{NL * 2 if self.p_info or self.r_info else ''}",
            *[p_info.docstring(1) for p_info in self.p_info],
            f'{ND}:return: {ret}\n',
            f"{ND if self.p_info or self.r_info else ''}'''"
        ])
        before = []
        after = []
        arg_list = ', '.join(p_info.t_info.arg(p_info.py_name, before, after) for p_info in self.p_info)
        resval, retval = self.ret('result', after)
        data = {
            'description': docstring,
            'param_list': ', '.join(p_info.py_param for p_info in self.p_info),
            'arg_list': arg_list,
            'r_type': '',
            'py_name': self.py_name,
            'c_name': self.name,
            'lib_name': 'rlapi',
            'result': resval,
            'before': (NL + ND) + (NL + ND).join(before) if before else '',
            'after': (NL + ND) + retval if retval else ''
        }
        return TEMPLATE_FUNCTION.format(**data)


class FieldInfo:

    def __init__(self, name, t_info, doc=""):
        self.name = name
        self.t_info = t_info
        self.doc = doc

    @property
    def py_name(self):
        return snakefy(self.name)

    def docstring(self, lv):
        return f"{ND * lv}:param {self.t_info.as_py_type()} {self.name}: `{self.t_info.rl_type}` in C raylib\n"

    def wrap(self):
        return f"        ('{self.py_name}', {self.t_info.as_c_type()}),\n"


class StructInfo:

    def __init__(self, name, f_info, alias, doc=""):
        self.name = name
        self.f_info = f_info
        self.doc = doc
        self.alias = alias

    @property
    def py_name(self):
        return snakefy(self.name)

    @property
    def ptr_name(self):
        return f"{self.name}Ptr"

    def wrap(self):
        docstring = ''.join([
            f"{ND * 2}'''{self.doc}{NL+NL if self.f_info else ''}",
            *[p_info.docstring(2) for p_info in self.f_info],
            f"{ND * 2 if self.f_info else ''}'''"
        ])
        field_map = ''.join([
            f"_fields_ = [{NL if self.f_info else ''}",
            *[f_info.wrap() for f_info in self.f_info],
            f"{ND if self.f_info else ''}]\n"
        ])
        extra_impl = ''
        if self.name == 'Vector2':
            extra_impl = VEC2_SWIZZLE_METHODS
        elif self.name == 'Vector3':
            extra_impl = VEC3_SWIZZLE_METHODS
        elif self.name == 'Vector4':
            extra_impl = VEC4_SWIZZLE_METHODS
        elif self.name == 'Color':
            extra_impl = RGBA_SWIZZLE_METHODS
        data = {
            'description': self.doc,
            'init_docstring': docstring,
            'init_params': ', '.join(f_info.py_name for f_info in self.f_info),
            'init_fields': ', '.join(f_info.py_name for f_info in self.f_info),
            'none_args': ', '.join(f.t_info.zero for f in self.f_info),
            'field_map': field_map,
            'py_name': self.py_name,
            'name': self.name,
            'extra_impl': extra_impl,
            'alias': NL.join(self.alias)
        }
        return TEMPLATE_BASE_STRUCT.format(**data)


class EnumerandInfo:

    def __init__(self, name, value, doc=""):
        self.name = name
        self.value = value
        self.doc = doc


class EnumInfo:

    def __init__(self, name, e_info, doc=""):
        self.name = name
        self.e_info = e_info
        self.doc = doc

    def wrap(self):
        code = f"\nclass {self.name}(IntEnum):"
        for e_info in self.e_info:
            code += f"\n{ND}{e_info.name} = {e_info.value}"

        code += NL * 2
        for e_info in self.e_info:
            code += f"\n# {e_info.doc}\n{e_info.name} = {self.name}.{e_info.name}"
        code += NL * 2

        return code


class CallbackInfo:

    def __init__(self, name, p_info, r_info, doc=""):
        self.name = name
        self.p_info = p_info
        self.r_info = r_info
        self.doc = doc

    def wrap(self):
        params = ', '.join([p.t_info.as_c_type() for p in self.p_info])
        return f"\n# {self.doc}\n{self.name} = CFUNCTYPE({params})"


class WrapInfo:

    def __init__(self):
        self._table = TypeTable()
        self.primitives = []
        self.defines = []
        self.structs = []
        self.aliases = []
        self.enums = []
        self.callbacks = []
        self.prototypes = []
        self.functions = []

    def wrap(self, out_fname):
        exports = NL.join(f"{ND}'{name}'," for name in ALL_NAMES)
        full_code = LIB_LOADER.format(exports=exports, lib_name=API_NAME)

        full_code += "# region TYPES\n\n"
        for primitive in self.primitives:
            full_code += primitive
        for s_info in self.structs:
            full_code += s_info.wrap()
        for alias in self.aliases:
            full_code += alias
        full_code += "\n# endregion (types)\n"

        full_code += "# region CONSTANTS AND ENUMS\n\n"
        for enum in self.enums:
            full_code += enum.wrap()
        for define in self.defines:
            full_code += define
        full_code += "\n# endregion (constants and enums)\n"

        full_code += "# region CALLBACKS\n\n"
        for cb in self.callbacks:
            full_code += cb.wrap()
        full_code += "\n# endregion (callbacks)\n"

        full_code += "\n# region PROTOTYPES\n\n"
        full_code += WRAPPER
        full_code += NL * 2
        for proto in self.prototypes:
            full_code += proto
        full_code += "\n# endregion (prototypes)\n"

        full_code += "# region API\n"
        for f_info in self.functions:
            full_code += f_info.wrap()
        full_code += "\n# endregion (api)\n"

        with open(out_fname, 'w', encoding='utf8') as code:
            code.write(full_code)

# endregion (classes)
# ---------------------------------------------------------
# region FUNCTIONS


def snakefy(name):
    lastchar = ''
    result = ''

    for char in name:
        if lastchar:
            if char.isupper():
                if lastchar.isupper() or lastchar.isdigit():
                    result += f'{char.lower()}'
                else:
                    result += f'_{char.lower()}'
            else:
                result += char
        else:
            result += char.lower()
        lastchar = char

    return result


def get_typ_info(type_str):
    if type_str == '...':
        return TypeInfo(type_str, False, False, None, None)

    match = REGEX_TYPE_RULE.fullmatch(type_str)
    if match:
        is_const, is_unsigned, t_name, length, pointer = match.groups()
        if is_unsigned:
            t_name = is_unsigned + t_name
        t_info = TypeInfo(
            t_name,
            is_const is not None,
            is_unsigned is not None,
            int(pointer, 10) if pointer and str(length).startswith('[') else None,
            len(length) if length and str(length).startswith('*') else None,
        )

        return t_info
    else:
        return TypeInfo('void', pointer="*")


def generate_wrapper(api_json, out_fname=None):

    with open(api_json, 'r', encoding='utf8') as rljson:
        api = json.load(rljson)

    wrapper = WrapInfo()

    for dname, dtype in PRIMITIVE_TYPES.items():
        wrapper.primitives.append(f"{dname} = {dtype.__name__}\n")
        wrapper.primitives.append(f"{dname}Ptr = POINTER({dtype.__name__})\n")

    for struct in api.get('structs', []):
        s_alias = []
        for alias in api.get('aliases', []):
            info = alias.get('description')
            base = alias.get('type')
            derived = alias.get('name')
            if base == struct.get('name'):
                STRUCT_TYPES.extend((derived, f'{derived}Ptr'))
                ALL_NAMES.extend((derived, f'{derived}Ptr'))
                s_alias.append(f"\n# {info}\n{derived} = {base}\n{derived}Ptr = {base}Ptr\n")

        s_info = StructInfo(struct.get('name'), [], s_alias, struct.get('description', ''))
        STRUCT_TYPES.extend((s_info.name, s_info.ptr_name))
        ALL_NAMES.extend((s_info.name, s_info.ptr_name))

        for i, field in enumerate(struct.get('fields', [])):
            t_info = get_typ_info(field.get('type', ''))
            f_info = FieldInfo(field.get('name', f'field{i}'), t_info, field.get('description', ''))
            s_info.f_info.append(f_info)

        wrapper.structs.append(s_info)

    for define in api.get('defines', []):
        defname = define.get('name')
        deftype = define.get('type')
        defvalue = define.get('value')
        definfo = define.get('description')
        definfo = f"\n# {definfo}" if definfo else ''

        if deftype == 'COLOR':
            match = REGEX_COLOR_RULE.match(defvalue)
            if match:
                valtype, r, g, b, a = match.groups()
                wrapper.defines.append(f"{definfo}\n{defname} = {valtype}({r}, {g}, {b}, {a})")
                ALL_NAMES.append(defname)

        elif deftype == 'FLOAT':
            wrapper.defines.append(f"{definfo}\n{defname} = {defvalue}")
            ALL_NAMES.append(defname)

        elif deftype == 'FLOAT_MATH':
            defvalue = defvalue.replace('.0f', '.0').replace('/', ' / ')
            wrapper.defines.append(f"{definfo}\n{defname} = {defvalue}")
            ALL_NAMES.append(defname)

        elif deftype == 'STRING':
            wrapper.defines.append(f"""{definfo}\n{defname} = \"{defvalue}\"""")
            ALL_NAMES.append(defname)

    for enumeration in api.get('enums', []):
        e_info = EnumInfo(enumeration.get('name'), [], enumeration.get('description'))
        ALL_NAMES.append(e_info.name)

        for value in enumeration.get('values', []):
            m_info = EnumerandInfo(value.get('name'), value.get('value'), value.get('description'))
            e_info.e_info.append(m_info)
            ALL_NAMES.append(m_info.name)

        wrapper.enums.append(e_info)

    for callback in api.get('callbacks'):
        c_info = CallbackInfo(callback.get('name'), [], get_typ_info(callback.get('returnType')),
                              callback.get('description'))

        for param in callback.get('params'):
            c_info.p_info.append(ParamInfo(param.get('name'), get_typ_info(param.get('type'))))

        wrapper.callbacks.append(c_info)
        STRUCT_TYPES.append(c_info.name)
        ALL_NAMES.append(c_info.name)

    for func in api.get('functions', []):
        f_info = FuncInfo(func.get('name'), [], None, func.get('description', ''))
        ALL_NAMES.append(f_info.py_name)

        for i, param in enumerate(func.get('params', [])):
            t_info = get_typ_info(param.get('type', ''))
            f_info.p_info.append(ParamInfo(param.get('name', f'param{i}'), t_info, param.get('type')))

        f_info.r_info = get_typ_info(func.get('returnType'))
        wrapper.functions.append(f_info)
        wrapper.prototypes.append(f_info.prototype(API_NAME, '_wrap'))

    if out_fname:
        wrapper.wrap(out_fname)
    # for t in ALL_TYPES:
    #     print(f"{ALL_TYPES[t]}: {t}")

# endregion (functions)
