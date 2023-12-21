# -*- encoding: utf8 -*-

# region LICENSE
# ------------------------------------------------------------------------------
# The MIT License
#
#
# Copyright 2023 Jorge A. Gomes
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
# endregion (license)

# region IMPORTS

import sys

from typing import Any, Sequence
from contextlib import contextmanager
from dataclasses import dataclass, field
from enum import Enum, auto

# endregion (imports)
# ---------------------------------------------------------
# region EXPORTS


__all__ = [
    'TPL_IMPORTS',
    'TPL_RAYLIBPY_LICENSE',
    'TPL_RAYLIB_LICENSE',
    'TPL_LIBRARY_LOADER',
    'TPL_UTILS',
    'TPL_GLOBALS',
    'TPL_COLOR_SWIZZLING',
    'TPL_COLOR_UTILS',
    'TPL_RECT_SWIZZLING',
    'TPL_RECT_UTILS',
    'TPL_VEC2_MATH',
    'TPL_VEC2_SWIZZLING',
    'TPL_VEC2_UTILS',
    'TPL_VEC3_MATH',
    'TPL_VEC3_SWIZZLING',
    'TPL_VEC3_UTILS',
    'TPL_VEC4_MATH',
    'TPL_VEC4_SWIZZLING',
    'TPL_VEC4_UTILS',
]


# endregion (exports)
# ---------------------------------------------------------
# region GLOBALS

# endregion (globals)
# ---------------------------------------------------------
# region CONSTANTS & ENUMS

TPL_IMPORTS = """import sys
import re
import os
import platform
import ctypes
import json
import struct

from typing import Generic, TypeVar
from enum import IntEnum
from contextlib import contextmanager
from ctypes import (
    CDLL, wintypes,
    c_bool,
    c_char, c_wchar, c_char_p, c_wchar_p,
    c_byte, c_short, c_int, c_long, c_longlong,
    c_ubyte, c_ushort, c_uint, c_ulong, c_ulonglong,
    c_float, c_double, c_longdouble,
    c_void_p, c_size_t,
    Array, Structure, POINTER, CFUNCTYPE, byref, cast, pointer, POINTER
)

from . import easings
"""

# region LICENSES


TPL_RAYLIBPY_LICENSE = """# raylib-py license

# ------------------------------------------------------------------------------
# The MIT License
#
#
# Copyright (c) 2023 Jorge A. Gomes
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
# ------------------------------------------------------------------------------"""

TPL_RAYLIB_LICENSE = """# C raylib license

# ------------------------------------------------------------------------------
# zlib/libpng
#
# raylib is licensed under an unmodified zlib/libpng license, which is an OSI-certified,
# BSD-like license that allows static linking with closed source software:
#
# Copyright (c) 2013-2023 Ramon Santamaria (@raysan5)
#
# This software is provided "as-is", without any express or implied warranty. In no event
# will the authors be held liable for any damages arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose, including commercial
# applications, and to alter it and redistribute it freely, subject to the following restrictions:
#
#    1. The origin of this software must not be misrepresented; you must not claim that you
#    wrote the original software. If you use this software in a product, an acknowledgment
#    in the product documentation would be appreciated but is not required.
#
#    2. Altered source versions must be plainly marked as such, and must not be misrepresented
#    as being the original software.
#
#    3. This notice may not be removed or altered from any source distribution.
#
# ------------------------------------------------------------------------------"""


# endregion (LICENSES)

# region LIBRAY LOADING

