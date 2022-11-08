# -*- encoding: utf8 -*-
# ------------------------------------------------------------------------------
# rlapi.py
# Created on 29/08/2022
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
from enum import IntEnum
import json
import re
import os

from raylib_formatting import *

# endregion (imports)
# ---------------------------------------------------------
# region EXPORTS


__all__ = [
    'generate_wrapper',
]


# endregion (exports)
# ---------------------------------------------------------
# region CONSTANTS

REGEX_TYPE_RULE = re.compile(r"\.\.\.|(const\s+)?(unsigned\s+)?(\w+|long long)\s*(\[(\d+)]|\*+)?")

# (py_type, ctypes_type, c_type, default)
PRIMITIVE_TYPE_MAPPING = {
    '...': ('bytes', 'VoidPtr', 'va_list', 'None', None),
    'va_list': ('bytes', 'VoidPtr', 'va_list', '', None),
    'void': ('None', 'None', 'void', 'None', None),
    'bool': ('bool', 'Bool', 'bool', 'False', 'bool({})'),
    'char': ('int', 'Char', 'char', '0', 'int({})'),
    'byte': ('int', 'Byte', 'byte', '0', 'int({})'),
    'short': ('int', 'Short', 'short', '0', 'int({})'),
    'int': ('int', 'Int', 'int', '0', 'int({})'),
    'long': ('int', 'Long', 'long', '0', 'int({})'),
    'long long': ('int', 'LongLong', 'long long', '0', 'int({})'),
    'void *': ('bytes', 'VoidPtr', 'void', 'None', None),
    'bool *': ('Union[Seq[bool], BoolPtr]', 'BoolPtr', 'bool', 'False', None),
    'char *': ('Union[str, CharPtr]', 'CharPtr', 'char *', 'None', '_str_in({})'),
    'char **': ('Seq[Union[str, CharPtr]]', 'CharPtrPtr', 'char **', 'None', 'str_in2({})'),
    'byte *': ('Union[Seq[int], BytePtr]', 'BytePtr', 'byte', 'None', None),
    'short *': ('Union[Seq[int], ShortPtr]', 'ShortPtr', 'short', 'None', None),
    'int *': ('Union[Seq[int], IntPtr]', 'IntPtr', 'int', 'None', None),
    'long *': ('Union[Seq[int], LongPtr]', 'LongPtr', 'long', 'None', None),
    'long long *': ('int', 'LongLongPtr', 'long long *', '0', 'int({})'),
    'unsigned char': ('int', 'UChar', 'unsigned char', '0', None),
    'unsigned byte': ('int', 'UByte', 'unsigned byte', '0', None),
    'unsigned short': ('int', 'UShort', 'unsigned short', '0', None),
    'unsigned int': ('int', 'UInt', 'unsigned int', '0', None),
    'unsigned long': ('int', 'ULong', 'unsigned long', '0', None),
    'unsigned long long': ('int', 'ULongLong', 'unsigned long long', '0', 'int({})'),
    'unsigned char *': ('Union[Seq[int], UCharPtr]', 'UCharPtr', 'unsigned char *', 'None', None),
    'unsigned byte *': ('Union[Seq[int], UBytePtr]', 'UBytePtr', 'unsigned byte *', 'None', None),
    'unsigned short *': ('Union[Seq[int], UShortPtr]', 'UShortPtr', 'unsigned short', 'None', None),
    'unsigned int *': ('Union[Seq[int], UIntPtr]', 'UIntPtr', 'unsigned int', 'None', None),
    'unsigned long *': ('Union[Seq[int], ULongPtr]', 'ULongPtr', 'unsigned long *', 'None', None),
    'unsigned long long': ('int', 'ULongLongPtr', 'unsigned long long *', '0', 'int({})'),
    'float': ('float', 'Float', 'float', '0.0', 'float({})'),
    'double': ('float', 'Double', 'double', '0.0', 'float({})'),
    'float *': ('Union[Seq[float], FloatPtr]', 'FloatPtr', 'float', '0.0', None),
    'double *': ('Union[Seq[float], FloatPtr]', 'DoublePtr', 'double', '0.0', None),
}

# endregion (constants)
# ---------------------------------------------------------
# region CLASSES

