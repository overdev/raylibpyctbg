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
import os
import os.path
import shutil
import re
import subprocess

from argparse import ArgumentParser, Namespace
from core import GlobalWrapperData
from rlapi3 import generate_binding_code

# endregion (imports)
# ---------------------------------------------------------
# region FUNCTIONS

RE_FNAME = re.compile(r"raylib_py-\d\.\d\.\d([abp]\d)?-py3-none-any.whl")


def readonly_handler(func, path, execinfo): 
    os.chmod(path, 128) #or os.chmod(path, stat.S_IWRITE) from "stat" module
    func(path)

# region COMMAND FUNCTIONS


def echo(msg):
    return 0, msg


def chdir_to(dirname):
    try:
        os.chdir(dirname)
        return -0, f"cwd: {os.getcwd()}"
    except Exception as e:
        return -2, f"{e.args}"


def rem_dir(dirname) -> 'tuple[int, str]':
    try:
        if os.path.exists(dirname):
            shutil.rmtree(dirname, onerror=readonly_handler)
            return 0, f"/{dirname} removed"
        else:
            return 0, f"/{dirname} already removed"
    except Exception as e:
        return -2, f"{e.args}"


def find_wheel() -> 'tuple[int, str]':
    for (r, d, f) in os.walk(os.getcwd()):
        for name in f:
            if m := RE_FNAME.fullmatch(name):
                return 1, name
    return -2, f"Wheel file not found in {r}"


def gen_binding(cfg_path, out_path) -> 'tuple[int, str]':
    try:
        wrapper = GlobalWrapperData.load(cfg_path)
        generate_binding_code(wrapper, out_path)
        return 0, f"Binding code generated and stored"

    except Exception as e:
        return -2, f"{e.args}"

# endregion (COMMAND FUNCTIONS)


def main() -> 'int':
    """Entry point"""

    NONE = 'None'

    parser = ArgumentParser()
    parser.add_argument('-c', '--config', help="Custom binding configuration (JSON) file path", default=NONE, type=str, required=False)
    parser.add_argument('-o', '--out', help="The binding code output file path", default=NONE, type=str, required=False)
    parser.add_argument('-g', '--generate', help="Generate the binding code", action="store_true", required=False)
    parser.add_argument('-d', '--docs', help="Generate the binding documentation (inactive)", action="store_true", required=False)
    parser.add_argument('-b', '--build', help="Build the package (requires build package) ", action="store_true", required=False)
    parser.add_argument('-i', '--install', help="[Re]Install the newly built package", action="store_true", required=False)
    parser.add_argument('-v', '--version', help="Print the version information and exits", action="store_true", required=False)

    args: Namespace = parser.parse_args()

    user_cwd = os.getcwd()
    proj_cwd = os.path.dirname(os.path.dirname(__file__))
    pckg_cwd = os.path.join(proj_cwd, 'package')

    if args.version:
        print("raylibpyctbg version 3.0.0")
        return 0

    if args.config == NONE:
        args.config = os.path.join(proj_cwd, 'input', 'rl500', 'global_config.json')

    if not os.path.isfile(args.config) or not os.path.exists(args.config):
        print(f"ERROR: Unable to load configuration file: '{args.config}'")
        return 1

    build_disabled = True
    if args.out == NONE:
        build_disabled = False
        args.out = os.path.join(proj_cwd, 'package', 'src', 'raylibpy', '__init__.py')

    if not os.path.isfile(args.out):
        print(f"ERROR: Invalid output filepath: '{args.out}'")
        return 1

    print(f"Loading config from: {args.config}")
    if args.generate:
        print(f"Saving output into: {args.out}")

    if args.docs:
        # print(f"Saving docs into: {args.out}")
        print(f"Documentation generation not available.")

    commands = []
    result_type = -1
    result_value = ''

    if args.generate:
        commands.append(("Status message", rf"echo(r'Binding code generation process started')"))
        commands.append(("Composing the source code", rf"gen_binding(r'{args.config}', r'{args.out}')"))
        commands.append(("Status message", rf"echo(r'Binding code generation process finished')"))

    if args.build:
        commands.append(("Status message", rf"echo(r'Building process started')"))
        commands.append(("Moving to /package", rf"chdir_to(r'{pckg_cwd}')"))
        commands.append(("Removing /dist", f"rem_dir('dist')"))
        commands.append(("Package building", [sys.executable, '-m', 'build']))
        commands.append(("Moving back to /package", rf"chdir_to(r'..')"))
        commands.append(("Status message", rf"echo(r'Building process finished')"))

    if args.install:
        commands.append(("Status message", rf"echo(r'Installation process started')"))
        commands.append(("Ensure we're in /package", rf"chdir_to(r'{pckg_cwd}')"))
        commands.append(("Moving to /dist", rf"chdir_to(r'dist')"))
        commands.append(("Searching for the wheel file", f"find_wheel()"))
        commands.append(("[Re]Installing package", [sys.executable, '-m', 'pip', 'install', '--force-reinstall']))
        commands.append(("Moving back to where we started", rf"chdir_to(r'../..')"))
        commands.append(("Status message", rf"echo(r'Installation process finished')"))

    print("CWD:", os.getcwd())

    if len(commands):
        print(f"Executing commands")
        cmd_argument = None
        n = len(commands)
        for i, (description, command) in enumerate(commands, start=1):
            try:
                print(f"\nStep {i}/{n} :: {description}\n")
                if isinstance(command, str):
                    result_type, result_value = eval(command)
                    if result_type == -2:
                        assert False, f"`{result_value}`"
                    elif result_type == -1:
                        pass
                    elif result_type == 0:
                        print(result_value)
                    elif result_type == 1:
                        cmd_argument = result_value

                elif isinstance(command, list):
                    if isinstance(cmd_argument, str):
                        command.append(cmd_argument)
                        cmd_argument = None
                    print(' '.join(command))
                    cp = subprocess.run(command, text=True, stderr=subprocess.STDOUT)
                    print(f"{cp.stdout}\n" if cp.stdout else '')
                    # print("COMMAND --> ", command)

            except Exception as e:
                print(f"ERROR: {description} failed: {', '.join(repr(arg) for arg in e.args) }", False, False)
                return 1
        
        print("\nFinished all processes.")

    return 0

# endregion (functions)
# ---------------------------------------------------------
# region ENTRYPOINT


if __name__ == '__main__':
    sys.exit(main())

# endregion (entrypoint)