TPL_LIBRARY_LOADER = """
# region CDLLEX

if sys.platform == 'win32':
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

_dotraylib_used = False
_dotraylib_loadinfo = []

def _check_dotraylib(lib, platform, bitness, default=None):
    \"\"\"Checks for the .raylib file in the current working directory

    The presence of this file allows the loading of binaries other than those
    provided by raylib. Example of .raylib file contents:

    ```json
    {
        "raylib": {
            "win32": {
                "32bit": "path/to/raylib/filename.dll",
                "64bit": "path/to/raylib/filename.dll"
            },
            "linux": {
                "32bit": "path/to/raylib/filename.so",
                "64bit": "path/to/raylib/filename.so"
            },
            "darwin": {
                "64bit": "path/to/raylib/filename.dylib"
            }
        }
    }
    ```
    \"\"\"

    global _dotraylib_loadinfo, _dotraylib_used
    _dotraylib = os.path.join(os.getcwd(), '.raylib')

    if os.path.exists(_dotraylib) and os.path.isfile(_dotraylib):
        _dotraylib_used = True

        with open(_dotraylib, 'r', encoding='utf8') as fp:
            try:
                _dotraylib_config = json.load(fp)
                _libpath = _dotraylib_config.get(lib, {}).get(platform, {}).get(bitness, default)
                _dotraylib_loadinfo.append("INFO: .raylib loaded successfully")
                return _libpath

            except json.JSONDecodeError:
                _dotraylib_loadinfo.append("ERROR: Could not decode .raylib file")
    else:
        _dotraylib_loadinfo.append("INFO: .raylib file not available")
    return default


def _load_library(lib_name, is_extension, basedir, **bin_fnames):
    global _dotraylib_loadinfo, _dotraylib_used

    _lib_fname = {
        'win32': bin_fnames.get('win32', 'no_file_specified.dll'),
        'linux': bin_fnames.get('linux', 'no_file_specified.so'),
        'darwin': bin_fnames.get('darwin', 'no_file_specified.dylib')
    }

    _dotraylib_used = False
    _lib_platform = sys.platform

    if _lib_platform == 'win32':
        _bitness = platform.architecture()[0]
    elif _lib_platform == 'darwin':
        _bitness = '64bit'
    else:
        _bitness = '64bit' if sys.maxsize > 2 ** 32 else '32bit'

    if is_extension:
        _lib_default = None
    else:
        _lib_default = os.path.join(*(d.format(os.path.dirname(__file__)) for d in basedir), _bitness, _lib_fname[_lib_platform])

    _lib_default = _check_dotraylib(lib_name, _lib_platform, _bitness, _lib_default)

    if not _lib_default:
        if is_extension:
            _dotraylib_loadinfo.append("ERROR: Platform ({}), bitness ({}) or valid filename not specified in .raylib file for {} extension".format(lib_name, _lib_platform, _bitness))
        else:
            _dotraylib_loadinfo.append("ERROR: Platform ({}), bitness ({}) or valid filename not specified in .raylib file for {}".format(lib_name, _lib_platform, _bitness))

        _lib_fname_abspath = ''
        _ok = False
    else:
        _lib_fname_abspath = os.path.normcase(os.path.normpath(_lib_default))
        _ok = True

    _cwd_info = os.getcwd()
    _load_info = "\\n            ".join(_dotraylib_loadinfo) if _dotraylib_loadinfo else "does not apply"

    print(
        \"\"\"Library loading info:
        platform: {}
        bitness: {}
        current working dir: {}
        .raylib used: {}
        .raylib status: {}
        absolute path: {}
        is extension: {}
        path exists: {}
        path leads to a file: {}
        \"\"\".format(
            _lib_platform,
            _bitness,
            _cwd_info,
            'yes' if _dotraylib_used else 'no',
            _load_info,
            _lib_fname_abspath,
            'yes' if is_extension else 'no',
            'yes' if os.path.exists(_lib_fname_abspath) else 'no',
            'yes' if os.path.isfile(_lib_fname_abspath) else 'no'
        )
    )

    if not _ok:
        print("Failed to load Shared library", lib_name)
        sys.exit(1)

    lib_ = None
    if _lib_platform == 'win32':

        try:
            lib_ = CDLLEx(_lib_fname_abspath, LOAD_WITH_ALTERED_SEARCH_PATH)
        except OSError as e:
            print("Unable to load {}: {}".format(_lib_fname[_lib_platform], e.args))
            lib_ = None
    else:
        lib_ = CDLL(_lib_fname_abspath)

    if lib_ is None:
        print("Failed to load Shared library", lib_name)
        sys.exit(1)
    else:
        print("Shared library loaded succesfully", lib_)

    return lib_
"""
# endregion (LIBRAY LOADING)

