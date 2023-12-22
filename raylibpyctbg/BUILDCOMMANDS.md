# Build Commands or How to Build a Custom Raylibpy Package

The idea behind raylibpyctbg is to provide an automated way of generating and maintaining Python bindings for C raylib. This is the tool used to generate [raylibpy](https://github.com/overdev/raylib-py) whenever a new release is made. But it turns out that some times users of raylibpy want to use the binding with some custom shared lib they had compiled on their machine.  It wouldn't be nice if a new relase of raylibpy was made whenever someone wanted some custom feature, so I decided to provide de source of this repo along with a little help for those wanting their own raylipy binding. 

## Getting started

The first thing to do is to clone the repo on you machine.

You can [download the zip](https://github.com/overdev/raylibpyctbg/archive/refs/heads/development.zip) or use the command line:

```
$ git clone https://github.com/overdev/raylibpyctbg.git
```

With the repo cloned, we can try to generate a package that suits our needs.

## Generation command

The intended way of issuing the command is to set the current working directory to the root dir of the repo, and then:

```
py -3.x raylibpyctbg --help
```

On Mac and/or Linux the command _probably_ is:

```
python3 raylibpyctbg --help
```

This command will cause a help message to be shown describing all options available:

```
usage: raylibpyctbg [-h] [-c CONFIG] [-o OUT] [-g] [-d] [-b] [-i] [-v]

options:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Custom binding configuration (JSON) file path
  -o OUT, --out OUT     The binding code output file path
  -g, --generate        Generate the binding code
  -d, --docs            Generate the binding documentation (inactive)
  -b, --build           Build the package (requires build package)
  -i, --install         [Re]Install the newly built package
  -v, --version         Print the version information and exits
```

Let's look more closely on each of these options


### `-c <filename>` or `--config <filename>`

With this option you can specify a custom global configuration file. It expects `<filename>` to be the path to a JSON file. If you omit this option, the default config in the `input/rl500/global_config.json` will be loaded.


### `-o <filename>` or `--out <filename>`

This option allows you the specify where you want the binding code to be stored. By default, `<filename>` is the `__init__.py` in the `package/src/raylibpy` dir.


### `-g` or `--generate`

Add this option if you want the binding code to be generated.


### `-b` or `--build`

Add this option if you want to build a python wheel (`*.whl`) with the package source. This option requires you to install the _build_ package with pip. Note that _build_ requires an internet connection.

### `-i` or `--install`

Add this option to install the package that was built with `-b` command. This is not a normal installation but a forced one, meaning that it will uninstall the previous one and install this new.

### `-d` or `--docs`

Adds this option if you want to generate the documentation for this binding. **This option is not functional yet.**


### `-v` or `--version`

Prints the raylibpyctbg version and exits.


### `-h` or `--help`

Prints the raylibpyctbg help information above and exits.


### Gen code, build and/or install

The options to generate the binding code, build the package or install it work independent of each other. You can combine them or isolate them.


## Global Configuration JSON file

The global configuration JSON file has the following contents:

```json
{
    "snakecaseFunctions": true,
    "snakecaseParameters": true,
    "snakecaseFields": true,
    "snakecaseProperties": true,
    "bindApiAsClassmethod": true,
    "bindApiAsDestructor": true,
    "bindApiAsStaticmethod": true,
    "bindApiAsMethod": true,
    "bindApiAsProperty": true,
    "bindApiAsContextManager": true,
    "addUtilityMethods": true,
    "addBinaryPackingMethods": false,
    "addContextManager": true,
    "addVectorMath": true,
    "addAttribSwizzling": true,
    "typeHint": true,
    "typeAnnotate": false,
    "coreLibrary": {/* ... */},
    "extensionLibraries": [/* ... */]
}
```


### `typeHint` or `typAnnotate` Options

These options define whether the binding will include type information on function parameters and return values. By default the binding includes no type information but it can be included in two flavors:

Type hint:
```python

def is_key_pressed(key):
    # type: (int) -> bool
    """Check if a key has been pressed once"""
    result = _IsKeyPressed(int(key))
    return result

```

Type annotation:
```python

def is_key_pressed(key: int) -> bool:
    """Check if a key has been pressed once"""
    result = _IsKeyPressed(int(key))
    return result

```


### `snakecase*` Options

By default the Python naming convention will be kept in the binding code, but this option allows C naming convention to be applied if and where necessary.

With `snakecaseFunctions` disabled:
```python
def IsKeyPressed(key):
    # ...
```

With `snakecaseFunctions` enabled:
```python
def is_key_pressed(key):
    # ...
```

There are also options for changing the case of function parameters, structure fields and properties. 

### `attribSwizzling` Option

This option causes some raylib types to be added a feature common in OpenGL Shading Language vectors. With this option `Vector2`, `Vector3`, `Vector4`, `Color` and `Rectangle` attributes can be mixed together as a single attribute:

```python
vec = Vector2(5.0, 7.0)
vec3 = vec.yxy  # make a new Vector3 by combining attributes 'x' and 'y' of 'vec' instance
```

### `bindApiAs*` Option

Raylib has many functions that relates to some of its structure types, like:

```python
def draw_model(model, position, scale, tint)
```

With this option, this function will be bound to the `Model` structure as an instance method:

```python
my_model = load_model("path/to/resource.ext")

# somewhere later in code
my_model.draw(Vector3(10.5, 20.0, 120.0), 1.5, YELLOW)
```

Which is the same as:

```python
my_model = load_model("path/to/resource.ext")

# somewhere later in code
draw_model(my_model, Vector3(10.5, 20.0, 120.0), 1.5, YELLOW)
```

Not all function will be bound to a type, only those that have a strong relation to a raylib structure. Besides that, functions that can be bound, will be bound as `@classmethod`, instance method, `@staticmethod`, `@property` or context manager (`__enter__()` and `__exit__()`).


### `addUtilityMethods` Option

This basically adds the classmethod `.array_of(sequence)` to all structure types, to create arrays from sequences.


### `addBinaryPackingMethods` Option

This is a work in progress aimed at allowing easy conversion of structure type to and from `bytes` or `bytearray`s. Not all classes will have or need this feature, but many will do. This may become the mechanism for storing game saves or states.


### `addContextManager` Option

This option is related to all pair of functions in raylib named with _begin_  and _end_, or _enable_ and _disable_ (many examples in rlgl). The functions

```python
def begin_drawing():
    # ...

def end_drawing():
    # ...
```

will become a context manager function to be called in a `with` statement:

```python
@contextmanager
def drawing():
    """Context manager for drawing"""
    _BeginDrawing()
    yield
    _EndDrawing()
```

This allows for a more readable code:

```python
with drawing():
    # render stuff
```

Which is the same as:

```python
begin_drawing()
    # render stuff
end_drawing()
```


### `addVectorMath` Option

This option adds special methods to `Vector2` and `Vector3` (and a few to `Vector4`) that overloads the operators `+`, `-`, `*`, `/`, `//`, `==`, `!=`, unary `-`, and `abs(x)`. The overloaded operators support operands of same type or scalars (`int`s and `float`s). For multiplication, `Matrix` supports the operation between two matrices, and between vector and a matrix. This option depends on the option `addAttribSwizzling` to be enabled.


### Library Object Options

Inside the global configuration there's also two options dealing with libraries: `coreLibrary` and `extensionLibraries`. The first defines the main library of the binding (raylib, of course) and its related names, paths, modules and extra configs. The second allows you to configure extra libraries in the same fashion as the main one, in case you have the binaries and the necessary JSON files.

Let's take a closer look on the contents of this object.

```json
{
    // (options seen above)
    "coreLibrary": {
        "libName": "rlapi",
        "libKeyName": "raylib",
        "libBasedir": ["{}/bin"],
        "includedModules": ["raylib", "raymath", "rlgl"],
        "binFilename": {
            "win32": "raylib.dll",
            "linux": "libraylib.so.5.0.0",
            "darwin": "libraylib.5.0.0.dylib"
        },
        "libModules": [
            {
                "modName": "raylib",
                "jsonApiFilename": "input/rl500/raylib_api.json",
                "jsonMetadataFilename": "input/rl500/raylib_api.bind.json"
            },
            {
                "modName": "raymath",
                "jsonApiFilename": "input/rl500/rmath_api.json",
                "jsonMetadataFilename": null
            },
            {
                "modName": "rlgl",
                "jsonApiFilename": "input/rl500/rlgl.json",
                "jsonMetadataFilename": "input/rl500/rlgl_api.bind.json"
            }
        ]
    },
    "extensionLibraries": []
}
```

### `libName` Option

This is the identifier for the object created and returned by the library loading process. This name is not exported, but is used to do all the necessary binding stuff we read in the `ctypes` documentation. When binding more than one dll/so/dylib binary, it is important that the `libName` is unique for each one.

### `libKeyName` Option

This is the identifier for this Library when the _.raylib_ file is being used to load the binaries from another location. The _.raylib_ file is the mechanism used to load another binary instead of the one provided by the package. It contains the paths to the files and will be checked when raylibpy is loading. If the currently working directory at the loading time contains a _.raylib_ file, it will be verified and respective binary will be loaded instead.

### `libBasedir` Option

This may change in the future, but this option expects a list of file path pieces that, when joined, form the path where the binary to be loaded is located. It can be defined as a format string (not a f-string specifically). In this case, the only formatting argument passed is the directory where raylibpy's `__init__.py` is located.

### `includedModules` Option

This option is a list containing the modules that compose this library. Not all libraries might have more than one module, but this is the case for raylib itself; it has at least 3 modules: the core (raylib), raymath and rlgl. More modules can be added if the binary exposes them, but this option defines whether the module APIs gets added to the binding by being or not being in the list. This option is closely related to the `libModules` below.

### `binFilename` Option

This option is used to specify the filenames for the binaries to be loaded for each platform: `win32` for Windows, `linux` for Linux and `darwin` for MacOS. These names are joined with values in `libBasedir` to form the full path. This does not apply when using _.raylib_ files because they already contain the full (absolute) path.

### `libModules` Option

This option contains a list of module configuration objects, like the one below:

```json
{
    "modName": "raylib",
    "jsonApiFilename": "input/rl500/raylib_api.json",
    "jsonMetadataFilename": "input/rl500/raylib_api.bind.json"
}
```

#### `modName` Option

This is the module name. If this identifier is present in the list of `includedModules`, this module API will be added to the binding.

#### `jsonApiFilename` Option

This option indicates a relative path to the JSON file containing the module's API to be added to the binding.

#### `jsonMetadataFilename` Option

Similar to the above, this option indicates a relative path to the JSON file containing extra detailed information on how this module API should be wrapped. These extra information relates, for example, on what functions should be called by context managers, what functions can be decorated with `@property`, `@classmethod` etc. There is more. You can specify some transformations that should occur to arguments before they're passed to the foreign function or to the value they return.

## `extensionLibraries` Option

The `coreLibrary` option defines the configuration for the main library to be loaded. But you can also specify more than one library to be wrapped and this is where other libs can be configured. This option receives a list on library configuration objects like the one in `coreLibrary`. Let's suppose you have two binaries, one for _raygui_ and another for _physac_. This is where you can add them.