class InfoBase:
    """InfoBase class

    Base class for all wrapper info objects
    """

    def __init__(self, header_name, info, meta_info, config, bind_generator):
        self.header_name = header_name
        self.info = info
        self.meta_info = meta_info
        self.config = config
        self.bind_generator = bind_generator

    @property
    def type_annotation(self):
        return ''

    @property
    def type_hint(self):
        return ''

    def gen_wrapper(self):
        """Wraps this info object"""
        return ''

    def gen_docs(self):
        """Generates documetation for this object in Markdown"""
        return ''


# region Values


class TypeInfo(InfoBase):

    def __init__(self, header_name, spec, meta_info, config, bind_generator):
        super().__init__(header_name, {}, meta_info, config, bind_generator)
        self.info['mapped'] = None
        self._parse(spec)

    @property
    def const(self):
        return self.info.get('const')

    @property
    def unsigned(self):
        return self.info.get('unsigned')

    @property
    def name(self):
        return self.info.get('name')

    @property
    def mapped(self):
        return self.info.get('mapped')

    @property
    def ptr_level(self):
        return self.info.get('ptr_level')

    @property
    def arr_length(self):
        return self.info.get('arr_length')

    @property
    def func(self):
        return self.meta_info.get('func')

    @property
    def description(self):
        return self.info.get('description')

    @property
    def is_string_type(self):
        return self.name == 'char' and (self.arr_length or self.ptr_level)

    def find(self):
        return self.bind_generator.get_type(self.get_c_type())

    def get_c_type(self, full=False):
        ptr_arr = ''
        if self.arr_length:
            ptr_arr = '[{}]'.format(self.arr_length)
        elif self.ptr_level:
            ptr_arr = ' {}'.format('*' * self.ptr_level)

        return "{}{}{}{}".format(
            'const ' if self.const and full else '',
            'unsigned ' if self.unsigned else '',
            self.name,
            ptr_arr
        )

    def get_py_type(self):
        typ = self.bind_generator.get_type(self.get_c_type(), None)
        if not typ:
            base = self.bind_generator.get_type(self.name)
            # if base:
            #     print(self.get_c_type(), '-->', self.get_ctype_type())
            name = base.py_type if base else self.name
            if self.is_string_type:
                if self.ptr_level > 1:
                    return 'Seq[str]'
                return 'str'
            if self.arr_length:
                return 'Seq[{}]'.format(name)
            elif self.ptr_level:
                return '{}Ptr'.format(name)
            return name

        return typ.py_type

    def get_ctype_type(self):
        typ = self.bind_generator.get_type(self.get_c_type(), None)
        if not typ:
            base = self.bind_generator.get_type(self.name)
            name = base.ctypes_type if base else self.name
            ptr_arr = ''
            if self.is_string_type:
                if self.ptr_level > 1:
                    return 'CharPtrPtr'
                return 'CharPtr'
            if self.arr_length:
                ptr_arr = ' * {}'.format(self.arr_length)
            elif self.ptr_level:
                ptr_arr = 'Ptr'
            elif name == 'Void':
                ptr_arr = 'None'
            return "{}{}".format(name, ptr_arr)

        return typ.ctypes_type

    def _parse(self, spec):
        if spec == '...':
            self.info['const'] = False
            self.info['unsigned'] = False
            self.info['name'] = '...'
            self.info['ptr_level'] = 0
            self.info['arr_length'] = 0
        else:
            match = REGEX_TYPE_RULE.fullmatch(spec)
            if match:
                is_const, is_unsigned, t_name, length, pointer = match.groups()
                self.info['const'] = True if is_const else False
                self.info['unsigned'] = True if is_unsigned else False
                self.info['name'] = t_name
                self.info['ptr_level'] = len(length) if length and str(length).startswith('*') else 0
                self.info['arr_length'] = int(pointer, 10) if pointer and str(length).startswith('[') else 0

            else:
                raise ValueError("Spec: '{}' couldn't be parsed".format(spec))

        typ = self.bind_generator.get_type(self.get_c_type(), None)
        if not typ:
            primitive = self.bind_generator.get_type(self.name)

            if self.ptr_level or self.arr_length:
                default = 'None'
            else:
                default = '{}()'.format(self.name) if not primitive else primitive.default

            typ = TypeMap(self.get_py_type(), self.get_ctype_type(), self.get_c_type(), default, self)
            # print('Added type:', typ.c_type)
            self.bind_generator.map_type(typ.c_type, typ)

        self.info['mapped'] = typ


