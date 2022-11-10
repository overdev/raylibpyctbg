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
