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

from rlapi2 import main as gen_wrapper

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
    $ python raylibpyctbg [options...]

    OPTIONS:
        -typeHint                       adds Python2 type hinting
        -typeAnnotate                   adds Python3.3+ type annotation
        -snakecase                      apply Python's naming convention to all names
        -attribSwizzling                adds attribute swizzling to Vector{2,3,4}, Color and Rectangle
        -bindApi                        binds functions as classmethod, staticmethod or instancemethod
        -snakecaseFunctions             apply Python's naming convention to functions (and methods)
        -snakecaseParameters            apply Python's naming convention to parameters
        -snakecaseFields                apply Python's naming convention to fields
        -bindApiAsClassmethod           binds functions as classmethod
        -bindApiAsStaticmethod          binds functions as staticmethod
        -bindApiAsMethod                binds functions as method
        -bindApiAsProperty              binds functions as property
        -addVectorAttribSwizzling       adds attribute swizzling to Vector{2,3,4}
        -addColorAttribSwizzling        adds attribute swizzling to Color
        -addRectangleAttribSwizzling    adds attribute swizzling to Rectangle
        -pythonic                       combines -bindApi -typeAnnotate -snakecase -attribSwizzling
        -spartan                        combines -no-bindApi -typeHint -no-snakecase -no-attribSwizzling

        -no-type                        no type hinting nor annotations
        -no-snakecase                   keeps lib naming convention (C99 camelCase/PascalCase) on all names
        -no-attribSwizzling             no attribute zwizzling at all
        -no-bindApi                     no functions as classmethod, staticmethod nor instancemethod
        -no-snakecaseFunctions          keeps lib naming convention to functions (and methods)
        -no-snakecaseParameters         keeps lib naming convention to parameters
        -no-snakecaseFields             keeps lib naming convention to fields
        -no-bindApiAsClassmethod        no classmethod binding of functions
        -no-bindApiAsStaticmethod       no staticmethod binding of functions
        -no-bindApiAsMethod             no method binding of functions
        -no-bindApiAsProperty           no property binding of functions
        -no-addVectorAttribSwizzling    no attribute swizzling to Vector{2,3,4}
        -no-addColorAttribSwizzling     no attribute swizzling to Color
        -no-addRectangleAttribSwizzling no attribute swizzling to Rectangle

        --libBaseDir <value>            set basepath to load the lib binaries to specified directory
        --win32LibFilename <value>      custom .dll binary to be loaded on Windows (only file name and extension)
        --linuxLibFilename <value>      custom .so binary to be loaded on Linux (only file name and extension)
        --darwinLibFilename <value>     custom .dylib binary to be loaded on MacOS (only file name and extension)
        --include <value>               include extra parsed headers:
                                            rmath: include rmath_api.json
                                            rlgl: include rlgl.json
                                            filepath to any other parsed header exposed in raylib (JSON)
        --out <value>                   filepath to write the binding into
        
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
        _, out_fname, *flags = args
    except (TypeError, ValueError):
        print(USAGE)
        return 1

    base = os.path.dirname(os.path.dirname(__file__))

    raylib = os.path.join(base, 'input/raylib_api.json')
    rmath = os.path.join(base, 'input/rmath_api.json')
    rlgl = os.path.join(base, 'input/rlgl.json')
    in_bind_info = os.path.join(base, 'input/raylib_api.bind.json')
    out_file = os.path.join(os.getcwd(), 'rl.py')

    include = [raylib]

    config = {}

    skip_arg = False
    for i, arg in enumerate(args):
        if skip_arg:
            skip_arg = False
            continue

        if arg.startswith('--'):
            key = arg[2:]
            val = args[i + 1]
            skip_arg = True

            if key == 'include':
                if val == 'rmath':
                    val = rmath
                elif val == 'rlgl':
                    val = rlgl

                if val not in include:
                    include.append(val)

            elif key == 'out':
                out_file = val

            else:
                config[key] = val


        elif arg.startswith('-no-'):
            key = arg[4:]
            if key == 'type':
                config['typeHint'] = False
                config['typeAnnotate'] = False
            elif key == 'attribSwizzling':
                config['addVectorAttribSwizzling'] = False
                config['addColorAttribSwizzling'] = False
                config['addRectangleAttribSwizzling'] = False
            elif key == 'bindApi':
                config['bindApiAsClassmethod'] = False
                config['bindApiAsStaticmethod'] = False
                config['bindApiAsMethod'] = False
                config['bindApiAsProperty'] = False
                config['bindApiAsContextManager'] = False
            elif key == 'snakecase':
                config['snakecaseFunctions'] = False
                config['snakecaseParameters'] = False
                config['snakecaseFields'] = False
            else:
                config[key] = False

        elif arg.startswith('-'):
            key = arg[1:]
            if key ==  'help':
                print(USAGE)
                exit()
            elif key == 'typeHint':
                config[key] = True
                config['typeAnnotate'] = False
            elif key == 'typeAnnotate':
                config[key] = True
                config['typeHint'] = False
            elif key == 'attribSwizzling':
                config['addVectorAttribSwizzling'] = False
                config['addColorAttribSwizzling'] = False
                config['addRectangleAttribSwizzling'] = False
            elif key == 'bindApi':
                config['bindApiAsClassmethod'] = True
                config['bindApiAsStaticmethod'] = True
                config['bindApiAsMethod'] = True
                config['bindApiAsProperty'] = True
                config['bindApiAsContextManager'] = True
            elif key == 'snakecase':
                config['snakecaseFunctions'] = True
                config['snakecaseParameters'] = True
                config['snakecaseFields'] = True
            elif key == 'pythonic':
                config["snakecaseFunctions"] = True
                config["snakecaseParameters"] = True
                config["snakecaseFields"] = True
                config["bindApiAsClassmethod"] = True
                config["bindApiAsStaticmethod"] = True
                config["bindApiAsMethod"] = True
                config["bindApiAsProperty"] = True
                config["bindApiAsContextManager"] = True
                config["typeHint"] = False
                config["typeAnnotate"] = True
                config["addVectorAttribSwizzling"] = True
                config["addColorAttribSwizzling"] = True
                config["addRectangleAttribSwizzling"] = True
            elif key == 'spartan':
                config["snakecaseFunctions"] = False
                config["snakecaseParameters"] = False
                config["snakecaseFields"] = False
                config["bindApiAsClassmethod"] = False
                config["bindApiAsStaticmethod"] = False
                config["bindApiAsMethod"] = False
                config["bindApiAsProperty"] = False
                config["bindApiAsContextManager"] = False
                config["typeHint"] = True
                config["typeAnnotate"] = False
                config["addVectorAttribSwizzling"] = False
                config["addColorAttribSwizzling"] = False
                config["addRectangleAttribSwizzling"] = False
            else:
                config[key] = False

    try:
        gen_wrapper(include, out_file, in_bind_info, **config)
    except Exception as e:
        print("Unable to generate the python binding due to an error:\n {}{}".format(e.__class__.__name__, e.args))
        return 1

    return 0


# endregion (functions)
# ---------------------------------------------------------
# region ENTRYPOINT


if __name__ == '__main__':
    sys.exit(main(*sys.argv))

# endregion (entrypoint)