class DefineInfo(InfoBase):

    @property
    def name(self):
        return self.info.get('name')

    @property
    def type(self):
        return self.info.get('type')

    @property
    def value(self):
        return self.info.get('value')

    @property
    def description(self):
        return self.info.get('description')

    def gen_wrapper(self):
        if self.type in ('FLOAT', 'DOUBLE', 'INT', 'UNKNOWN'):
            return TPL_DEFINE_CONST.format(name=self.name, value=self.value, annotation=self.type_annotation, type_hint=self.type_hint)

        elif self.type == 'STRING':
            val = "'{}'".format(self.value)
            return TPL_DEFINE_CONST.format(name=self.name, value=val, annotation=self.type_annotation, type_hint=self.type_hint)

        elif self.type == 'FLOAT_MATH':
            return TPL_DEFINE_CONST.format(name=self.name, value=self.value.replace('.0f', '.0').replace('/', ' / '),
                                           annotation=self.type_annotation, type_hint=self.type_hint)

        elif self.type == 'COLOR':
            return TPL_DEFINE_COLOR.format(description=self.description, name=self.name, struct_name='Color',
                                           rgba=self.value.replace('CLITERAL(Color){', '').replace('}', ''),
                                           annotation=self.type_annotation, type_hint=self.type_hint)
        return '\n'

    def gen_docs(self):
        return "{name}: TODO.\n".format(name=self.name)


class AliasInfo(InfoBase):

    def __init__(self, header_name, info, meta_info, config, bind_generator):
        super().__init__(header_name, {}, meta_info, config, bind_generator)
        self.info['name'] = info.get('name')
        self.info['description'] = info.get('description')
        self.info['type'] = TypeInfo(header_name, info.get('type'), bind_generator.type_meta, config, bind_generator)


    @property
    def name(self):
        return self.info.get('name')

    @property
    def type(self):
        return self.info.get('type').find()

    @property
    def description(self):
        return self.info.get('description')

    def gen_wrapper(self):
        return TPL_DEFINE_ALIAS.format(description=self.description, name=self.name, type=self.type.py_type,
                                       annotation=self.type_annotation, type_hint=self.type_hint)

    def gen_docs(self):
        return "{name}: TODO.\n".format(name=self.name)

# endregion (values)

# region Functions


class ParameterInfo(InfoBase):

    def __init__(self, header_name, info, meta_info, config, bind_generator):
        super().__init__(header_name, {}, meta_info, config, bind_generator)
        self.info['name'] = info.get('name')
        self.info['type'] = TypeInfo(header_name, info.get('type'), bind_generator.type_meta, config, bind_generator)

    @property
    def name(self):
        return self.info.get('name')

    @property
    def py_name(self):
        return snakefy(self.info.get('name')) if self.config.snakefy_params else self.name

    @property
    def type(self):
        return self.info.get('type').find()

    @property
    def defaults_to(self):
        return self.meta_info.get('defaultsTo')

    @property
    def out_param(self):
        return self.meta_info.get('outParam')

    @property
    def var_args(self):
        return self.meta_info.get('varArgs')

    @property
    def ommit(self):
        return self.meta_info.get('ommit')

    @property
    def len_of_param(self):
        return self.meta_info.get('lenOfParam')

    @property
    def use_as_length(self):
        return self.meta_info.get('useAsLength')

    @property
    def func(self):
        return self.meta_info.get('func')

    @property
    def type_annotation(self):
        if self.config.type_annotate:
            return ": '{}'".format(self.type.py_type)
        return ''

    @property
    def type_hint(self):
        if self.config.type_hint:
            return self.type.py_type
        return ''

    def gen_wrapper(self):
        return "{name}{annotation}".format(
            name=self.py_name,
            annotation=self.type_annotation
        )

    def gen_wrapper_as_arg(self, is_self=False):
        if is_self:
            name = 'self'
        else:
            name = 'byref({})'.format(self.py_name) if self.out_param else self.py_name
        if self.len_of_param:
            return "len({})".format(snakefy(self.len_of_param))
        elif self.func:
            return self.func.format(name)
        elif self.type.info.func:
            return self.type.info.func.format(name)
        elif self.type.info.is_string_type:
            return "_str_in({})".format(self.py_name)
        return name

    def gen_docs(self):
        return "{name}: TODO.\n".format(name=self.name)


