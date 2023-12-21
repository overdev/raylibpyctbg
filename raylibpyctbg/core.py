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
import keyword
import json
import os

from typing import Any, Sequence
from contextlib import contextmanager
from dataclasses import dataclass, field
from enum import Enum, auto

# endregion (imports)
# ---------------------------------------------------------
# region EXPORTS


__all__ = [
    'PythonSourceComposer',
    'ObjectMap',
    'DefineWrapperData',
    'StructFieldWrapperData',
    'AliasWrapperData',
    'StructWrapperData',
    'EnumerandWrapperData',
    'EnumWrapperData',
    'ParameterWrapperData',
    'CallbackWrapperData',
    'FunctionWrapperData',
    'TypeWrapperData',
    'ModuleWrapperData',
    'snakefy',
]


# endregion (exports)
# ---------------------------------------------------------
# region GLOBALS

# endregion (globals)
# ---------------------------------------------------------
# region CONSTANTS & ENUMS

# endregion (constants)
# ---------------------------------------------------------
# region CLASSES

# region WRAPPER OBJECTS


@dataclass
class DefineWrapperData:
    name: str
    kind: str
    value: str | int | float
    description: str
    module: str | None = None
    library: str | None = None
    metadata: dict[str, Any] | None = None

    @classmethod
    def load(cls, data: dict[str, Any], metadata: dict[str, Any] | None = None, module: str | None = None, library: str | None = None) -> 'DefineWrapperData':
        return cls(
            data.get('name', '_unnamed_'),
            data.get('type', ""),
            data.get('value', ""),
            data.get('description', ""),
            module,
            library,
            metadata,
        )


@dataclass
class StructFieldWrapperData:
    dtype: list
    name: str
    description: str
    metadata: dict[str, Any] | None = None

    @classmethod
    def load(cls, data: dict[str, Any], metadata: dict[str, Any] | None = None) -> 'StructFieldWrapperData':
        return cls(
            data.get('type', ""),
            data.get('name', '_unnamed_'),
            data.get('description', ""),
            metadata
        )


@dataclass
class AliasWrapperData:
    dtype: str
    name: str
    description: str
    module: str | None = None
    library: str | None = None
    metadata: dict[str, Any] | None = None

    @classmethod
    def load(cls, data: dict[str, Any], metadata: dict[str, Any] | None = None, module: str | None = None, library: str | None = None) -> 'AliasWrapperData':
        return cls(
            data.get('type', ""),
            data.get('name', '_unnamed_'),
            data.get('description', ""),
            module,
            library,
            metadata
        )


@dataclass
class StructWrapperData:
    name: str
    description: str
    fields: list[StructFieldWrapperData]
    aliases: list[AliasWrapperData] | None = None
    argument_cast: str | None = None
    module: str | None = None
    library: str | None = None
    metadata: dict[str, Any] | None = None

    @classmethod
    def load(cls, data: dict[str, Any], metadata: dict[str, Any] | None = None, aliases: list[AliasWrapperData] | None = None, module: str | None = None, library: str | None = None) -> 'StructWrapperData':
        fields: list[StructFieldWrapperData] = []
        for field_data in data.get('fields', []):
            fields.append(StructFieldWrapperData.load(field_data, None))

        return cls(
            data.get('name', '_unnamed_'),
            data.get('description', ""),
            fields,
            aliases,
            metadata.get('func') if metadata else None,
            module,
            library,
            metadata
        )


@dataclass
class EnumerandWrapperData:
    name: str
    value: str | int
    description: str
    metadata: dict[str, Any] | None = None

    @classmethod
    def load(cls, data: dict[str, Any], metadata: dict[str, Any] | None = None) -> 'EnumerandWrapperData':
        return cls(
            data.get('name', '_unnamed_'),
            data.get('value', ""),
            data.get('description', ""),
            metadata
        )


@dataclass
class EnumWrapperData:
    name: str
    description: str
    values: list[EnumerandWrapperData]
    module: str | None = None
    library: str | None = None
    metadata: dict[str, Any] | None = None

    @classmethod
    def load(cls, data: dict[str, Any], metadata: dict[str, Any] | None = None, module: str | None = None, library: str | None = None) -> 'EnumWrapperData':
        values: list[EnumerandWrapperData] = []
        for member_data in data.get('values', []):
            values.append(EnumerandWrapperData.load(member_data, None))

        return cls(
            data.get('name', '_unnamed_'),
            data.get('description', ""),
            values,
            module,
            library,
            metadata
        )