TPL_GLOBALS = """
# Used to store temporarily out param argument passed to functions
# so that the values can be retrieved following the call
_in_out = []

# TypeVar for generic Array class
_T = TypeVar('_T')

RE_C_FMT_STRING = re.compile(r"%(?P<flags>[ \-+#0])?(?P<width>\d+|\*)?(?P<precision>\.[*\d])?(?P<length>hh|h|ll|l|j|z|t|L)?(?P<spec>[diuoxXfFeEgGaAcspn])")

FMT_SPEC_TABLE = {
    'd': {'*': c_int,          'hh': c_byte,   'h': c_short,          'l': c_long,          'll': c_longlong,          'j': None, 'z': c_size_t,          't': None, 'L': None},
    'i': {'*': c_int,          'hh': c_byte,   'h': c_short,          'l': c_long,          'll': c_longlong,          'j': None, 'z': c_size_t,          't': None, 'L': None},
    'u': {'*': c_uint,         'hh': c_ubyte,  'h': c_ushort,         'l': c_ulong,         'll': c_ulonglong,         'j': None, 'z': c_size_t,          't': None, 'L': None},
    'o': {'*': c_uint,         'hh': c_ubyte,  'h': c_ushort,         'l': c_ulong,         'll': c_ulonglong,         'j': None, 'z': c_size_t,          't': None, 'L': None},
    'x': {'*': c_uint,         'hh': c_ubyte,  'h': c_ushort,         'l': c_ulong,         'll': c_ulonglong,         'j': None, 'z': c_size_t,          't': None, 'L': None},
    'X': {'*': c_uint,         'hh': c_ubyte,  'h': c_ushort,         'l': c_ulong,         'll': c_ulonglong,         'j': None, 'z': c_size_t,          't': None, 'L': None},
    'f': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'F': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'e': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'E': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'g': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'G': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'a': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'A': {'*': c_double,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': c_longdouble},
    'c': {'*': c_int,          'hh': None,     'h': None,             'l': c_wchar,         'll': None,                'j': None, 'z': None,              't': None, 'L': None},
    's': {'*': c_char_p,       'hh': None,     'h': None,             'l': c_wchar_p,       'll': None,                'j': None, 'z': None,              't': None, 'L': None},
    'p': {'*': c_void_p,       'hh': None,     'h': None,             'l': None,            'll': None,                'j': None, 'z': None,              't': None, 'L': None},
    'n': {'*': POINTER(c_int), 'hh': c_char_p, 'h': POINTER(c_short), 'l': POINTER(c_long), 'll': POINTER(c_longlong), 'j': None, 'z': POINTER(c_size_t), 't': None, 'L': None},
}

_fmt_cache = {}

# Vector component swizzling helppers
RE_VEC2_GET_SWZL = re.compile(r'[xy]{,4}')
RE_VEC3_GET_SWZL = re.compile(r'[xyz]{,4}')
RE_VEC4_GET_SWZL = re.compile(r'[xyzw]{,4}')
RE_RGBA_GET_SWZL = re.compile(r'[rgba]{1,4}')
RE_RECT_GET_SWZL = re.compile(r'(width|height|[xywhcmrb]{,4})')

RE_VEC2_SET_SWZL = re.compile(r'[xy]{,2}')
RE_VEC3_SET_SWZL = re.compile(r'[xyz]{,3}')
RE_VEC4_SET_SWZL = re.compile(r'[xyzw]{,4}')
RE_RGBA_SET_SWZL = re.compile(r'[rgba]{1,4}')
RE_RECT_SET_SWZL = re.compile(r'(width|height|[xywhcmrb]{,4})')"""

# region UTILITIES


