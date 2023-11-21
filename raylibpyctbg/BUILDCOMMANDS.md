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
py -3.x raylibpyctbg -help
```

On Mac and/or Linux the command _probably_ is:

```
python3 raylibpyctbg -help
```

This command will cause a help message to be shown describing all options available:

```
raylibpy ctypes binding generator help

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
        --extension <value>             similar to --include but intended for standalone libs:
                                            <value> must be the lib name to be looked up in binding config json file
        --in <value>                    dirpath to load the json files from (defaults to 'input/'; must precede --include)
        --out <value>                   filepath to write the binding into
        --markdown <value>              filepath to write the api reference (Markdown format) into

```

Let's look more closely on each of these options

## Generation Options

### `-typeHint` or `-typAnnotate` Options

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


### `-snakecase` Option

By default the C naming convention will be kept in the binding code, but this option allows python naming convention to be applied where necessary.

Default:
```python
def IsKeyPressed(key):
    # ...
```

_Snakecased_ names:
```python
def is_key_pressed(key):
    # ...
```

### `-attribSwizzling` Option

This option causes some raylib types to be added a feature common in OpenGL Shading Language vectors. With this option `Vector2`, `Vector3`, `Vector4`, `Color` and `Rectangle` attributes can be mixed together as a single attribute:

```python
vec = Vector2(5.0, 7.0)
vec3 = vec.yxy  # make a new Vector3 by combining attributes 'x' and 'y' of 'vec' instance
```

### `-bindApi` Option

Raylib has many functions that relates to some of its structure types, like:

```python
def draw_model(model, position, scale, tint)
```

With this option, this function will be bound to the `Model` structure as a instance method:

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

Not all function will be bound to a type, only those that have a strong relation to a raylib structure. Besides that, functions that can be bound, will be bound as `@classmethod`, instance method, `@staticmethod` or `@property`.


### `-addContextManager` Option

This option is related to all pair of functions in raylib named with _begin_  and _end_. The functions

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


### `-addVectorMath` Option

This option adds special methods to `Vector2`, `Vector3` and `Vector4` that overloads the operators `+`, `-`, `*`, `/`, `//`, `==`, `!=`, unary `-`, and `abs(x)`. The overloaded operators support operands of same type or scalars (`int`s and `float`s). For multiplication, `Matrix` are also supported between two matrices and a vector and a matrix. This option requires the options `--include rmath` and `-attribSwizzling` to be added.


### `-pythonic` or `-spartan` Options

These options exist in order to simplify the generation command. Both of these have the effect of combining some of the options seen above. Also, they are mutually exclusive.

The `-pythonic` option includes all options that apply to the binding code coding conventions and features specific to Python, like naming convetion, object orientation, context manages and so on.

The `-spartan` option on the other hand includes all options that disable any attempt to pythonize the binding code, making it as close as possible to the C api.


### `-onlyDocs` Option

This option prevents the binding generator to generate binding code. This causes only the api documentation Markdown to be generated if the `--markdown <filename>` option is specified.


### `-no*` Options

Most of the generation options have a _negation_ counterpart. These options are prefixed wit `-no` and are intended to be used with `-spartan` or `-pythonic` options when specific option is wanted to be added to `-spartan` or removed from `-pythonic`.


### `--include <extension>` Option

This option is for optional api available in raylib but not exposed in `raylib.h`. These are _raymath_ and _rlgl_. `--included rmath` will include api in _raymath_ and `--include rlgl` will include api in _rlgl_.

Any other api to be included must have as a value the path to a _JSON_ file describing its components.


### `--out <filename>` Option

This option allow to specify the file where the binding code will be written to.


### `--markdown <filename>` Option

This option allow to specify the file where the binding api documentation will be written to.


### `--libBasedir <dirpath>` Option

This option allow to compose part of the path that indicates where the binaries to be loaded are located. The resultand path pointing to the apropriate binary will be mostly like the code below:

```python
# the default value for libBasedir is this
libBasedir = os.path.dirname(__file__)
# these values are resolved at runtime
platform = 'linux'
byteness = '32bit'
filename = 'libraylib.so.4.5.0'
path = os.path.join(libBasedir, platform, byteness, libfilename)
```


### `--win32LibFilename <name.ext>`, `--linuxLibFilename <name.ext>` and `--darwinLibFilename <name.ext>` Options

These options allow to override the file name of the binaries. Like `--libBasedir` option, these values will compose part of the path to the binary files. They need to be specified only if the binary file names are different from the default ones provided by C raylib.


### Binging generation: full pythonic

The command issued to generate raylibpy releases is the following:

```
py -3.10 raylibpyctbg --include rmath --include rlgl -pythonic -typeHint --out package/src/raylibpy/__init__.py --libBasedir "os.path.dirname(__file__), 'bin'" --markdown package/DOCS.md
```

It outputs change the template package in the `/package` directory. Once the binding is generated, a Python package can be built.


### Build wheel

The package is generated with the `build` command.

```
cd `package`
```

For a reason that's beyond me, this command requires internet connection.

```
py -3.10 -m build
```

Build will produce two files, a `.whl` and a `.tar.gz`.


#### Install

```
cd package/dist
```
then

```
py -3.10 -m pip install raylib_py-4.5.0-py3-none-any.whl --force-reinstall
```