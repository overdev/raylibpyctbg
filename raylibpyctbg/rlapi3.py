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
import json
import re

from typing import Any, Sequence
from contextlib import contextmanager
from dataclasses import dataclass, field
from enum import Enum, auto

from rlapi3_templates import *
from core import (snakefy,
    PythonSourceComposer,
    DefineWrapperData,
    StructFieldWrapperData,
    AliasWrapperData,
    StructWrapperData,
    EnumerandWrapperData,
    EnumWrapperData,
    ParameterWrapperData,
    CallbackWrapperData,
    FunctionWrapperData,
    TypeWrapperData,
    ModuleWrapperData,
    GlobalWrapperData,
    ObjectMap)

# endregion (imports)
# ---------------------------------------------------------
# region EXPORTS


__all__ = [
    'generate_binding_code',
]


# endregion (exports)
# ---------------------------------------------------------
# region GLOBALS

# endregion (globals)
# ---------------------------------------------------------
# region CONSTANTS & ENUMS

GLOBAL_GROUPS = 'types structs enums aliases enumerands defines callbacks functions contexts'.split()

RE_COLOR_DEFINE_VALUE = re.compile(r"CLITERAL\(Color\)\{\s*(\d+,\s*\d+,\s*\d+,\s*\d+)\s*\}")
RE_FLOATMATH_DEFINE_VALUE = re.compile(r"\((PI|\d+\.\d+)[fd]?/(PI|\d+\.\d+)[fd]?\)")
RE_UNKNOWN_DEFINE_VALUE = re.compile(r"[A-Z_][A-Z_0-9]+")

RE_TYPE_SPEC = re.compile(r"(const\b\s*)?(unsigned\b\s*)?([\.\w]+\s*)([*]+|\[[\w\d\s\-+/*]+\])?\s*")

PRIMITIVE_C_TYPES = [
    'bool',
    'char',
    'byte',
    'short',
    'int',
    'long',
    'longlong',
    'float',
    'double',
    'void',
]

MAP_CTYPE_PY = {
    'c_bool': 'bool',
    'c_char': 'int | str',
    'c_uchar': 'int',
    'c_char_p': 'bytes | str | None',
    'c_byte': 'int',
    'c_ubyte': 'int',
    'c_short': 'int',
    'c_ushort': 'int',
    'c_int': 'int',
    'c_uint': 'int',
    'c_long': 'int',
    'c_ulong': 'int',
    'c_longlong': 'int',
    'c_ulonglong': 'int',
    'c_float': 'float',
    'c_double': 'float',
    'c_void': 'None',
    'c_void_p': 'bytes | str | None',
}

MAP_CTYPE_ACTION = {
    'c_bool': '_bool({})',
    'c_char': '_int({}, (-128, 127))',
    'c_uchar': '_int({}, (0, 255))',
    'c_char_p': '_str_in({})',
    'c_byte': '_int({}, (-128, 127))',
    'c_ubyte': '_int({}, (0, 255))',
    'c_short': '_int({}, (-32768, 32767))',
    'c_ushort': '_int({}, (0, 65535))',
    'c_int': '_int({})',
    'c_uint': '_int({})',
    'c_long': '_int({})',
    'c_ulong': '_int({})',
    'c_longlong': '_int({})',
    'c_ulonglong': '_int({})',
    'c_float': '_float({})',
    'c_double': '_float({})',
    'c_longdouble': '_float({})',
    'c_void_p': '{}',
}

MAP_CTYPE_ZERO = {
    'c_bool': '0',
    'c_char': '0',
    'c_uchar': '0',
    'c_char_p': 'None',
    'c_byte': '0',
    'c_ubyte': '0',
    'c_short': '0',
    'c_ushort': '0',
    'c_int': '0',
    'c_uint': '0',
    'c_long': '0',
    'c_ulong': '0',
    'c_longlong': '0',
    'c_ulonglong': '0',
    'c_float': '0.0',
    'c_double': '0.0',
    'c_longdouble': '0.0',
    'c_void_p': 'None',
}

EXPORT_UTILS = [
    'pop_out_param',
    'float_array',
    'double_array',
    'int_array',
    'uint_array',
    'short_array',
    'ushort_array',
    'byte_array',
    'ubyte_array',
    'string_array',
]

RESERVED_NAMES = [
    'abs',
    'aiter',
    'all',
    'any',
    'anext',
    'ascii',
    'bin',
    'bool',
    'breakpoint',
    'bytearray',
    'bytes',
    'callable',
    'chr',
    'classmethod',
    'compile',
    'complex',
    'delattr',
    'dict',
    'dir',
    'divmod',
    'enumerate',
    'eval',
    'exec',
    'filter',
    'float',
    'format',
    'frozenset',
    'getattr',
    'globals',
    'hasattr',
    'hash',
    'help',
    'hex',
    'id',
    'input',
    'int',
    'isinstance',
    'issubclass',
    'iter',
    'len',
    'list',
    'locals',
    'map',
    'max',
    'memoryview',
    'min',
    'next',
    'object',
    'oct',
    'open',
    'ord',
    'pow',
    'print',
    'property',
    'range',
    'repr',
    'reversed',
    'round',
    'set',
    'setattr',
    'slice',
    'sorted',
    'staticmethod',
    'str',
    'sum',
    'super',
    'tuple',
    'type',
    'vars',
    'zip',
]

VECTOR_MATH_TEMPLATES = {
    'Vector2': TPL_VEC2_MATH,
    'Vector3': TPL_VEC3_MATH,
    'Vector4': TPL_VEC4_MATH
}

STRUCT_SWIZZLING_TEMPLATES = {
    'Vector2': TPL_VEC2_SWIZZLING,
    'Vector3': TPL_VEC3_SWIZZLING,
    'Vector4': TPL_VEC4_SWIZZLING,
    'Rectangle': TPL_RECT_SWIZZLING,
    'Color': TPL_COLOR_SWIZZLING
}

