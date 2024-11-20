# -*- encoding: utf8 -*-

# region LICENSE
# ------------------------------------------------------------------------------
# The MIT License
#
#
# Copyright © 2024 Jorge A. Gomes
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
import json

from re import Pattern, Match
from types import FunctionType, SimpleNamespace
from typing import Any, Sequence
from contextlib import contextmanager
from dataclasses import dataclass, field
from enum import Enum, IntEnum, auto

# endregion (imports)
# ---------------------------------------------------------
# region EXPORTS


__all__ = [
    'log_changes',
    'RAYLIB_550',
    'RAYMATH_550',
    'RLGL_550',
    'RAYLIB_500',
    'RAYMATH_500',
    'RLGL_500',
    'RAYLIB_420',
    'RAYMATH_420',
    'RLGL_420',
]


# endregion (exports)
# ---------------------------------------------------------
# region GLOBALS

# endregion (globals)
# ---------------------------------------------------------
# region CONSTANTS, ENUMS & NAMEDTUPLES

ApiData = dict[str, Any]

path_fmt: str = "input\\rl{ver}\\{api}.json"


RAYLIB_550: tuple[str, str] = ('raylib_api', '550')
RAYMATH_550: tuple[str, str] = ('rmath_api', '550')
RLGL_550: tuple[str, str] = ('rlgl_api', '550')
RAYLIB_500: tuple[str, str] = ('raylib_api', '500')
RAYMATH_500: tuple[str, str] = ('rmath_api', '500')
RLGL_500: tuple[str, str] = ('rlgl', '500')
RAYLIB_420: tuple[str, str] = ('raylib_api', '420')
RAYMATH_420: tuple[str, str] = ('rmath_api', '420')
RLGL_420: tuple[str, str] = ('rlgl_api', '420')

# endregion (constants)
# ---------------------------------------------------------
# region CLASSES

# endregion (classes)
# ---------------------------------------------------------
# region FUNCTIONS


def added(name: str, indent: int = 0) -> str:
    return f"{' ' * indent}ADDED: {name}"


def changed(name: str, indent: int = 0) -> str:
    return f"{' ' * indent}CHANGED: {name}"


def removed(name: str, indent: int = 0) -> str:
    return f"{' ' * indent}REMOVED: {name}"


def clsn(o_: Any) -> str:
    return o_.__class__.__name__


def load_api(module: str, version: str) -> ApiData:
    fname: str = path_fmt.format(ver=version, api=module)

    with open(fname, 'r', encoding='utf8') as fp:
        api: ApiData = json.load(fp)

    return api


def compare_apis(base: ApiData, current: ApiData, lines: list[str]) -> None:
    empty: ApiData = {}

    for (section, key) in (('defines', 'name'), ('structs', 'name'), ('aliases', 'type'), ('enums', 'name'), ('functions', 'name')):
        lines.append(f'API - {section}')
        lines.append('')
        section_base: list[ApiData] = base.get(section, empty)
        section_current: list[ApiData] = current.get(section, empty)
        lines.append('')
        lines.append(f'[BASE: {len(section_base)} items][CURRENT: {len(section_current)} items]')
        lines.append('')

        nbase: list[str] = [item['name'] for item in section_base]
        ncurr: list[str] = [item['name'] for item in section_current]

        for name in ncurr:
            if name not in nbase:
                lines.append(added(name))

        for name in nbase:
            if name not in ncurr:
                lines.append(removed(name))


def log_changes(base_ver: tuple[str, str], current_ver: tuple[str, str], out_fname: str) -> None:
    base_api: ApiData = load_api(*base_ver)
    current_api: ApiData = load_api(*current_ver)

    changes: list[str] = [
        f"API CHANGES BETWEEN {base_ver[0]} v{base_ver[1]} (BASE) AND {current_ver[0]} v{current_ver[1]} (CURRENT)",
        "",
        "",
    ]
    compare_apis(base_api, current_api, changes)

    with open(out_fname, 'w', encoding='utf8') as fp:
        fp.write("\n".join(changes))

# endregion (functions)