TPL_UTILS = """
# region INTERNAL


def _extract_argtypes(format_string):
    \"\""Generator function to extract all specifiers as ctypes types from the format string
    
    (yielded items are tuples of slice, str and a ctypes type or None)
    "\"\"
    # type: (str) -> Iterator[tuple[slice, str, Any]]
    for m in RE_C_FMT_STRING.finditer(format_string):
        spec = m.group('spec')
        length = m.group('length') or '*'
        ctypes_type = FMT_SPEC_TABLE.get(spec, {}).get(length)
        yield slice(*m.span()), m[0], ctypes_type


def _transform_fmt(format_string, args):
    n = len(args)
    vals = []
    sentinel = object()
    for i, (slc, str, ctype) in enumerate(_extract_argtypes(format_string[:])):
        try:
            val = ctype(args[i])
        except Exception:
            val = sentinel
        if i >= n or ctype is None or val is sentinel:
            left = format_string[:slc.start]
            right = format_string[slc.stop:]
            middle = '_' * len(str)
            format_string = left + middle + right

        vals.append(val)

    return format_string, vals


def _clsname(obj):
    return obj.__class__.__name__


def is_number(obj):
    return isinstance(obj, (int, float))


def is_component(value):
    return isinstance(value, int) and 0 <= value <= 255


def _clamp_rgba(*args):
    return tuple(value & 255 for value in args)


def _str_in(value):
    return value.encode('utf-8', 'ignore') if isinstance(value, str) else value


def _str_in2(values):
    return _arr_in(CharPtr, tuple(_str_in(value) for value in values))


def _str_out(value):
    return value.decode('utf-8', 'ignore') if isinstance(value, bytes) else value


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
    return Color(_int(r, rng), _int(g, rng), _int(b, rng), _int(q, rng))


def _array_in(sequence, type_ctype=None):
    if isinstance(sequence, BaseArray):
        return sequence
    else:
        return (type_ctype * len(sequence))(*sequence)


def _clear_in_out():
    global _in_out

    _in_out.clear()


def _push_in_out(ctype_pointer_type):
    global _in_out

    _in_out.append(ctype_pointer_type)


def _wrap(api, res_type, *arg_types):
    \"\"\"Configure the paramters and return types for the wrapped C function and returns it\"\"\"
    api.argtypes = arg_types
    api.restype = res_type
    return api

# endregion (internal)


BaseArray = Array

class Array(Generic[_T]):
    \"\"\"Generic class defined only for type hinting/annotation purposes (e.g. Array[Color]).\"\"\"
    pass


def clear_format_string_cache():
    global _fmt_cache

    _fmt_cache.clear()


def pop_out_param(default=None):
    \"\"\"Pops and returns the out param argument passed to the last call, or the default value otherwise\"\"\"
    global _in_out

    if len(_in_out):
        return _in_out.pop()
    return default


def float_array(sequence):
    \"\"\"Factory function to create and return an array of floats\"\"\"
    if isinstance(sequence, Array):
        return sequence

    return (Float * len(sequence))(*sequence)


def double_array(sequence):
    \"\"\"Factory function to create and return an array of doubles\"\"\"
    if isinstance(sequence, Array):
        return sequence

    return (Double * len(sequence))(*sequence)


def int_array(sequence):
    \"\"\"Factory function to create and return an array of signed int numbers\"\"\"
    if isinstance(sequence, Array):
        return sequence
    elif isinstance(sequence, str):
        sequence = [ord(ch) for ch in sequence]

    return (Int * len(sequence))(*sequence)


def uint_array(sequence):
    \"\"\"Factory function to create and return an array of unsigned int numbers\"\"\"
    if isinstance(sequence, Array):
        return sequence
    elif isinstance(sequence, str):
        sequence = [ord(ch) for ch in sequence]

    return (UInt * len(sequence))(*sequence)


def short_array(sequence):
    \"\"\"Factory function to create and return an array of signed short numbers\"\"\"
    if isinstance(sequence, Array):
        return sequence
    elif isinstance(sequence, str):
        sequence = [ord(ch) for ch in sequence]

    return (Short * len(sequence))(*sequence)


def ushort_array(sequence):
    \"\"\"Factory function to create and return an array of unsigned short numbers\"\"\"
    if isinstance(sequence, Array):
        return sequence
    elif isinstance(sequence, str):
        sequence = [ord(ch) for ch in sequence]

    return (UShort * len(sequence))(*sequence)


def byte_array(sequence):
    \"\"\"Factory function to create and return an array of signed byte numbers\"\"\"
    if isinstance(sequence, Array):
        return sequence
    elif isinstance(sequence, str):
        sequence = [ord(ch) for ch in sequence]

    return (Byte * len(sequence))(*sequence)


def ubyte_array(sequence):
    \"\"\"Factory function to create and return an array of unsigned byte numbers\"\"\"
    if isinstance(sequence, Array):
        return sequence
    elif isinstance(sequence, str):
        sequence = [ord(ch) for ch in sequence]

    return (UByte * len(sequence))(*sequence)


def string_array(sequence, encoding='utf8', errors='ignore'):
    \"\"\"Factory function to create and return an array of char * (a char **)\"\"\"
    if isinstance(sequence, Array):
        return sequence
    elsequence = [s.encode(encoding, ignore) for s in sequence]

    return (CharPtr * len(sequence))(*sequence)

"""