STRUCT_UTILITY_TEMPLATES = {
    'Vector2': TPL_VEC2_UTILS,
    'Vector3': TPL_VEC3_UTILS,
    'Vector4': TPL_VEC4_UTILS,
    'Rectangle': TPL_RECT_UTILS,
    'Color': TPL_COLOR_UTILS
}

# endregion (constants)
# ---------------------------------------------------------
# region CLASSES

# endregion (classes)
# ---------------------------------------------------------
# region FUNCTIONS


def map_get(o: dict, *keys: str, default: Any = None) -> Any:
    try:
        for k in keys:
            v = o.get(k, default)
            if v is default:
                return default
            o = v
    except KeyError:
        return default

    return o


def scan_types(config: GlobalWrapperData) -> list[str]:
    """Returns a list of all types defined and specified across the library"""
    type_list: list[str] = []

    for library in config.libraries.values():
        for module in library.modules.values():
            bind_data = module.bind_data

            for group in bind_data:
                if group in ('defines', 'enums'):
                    continue

                elif group == 'structs':

                    for struct_data in bind_data[group]:
                        type_name = struct_data.get('name')
                        if type_name.startswith('const '):
                            type_name = type_name[6:]
                        if type_name and type_name not in type_list:
                            type_list.append(type_name)

                        for field in struct_data.get('fields', []):
                            type_name = field.get('type')
                            if type_name.startswith('const '):
                                type_name = type_name[6:]
                            if type_name and type_name not in type_list:
                                type_list.append(type_name)

                elif group == 'alias':
                    for alias_data in bind_data[group]:
                        type_name = alias_data.get('name')
                        if type_name.startswith('const '):
                            type_name = type_name[6:]
                        if type_name and type_name not in type_list:
                            type_list.append(type_name)

                elif group in ('callbacks', 'functions'):
                    for call_data in bind_data[group]:
                        if group == 'callbacks':
                            type_name = call_data.get('name')
                            if type_name.startswith('const '):
                                type_name = type_name[6:]
                            if type_name and type_name not in type_list:
                                type_list.append(type_name)

                        type_name = call_data.get('returnType')
                        if type_name.startswith('const '):
                            type_name = type_name[6:]
                        if type_name and type_name not in type_list:
                            type_list.append(type_name)

                        for param in call_data.get('params', []):
                            type_name = param.get('type')
                            if type_name.startswith('const '):
                                type_name = type_name[6:]
                            if type_name and type_name not in type_list:
                                type_list.append(type_name)

    return sorted(type_list)

# region CODE GENERATION


def wrap_enum(composer: PythonSourceComposer, enum_data: EnumWrapperData, metadata: dict[str, Any] | None = None):
    """Generates binding code for a C enum from the WrapperData object and optional metadata"""
    with composer.class_def(enum_data.name, ['IntEnum'], None, enum_data.description):
        num_members = len(enum_data.values)

        for i, enumerand in enumerate(enum_data.values):
            composer.add_line(f"{enumerand.name} = {enumerand.value}")

            if enumerand.description:
                composer.add_docstring(f"{enumerand.description}")

            if i != num_members - 1:
                composer.add_empty()

    composer.add_empty(2)
    for i, enumerand in enumerate(enum_data.values):
        composer.add_line(f"{enumerand.name} = {enum_data.name}.{enumerand.name}")


def wrap_alias(composer: PythonSourceComposer, alias_data: AliasWrapperData, **metadata: Any):
    """Generates binding code for a C typedef from the WrapperData object and optional metadata"""
    assert isinstance(alias_data, AliasWrapperData), alias_data
    if alias_data.description:
        composer.add_comment(alias_data.description)

    composer.add_line(f"{alias_data.name} = {alias_data.dtype}")
    composer.add_line(f"{alias_data.name}Ptr = POINTER({alias_data.dtype})")

# region MEMBERS


def wrap_classmethod(composer: PythonSourceComposer, config: GlobalWrapperData, struct_data: StructWrapperData, **metadata: Any):
    if api := metadata.get('api'):
        params = {'cls': ('cls', find_type_wrapper(config, struct_data.name))}
        rename = metadata.get('renameAs')

        for k, v in zip_parameters(config, api).items():
            params[k] = v

        wrap_function(composer, config, api, False, True, decorators=['classmethod'], zipped_params=params, this=struct_data.name, renameAs=rename)
    else:
        print(f"Couldn't wrap method for {struct_data.name}: missing api")


def wrap_constructor(composer: PythonSourceComposer, config: GlobalWrapperData, struct_data: StructWrapperData, **metadata: Any):
    if zf := metadata.get('zipped_fields'):
        zipped_fields = zf
    else:
        zipped_fields = zip_initializers(config, struct_data)

    fields = []
    attr_inits = []
    arg_inits = []
    hint = []
    add_hint = config.config.typeHint
    add_annotation = config.config.typeAnnotate
    initializers = map_get(struct_data.metadata, 'init', default=[])

    for i, (field_name, (fieldName, type_wrapper)) in enumerate(zipped_fields.items()):
        check_meta = field_name not in ('self', 'cls')
        field_decl = field_name
        field_type = type_wrapper.type_py if type_wrapper else None
        field_init = initializers[i-1] if initializers and i-1 < len(initializers) else "None"
        field_meta = map_get(struct_data.metadata, 'fields', fieldName, default={})
        meta_type = map_get(field_meta, 'type', 'typePy', default=field_type) if check_meta else None
        pass_action = field_meta.get('passAction', '{}')

        if meta_type:
            field_type = meta_type

        if add_annotation and field_decl != "self":
            field_decl = f"{field_decl}: '{field_type}'=None"
        elif field_decl != "self":
            field_decl = f"{field_decl}=None"

        hint.append(field_type)
        fields.append(field_decl)
        if field_name != 'self':
            attr_inits.append(f"{pass_action.format(field_name)} or {field_init}" if field_init != "None" else pass_action.format(field_name))

    type_hint = f"({', '.join(hint)}) -> None" if add_hint else None
    rtype_annotation = 'None' if add_annotation else None

    with composer.function_def('__init__', fields, None, rtype_annotation, type_hint, f"Initializes this {struct_data.name}"):
        # arguments = ', '.join(attr_inits)
        composer.add_line(f"super({struct_data.name}, self).__init__(")

        with composer.indented():
            for i, init in enumerate(attr_inits):
                composer.add_line(f"{init}")
                if i < len(attr_inits) -1:
                    composer.add_inline(",")
        composer.add_line(")")