@dataclass
class ParameterWrapperData:
    dtype: str
    name: str
    metadata: dict[str, Any] | None = None

    @classmethod
    def load(cls, data: dict[str, Any], metadata: dict[str, Any] | None = None) -> 'ParameterWrapperData':
        return cls(
            data.get('type', ""),
            data.get('name', '_unnamed_'),
            metadata
        )


@dataclass
class CallbackWrapperData:
    name: str
    description: str
    rtype: str
    params: list[ParameterWrapperData]
    module: str | None = None
    library: str | None = None
    metadata: dict[str, Any] | None = None

    @classmethod
    def load(cls, data: dict[str, Any], metadata: dict[str, Any] | None = None, module: str | None = None, library: str | None = None) -> 'CallbackWrapperData':
        params: list[ParameterWrapperData] = []

        for param_data in data.get('params', []):
            params.append(ParameterWrapperData.load(param_data, None))

        return cls(
            data.get('name', '_unnamed_'),
            data.get('description', ""),
            data.get('returnType', ""),
            params,
            module,
            library,
            metadata
        )


@dataclass
class FunctionWrapperData:
    name: str
    description: str
    rtype: str
    params: list[ParameterWrapperData]
    module: str | None = None
    library: str | None = None
    metadata: dict[str, Any] | None = None

    @classmethod
    def load(cls, data: dict[str, Any], metadata: dict[str, Any] | None = None, module: str | None = None, library: str | None = None) -> 'FunctionWrapperData':
        params: list[ParameterWrapperData] = []

        for param_data in data.get('params', []):
            params.append(ParameterWrapperData.load(param_data, None))

        return cls(
            data.get('name', '_unnamed_'),
            data.get('description', ""),
            data.get('returnType', ""),
            params,
            module,
            library,
            metadata
        )


@dataclass
class TypeWrapperData:
    type_spec: str
    type_ctype: str = ""
    type_ctype2: str = ""
    type_py: str = ""
    max_indirection: int = 0
    declarator: str | None = None
    initializer: str | None = None
    cast_func: str | None = None
    module: str | None = None
    library: str | None = None
    metadata: dict[str, Any] | None = None


@dataclass
class ModuleWrapperData:
    name: str
    library: str
    bind_data: dict[str, Any]
    meta_data: dict[str, Any]
    opaque_types: list[str] | None = None
    ignored_functions: list[str] | None = None

    defines: dict[str, DefineWrapperData] | None = None
    structs: dict[str, StructWrapperData] | None = None
    aliases: dict[str, AliasWrapperData] | None = None
    enums: dict[str, EnumWrapperData] | None = None
    callbacks: dict[str, CallbackWrapperData] | None = None
    functions: dict[str, FunctionWrapperData] | None = None

    @classmethod
    def load(cls, module_name: str, library_name: str, bind_data_fname: str, meta_data_fname: str | None = None) -> 'ModuleWrapperData':
        with open(bind_data_fname, 'r', encoding='utf8') as fp:
            bind_data = json.load(fp)

        if meta_data_fname:
            with open(meta_data_fname, 'r', encoding='utf8') as fp:
                meta_data = json.load(fp)

        else:
            meta_data = { '_empty': True }

        return cls(module_name, library_name, bind_data, meta_data)


@dataclass
class LibraryWrapperData:
    name: str
    key_name: str
    base_dir: str
    is_extension: bool
    modules: dict[str: ModuleWrapperData]
    bin_fnames: 'ObjectMap'
    meta_data: dict[str, Any] | None = None