class FunctionInfo(InfoBase):

    def __init__(self, header_name, info, meta_info, config, bind_generator):
        super().__init__(header_name, info, {}, config, bind_generator)
        self.params = [ParameterInfo(header_name, p, meta_info.get('params', {}).get(p.get('name'), {}), config, bind_generator) for p in info.get('params', [])]
        self.info['returnType'] = TypeInfo(header_name, info.get('returnType'), bind_generator.type_meta, config, bind_generator)

    @property
    def name(self):
        return self.info.get('name')

    @property
    def py_name(self):
        return snakefy(self.info.get('name')) if self.config.snakefy_functions else self.name

    @property
    def type(self):
        return self.info.get('returnType').find()

    @property
    def description(self):
        return self.info.get('description')

    @property
    def type_annotation(self):
        if self.config.type_annotate:
            return " -> '{}'".format(self.type.py_type)
        return ''

    @property
    def type_hint(self):
        if self.config.type_hint:
            t_params = ', '.join([p.type_hint for p in self.params if not p.ommit])
            return "# type: ({}) -> {}".format(t_params, self.type.py_type)
        return ''

    def gen_wrapper_proto(self, lib_name='raylib'):
        arg_types = ', '.join([p.type.ctypes_type for p in self.params])
        res_type = self.type.ctypes_type if (self.type and self.type.ctypes_type != 'Void') else "None"

        return TPL_FUNCTION_WRAPCALL.format(
            lib_name=lib_name,
            api_name=self.name,
            arg_types=arg_types,
            res_type=res_type
        )

    def gen_param_list(self, bound_as=''):
        plist = [p.gen_wrapper() for p in self.params if not p.ommit]
        if bound_as == 'classmethod':
            if plist:
                plist.insert(0, 'cls')
        elif bound_as == 'staticmethod':
            pass
        elif bound_as == 'method':
            if plist:
                plist[0] = 'self'

        return ', '.join(plist)

    def gen_arg_list(self, bound_as='', byref=False):
        alist = [p.gen_wrapper_as_arg() for p in self.params]
        if bound_as == 'classmethod':
            pass
        elif bound_as == 'staticmethod':
            pass
        elif bound_as in ('method', 'property'):
            if alist:
                alist[0] = 'self.byref' if byref else 'self'

        return ', '.join(alist)

    def gen_wrapper(self, bound=False, bound_as='', rename='', byref=False, inplace=False, attr=None):
        result = ''
        before = ''
        after = ''
        a = b = ''
        template = TPL_FUNCTION
        name = self.name
        decorator = ''
        indent = '    '
        if bound:
            indent = '        '
            if bound_as in ('classmethod', 'method', 'staticmethod'):
                template = TPL_STRUCTURE_METHOD
                decorator = '@{}\n    '.format(bound_as) if bound_as != 'method' else ''
            elif bound_as == 'property':
                template = TPL_STRUCTURE_GETTER
                decorator = '@property'

            name = rename

        if self.config.snakefy_functions:
            name = snakefy(name)

        for p in self.params:
            if p.out_param:
                before += '\n{}{} = {}(0)'.format(indent, p.py_name, p.type.ctypes_type.replace('Ptr', ''))
            if p.use_as_length:
                b = ', {}.value)'.format(p.py_name)

        if self.type.c_type != "void":
            if inplace:
                result = 'self.{} = '.format(attr)
                after = '\n{}return self'.format(indent)
            else:
                result = 'result = '
                after = '\n{}return result'.format(indent)
            if self.type.info.ptr_level:
                a = '_ptr_out('
                b =  b if b else ')'
            elif self.type.info.ptr_level:
                a = '_arr_out('
                b = b if b else ')'

        return template.format(
            py_name=name,
            decorator=decorator,
            annotation=self.type_annotation,
            type_hint='\n{}{}'.format(indent, self.type_hint) if self.config.type_hint else '',
            description=self.description,
            param_list=self.gen_param_list(bound_as),
            arg_list=self.gen_arg_list(bound_as, byref),
            result=result,
            before=before,
            after=after,
            prefix='_',
            a=a,
            b=b,
            c_name=self.name
        )

    def gen_wrapper_as_arg(self):
        return self.name

    def gen_docs(self):
        return "{name}: TODO.\n".format(name=self.name)