# endregion (UTILITIES)

# region VECTOR MATH

# region VEC2

TPL_VEC2_MATH = """def __eq__(self, other):
    return _Vector2Equals(self, other)

def __ne__(self, other):
    return not _Vector2Equals(self, other)

def __pos__(self):
    return Vector2(+self.x, +self.y)

def __neg__(self):
    return Vector2(-self.x, -self.y)

def __abs__(self):
    return Vector2(abs(self.x), abs(self.y))

def __add__(self, other):
    if isinstance(other, (int, float)):
        return _Vector2AddValue(self, float(other))
    return _Vector2Add(self, Vector2(other[0], other[1]))

def __radd__(self, other):
    if isinstance(other, (int, float)):
        return _Vector2AddValue(self, float(other))
    return _Vector2Add(self, Vector2(other[0], other[1]))

def __iadd__(self, other):
    if isinstance(other, (int, float)):
        self.xy = _Vector2AddValue(self, float(other))
    else:
        self.xy = _Vector2Add(self, Vector2(other[0], other[1]))
    return self

def __sub__(self, other):
    if isinstance(other, (int, float)):
        return _Vector2SubtractValue(self, float(other))
    return _Vector2Subtract(self, Vector2(other[0], other[1]))

def __rsub__(self, other):
    if isinstance(other, (int, float)):
        return Vector2(other - self.x, other - self.y)
    return _Vector2Subtract(Vector2(other[0], other[1]), self)

def __isub__(self, other):
    if isinstance(other, (int, float)):
        self.xy = _Vector2SubtractValue(self, float(other))
    else:
        self.xy = _Vector2Subtract(self, Vector2(other[0], other[1]))
    return self

def __mul__(self, other):
    if isinstance(other, (int, float)):
        return _Vector2Scale(self, float(other))
    elif isinstance(other, Matrix):
        return _Vector2Transform(self, other)
    return _Vector2Multiply(self, Vector2(other[0], other[1]))

def __rmul__(self, other):
    if isinstance(other, (int, float)):
        return _Vector2Scale(self, float(other))
    return _Vector2Multiply(self, Vector2(other[0], other[1]))

def __imul__(self, other):
    if isinstance(other, (int, float)):
        self.xy = _Vector2Scale(self, float(other))
    elif isinstance(other, Matrix):
        self.xy = _Vector2Transform(self, other)
    else:
        self.xy = _Vector2Multiply(self, Vector2(other[0], other[1]))
    return self

def __truediv__(self, other):
    if isinstance(other, (int, float)):
        return _Vector2Divide(self, Vector2(other, other))
    return _Vector2Divide(self, Vector2(other[0], other[1]))

def __rtruediv__(self, other):
    if isinstance(other, (int, float)):
        return Vector2(other / self.x, other / self.y)
    return _Vector2Divide(Vector2(other[0], other[1]), self)

def __itruediv__(self, other):
    if isinstance(other, (int, float)):
        self.xy = _Vector2Divide(self, Vector2(other, other))
    else:
        self.xy = _Vector2Divide(self, Vector2(other[0], other[1]))
    return self"""