def wrap_context(composer: PythonSourceComposer, config: GlobalWrapperData, struct_data: StructWrapperData, **metadata: Any):
    enter = metadata.get('api_enter')
    leave = metadata.get('api_leave')
    if enter and leave:
        composer.add_empty()
        wrap_method(composer, config, struct_data, api=enter, renameAs='__enter__')
        composer.add_empty()
        wrap_method(composer, config, struct_data, api=leave, renameAs='__exit__')
    else:
        print(f"Couldn't add context management for {struct_data.name}: missing apis")


def wrap_method(composer: PythonSourceComposer, config: GlobalWrapperData, struct_data: StructWrapperData, **metadata: Any):
    if api := metadata.get('api'):
        params = {}
        in_place = metadata.get('inplace', False)
        attr = metadata.get('attr')
        rename = metadata.get('renameAs')

        for i, (k, v) in enumerate(zip_parameters(config, api).items()):
            params['self' if i == 0  else k] = v

        wrap_function(composer, config, api, False, True, zipped_params=params, this=struct_data.name, inplace=in_place, attr=attr, renameAs=rename)
    else:
        print(f"Couldn't wrap method for {struct_data.name}: missing api")


def wrap_staticmethod(composer: PythonSourceComposer, config: GlobalWrapperData, struct_data: StructWrapperData, **metadata: Any):
    if api := metadata.get('api'):
        rename = metadata.get('renameAs')

        wrap_function(composer, config, api, False, True, decorators=['staticmethod'], this=struct_data.name, renameAs=rename)
    else:
        print(f"Couldn't wrap staticmethod for {struct_data.name}: missing api")


# endregion (MEMBERS)

def wrap_members(composer: PythonSourceComposer, config: GlobalWrapperData, struct_data: StructWrapperData, metadata: dict[str, Any] | None = None):
    """Generates binding code for C functions as class members from the WrapperData object and optional metadata"""
    add_utils = config.config.addUtilityMethods
    meta = struct_data.metadata or {}
    struct = struct_data.name
    this = ['self']

    # print(*struct_data.metadata.keys() if struct_data.metadata else f'No metadata for {struct_data.name}')

    if add_utils:
        with composer.function_def('array_of', ['cls', 'sequence'], ['classmethod'], None, None, f"Creates and returns an array of {struct} elements"):
            composer.add_line(f"return ({struct} * len(sequence))(*sequence)")

    if config.config.bindApiAsClassmethod:
        for api in meta.get('bindApiAsClassmethod', []):
            api_lib = api.get('library', struct_data.library)
            api_mod = api.get('module', struct_data.module)
            api_name = api.get('api')
            rename = api.get('renameAs') or api_name

            if target := config.find(api_lib, api_mod, 'functions', api_name):
                composer.add_empty()
                wrap_classmethod(composer, config, struct_data, api=target, renameAs=rename)
            else:
                print(f"Not found: {api_lib}.{api_mod}.functions.{api_name}")

    # constructor
    composer.add_empty()
    wrap_constructor(composer, config, struct_data)

    composer.add_empty()
    with composer.function_def('__str__', this, None, None, None, None):
        impl = meta.get('dunderStrExpression', "return \"[{} at {}]\".format(_clsname(self), id(self))")
        composer.add_line(impl)

    composer.add_empty()
    with composer.function_def('__repr__', this, None, None, None, None):
        impl = meta.get('dunderReprExpression', "return \"{}()\".format(_clsname(self))")
        composer.add_line(impl)

    # destructor
    # NOTE: can't add this feature due to ctypes lack of OOR (original object return)
    # if config.config.bindApiAsDestructor:
    #     if len(meta.get('bindApiAsDestructor', [])):
    #         api = meta.get('bindApiAsDestructor')[0]
    #         api_name = api.get('api')
    #         composer.add_empty()
    #         with composer.function_def('__del__', this, None, None, None, f"Releases the resources allocated by this {struct}"):
    #             composer.add_line(f"_{api_name}(self)")

    if config.config.bindApiAsContextManager:
        if api := meta.get('bindApiAsContextManager'):
            api_lib = api.get('library', struct_data.library)
            api_mod = api.get('module', struct_data.module)
            api_enter = api.get('enter')
            api_leave = api.get('leave')

            enter = config.find(api_lib, api_mod, 'functions', api_enter)
            leave = config.find(api_lib, api_mod, 'functions', api_leave)
            if enter and leave:
                wrap_context(composer, config, struct_data, api_enter=enter, api_leave=leave)
            else:
                print(f"Not found: {api_lib}.{api_mod}.functions.({api_enter} or {api_leave})")

    if config.config.addVectorMath:
        if template := VECTOR_MATH_TEMPLATES.get(struct):
            composer.add_empty()
            composer.add_template(template, False)

    if config.config.addAttribSwizzling:
        if template := STRUCT_SWIZZLING_TEMPLATES.get(struct):
            composer.add_empty()
            composer.add_template(template, False)

    composer.add_empty()
    with composer.getter('byref', docstring=f"Gets a pointer to this {struct}"):
        composer.add_line("return byref(self)")

    if config.config.bindApiAsProperty:
        for api in meta.get('bindApiAsProperty', []):
            api_lib = api.get('library', struct_data.library)
            api_mod = api.get('module', struct_data.module)
            api_name = api.get('api')
            rename = api.get('renameAs') or api_name

            if config.config.snakecaseProperties:
                rename = snakefy(rename)

            if target := config.find(api_lib, api_mod, 'functions', api_name):
                composer.add_empty()
                with composer.getter(rename, docstring=target.description):
                    composer.add_line(f"return _{target.name}(self)")
            else:
                print(f"Not found: {api_lib}.{api_mod}.functions.{api_name}")

    if config.config.bindApiAsMethod:
        for api in meta.get('bindApiAsMethod', []):
            api_lib = api.get('library', struct_data.library)
            api_mod = api.get('module', struct_data.module)
            api_name = api.get('api')
            inplace = api.get('inplace', False)
            attr = api.get('attr')
            rename = api.get('renameAs')

            if target := config.find(api_lib, api_mod, 'functions', api_name):
                composer.add_empty()
                wrap_method(composer, config, struct_data, api=target, inplace=inplace, attr=attr, renameAs=rename)

    if config.config.addAttribSwizzling:
        if template := STRUCT_UTILITY_TEMPLATES.get(struct):
            composer.add_empty()
            composer.add_template(template, False)

    if config.config.addBinaryPackingMethods:
        if info := meta.get('binaryData', {}):
            pack_format = info.get('format', struct_data.library)
            pack_args = info.get('args', struct_data.module)

            composer.add_empty()
            with composer.function_def("pack", this, None, None, None, f"Packs this {struct} as a bytes object"):
                composer.add_line(f"return struct.pack('{pack_format}', {pack_args})")

            composer.add_empty()
            with composer.function_def("pack_into", ['self', 'buffer', 'offset'], None, None, None, f"Packs this {struct} as a bytes object"):
                composer.add_line(f"return struct.pack_into('{pack_format}', buffer, offset, {pack_args})")


    if config.config.bindApiAsStaticmethod:
        for api in meta.get('bindApiAsStaticmethod', []):
            api_lib = api.get('library', struct_data.library)
            api_mod = api.get('module', struct_data.module)
            api_name = api.get('api')
            rename = api.get('renameAs')

            if target := config.find(api_lib, api_mod, 'functions', api_name):
                composer.add_empty()
                wrap_staticmethod(composer, config, struct_data, api=target, renameAs=rename)
            else:
                print(f"Not found: {api_lib}.{api_mod}.functions.{api_name}")