class CallbackInfo(InfoBase):

    def __init__(self, header_name, info, meta_info, config, bind_generator):
        super().__init__(header_name, {}, meta_info, config, bind_generator)
        self.params = [ParameterInfo(header_name, p, meta_info, config, bind_generator) for p in info.get('params', [])]
        self.info['name'] = info.get('name')
        self.info['description'] = info.get('description')
        self.info['returnType'] = TypeInfo(header_name, info.get('returnType'), bind_generator.type_meta, config, bind_generator)

    @property
    def name(self):
        return self.info.get('name')

    @property
    def type(self):
        return self.info.get('returnType').find()

    @property
    def description(self):
        return self.info.get('description')

    @property
    def type_annotation(self):
        if self.config.type_annotate:
            return " -> {}".format(self.type.py_type)
        return ''

    @property
    def type_hint(self):
        if self.config.type_hint:
            t_params = ', '.join([p.type_hint for p in self.params])
            return "\n    # type: ({}) -> {}".format(t_params, self.type.py_type)
        return ''

    def gen_wrapper(self):
        args = [p.type.ctypes_type for p in self.params]
        args.insert(0, self.type.ctypes_type)
        return TPL_FUNCTION_TYPE.format(
            name=self.name,
            description=self.description,
            args=', '.join(args)
        )

# endregion (functions)

# region Enums


class EnumerationInfo(InfoBase):

    def __init__(self, header_name, info, meta_info, config, bind_generator):
        super().__init__(header_name, {}, meta_info, config, bind_generator)
        self.info['name'] = info.get('name')
        self.info['description'] = info.get('description')
        self.info['values'] = [
            EnumerandInfo(header_name, e, meta_info, config, bind_generator)
            for e in info.get('values', [])
        ]

    @property
    def name(self):
        return self.info.get('name')

    @property
    def description(self):
        return self.info.get('description')

    @property
    def values(self):
        return self.info.get('values')

    def gen_members_wrapper(self):
        return '\n'.join([m.gen_wrapper() for m in self.values])

    def gen_members_wrapper_unbound(self):
        return '\n'.join([m.gen_wrapper_unbound(self.name) for m in self.values])

    def gen_wrapper(self):
        return TPL_ENUMERATION.format(
            name=self.name,
            description=self.description,
            members=self.gen_members_wrapper(),
            unbound_members=self.gen_members_wrapper_unbound(),
        )


class EnumerandInfo(InfoBase):

    @property
    def name(self):
        return self.info.get('name')

    @property
    def description(self):
        return self.info.get('description')

    @property
    def value(self):
        return self.info.get('value')

    def gen_wrapper(self):
        return TPL_ENUMERATION_MEMBER.format(
            name=self.name,
            value=self.value,
            description=self.description
        )

    def gen_wrapper_unbound(self, enum_name):
        return "{name} = {enum_name}.{name}".format(
            enum_name=enum_name,
            name=self.name,
            descr=self.description
        )


# endregion (enums)

# region Structures


class FieldInfo(InfoBase):

    def __init__(self, header_name, info, meta_info, config, bind_generator):
        super().__init__(header_name, {}, meta_info, config, bind_generator)   
        self.info['name'] = info.get('name')
        self.info['description'] = info.get('description')
        self.info['type'] = TypeInfo(header_name, info.get('type'), bind_generator.type_meta, config, bind_generator)

    @property
    def name(self):
        return self.info.get('name')

    @property
    def type(self):
        return self.info.get('type').find()

    @property
    def py_name(self):
        return snakefy(self.info.get('name')) if self.config.snakefy_fields else self.name

    @property
    def description(self):
        return self.info.get('description')

    @property
    def type_annotation(self):
        if self.config.type_annotate:
            return ": {}".format(self.type.py_type)
        return ''

    def gen_wrapper(self):
        return "        ('{}', {}),".format(
            self.py_name,
            self.type.ctypes_type
        )

    def gen_param_wrapper(self):
        eq = ' = ' if self.config.type_annotate else '='
        name = self.py_name
        if globals().get(name):
            name = '{}_'.format(name)
        return "{name}{annotation}{eq}None".format(
            name=name,
            annotation=self.type_annotation,
            eq=eq
        )

    def gen_arg_wrapper(self):
        info = self.info['type']
        name = self.py_name
        if globals().get(name):
            name = '{}_'.format(name)
        if info.ptr_level or info.arr_length:
            return name
        return "{} or {}".format(name, self.type.default)


