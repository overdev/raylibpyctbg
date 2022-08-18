# -*- encoding: utf8 -*-
# ------------------------------------------------------------------------------
# __main__.py
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

import sys, os

from rlapi import generate_wrapper

# endregion (imports)
# ---------------------------------------------------------
# region EXPORTS


__all__ = [
    '',
]


# endregion (exports)
# ---------------------------------------------------------
# region CONSTANTS & ENUMS

USAGE = '''raylibpy wrapper tools

Usage:
    $ python raylib_wrapper "path/to/raylib_api.json" "path/to/output/python/file"
'''

# endregion (constants)
# ---------------------------------------------------------
# region CLASSES

# endregion (classes)
# ---------------------------------------------------------
# region FUNCTIONS


def main(*args) -> int:
    # generate_wrapper('./raylib_api.json', './raylib_api.txt')
    print(os.getcwd())
    try:
        _, rlapi_jsonfile, out_fname, *a = args
    except (TypeError, ValueError):
        print(USAGE)
        return 1

    generate_wrapper(rlapi_jsonfile, out_fname)
    return 0


# endregion (functions)
# ---------------------------------------------------------
# region ENTRYPOINT


if __name__ == '__main__':
    sys.exit(main(*sys.argv))

# endregion (entrypoint)