def wrap_struct(composer: PythonSourceComposer, config: GlobalWrapperData, struct_data: StructWrapperData,
                metadata: dict[str, Any] | None = None, declare_class: bool = True, declare_fields: bool = False):
    """Generates binding code for a C struct from the WrapperData object and optional metadata
    
    Structure fields can be declared posteriorly to the type definition, to prevent bugs due to C forward declarations"""

    if declare_class:

        with composer.class_def(struct_data.name, ['Structure'], None, struct_data.description):
            if declare_fields:
                composer.add_line('_fields_ = [')

                with composer.indented():
                    for i, field in enumerate(struct_data.fields):
                        composer.add_line(f"('{snakefy(field.name)}', {field.dtype}),")

                composer.add_line(']')
            else:
                wrap_members(composer, config, struct_data, None)

        indirections = config.indirections.get(struct_data.name, 0)
        type_name = struct_data.name
        for i in range(indirections):
            composer.add_empty()
            composer.add_comment(f"Pointer types for {struct_data.name}")
            composer.add_line(f"{type_name}Ptr = POINTER({type_name})")
            type_name = f"{type_name}Ptr"


        if struct_data.aliases:
            composer.add_empty()
            for alias in struct_data.aliases:
                composer.add_empty()
                wrap_alias(composer, alias, indirections=indirections)

    elif declare_fields:
        composer.add_line(f"{struct_data.name}._fields_ = [")

        with composer.indented():
            last_field = None
            for i, field in enumerate(struct_data.fields):

                # NOTE: this is a fix for rlVertexBuffer.indices field in rlgl.json
                if field == last_field:
                    continue
                last_field = field

                # NOTE: this is also a fix for rlVertexBuffer.indices field in rlgl.json
                if not RE_TYPE_SPEC.fullmatch(field.dtype):
                    continue

                type_wrapper = find_type_wrapper(config, field.dtype)
                type_ctype = type_wrapper.type_ctype if type_wrapper else 'UnknownType'
                composer.add_line(f"('{snakefy(field.name)}', {type_ctype}),")

        composer.add_line(f"]")


def zip_parameters(config: GlobalWrapperData, func_data: FunctionWrapperData) -> dict[str, tuple[str, TypeWrapperData]]:
    zipped = {}

    for i, param in enumerate(func_data.params):
        param_name = snakefy(param.name) if config.config.snakecaseParameters else param.name
        if param_name in RESERVED_NAMES:
            param_name = f'{param_name}_'
        if param.dtype in ('...', 'va_list'):
            type_wrapper = None
        else:
            type_wrapper = find_type_wrapper(config, param.dtype)

        zipped[param_name] = (param.name, type_wrapper)

    return zipped


def zip_initializers(config: GlobalWrapperData, struct_data: StructWrapperData) -> dict[str, tuple[str, TypeWrapperData]]:
    zipped = {'self': (struct_data.name, find_type_wrapper(config, struct_data.name))}

    for i, field in enumerate(struct_data.fields):
        field_name = snakefy(field.name) if config.config.snakecaseFields else field.name
        if field_name in RESERVED_NAMES:
            field_name = f'{field_name}_'

        type_wrapper = find_type_wrapper(config, field.dtype)

        zipped[field_name] = (field.name, type_wrapper)

    return zipped