class StructureInfo(InfoBase):

    def __init__(self, header_name, info, meta_info, config, bind_generator):
        super().__init__(header_name, info, meta_info, config, bind_generator)
        self.fields = [FieldInfo(header_name, f, meta_info, config, bind_generator) for f in info.get('fields', [])]

    @property
    def name(self):
        return self.info.get('name')

    @property
    def py_name(self):
        return snakefy(self.info.get('name'))

    @property
    def func(self):
        return self.meta_info.get('func')

    @property
    def description(self):
        return self.info.get('description')

    def gen_field_list(self):
        return TPL_STRUCTURE_FIELD_MAP.format(
            fields='\n'.join(f.gen_wrapper() for f in self.fields)
        )

    def gen_args_list(self):
        return ',\n            '.join([f.gen_arg_wrapper() for f in self.fields])

    def gen_param_list(self):
        sep = ', ' if len(self.fields) <= 4 else ',\n                 '
        return sep.join([f.gen_param_wrapper() for f in self.fields])

    def gen_extra_classmethods(self):
        extra_methods = ''
        if self.config.bind_classmethods:
            methods = self.meta_info.get('bindApiAsClassmethod', [])
            for bind_data in methods:
                api = bind_data.get('api')
                rename = bind_data.get('renameAs')
                byref = bind_data.get('byref', False)
                info = self.bind_generator.functions_by_name.get(api)

                if info is not None:
                    extra_methods += info.gen_wrapper(True, 'classmethod', rename, byref)

        return extra_methods

    def gen_dunder_methods(self):
        return ''

    def gen_extra_methods(self): 
        extra_methods = ''
        if self.name == "Vector2" and self.config.add_vector_attrib_swizzling:
            extra_methods += TPL_VECTOR2_SWIZZLING

        if self.name == "Vector3" and self.config.add_vector_attrib_swizzling:
            extra_methods += TPL_VECTOR3_SWIZZLING

        if self.name == "Vector4" and self.config.add_vector_attrib_swizzling:
            extra_methods += TPL_VECTOR4_SWIZZLING

        if self.name == "Color" and self.config.add_color_attrib_swizzling:
            extra_methods += TPL_COLOR_SWIZZLING

        if self.name == "Rectangle" and self.config.add_rect_attrib_swizzling:
            extra_methods += TPL_RECTANGLE_SWIZZLING

        if self.meta_info.get('dunderStrExpression', False):
            extra_methods += "\n    def __str__(self):\n        {}\n".format(self.meta_info.get('dunderStrExpression'))

        if self.meta_info.get('dunderReprExpression', False):
            extra_methods += "\n    def __repr__(self):\n        {}\n".format(self.meta_info.get('dunderReprExpression'))

        if self.config.bind_context:

            context = self.meta_info.get('bindApiAsContextManager', {})
            if context:
                ctx_enter = self.bind_generator.functions_by_name.get(context.get('enter'))
                ctx_leave = self.bind_generator.functions_by_name.get(context.get('leave'))
                if ctx_enter and ctx_leave:
                    extra_methods += TPL_CONTEXT_MANAGER.format(
                        enter='_' + ctx_enter.name,
                        leave='_' + ctx_leave.name)

        if self.config.bind_property:
            methods = self.meta_info.get('bindApiAsProperty', [])
            for bind_data in methods:
                api = bind_data.get('api')
                rename = bind_data.get('renameAs')
                byref = bind_data.get('byref', False)
                info = self.bind_generator.functions_by_name.get(api)

                if info is not None:
                    extra_methods += info.gen_wrapper(True, 'property', rename, byref)

        if self.config.bind_methods:
            methods = self.meta_info.get('bindApiAsMethod', [])
            for bind_data in methods:
                api = bind_data.get('api')
                rename = bind_data.get('renameAs')
                inplace = bind_data.get('inplace', False)
                attr = bind_data.get('attr', None)
                byref = bind_data.get('byref', False)
                info = self.bind_generator.functions_by_name.get(api)

                if info is not None:
                    extra_methods += info.gen_wrapper(True, 'method', rename, byref, inplace, attr)

        if self.config.bind_staticmethods:
            methods = self.meta_info.get('bindApiAsStaticmethod', [])
            for bind_data in methods:
                api = bind_data.get('api')
                rename = bind_data.get('renameAs')
                byref = bind_data.get('byref', False)
                info = self.bind_generator.functions_by_name.get(api)

                if info is not None:
                    extra_methods += info.gen_wrapper(True, 'staticmethod', rename, byref)

        return extra_methods

    def gen_extra_props(self):
        return ''

    def gen_init_typehint(self):
        if self.config.type_hint:
            return "\n        # type: ({}) -> None".format(
                ', '.join([f.type.py_type for f in self.fields])
            )
        return ''

    def gen_wrapper(self):
        return TPL_STRUCTURE.format(
            name=self.name,
            py_name=self.py_name,
            description=self.description,
            field_map=self.gen_field_list(),
            init_fields=self.gen_args_list(),
            init_params=self.gen_param_list(),
            extra_classmethods=self.gen_extra_classmethods(),
            dunder_methods=self.gen_dunder_methods(),
            extra_props=self.gen_extra_props(),
            extra_methods=self.gen_extra_methods(),
            type_hint=self.gen_init_typehint(),
            alias=''
        )