@dataclass
class GlobalWrapperData:
    config: 'ObjectMap | None'
    libraries: dict[str, LibraryWrapperData]
    types: list[str] | None = None
    type_map: dict[str, TypeWrapperData] | None = None
    global_names: dict[str, list[str]] | None = None
    indirections: dict[str, int] | None = None

    @classmethod
    def load(cls, config_fname: str) -> 'GlobalWrapperData':
        libraries = {}

        with open(config_fname, 'r', encoding='utf8') as fp:
            config = ObjectMap.load_any(json.load(fp))

        lib = cls.load_library_configuration(config.coreLibrary, False)
        libraries[lib.name] = lib

        for extension in config.extensionLibraries:
            lib = cls.load_library_configuration(extension, True)
            libraries[lib.name] = lib

        return cls(config, libraries, global_names={})

    @classmethod
    def load_library_configuration(cls, config: 'ObjectMap', is_extension: bool) -> LibraryWrapperData:
        basedir = os.path.dirname(os.path.dirname(__file__))
        modules = {}

        for module in config.libModules:
            if module.modName in config.includedModules:
                is_absolute = os.path.isabs(module.jsonApiFilename)
                bind_data_fname = module.jsonApiFilename if is_absolute else os.path.join(basedir, module.jsonApiFilename)

                if module.jsonMetadataFilename:
                    is_absolute = os.path.isabs(module.jsonApiFilename)
                    meta_data_fname = module.jsonMetadataFilename if is_absolute else os.path.join(basedir, module.jsonMetadataFilename)
                else:
                    meta_data_fname = None

                mod_wrapper = ModuleWrapperData.load(module.modName, config.libName, bind_data_fname, meta_data_fname)
                modules[module.modName] = mod_wrapper

        return LibraryWrapperData(config.libName, config.libKeyName, config.libBasedir, is_extension, modules, config.binFilename)

    def find(self, library: str, module: str, group: str, name: str, default: Any = None):
        if lib := self.libraries.get(library):
            if mod := lib.modules.get(module):
                # print('ok')
                group_map = {
                    'defines': mod.defines,
                    'structs': mod.structs,
                    'aliases': mod.aliases,
                    'enums': mod.enums,
                    'callbacks': mod.callbacks,
                    'functions': mod.functions,
                }.get(group, {})

                return group_map.get(name, default)

        return default

# endregion (WRAPPER OBJECTS)

