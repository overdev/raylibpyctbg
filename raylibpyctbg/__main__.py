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
import traceback

from argparse import ArgumentParser, Namespace
from core import GlobalWrapperData
from rlapi3 import generate_binding_code, update_package_manifest
import rlapi_changes as rlch

# endregion (imports)
# ---------------------------------------------------------
# region FUNCTIONS

RE_FNAME = re.compile(r"raylib_py-\d\.\d\.\d(?:(?:a|b|.post)\d)?-py3-none-any.whl")


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
    r = '<dir>'
    for (r, d, f) in os.walk(os.getcwd()):
        for name in f:
            if m := RE_FNAME.fullmatch(name):
                return 1, name
    return -2, f"Wheel file not found in {r}"


def gen_binding(cfg_path, package_path, out_path) -> 'tuple[int, str]':
    try:
        wrapper = GlobalWrapperData.load(cfg_path)
        generate_binding_code(wrapper, out_path)
        update_package_manifest(wrapper, os.path.join(package_path, "MANIFEST.in"))
        return 0, f"Binding code generated and stored; manifest file updated"

    except Exception as e:
        traceback.print_exc()
        return -2, f"{e.args}"


def compare_apis(base, current) -> 'tuple[int, str]':
    lib, vbase = base
    _, vcurr = current
    fname = f"api_changes_{lib}_{vbase}_{vcurr}.txt"

    try:
        rlch.log_changes(base, current, f"output\\{fname}")
        return 0, f"Compared {base} and {current}. Check output\\{fname} for details"

    except Exception as e:
        traceback.print_exc()
        return -2, f"{e.args[0]}"

# endregion (COMMAND FUNCTIONS)


def main() -> 'int':
    """Entry point"""

    NONE = 'None'

    parser = ArgumentParser()
    parser.add_argument('-c', '--config', help="Custom binding configuration (JSON) file path", default=NONE, type=str, required=False)
    parser.add_argument('-o', '--out', help="The binding code output file path", default=NONE, type=str, required=False)
    parser.add_argument('-a', '--api', help="Select the api version from which to generate the binding (default is 550)", default='550', type=str, required=False)
    parser.add_argument('-g', '--generate', help="Generate the binding code", action="store_true", required=False)
    parser.add_argument('-d', '--docs', help="Generate the binding documentation (inactive)", action="store_true", required=False)
    parser.add_argument('-b', '--build', help="Build the package (requires build package) ", action="store_true", required=False)
    parser.add_argument('-i', '--install', help="[Re]Install the newly built package", action="store_true", required=False)
    parser.add_argument('-m', '--compare', help="Compare base vs current API versions (e.g. -m 500 550)", nargs=2, type=str, required=False)
    parser.add_argument('-v', '--version', help="Print the version information and exits", action="store_true", required=False)

    args: Namespace = parser.parse_args()

    user_cwd = os.getcwd()
    proj_cwd = os.path.dirname(__file__)
    proj_root_cwd = os.path.dirname(os.path.dirname(__file__))
    pckg_cwd = os.path.join(proj_root_cwd, 'package')

    if args.version:
        print("raylibpyctbg version 5.5.0")
        return 0

    if args.config == NONE:
        apidir = f"rl{args.api}"
        args.config = os.path.join(proj_root_cwd, 'input', apidir, 'global_config.json')

    if not os.path.isfile(args.config) or not os.path.exists(args.config):
        print(f"ERROR: Unable to load configuration file: '{args.config}'")
        return 1

    build_disabled = True
    if args.out == NONE:
        build_disabled = False
        args.out = os.path.join(proj_root_cwd, 'package', 'src', 'raylibpy', '__init__.py')
        args.out = os.path.normpath(args.out)

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

    if args.compare:
        base, curr = args.compare
        commands.append(("Status message", rf"echo(r'   Comparing API versions')"))
        commands.append(("Comparing APIs: raylib", rf"compare_apis(rlch.RAYLIB_{base}, rlch.RAYLIB_{curr})"))
        commands.append(("Comparing APIs: raymath", rf"compare_apis(rlch.RAYMATH_{base}, rlch.RAYMATH_{curr})"))
        commands.append(("Comparing APIs: rlgl", rf"compare_apis(rlch.RLGL_{base}, rlch.RLGL_{curr})"))
        commands.append(("Status message", rf"echo(r'   API comparison finished')"))

    if args.generate:
        commands.append(("Status message", rf"echo(r'   Binding code generation process started')"))
        commands.append(("Composing the source code", rf"gen_binding(r'{args.config}', r'{pckg_cwd}', r'{args.out}')"))
        commands.append(("Status message", rf"echo(r'   Binding code generation process finished')"))

    if args.build:
        commands.append(("Status message", rf"echo(r'   Building process started')"))
        commands.append(("Moving to /package", rf"chdir_to(r'{pckg_cwd}')"))
        commands.append(("Removing /dist", f"rem_dir('dist')"))
        commands.append(("Package building", [sys.executable, '-m', 'build', '-nx']))
        commands.append(("Moving back to /package", rf"chdir_to(r'..')"))
        commands.append(("Status message", rf"echo(r'   Building process finished')"))

    if args.install:
        commands.append(("Status message", rf"echo(r'   Installation process started')"))
        commands.append(("Ensure we're in /package", rf"chdir_to(r'{pckg_cwd}')"))
        commands.append(("Moving to /dist", rf"chdir_to(r'dist')"))
        commands.append(("Searching for the wheel file", f"find_wheel()"))
        commands.append(("[Re]Installing package", [sys.executable, '-m', 'pip', 'install', '--force-reinstall']))
        commands.append(("Moving back to where we started", rf"chdir_to(r'../..')"))
        commands.append(("Status message", rf"echo(r'   Installation process finished')"))

    print("CWD:", os.getcwd())

    if len(commands):
        print(f"Executing commands")
        cmd_argument = None
        n = len(commands)
        has_error = False
        for i, (description, command) in enumerate(commands, start=1):
            if has_error:
                print(f"\nStep {i}/{n} :: {description} :: Skipped due to error\n")
                continue
            try:
                print(f"\nStep {i}/{n} :: {description}\n")
                if isinstance(command, str):
                    result_type, result_value = eval(command)
                    if result_type == -2:
                        print("CMD:", command)
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
                    if cp.returncode != 0:
                        has_error = True
                    # print(f"{cp.stdout}\n" if cp.stdout else '')
                    # print("COMMAND --> ", command)

            except (Exception, subprocess.CalledProcessError) as e:
                with open("traceback.log", 'w', encoding='utf8') as fp:
                    traceback.print_exc(file=fp)
                print(f"ERROR: {description} failed: {', '.join(repr(arg) for arg in e.args) }\n\tCheck 'output/traceback.log' for more information",)

                return 1
        
        print("\nFinished all processes.")

    return 0

# endregion (functions)
# ---------------------------------------------------------
# region ENTRYPOINT


if __name__ == '__main__':
    sys.exit(main())

# endregion (entrypoint)