TPL_VEC2_SWIZZLING = """def __len__(self):
    return 2

def __getitem__(self, key):
    return (self.x, self.y).__getitem__(key)

def __getattr__(self, attr):
    m = RE_VEC2_GET_SWZL.fullmatch(attr)
    if not m:
        raise AttributeError("Vector2 object does not have attribute '{}'.".format(attr))
    cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
    v = self.todict()
    return cls(*(v[ch] for ch in attr))

def __setattr__(self, attr, value):
    m = RE_VEC2_SET_SWZL.fullmatch(attr)
    if not m:
        raise AttributeError("Vector2 object does not have attribute '{}'.".format(attr))
    if len(attr) == 1:
        super(Vector2, self).__setattr__(attr, float(value))
    else:
        for i, ch in enumerate(attr):
            super(Vector2, self).__setattr__(ch, float(value[i]))"""

TPL_VEC2_UTILS = """def todict(self):
    '''Returns a dict mapping this Vector2's components'''
    return {'x': self.x, 'y': self.y}

def fromdict(self, d):
    '''Apply the mapping `d` to this Vector2's components'''
    self.x = float(d.get('x', self.x))
    self.y = float(d.get('y', self.y))"""
# endregion (VEC2)

# region VEC3

TPL_VEC3_MATH = """def __eq__(self, other):
    return _Vector3Equals(self, other)

def __ne__(self, other):
    return not _Vector3Equals(self, other)

def __pos__(self):
    return Vector3(+self.x, +self.y, +self.z)

def __neg__(self):
    return Vector3(-self.x, -self.y, -self.z)

def __abs__(self):
    return Vector3(abs(self.x), abs(self.y), abs(self.z))

def __add__(self, other):
    if isinstance(other, (int, float)):
        return _Vector3AddValue(self, float(other))
    return _Vector3Add(self, Vector3(other[0], other[1], other[2]))

def __radd__(self, other):
    if isinstance(other, (int, float)):
        return _Vector3AddValue(self, float(other))
    return _Vector3Add(self, Vector3(other[0], other[1], other[2]))

def __iadd__(self, other):
    if isinstance(other, (int, float)):
        self.xy = _Vector3AddValue(self, float(other))
    else:
        self.xy = _Vector3Add(self, Vector3(other[0], other[1], other[2]))
    return self

def __sub__(self, other):
    if isinstance(other, (int, float)):
        return _Vector3SubtractValue(self, float(other))
    return _Vector3Subtract(self, Vector3(other[0], other[1], other[2]))

def __rsub__(self, other):
    if isinstance(other, (int, float)):
        return Vector3(other - self.x, other - self.y, other - self.z)
    return _Vector3Subtract(Vector3(other[0], other[1], other[2]), self)

def __isub__(self, other):
    if isinstance(other, (int, float)):
        self.xy = _Vector3SubtractValue(self, float(other))
    else:
        self.xy = _Vector3Subtract(self, Vector3(other[0], other[1], other[2]))
    return self

def __mul__(self, other):
    if isinstance(other, (int, float)):
        return _Vector3Scale(self, float(other))
    elif isinstance(other, Matrix):
        return _Vector3Transform(self, other)
    return _Vector3Multiply(self, Vector3(other[0], other[1], other[2]))

def __rmul__(self, other):
    if isinstance(other, (int, float)):
        return _Vector3Scale(self, float(other))
    return _Vector3Multiply(self, Vector3(other[0], other[1], other[2]))

def __imul__(self, other):
    if isinstance(other, (int, float)):
        self.xy = _Vector3Scale(self, float(other))
    elif isinstance(other, Matrix):
        self.xy = _Vector3Transform(self, other)
    else:
        self.xy = _Vector3Multiply(self, Vector3(other[0], other[1], other[2]))
    return self

def __truediv__(self, other):
    if isinstance(other, (int, float)):
        return _Vector3Divide(self, Vector3(other, other))
    return _Vector3Divide(self, Vector3(other[0], other[1]))

def __rtruediv__(self, other):
    if isinstance(other, (int, float)):
        return Vector3(other / self.x, other / self.y, other / self.z)
    return _Vector3Divide(Vector3(other[0], other[1], other[2]), self)

def __itruediv__(self, other):
    if isinstance(other, (int, float)):
        self.xy = _Vector3Divide(self, Vector3(other, other))
    else:
        self.xy = _Vector3Divide(self, Vector3(other[0], other[1], other[2]))
    return self"""