class PythonSourceComposer:

    # region DUNDER METHODS
    
    def __init__(self):
        # store as separete lines instead of concatenated strings
        self.lines: list[str] = []
        self.indent_level: int = 0

    def __len__(self) -> int:
        return len(self.lines)

    # endregion (DUNDER METHODS)

    # region PROPERTIES

    @property
    def last_line(self) -> str | None:
        """Gets the last line string or None if nothing was added"""
        return self.lines[-1] if self.lines else None

    @property
    def indentation(self) -> str:
        """Gets the current indentation level as a string of whitespaces"""
        return '    ' * max(0, self.indent_level)

    # endregion (PROPERTIES)

    # region CONTEXT MANAGERS

    @contextmanager
    def indented(self, levels: int = 1):
        """Increase the indentation by given levels in the context"""
        level = self.indent_level
        self.indent_level = max(1, level + levels)
        yield
        self.indent_level = level

    @contextmanager
    def dedented(self, levels: int = 1):
        """Decrease the indentation by given levels in the context"""
        level = self.indent_level
        self.indent_level = max(0, level - levels)
        yield
        self.indent_level = level

    @contextmanager
    def region(self, label: str, padding: int = 0, margin: int = 0):
        """Adds a collapsible code region"""
        if margin > 0:
            self.add_empty(margin)
        self.add_comment(f"region {label.upper()}")
        if padding > 0:
            self.add_empty(padding)
        yield
        if padding > 0:
            self.add_empty(padding)
        self.add_comment(f"endregion ({label.lower()})")
        if margin > 0:
            self.add_empty(margin)

    @contextmanager
    def stmt_if(self, condition: str, is_elif: bool = False):
        """Adds an if statement"""
        kw = 'elif' if is_elif else 'if'
        level = self.indent_level
        self.add_line(f"{kw} {condition}:")

        self.indent_level += 1
        yield
        self.indent_level = level

    @contextmanager
    def stmt_while(self, condition: str):
        """Adds an while statement"""
        level = self.indent_level
        self.add_line(f"while {condition}:")

        self.indent_level += 1
        yield
        self.indent_level = level

    @contextmanager
    def stmt_for(self, element: str, container: str):
        """Adds an while statement"""
        level = self.indent_level
        self.add_line(f"for {element} in {container}:")

        self.indent_level += 1
        yield
        self.indent_level = level

    @contextmanager
    def stmt_else(self):
        """Adds an else statement"""
        level = self.indent_level
        self.add_line(f"else:")
        self.indent_level += 1
        yield
        self.indent_level = level

    @contextmanager
    def function_def(self, name: str, parameters: list[str] | None, decorators: list[str] | None,
                 return_type_annotation: str | None = None, type_hint: str | None = None, docstring: str | None = None):
        """Adds a function definition"""
        if decorators:
            for decorator in decorators:
                self.add_line(f"@{decorator}")

        param_list = ', '.join(parameters) if parameters else ''
        typ_return = f" -> '{return_type_annotation}'" if return_type_annotation  else ''
        self.add_line(f"def {name}({param_list}){typ_return}:")

        with self.indented():
            if type_hint:
                self.add_line(f"# type: {type_hint}")
            if docstring:
                self.add_docstring(docstring)
            yield

    @contextmanager
    def class_def(self, name: str, bases: list[str] | None, decorators: list[str] | None, docstring: str | None = None,
                  dataclass_fields: list[str] | None = None):
        """Adds a class definition"""
        if decorators is not None:
            for decorator in decorators:
                self.add_line(f"@{decorator}")

        if decorators is not None and 'dataclass' not in decorators and dataclass_fields:
            self.add_line("@dataclass")

        base_classes = ', '.join(bases) if bases else ''
        self.add_line(f"class {name}({base_classes}):")

        with self.indented():
            if docstring:
                self.add_docstring(docstring)
                self.add_empty()
            yield

    @contextmanager
    def getter(self, name: str, return_type_annotation: str | None = None, type_hint: str | None = None,
               docstring: str | None = None):
        """Adds a property getter"""
        with self.function_def(name, ['self'], ['property'], return_type_annotation, type_hint, docstring):
            yield

    @contextmanager
    def setter(self, name: str, value_param: str = 'value', type_hint: str | None = None,
               docstring: str | None = None):
        """Adds a property getter"""
        with self.function_def(name, ['self', value_param], [f'{name}.setter'], None, type_hint, docstring):
            yield

    @contextmanager
    def entrypoint(self):
        """Adds an entrypoint to the script (resets indentation)"""
        self.indent_level = 0
        with self.stmt_if('__name__ == "__main__"'):
            yield

    # endregion (CONTEXT MANAGERS)

    # region ONE-LINERS

    def add_ruler(self, char: str = '-', length: int = 78):
        """Adds a separation line with optional character (default is '-') and length (default is 78)"""
        ruler = char[0] * (length - len(self.indentation))
        self.add_comment(ruler)

    def add_line(self, code: str):
        """Adds a line of code following current indentation"""
        self.lines.append(f"{self.indentation}{code}")

    def add_inline(self, code: str):
        """Adds code to the last line"""
        if self.last_line:
            self.lines[-1] = f"{self.last_line}{code}"
        else:
            self.add_line(f"# {code}")

    def add_comment(self, comment: str, inline: bool = False):
        """Adds a commented line, optionally inline"""
        if inline and self.last_line:
            self.lines[-1] = f"{self.last_line}    # {comment}"
        else:
            self.add_line(f"# {comment}")

    def add_empty(self, count: int = 1):
        """Adds one or more empty lines"""
        for _ in range(count):
            self.lines.append("")

    def remove_line(self, count: int = 1):
        """Discards the last specified number of lines previously added"""
        for _ in range(count):
            if self.lines:
                self.lines.pop()

    # endregion (ONE-LINERS)

    # region MULTI-LINERS

    def add_docstring(self, comment: str, use_single_quotes: bool = False):
        """Adds a [multi]line comment"""
        lines = comment.split("\n")
        quotes = "'''" if use_single_quotes else '"""'
        lines[0] = f"{quotes}{lines[0]}"
        lines[-1] = f"{lines[-1]}{quotes}"

        for line in lines:
            self.add_line(line)

    def add_imported_names(self, lib: str, names: list[str] | None = None):
        """Adds an import statement"""
        if names:
            imported_names = ', '.join(names)
            self.add_line(f"from {lib} import {imported_names}")
        else:
            self.add_line(f"import {lib}")

    def add_exported_names(self, names: list[str]):
        """Defines and adds the __all__ module global"""
        level = self.indent_level
        self.indent_level = 0
        self.add_line("__all__ = [")

        with self.indented():
            for name in sorted(names):
                self.add_line(f"'{name}',")

        self.add_line("]")
        self.indent_level = level

    def add_template(self, template: str, exact: bool, *args, **kwargs):
        """Adds a template string with format args and kwargs, following indentation if exact is false"""
        if args or kwargs:
            template = template.format(*args, **kwargs)

        lines = template.split('\n')
        for line in lines:
            if exact:
                self.lines.append(line)
            else:
                self.add_line(line)

    # endregion (MULTI-LINERS)

    def get_source(self) -> str:
        """Returns the full source string"""
        return '\n'.join(self.lines)


