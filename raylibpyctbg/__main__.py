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

USAGE = '''raylibpy ctypes binding generator help

Usage:
    $ python raylibpyctbg [options...]

    OPTIONS:
        OPT NAME                        DEFAULT?    DESCRIPTION
        -help                           --          prints this message and exits
        -typeHint                       no          adds Python2 type hinting
        -typeAnnotate                   no          adds Python3.3+ type annotation
        -snakecase                      no          apply Python's naming convention to all names
        -attribSwizzling                no          adds attribute swizzling to Vector{2,3,4}, Color and Rectangle
        -bindApi                        no          binds functions as property, context manager, classmethod, staticmethod and instancemethod
        -snakecaseFunctions             no          apply Python's naming convention to functions (and methods)
        -snakecaseParameters            no          apply Python's naming convention to parameters
        -snakecaseFields                no          apply Python's naming convention to fields
        -bindApiAsClassmethod           no          binds functions as classmethod
        -bindApiAsStaticmethod          no          binds functions as staticmethod
        -bindApiAsMethod                no          binds functions as method
        -bindApiAsProperty              no          binds functions as property
        -bindApiAsContextManager        no          context management binding for structs (Camera{2,3}D, Shader, VrStereoConfig, RenderTexture)
        -addContextManager              no          context management for Mode functions (Drawing, Scissor, Blend, 2D, 3D, Shader, Texture, VrStereoMode)
        -addVectorAttribSwizzling       yes         adds attribute swizzling to Vector{2,3,4}
        -addVectorMath                  yes         adds vector math to Vector{2,3} (requires swizzling and rmath to be included)
        -addColorAttribSwizzling        yes         adds attribute swizzling to Color
        -addRectangleAttribSwizzling    yes         adds attribute swizzling to Rectangle
        -pythonic                       no          combines -bindApi -typeAnnotate -snakecase -attribSwizzling -addContextManager -addVectorMath
        -spartan                        no          combines -no-bindApi -typeHint -no-snakecase -no-attribSwizzling -no-addContextManager -no-addVectorMath
        -onlyDocs                       no          no binding code generation, only documentation

        OPT NAME                        DESCRIPTION
        -no-type                        no type hinting nor annotations
        -no-snakecase                   keeps lib naming convention (C99 camelCase/PascalCase) on all names
        -no-attribSwizzling             no attribute zwizzling at all
        -no-bindApi                     no functions as property, context manager, classmethod, staticmethod nor instancemethod
        -no-snakecaseFunctions          keeps lib naming convention to functions (and methods)
        -no-snakecaseParameters         keeps lib naming convention to parameters
        -no-snakecaseFields             keeps lib naming convention to fields
        -no-bindApiAsClassmethod        no classmethod binding of functions
        -no-bindApiAsStaticmethod       no staticmethod binding of functions
        -no-bindApiAsMethod             no method binding of functions
        -no-bindApiAsProperty           no property binding of functions
        -no-bindApiAsContextManager     no context management binding for structs (Camera{2,3}D, Shader, VrStereoConfig, RenderTexture)
        -no-addContextManager           no context management for Mode functions (Drawing, Scissor, Blend, 2D, 3D, Shader, Texture, VrStereoMode)
        -no-addVectorAttribSwizzling    no attribute swizzling to Vector{2,3,4}
        -no-addVectorMath               no vector math to Vector{2,3}
        -no-addColorAttribSwizzling     no attribute swizzling to Color
        -no-addRectangleAttribSwizzling no attribute swizzling to Rectangle

        --libBaseDir <value>            set basepath to load the lib binaries to specified directory
                                            Note: this value is passed as first argument(s) to os.path.join()
        --win32LibFilename <value>      custom .dll binary to be loaded on Windows (only file name and extension)
        --linuxLibFilename <value>      custom .so binary to be loaded on Linux (only file name and extension)
        --darwinLibFilename <value>     custom .dylib binary to be loaded on MacOS (only file name and extension)
        --include <value>               include extra parsed headers:
                                            use 'rmath' to include rmath.h functions from 'input/rmath_api.json'
                                            use 'rlgl' to include rlgl.h functions and types from 'input/rlgl.json'
                                            filepath to any other parsed header exposed in raylib (JSON)
        --out <value>                   filepath to write the binding into
        --markdown <value>              filepath to write the api reference (Markdown format) into
        
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
    doc_out_fname = None

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
                    config['rmathIncluded'] = True
                elif val == 'rlgl':
                    val = rlgl
                    config['rlglIncluded'] = True

                if val not in include:
                    include.append(val)

            elif key == 'out':
                out_file = val

            elif key == 'markdown':
                doc_out_fname = val

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
                config["addContextManager"] = True
                config["addVectorMath"] = True
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
                config["addContextManager"] = False
                config["addVectorMath"] = False
            else:
                config[key] = True

    try:
        gen_wrapper(include, out_file, in_bind_info, doc_out_fname, **config)
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
