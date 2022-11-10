# region HEADER & FOOTER

TPL_DOC_HEADER = '''# Raylib-py API reference

This is an API reference documentation generated for Raylib {version}.

<h2 id="toc">Table of Contents</h2>

- <a href="#structs">Structures</a>
- <a href="#aliases">Aliases</a>
- <a href="#enums">Enumerations</a>
- <a href="#defines">Constants</a>
- <a href="#funcs">Functions</a>
- <a href="#callbacks">Callbacks</a>
- <a href="#contexts">Context Managers</a>

---

## Helper Types

Many types are aliases to ctypes types. Types suffixed with `Ptr` are pointer types.

To create array types, you can multiply the type to the array length, like below:

```python

# Create an array of 4 floats:
arr = (Float * 4)(1.0, 3.5, -10.0, 0.0)

```

Raylib wrapped structures provide the `array_of()` classmethod for this same purpose:

```python

# Create an array of Vector2:
v_arr = Vector2.array_of([vec1, vec2, vec3, vec4])

```

Alias | Ctypes type
------|-------
`Bool` | `c_bool`
`BoolPtr` | `POINTER(c_bool)`
`Byte` | `c_byte`
`BytePtr` | `POINTER(c_byte)`
`Char` | `c_char`
`CharPtr` | `POINTER(c_char)`
`Short` | `c_short`
`ShortPtr` | `POINTER(c_short)`
`Int` | `c_long`
`IntPtr` | `POINTER(c_long)`
`Long` | `c_long`
`LongPtr` | `POINTER(c_long)`
`LongLong` | `c_longlong`
`LongLongPtr` | `POINTER(c_longlong)`
`UChar` | `c_ubyte`
`UCharPtr` | `POINTER(c_ubyte)`
`UByte` | `c_ubyte`
`UBytePtr` | `POINTER(c_ubyte)`
`UShort` | `c_ushort`
`UShortPtr` | `POINTER(c_ushort)`
`UInt` | `c_ulong`
`UIntPtr` | `POINTER(c_ulong)`
`ULong` | `c_ulong`
`ULongPtr` | `POINTER(c_ulong)`
`ULongLong` | `c_ulonglong`
`ULongLongPtr` | `POINTER(c_ulonglong)`
`Float` | `c_float`
`FloatPtr` | `POINTER(c_float)`
`Double` | `c_double`
`DoublePtr` | `POINTER(c_double)`
`VoidPtr` | `c_void_p`
`VoidPtrPtr` | `POINTER(c_void_p)`
`CharPtr` | `c_char_p`
`CharPtrPtr` | `POINTER(c_char_p)`

'''

TPL_DOC_FOOTER = '''---

<small>Generation date: {gen_date}</small>
'''

# endregion (HEADER & FOOTER)

# region ENUMERATIONS

TPL_DOC_ENUMS = '''<h2 id="enums">Enumerations</h2>

{enum_list}

[ <a href="#toc">ToC</a> ]

'''

TPL_DOC_ENUMERATION = '''<h2 id="{enum_id}"><code>{name}</code> enum</h2>

**Members**

Name | Value | Description
-----|-------|------------
{members}

[ <a href="#enums">Enums</a> | <a href="#toc">ToC</a> ]

---
'''

# endregion (ENUMERATIONS)

# region STRUCTURES

TPL_DOC_STRUCTS = '''<h2 id="structs">Structures</h2>

{struct_list}

[ <a href="#toc">ToC</a> ]
'''

TPL_DOC_STRUCTURE = '''<h2 id="{struct_id}"><code>{name}</code> structure</h2>

{struct_description}

**Fields**

Name | Type (Python) | Type (Ctypes) | Type (C) | Description
-----|---------------|---------------|----------|------------
{members}

{doc_properties}{doc_methods}{doc_context}

[ <a href="#structs">Structs</a> | <a href="#toc">ToC</a> ]

---
'''

TPL_DOC_METHODS = '''### Methods

Bound as | Name | API
---------|------|----
{method_list}

'''

TPL_DOC_PROPERTIES = '''### Properties

Name | API
-----|----
{property_list}

'''

TPL_DOC_CONTEXTMANAGERS = '''### Context Manager

Context | API
--------|----
Enter | {ctx_enter}
Leave | {ctx_leave}

'''

# endregion (STRUCTURES)

# region FUNCTIONS

TPL_DOC_FUNCS = '''<h2 id="funcs">Functions</h2>

{func_list}

[ <a href="#toc">ToC</a> ]

'''

TPL_DOC_FUNCTION = '''<h2 id="{func_id}"><code>{name}</code> function</h2>

> {func_description}

Defined in {defn_header}:

```c
{c_decl}
```

Python wrapper:

```python
{py_decl}
```
{see_also}
[ <a href="#funcs">Funcs</a> | <a href="#toc">ToC</a> ]

---
'''
# endregion (FUNCTIONS)

# region CONTEXT MANAGERS

TPL_DOC_CONTEXTS = '''<h2 id="contexts">Context Managers</h2>

To use context managers, you can do like below:

```python
# this example shows a rendering step

with drawing():

    with texture_mode(minimap_texture):
        # render the minimap
        draw_line(2, 2, 5, 5, RED)
    # no texture mode after this line

    with mode2d(main_camera):
        # 2d drawing logic...
        draw_texture(minimap_texture, 10, 10, WHITE)
    # no mode 2d after this line
# no drawing after this line

```

{ctx_list}

[ <a href="#toc">ToC</a> ]

'''

TPL_DOC_CONTEXTMANAGER = '''<h2 id="{ctx_id}"><code>{name}</code> context manager</h2>

> On entering the context: *{ctx_description_enter}*
> On leaving the context: *{ctx_description_leave}*

```python
@contextmanager
{py_decl}
```

[ <a href="#contexts">Contexts</a> | <a href="#toc">ToC</a> ]

---
'''
# endregion (CONTEXT MANAGERS)

# region DEFINES

TPL_DOC_DEFINES = '''<h2 id="defines">Constants</h2>

Name | Value | Description
-----|-------|------------
{defn_list}

[ <a href="#toc">ToC</a> ]

'''

# endregion (DEFINES)

# region ALIASES

TPL_DOC_ALIASES = '''<h2 id="aliases">Aliases</h2>

Alias Name | Type | Description
-----------|------|------------
{aliases_list}

[ <a href="#toc">ToC</a> ]

'''

# endregion (ALIASES)

# region CALLBACKS

TPL_DOC_CALLBACKS = '''<h2 id="callbacks">Callbacks</h2>

To define and use your own callbacks, you can do like below:

```python
# defines a callback function decorating it with the AudioCallback CFUNCTYPE
@AudioCallback
def my_callback(data, frames):
    # TODO: some logic
    pass

# then, somewhere ahead in the code
set_audio_stream_callback(some_stream, my_callback)

```

Name | Signature | Description
-----|-----------|------------
{cb_list}

[ <a href="#toc">ToC</a> ]

'''

# endregion (CALLBACKS)