# endregion (structures)


class TypeMap:

    def __init__(self, py_type, ctypes_type, c_type, default, info):
        self.py_type = py_type
        self.ctypes_type = ctypes_type
        self.c_type = c_type
        self.default = default
        self.info = info


class BindGenerator:

    def __init__(self):
        self.defines = []
        self.structs = []
        self.aliases = []
        self.enums = []
        self.callbacks = []
        self.functions = []
        self.functions_by_name = {}
        self.export_names = []
        self.type_map = {}
        self.type_meta = {}

        #load primitive type mappings
        for key, (py_type, ctypes_type, c_type, default, func) in PRIMITIVE_TYPE_MAPPING.items():
            info = TypeInfo('raylib', key, {'func': func}, None, self)
            self.type_map[key] = TypeMap(py_type, ctypes_type, c_type, default, info)

    def map_type(self, c_type, type_map):
        if c_type in self.type_map:
            return
        self.type_map[c_type] = type_map

    def get_type(self, c_type, default=None):
        return self.type_map.get(c_type, default)

    def load_info(self, header_name, info, meta_info, config):
        loaded_structs = []
        self.type_meta = meta_info.get('types', {})

        for struct_info in info.get('structs', []):
            name = struct_info.get('name')
            if name in loaded_structs:
                print('{} already loaded'.format(name))
                continue
            loaded_structs.append(name)
            struct_meta = meta_info.get('structs', {}).get(name, {})
            s_info = TypeInfo(header_name, name, struct_meta, config, self)
            self.export_names.append(name)
            self.map_type(s_info.name, TypeMap(
                s_info.get_ctype_type(),
                s_info.get_c_type(),
                s_info.get_py_type(),
                '{}()'.format(name),
                s_info
            ))
            s_info_ptr = TypeInfo(header_name, name + ' *', struct_meta, config, self)
            self.map_type(s_info_ptr.name, TypeMap(
                s_info_ptr.get_ctype_type(),
                s_info_ptr.get_c_type(),
                s_info_ptr.get_py_type(),
                'None',
                s_info_ptr
            ))
            self.structs.append(StructureInfo(header_name, struct_info, struct_meta, config, self))

        for define_info in info.get('defines', []):
            if define_info.get('type') in ('GUARD', 'UNKNOWN', 'MACRO'):
                continue
            self.export_names.append(define_info.get('name'))
            define_meta = meta_info.get('defines', {})
            self.defines.append(DefineInfo(header_name, define_info, define_meta, config, self))

        for alias_info in info.get('aliases', []):
            alias_meta = meta_info.get('aliases', {})
            self.export_names.append(alias_info.get('name'))
            self.aliases.append(AliasInfo(header_name, alias_info, alias_meta, config, self))

        for enum_info in info.get('enums', []):
            enum_meta = meta_info.get('enums', {})
            self.export_names.append(enum_info.get('name'))
            e_info = EnumerationInfo(header_name, enum_info, enum_meta, config, self)
            for m in e_info.values:
                self.export_names.append(m.name)
            self.enums.append(e_info)

        for callback_info in info.get('callbacks', []):
            callback_meta = meta_info.get('callbacks', {})
            self.export_names.append(callback_info.get('name'))
            self.callbacks.append(CallbackInfo(header_name, callback_info, callback_meta, config, self))

        for function_info in info.get('functions', []):
            name = function_info.get('name')
            function_meta = meta_info.get('functions', {}).get(name, {})
            ignored = name in meta_info.get('functions', {}).get('*', {}).get('ignore', [])
            if ignored:
                continue
            f_info = FunctionInfo(header_name, function_info, function_meta, config, self)
            self.export_names.append(f_info.py_name)
            self.functions.append(f_info)
            self.functions_by_name[name] = f_info

    def gen_wrapper(self, out_fname, config):
        LIBNAME = 'rlapi'
        fullcode = TPL_HEADER_IMPORTS.format(
            lib_name=config.lib_name,
            exports="".join("\n    '{}',".format(n) for n in self.export_names),
            lib_basedir=config.lib_basedir,
            win32_lib_filename=config.win32_lib_fname,
            linux_lib_filename=config.linux_lib_fname,
            darwin_lib_filename=config.darwin_lib_fname,
        )

        fullcode += TPL_HEADER_UTILS

        for struct in self.structs:

            wrp = struct.gen_wrapper()
            fullcode += wrp

            for alias in self.aliases:
                if alias.type.py_type == struct.name:
                    fullcode += alias.gen_wrapper()

        for enum in self.enums:
            fullcode += enum.gen_wrapper()

        for define in self.defines:
            fullcode += define.gen_wrapper()

        for callback in self.callbacks:
            fullcode += callback.gen_wrapper()

        for function in self.functions:
            fullcode += function.gen_wrapper_proto(config.lib_name)

        for function in self.functions:
            fullcode += function.gen_wrapper()

        with open(out_fname, 'w', encoding='utf8') as wrapper:
            wrapper.write(fullcode)