TPL_VEC3_SWIZZLING = """def __len__(self):
    return 3

def __getitem__(self, key):
    return (self.x, self.y, self.z).__getitem__(key)

def __getattr__(self, attr):
    m = RE_VEC3_GET_SWZL.fullmatch(attr)
    if not m:
        raise AttributeError("Vector3 object does not have attribute '{}'.".format(attr))
    cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
    v = self.todict()
    return cls(*(v[ch] for ch in attr))

def __setattr__(self, attr, value):
    m = RE_VEC3_SET_SWZL.fullmatch(attr)
    if not m:
        raise AttributeError("Vector3 object does not have attribute '{}'.".format(attr))
    if len(attr) == 1:
        super(Vector3, self).__setattr__(attr, float(value))
    else:
        for i, ch in enumerate(attr):
            super(Vector3, self).__setattr__(ch, float(value[i]))"""

TPL_VEC3_UTILS = """def todict(self):
    '''Returns a dict mapping this Vector3's components'''
    return {'x': self.x, 'y': self.y, 'z': self.z}

def fromdict(self, d):
    '''Apply the mapping `d` to this Vector3's components'''
    self.x = float(d.get('x', self.x))
    self.y = float(d.get('y', self.y))
    self.z = float(d.get('z', self.z))"""

# endregion (VEC3)

# region VEC4

TPL_VEC4_MATH = """def __eq__(self, other):
    return _Vector3Equals(self.xyz, other[:3])

def __ne__(self, other):
    return not _Vector3Equals(self.xyz, other[:3])

def __pos__(self):
    return Vector4(+self.x, +self.y, +self.z, +self.w)

def __neg__(self):
    return Vector4(-self.x, -self.y, -self.z, -self.w)

def __abs__(self):
    return Vector4(abs(self.x), abs(self.y), abs(self.z), abs(self.w))"""

TPL_VEC4_SWIZZLING = """def __len__(self):
    return 4

def __getitem__(self, key):
    return (self.x, self.y, self.z, self.w).__getitem__(key)

def __getattr__(self, attr):
    m = RE_VEC4_GET_SWZL.fullmatch(attr)
    if not m:
        raise AttributeError("Vector4 object does not have attribute '{}'.".format(attr))
    cls = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
    v = self.todict()
    return cls(*(v[ch] for ch in attr))

def __setattr__(self, attr, value):
    m = RE_VEC4_SET_SWZL.fullmatch(attr)
    if not m:
        raise AttributeError("Vector4 object does not have attribute '{}'.".format(attr))
    if len(attr) == 1:
        super(Vector4, self).__setattr__(attr, float(value))
    else:
        for i, ch in enumerate(attr):
            super(Vector4, self).__setattr__(ch, float(value[i]))"""

TPL_VEC4_UTILS = """def todict(self):
    '''Returns a dict mapping this Vector4's components'''
    return {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}

def fromdict(self, d):
    '''Apply the mapping `d` to this Vector4's components'''
    self.x = float(d.get('x', self.x))
    self.y = float(d.get('y', self.y))
    self.z = float(d.get('z', self.z))
    self.w = float(d.get('w', self.w))"""

# endregion (VEC4)

# region MAT4

# endregion (MAT4)

# endregion (VECTOR MATH)

# region RECT