def wrap_function(composer: PythonSourceComposer, config: GlobalWrapperData, func_data: FunctionWrapperData,
                  declare_types: bool = False, declare_function: bool = True, **metadata: dict[str, Any]):
    """Generates binding code for a C function from the WrapperData object and optional metadata"""
    if zp := metadata.get('zipped_params'):
        zipped_params = zp
    else:
        zipped_params = zip_parameters(config, func_data)

    if declare_types:
        ptypes = [ t.type_ctype2 for (_, t) in zipped_params.values() if t ]

        if func_data.rtype == 'void':
            rtype = 'None'
        else:
            rtype_wrapper = find_type_wrapper(config, func_data.rtype)
            rtype = rtype_wrapper.type_ctype2 if rtype_wrapper else 'UnknownType'

        ptypes_list = f", {', '.join(ptypes)}" if len(ptypes) else ''

        composer.add_line(f"_{func_data.name} = _wrap({func_data.library}.{func_data.name}, {rtype}{ptypes_list})")

    if declare_function:
        params = []
        args = []
        hint = []
        add_hint = config.config.typeHint
        add_annotation = config.config.typeAnnotate
        inplace = metadata.get('inplace', False)
        attr = metadata.get('attr')
        func_name = func_data.name
        if fn := metadata.get('renameAs'):
            func_name = fn
        if config.config.snakecaseFunctions:
            func_name = snakefy(func_name)

        decorators = []
        for decorator in metadata.get('decorators', []):
            if decorator not in decorators:
                decorators.append(decorator)

        for i, (param_name, (paramName, type_wrapper)) in enumerate(zipped_params.items()):
            check_meta = param_name not in ('self', 'cls')
            param_decl = param_name
            param_type = type_wrapper.type_py if type_wrapper else None
            param_meta = map_get(func_data.metadata, 'params', paramName, default={})
            meta_type = map_get(param_meta, 'type', 'typePy', default=param_type) if check_meta else None

            default_action = '{}'
            if type_wrapper:
                struct = config.find(func_data.library, func_data.module, 'structs', type_wrapper.type_ctype2, default=None)
                if struct and struct.metadata:
                    default_action = struct.metadata.get('func', '{}')
                else:
                    default_action = MAP_CTYPE_ACTION.get(type_wrapper.type_ctype, default_action)
            pass_action = param_meta.get('passAction', default_action)

            # NOTE: va_list param type is set to None
            if param_type is None:
                param_decl = '*args'
                param_type = 'bool | int | float | str | bytes | None'

            # param_type = type_wrapper.type_py if type_wrapper else 'Any'

            if meta_type:
                param_type = meta_type

            if add_annotation and param_decl not in ('self', 'cls'):
                param_decl = f"{param_decl}: '{param_type}'"

            # NOTE: this one if for the type hint
            if param_decl == '*args':
                param_type = '...'
                param_name = param_decl

            hint.append(param_type)
            params.append(param_decl)
            if param_name != 'cls':
                args.append(pass_action.format(param_name))

        if func_data.rtype == 'void':
            rtype = 'None'
        else:
            rtype_wrapper = find_type_wrapper(config, func_data.rtype)
            rtype = rtype_wrapper.type_py if rtype_wrapper else 'UnknownType'

        rtype = map_get(func_data.metadata, 'type', 'typePy', default=rtype)

        type_hint = f"({', '.join(hint)}) -> {rtype}" if add_hint else None
        rtype_annotation = rtype if add_annotation else None

        with composer.function_def(func_name, params, decorators, rtype_annotation, type_hint, func_data.description or None):
            has_return = rtype != 'None'
            transformed_return = False
            out_params = []
            transform_return_actions = []
            return_action = map_get(func_data.metadata, 'returnAction', default='{}')

            for pname, (pName, ptype) in zipped_params.items():

                if pmeta := map_get(func_data.metadata, 'params', pName):
                    transform_action = pmeta.get('transformAction')

                    if transform_return_action := pmeta.get('transformReturnAction', None):
                        transform_return_actions.append((transform_return_action, pname))

                    if pmeta.get('outParam', False):
                        push_action = pmeta.get('pushAction', '{}')
                        out_params.append(push_action.format(pname))

                    if transform_action:
                        composer.add_line(f"{pname} = {transform_action.format(pname)}")

            ret = ''
            if len(out_params) or len(transform_return_actions):
                transformed_return = True
                ret = 'result = '
            elif has_return:
                ret = f'self.{attr} = ' if inplace else 'return '

            arguments = ', '.join(args)
            call = f"_{func_data.name}({arguments})"

            composer.add_line(f"{ret}{return_action.format(call)}")

            if has_return and inplace and not transformed_return:
                composer.add_line(f'return self')

            for action, pname in transform_return_actions:
                call = action.format(ret='result', arg=pname)
                composer.add_line(f"result = {call}")

            if len(out_params):
                composer.add_line(f"_clear_in_out()")
                for oparam in out_params:
                    composer.add_line(f"_push_in_out({oparam})")

            if transformed_return:
                if inplace:
                    composer.add_line(f'self.{attr} = result')
                    composer.add_line(f'return self')
                else:
                    composer.add_line("return result")


def wrap_callback(composer: PythonSourceComposer, config: GlobalWrapperData, callback_data: CallbackWrapperData, metadata: dict[str, Any] | None = None):
    """Generates binding code for a C function pointer from the WrapperData object and optional metadata"""
    params = []
    for i, param in enumerate(callback_data.params):
        type_wrapper = find_type_wrapper(config, param.dtype)
        if param.dtype in ('...', 'va_list'):
            continue

        params.append(type_wrapper.type_ctype2 if type_wrapper else 'UnknownType')

    if callback_data.description:
        composer.add_comment(callback_data.description)

    composer.add_line(f"{callback_data.name} = CFUNCTYPE({', '.join(params)})")