class ObjectMap:

    @classmethod
    def load_any(cls, obj_: Any) -> Any:
        if isinstance(obj_, dict):
            return cls.load_dict(obj_)
        elif isinstance(obj_, list):
            return cls.load_list(obj_)
        else:
            return obj_

    @classmethod
    def load_dict(cls, mapping: dict[str, Any]) -> 'ObjectMap':
        for k in list(mapping.keys()):
            v = mapping[k]

            if isinstance(v, dict):
                mapping[k] = cls.load_dict(v)
            elif isinstance(v, (list, tuple)):
                mapping[k] = cls.load_list(v)

        return cls(**mapping)

    @classmethod
    def load_list(cls, sequence: list[Any]) -> list[Any]:
        for i in range(len(sequence)):
            v = sequence[i]

            if isinstance(v, dict):
                sequence[i] = cls.load_dict(v)
            elif isinstance(v, (list, tuple)):
                sequence[i] = cls.load_list(v)

        return sequence

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, self.__class__.load_any(v))

    def get(self, name: str, default: Any = None) -> Any:
        return getattr(self, name, default)

# endregion (classes)
# ---------------------------------------------------------
# region FUNCTIONS


def snakefy(name: str) -> str:
    """Converts a PascalCase or camelCase name into snake_case"""
    prevchar = ''
    nextchar = ''
    result = ''
    namelen = len(name)

    for i, char in enumerate(name):
        nextchar = name[i + 1] if i < namelen - 1 else ''

        if prevchar:
            if char.isdigit():  # ?[1]
                if prevchar.isdigit():  # 0[1] -> 01
                    result += char

                elif prevchar.isupper():    # A[1]
                    if nextchar == '':      # A[1]! -> a0
                        result += char
                    elif nextchar.isdigit():  # A[1]2 -> a12
                        result += char
                    elif nextchar.isupper():  # A[1]C -> a0_c
                        result += f"_{char}"
                    else:                   # A[1]c
                        result += char
                else:   # a[1]
                    if nextchar == '':      # a[1]! -> a0
                        result += char
                    elif nextchar.isdigit():  # a[1]2 -> a12
                        result += char
                    elif nextchar.isupper():  # a[1]C -> a0c
                        result += char
                    else:                   # a[1]c -> a1_c
                        result += f"_{char}"

            elif char.isupper():  # ?[B]
                if prevchar.isdigit():  # 0B -> ab
                    if nextchar == '':      # 0[B]! -> 0b
                        result += char.lower()
                    elif nextchar.isdigit():  # 0[B]2 -> 0b2
                        result += char.lower()
                    elif nextchar.isupper():  # 0[B]C -> 0bc
                        result += char.lower()
                    else:                   # 0[B]c -> ab_c
                        result += f"_{char.lower()}"

                elif prevchar.isupper():  # AB -> ab
                    result += f'{char.lower()}'
                else:   # aB -> a_b
                    result += f'_{char.lower()}'

            else:       # ab
                if prevchar.isdigit():  # 0b?
                    if nextchar == '':
                        result += char
                    elif nextchar.islower() or nextchar.isdigit():  # 0bc -> 0bc; 0b2 -> 0b2
                        result += f'_{char.lower()}'
                    else:  # 0bC -> 0b_c
                        result += char
                if prevchar.isupper():  # Ab
                    result += char
                else:   # ab -> ab
                    result += char
        else:
            result += char.lower()
        prevchar = char

    if keyword.iskeyword(result):
        return "{}_".format(result)

    return result

# endregion (functions)

# region ENTRYPOINT

# if __name__ == '__main__':
#     for name in ['BeginMode3D', 'Vec3ToVec2', 'ColorRGB', 'Vector2Add']:
#         print(f"{name} -> {snakefy(name)}")

#     obj = ObjectMap.load_any({'x': [{'y': 123, 'z': '345'}, {'y': 890, 'z': '631'}], 'b': 'someval', 'c': {'post': 100}})

#     print('obj.x[0].z:', obj.x[0].z)
#     print('obj.x[1].y:', obj.x[1].y)
#     print('obj.b:', obj.b)
#     print('obj.c.post:', obj.c.post)

# endregion (ENTRYPOINT)