class Config:

    def __init__(self, info):
        self.info = info

    @property
    def type_hint(self):
        return self.info.get('typeHint', False)

    @property
    def type_annotate(self):
        return self.info.get('typeAnnotate', False)

    @property
    def lib_name(self):
        return self.info.get('libName')

    @property
    def snakefy_functions(self):
        return self.info.get('snakecaseFunctions', False)

    @property
    def snakefy_params(self):
        return self.info.get('snakecaseParameters', False)

    @property
    def snakefy_fields(self):
        return self.info.get('snakecaseFields', False)

    @property
    def add_vector_attrib_swizzling(self):
        return self.info.get('addVectorAttribSwizzling', False)

    @property
    def add_color_attrib_swizzling(self):
        return self.info.get('addColorAttribSwizzling', False)

    @property
    def add_rect_attrib_swizzling(self):
        return self.info.get('addRectangleAttribSwizzling', False)

    @property
    def bind_classmethods(self):
        return self.info.get('bindApiAsClassmethod', False)

    @property
    def bind_staticmethods(self):
        return self.info.get('bindApiAsStaticmethod', False)

    @property
    def bind_methods(self):
        return self.info.get('bindApiAsMethod', False)

    @property
    def bind_property(self):
        return self.info.get('bindApiAsProperty', False)

    @property
    def bind_context(self):
        return self.info.get('bindApiAsContextManager', False)

    @property
    def win32_lib_fname(self):
        return self.info.get('win32LibFilename')

    @property
    def linux_lib_fname(self):
        return self.info.get('linuxLibFilename')

    @property
    def darwin_lib_fname(self):
        return self.info.get('darwinLibFilename')

    @property
    def lib_basedir(self):
        return self.info.get('libBasedir')


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


def main(in_fnames, out_fname, in_meta=None, **config):
    generator = BindGenerator()
    default_config = {
        "libBasedir": "os.path.dirname(__file__)",
        "libName": "rlapi",
        "snakecaseFunctions": True,
        "snakecaseParameters": True,
        "snakecaseFields": True,
        "bindApiAsClassmethod": True,
        "bindApiAsStaticmethod": True,
        "bindApiAsMethod": True,
        "bindApiAsProperty": True,
        "typeHint": True,
        "typeAnnotate": False,
        "win32LibFilename": "raylib.dll",
        "linuxLibFilename": "libraylib.so.4.2.0",
        "darwinLibFilename": "libraylib.4.2.0.dylib"
    }

    meta_info = {}
    if in_meta:
        with open(in_meta, 'r', encoding='utf8') as meta:
            meta_info = json.load(meta)
            default_config.update(meta_info.get('CONFIG', {}))
            default_config.update(config)

    config = Config(default_config)

    for fname in in_fnames:
        with open(fname, 'r', encoding='utf8') as info:
            generator.load_info(os.path.basename, json.load(info), meta_info, config)

    generator.gen_wrapper(out_fname, config)


if __name__ == '__main__':
    main(
        ['../input/raylib_api.json', '../input/rmath_api.json', '../input/rlgl.json'],
        '../output/rl.py',
        '../input/raylib_api.bind.json'
    )


# endregion (functions)
# ---------------------------------------------------------