def wrap_define(composer: PythonSourceComposer, define_data: DefineWrapperData, metadata: dict[str, Any] | None = None) -> bool:
    """Generates binding code for a C #define from the WrapperData object and optional metadata (returns true if code was generated)"""
    kind = define_data.kind

    if kind in ('INT', 'FLOAT', 'DOUBLE', 'STRING'):
        if define_data.description:
            composer.add_comment(f"{define_data.description}")
        composer.add_line(f"{define_data.name} = {define_data.value}")
        return True

    elif kind == 'FLOAT_MATH':
        if m := RE_FLOATMATH_DEFINE_VALUE.fullmatch(define_data.value):
            if define_data.description:
                composer.add_comment(f"{define_data.description}")
            composer.add_line(f"{define_data.name} = {m[1]} / {m[2]}")
            return True
        else:
            composer.add_comment(f"FIXME: FLOAT_MATH {define_data.name} regex matching failed.")

    elif kind == 'COLOR':
        if m := RE_COLOR_DEFINE_VALUE.fullmatch(define_data.value):
            if define_data.description:
                composer.add_comment(f"{define_data.description}")
            composer.add_line(f"{define_data.name} = Color({m[1]})")
            return True
        else:
            composer.add_comment(f"FIXME: COLOR define {define_data.name} regex matching failed.")

    elif kind == 'UNKNOWN':
        if m := RE_UNKNOWN_DEFINE_VALUE.fullmatch(define_data.value):
            if define_data.description:
                composer.add_comment(f"{define_data.description}")
            composer.add_line(f"{define_data.name} = {m[0]}")
            return True

    return False


def wrap_context_manager(composer: PythonSourceComposer, config: GlobalWrapperData, cm: dict[str, str]):
    enter_name = cm.get('enter')
    leave_name = cm.get('leave')
    enter = config.find(cm.get('library'), cm.get('module'), 'functions', enter_name)
    leave = config.find(cm.get('library'), cm.get('module'), 'functions', leave_name)

    if enter and leave:
        name = snakefy(cm.get('api')) if config.config.snakecaseFunctions else cm.get('api')

        zp_enter = zip_parameters(config, enter)
        enter_params = []
        for param in zp_enter:
            if config.config.snakecaseParameters:
                enter_params.append(snakefy(param))
            else:
                enter_params.append(param)

        with composer.function_def(name, enter_params, ['contextmanager'], None, None, f"Context manager for {enter_name} and {leave_name}"):
            composer.add_line(f"_{enter_name}({', '.join(enter_params)})")
            composer.add_line("yield")
            composer.add_line(f"_{leave_name}()")
    else:
        print(f"Couldn't add context management for {enter_name} and {leave_name} pair: missing apis")


def wrap_ctypes(composer: PythonSourceComposer, config: GlobalWrapperData):
    """Generates binding code for a C fundamental type specifier from the WrapperData object"""
    for type_spec, type_wrapper in config.type_map.items():
        if type_wrapper.declarator:
            composer.add_empty()
            composer.add_comment(f"Type wrapper for `{type_spec}`")
            composer.add_line(type_wrapper.declarator)