TPL_RECT_SWIZZLING = """def __len__(self):
    return 4

def __getitem__(self, key):
    return (self.x, self.y, self.width, self.height).__getitem__(key)

def __getattr__(self, attr):
    m = RE_RECT_GET_SWZL.fullmatch(attr)
    if not m:
        raise AttributeError("Rectangle object does not have attribute '{}'.".format(attr))
    cls = {1: float, 2: Vector2, 3: Vector3, 4: Rectangle}.get(len(attr))
    v = self.todict()
    return cls(*(v[ch] for ch in attr))

def __setattr__(self, attr, value):
    m = RE_RECT_SET_SWZL.fullmatch(attr)
    if not m:
        raise AttributeError("Rectangle object does not have attribute '{}'.".format(attr))
    w = self.width
    h = self.height
    if attr in ('width', 'height') or len(attr) == 1:
        if attr == 'c':
            super(Rectangle, self).__setattr__('x', float(value - w * 0.5))
        elif attr == 'r':
            super(Rectangle, self).__setattr__('x', float(value - w))
        elif attr == 'm':
            super(Rectangle, self).__setattr__('y', float(value - h * 0.5))
        elif attr == 'b':
            super(Rectangle, self).__setattr__('y', float(value - h))
        elif attr == 'w':
            super(Rectangle, self).__setattr__('width', value)
        elif attr == 'h':
            super(Rectangle, self).__setattr__('height', value)
        else:
            super(Rectangle, self).__setattr__(attr, float(value))
    else:
        for i, ch in enumerate(attr):
            if ch in ('x', 'y'):
                super(Rectangle, self).__setattr__(ch, float(value[i]))
            elif ch == 'c':
                super(Rectangle, self).__setattr__('x', float(value[i] - w * 0.5))
            elif ch == 'r':
                super(Rectangle, self).__setattr__('x', float(value[i] - w))
            elif ch == 'm':
                super(Rectangle, self).__setattr__('y', float(value[i] - h * 0.5))
            elif ch == 'b':
                super(Rectangle, self).__setattr__('y', float(value[i] - h))
            elif ch == 'w':
                super(Rectangle, self).__setattr__('width', value[i])
            elif ch == 'h':
                super(Rectangle, self).__setattr__('height', value[i])"""

TPL_RECT_UTILS = """def todict(self):
    '''Returns a dict mapping this Rectangle's components'''
    return {'x': self.x, 'y': self.y, 'w': self.width, 'h': self.height,
            'c': self.x + self.width * 0.5, 'm': self.y + self.height * 0.5,
            'r': self.x + self.width, 'b': self.y + self.height}

def fromdict(self, d):
    '''Apply the mapping `d` to this Rectangle's components'''
    self.x = float(d.get('x', self.x))
    self.y = float(d.get('y', self.y))
    self.width = float(d.get('w', self.width))
    self.height = float(d.get('h', self.height))"""

# endregion (RECT)

# region COLOR


TPL_COLOR_SWIZZLING = """def __len__(self):
    return 4

def __getitem__(self, key):
    return (self.r, self.g, self.b, self.a).__getitem__(key)

def __getattr__(self, attr):
    m = RE_RGBA_GET_SWZL.fullmatch(attr)
    if not m:
        raise AttributeError("Color object does not have attribute '{}'.".format(attr))
    cls = {1: int, 4: Color}.get(len(attr))
    v = self.todict()
    return cls(*(v[ch] for ch in attr))

def __setattr__(self, attr, value):
    m = RE_RGBA_SET_SWZL.fullmatch(attr)
    if not m:
        raise AttributeError("Color object does not have attribute '{}'.".format(attr))
    if len(attr) == 1:
        super(Color, self).__setattr__(attr, int(value))
    else:
        for i, ch in enumerate(attr):
            super(Color, self).__setattr__(ch, int(value[i]))"""

TPL_COLOR_UTILS = """def todict(self):
    '''Returns a dict mapping this Color's components'''
    return {'r': self.r, 'g': self.g, 'b': self.b, 'a': self.a}

def fromdict(self, d):
    '''Apply the mapping `d` to this Color's components'''
    self.r = int(d.get('r', self.r))
    self.g = int(d.get('g', self.g))
    self.b = int(d.get('b', self.b))
    self.a = int(d.get('a', self.a))"""

# endregion (COLOR)

# endregion (constants)
# ---------------------------------------------------------
# region CLASSES

# endregion (classes)
# ---------------------------------------------------------
# region FUNCTIONS

# endregion (functions)