def generate_binding_code(config: GlobalWrapperData, out_filename: str):
    composer = PythonSourceComposer()
    modules: list[ModuleWrapperData] = []

    process_type_information(config)

    for library in config.libraries.values():
        for module in library.modules.values():
            modules.append(module)
            load_wrapper_data(config, module)


    # code is organized as:
    #   shebang
    #   header - license and other comments
    #   imports - dependencies
    #   exports - global names that may be imported by the user
    #   libloadig - dll/so/dylib loading
    #   utils - helper functions used throughout the code
    #   c types
    #   enums
    #   structs
    #   defines
    #   callbacks
    #   internals
    #   functions
    #   contextmanagers

    composer.add_comment("#!/usr/bin/python3")
    composer.add_comment("-*- encoding: utf8 -*-")

    composer.add_empty()

    with composer.region('license information', padding=1):

        composer.add_template(TPL_RAYLIB_LICENSE, True)
        composer.add_empty()
        composer.add_template(TPL_RAYLIBPY_LICENSE, True)

    composer.add_empty()

    with composer.region('imports', padding=1):
        composer.add_template(TPL_IMPORTS, True)

    composer.add_empty()

    with composer.region('exports', padding=1):
        composer.add_line("__all__ = [")
        with composer.indented():

            for group_name in GLOBAL_GROUPS:
                if group := config.global_names.get(group_name):
                    composer.add_empty()
                    composer.add_comment(group_name)
                    for name in sorted(group):
                        composer.add_line(f"'{name}',")

        composer.add_line("]")

    composer.add_empty()

    with composer.region('library loading', padding=1):
        composer.add_template(TPL_LIBRARY_LOADER, exact=True)
        composer.add_empty()

        for lib in config.libraries.values():
            composer.add_line(f"{lib.name} = _load_library('{lib.key_name}', {lib.is_extension}, {lib.base_dir}, win32='{lib.bin_fnames.win32}', linux='{lib.bin_fnames.linux}', darwin='{lib.bin_fnames.darwin}')")

    composer.add_line("print('\\nInitializing. Please wait.\\n')")

    composer.add_empty()

    with composer.region('globals'):
        composer.add_template(TPL_GLOBALS, exact=True)

    composer.add_empty()

    with composer.region('utils'):
        composer.add_template(TPL_UTILS, exact=True)

    composer.add_empty()

    with composer.region('c types', padding=1):
        wrap_ctypes(composer, config)

    composer.add_empty()

    with composer.region('enumerations'):
        for module in modules:

            if not module.enums:
                continue

            composer.add_empty()
            composer.add_comment(f"{module.library}::{module.name}")
            composer.add_ruler()
            
            for wrap_data in module.enums.values():
                composer.add_empty()
                wrap_enum(composer, wrap_data)
                composer.add_empty()

    composer.add_empty()

    with composer.region('structures'):
        for module in modules:

            if not module.structs:
                continue

            composer.add_empty()
            composer.add_comment(f"{module.library}::{module.name}")
            composer.add_ruler()

            for wrap_data in module.structs.values():
                composer.add_empty()
                wrap_struct(composer, config, wrap_data, declare_class=True, declare_fields=False)
                composer.add_empty()

            for name in module.opaque_types:
                with composer.class_def(name, ['Structure'], None, f"Opaque structure type"):
                    composer.add_line("pass")

                composer.add_empty()
                composer.add_line(f"{name}Ptr = POINTER({name})")

        composer.add_empty()

        # composer.add_template(TPL_POST_STRUCTURES, exact=True)

    composer.add_empty()

    with composer.region('callbacks'):
        for module in modules:

            if not module.callbacks:
                continue

            composer.add_empty()
            composer.add_comment(f"{module.library}::{module.name}")
            composer.add_ruler()
            composer.add_empty()

            for wrap_data in module.callbacks.values():
                composer.add_empty()
                wrap_callback(composer, config, wrap_data)
                composer.add_empty()

    composer.add_empty()

    with composer.region('internals'):
        for module in modules:

            if not module.structs:
                continue

            composer.add_empty()
            composer.add_comment(f"{module.library}::{module.name}")
            composer.add_ruler()

            for wrap_data in module.structs.values():
                composer.add_empty()
                wrap_struct(composer, config, wrap_data, declare_class=False, declare_fields=True)
                composer.add_empty()

            composer.add_empty()
            for wrap_data in module.functions.values():
                if wrap_data.name in module.ignored_functions:
                    continue

                wrap_function(composer, config, wrap_data, declare_function=False, declare_types=True)
            composer.add_empty()

    composer.add_empty()

    with composer.region('defines'):
        for module in modules:

            if not module.defines:
                continue

            composer.add_empty()
            composer.add_comment(f"{module.library}::{module.name}")
            composer.add_ruler()
            
            for wrap_data in module.defines.values():
                if wrap_define(composer, wrap_data):
                    composer.add_empty()

    composer.add_empty()

    with composer.region('functions'):
        for module in modules:

            if not module.functions:
                continue

            composer.add_empty()
            composer.add_comment(f"{module.library}::{module.name}")
            composer.add_ruler()

            for wrap_data in module.functions.values():
                if wrap_data.name in module.ignored_functions:
                    continue

                composer.add_empty()
                wrap_function(composer, config, wrap_data, declare_function=True, declare_types=False)
                composer.add_empty()

    composer.add_empty()

    if config.config.addContextManager:
        with composer.region('context managers'):

            for module in modules:
                ctx_managers = map_get(module.meta_data, 'functions', '*', 'contextManager', default=[])

                if not ctx_managers:
                    continue

                composer.add_empty()
                composer.add_comment(f"{module.library}::{module.name}")
                composer.add_ruler()

                for cm in ctx_managers:
                    composer.add_empty()
                    wrap_context_manager(composer, config, cm)
                    composer.add_empty()

        composer.add_empty()

    with open(out_filename, 'w', encoding='utf8') as fp:
        fp.write(composer.get_source())

# endregion (CODE GENERATION)


def find_type_wrapper(config: GlobalWrapperData, type_spec: str) -> TypeWrapperData | None:
    if type_spec.startswith('const '):
        type_spec = type_spec[6:]

    return config.type_map.get(type_spec)


def process_type_information(config: GlobalWrapperData):
    type_list: list[str] = scan_types(config)
    type_map: dict[str, TypeWrapperData] = {}

    config.global_names['types'] = []
    config.indirections = {}

    for type_spec in type_list:
        if m := RE_TYPE_SPEC.fullmatch(type_spec):
            const = m[1].rstrip(' ') if m[1] else None
            unsigned = m[2].rstrip(' ') if m[2] else None
            typename = m[3].rstrip(' ') if m[3] else None
            ptr_or_cap = m[4].rstrip(' ') if m[4] else None
            pointer = capacity = None
            if ptr_or_cap:
                pointer = m[4] if m[4].startswith('*') else None
                capacity = m[4].strip('[]') if m[4].startswith('[') else None

            # print(f"'{type_spec}': const: '{const}', unsigned: '{unsigned}', type: '{typename}', ptr: '{pointer}', cap: '{capacity}'")

            max_indirection = 0
            if typename in PRIMITIVE_C_TYPES:
                type_ctype = f"c_{'u' if unsigned else ''}{typename}"
                if typename == 'char' and unsigned:
                    type_ctype = "c_ubyte"
                type_ctype2 = f"{'U' if unsigned else ''}{typename.capitalize()}"

                if pointer == '*' and typename in ('char', 'void'):
                    pointer = None
                    type_ctype = f"{type_ctype}{'_p' if not unsigned else ''}"
                    type_ctype2 = f"{type_ctype2}Ptr"

                elif pointer == '**' and typename in ('char', 'void'):
                    pointer = '*'
                    type_ctype = f"{type_ctype}{'_p' if not unsigned else ''}"
                    type_ctype2 = f"{type_ctype2}Ptr"

            else:
                type_ctype = f"{typename}"
                type_ctype2 = f"{typename}"
                type_py = f"{typename}"

                while isinstance(pointer, str):
                    pointer = None if pointer == '*' else pointer[:-1]
                    type_ctype = f"{type_ctype}Ptr"
                    type_ctype2 = f"{type_ctype2}Ptr"
                    max_indirection += 1

                # elif pointer == '**':
                #     pointer = '*'
                #     type_ctype = f"{type_ctype}Ptr"
                #     type_ctype2 = f"{type_ctype2}Ptr"

                # print(type_spec if "**" in type_spec else '')

            if pointer == '*':
                type_ctype = f"POINTER({type_ctype})"
                type_ctype2 = f"{type_ctype2}Ptr"
                pointer = None

            if type_ctype in ('c_void', '...'):
                continue

            type_py = MAP_CTYPE_PY.get(type_ctype, type_ctype2)

            if type_ctype2 == 'CharPtrPtr':
                type_py = f"{type_ctype2} | list[CharPtr | str] | None"

            if capacity:
                type_ctype = f"{type_ctype} * {capacity}"
                type_ctype2 = f"{type_ctype2}{capacity}"
                if typename == 'char':
                    type_py = f"{type_ctype2} | list[{type_py}] | str"
                else:
                    type_py = f"{type_ctype2} | list[{type_py}]"

            decl = None
            if typename in PRIMITIVE_C_TYPES:
                decl = f"{type_ctype2} = {type_ctype}"
                config.global_names['types'].append(type_ctype2)

            elif max_indirection:
                config.global_names['types'].append(type_ctype2)

                if typename not in config.indirections:
                    config.indirections[typename] = 1
                else:
                    config.indirections[typename] += 1

            # print(f"{type_spec:<22} ctype: {type_ctype:<22} ctype2: {type_ctype2:<22}  py: {type_py:30} decl: {decl}")

            type_map[type_spec] = TypeWrapperData(type_spec, type_ctype, type_ctype2, type_py, max_indirection, decl)

        # else:
        #     print(f"Couldn't match '{type_spec}'")

    config.type_list = type_list
    config.type_map = type_map


def load_wrapper_data(config: GlobalWrapperData, module: ModuleWrapperData):
    for group in GLOBAL_GROUPS:
        if group not in config.global_names:
            config.global_names[group] = []

    for group in module.bind_data:
        if group not in config.global_names:
            config.global_names[group] = []

        if group == 'functions':
            module.functions = {}
            module.ignored_functions = map_get(module.meta_data, group, '*', 'ignore', default=[])

            if config.config.addContextManager:
                if 'contexts' not in config.global_names:
                    config.global_names['contexts'] = []

                for ctxmgr in map_get(module.meta_data, 'functions', '*', 'contextManager', default=[]):
                    api_name = ctxmgr.get('api')

                    if config.config.snakecaseFunctions:
                        api_name = snakefy(api_name)

                    config.global_names['contexts'].append(api_name)

            for func_data in module.bind_data[group]:

                name = func_data.get('name')
                if name in module.ignored_functions:
                    continue

                py_name = snakefy(name)
                if py_name in config.global_names[group]:
                    continue
                config.global_names[group].append(py_name if config.config.snakecaseFunctions else name)

                meta_data = map_get(module.meta_data, group, name, default={ '_empty': True })
                wrap_data = FunctionWrapperData.load(func_data, meta_data, module.name, module.library)
                module.functions[name] = wrap_data

        elif group == 'defines':
            module.defines = {}

            for define_data in module.bind_data[group]:

                name = define_data.get('name')
                kind = define_data.get('type')
                if name in config.global_names[group] or kind in ('GUARD', 'MACRO'):
                    continue
                elif kind == 'UNKNOWN' and not RE_UNKNOWN_DEFINE_VALUE.fullmatch(define_data.get('value')):
                    continue
                config.global_names[group].append(name)

                wrap_data = DefineWrapperData.load(define_data, None, module.name, module.library)
                module.defines[wrap_data.name] = wrap_data

        elif group == 'structs':
            module.structs = {}
            module.opaque_types = map_get(module.meta_data, group, '*', 'opaque', default=[])

            for struct_data in module.bind_data[group]:

                name = struct_data.get('name')
                if name in config.global_names[group]:
                    continue
                config.global_names[group].append(name)

                meta_data = map_get(module.meta_data, group, struct_data.get('name'), default={ '_empty': True })
                wrap_data = StructWrapperData.load(struct_data, meta_data, None, module.name, module.library)

                if 'aliases' not in config.global_names:
                    config.global_names['aliases'] = []
                for alias_data in module.bind_data.get('aliases', []):
                    if alias_data.get('type') == wrap_data.name:
                        if wrap_data.aliases is None:
                            wrap_data.aliases = []
                        wrap_data.aliases.append(AliasWrapperData.load(alias_data, None, module.name, module.library))
                        config.global_names['aliases'].append(alias_data.get('name'))
                        config.global_names['aliases'].append(f"{alias_data.get('name')}Ptr")

                module.structs[wrap_data.name] = wrap_data

        elif group == 'enums':
            module.enums = {}

            for enum_data in module.bind_data[group]:

                name = enum_data.get('name')
                if name in config.global_names[group]:
                    continue
                config.global_names[group].append(name)

                for values_data in enum_data.get('values', []):

                    value_name = values_data.get('name')
                    if value_name in config.global_names['enumerands']:
                        continue
                    config.global_names['enumerands'].append(value_name)

                wrap_data = EnumWrapperData.load(enum_data, None, module.name, module.library)
                module.enums[wrap_data.name] = wrap_data

        elif group == 'callbacks':
            module.callbacks = {}

            for callback_data in module.bind_data[group]:

                name = callback_data.get('name')
                if name in config.global_names[group]:
                    continue
                config.global_names[group].append(name)

                wrap_data = CallbackWrapperData.load(callback_data, None, module.name, module.library)
                module.callbacks[wrap_data.name] = wrap_data

# region ENTRYPOINT

if __name__ == '__main__':
    # make sure we're HERE
    os.chdir(os.path.dirname(__file__))
    wrapper = GlobalWrapperData.load('../input/rl500/global_config.json')
    # generate_binding_code(wrapper, 'test_rlapi3.py')
    generate_binding_code(wrapper, '../package/src/raylibpy/__init__.py')

# endregion (ENTRYPOINT)

# endregion (functions)
