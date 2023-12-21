<img align="left" src="/logo/raylibpy-256x256.png" width=256>

# Raylib Ctypes Binding Generator

A very basic raylib binding generator for Python

This tool generates Python bindings for the awesome C library [Raylib](https://github.com/raysan5/raylib).
It makes use of json files generated by the Raylib's header parser.

You can use this tool to generate a Raylib Python binding for you to tweak and use in your projects. It is very simple to use.

## Usage

Dowload and unzip it in a directory of you choosing, open the terminal, navigate
to the selected directory, and then:
```
$ python raylibpyctbg -help
```

to get a list of options you can pass to customize the bind generation

## Documentation

You can take a look on the [last generated documentation file](https://github.com/overdev/raylibpyctbg/blob/development/package/DOCS.md).

## Customization

With *raylibctbg* you can customize many aspects of the binding.

Options related to code style and naming conventions are:

- **Naming convention**: choose whether you want names the same as in C Raylib (C99)
  or following Python's PEP8 convention. You can choose which names you want to keep or change the casing: fields, parameters or functions.

- **Typing**: choose what type information to be added to names: as type hints or annotations.

- **Member functions**: choose whether you want some functions to be bound to structure types as
  methods, classmethods, staticmethods, properties or context managers.

- **Pretty-printing**: you can specify what gets returned by `__str__` and `__repr__`.

- **Attribute swizzling**: choose whether to add attribute swizzling to Vectors, Color and Rectangle types.

- **Context manager**: choose whether you want function pairs named `Begin*` and `End*` to form context 
  managers.

You can also customize library loading file paths/names, inclusion of extension headers and output filepath.

Many of these options can be tweaked via `input/rl500/global_config.json` file, but for deeper customizations you can check out the `input/rl500/raylib_api.bind.json` file.

### `Vector{2|3|4}` swizzling:

When added to the binding, it allows attributes to be joined and mixed in any order:

```python

vec2 = Vector2(1, 2, 3)
vec3 = vec2.xyx
vec4 = vec3.yyzx
vec3.xz = 5.0, 3.0
```

It also works for `Color`:
```python
col = Color(127, 63, 31, 255)
col2 = col.grab
col.rg = 255, 0
```

### A little bit of OOP:

When added to the binding, it binds some functions to be called as methods:


```python
# Load the sound; same as `sound = load_sound('my/sound/file')`
sound = Sound.load("my/sound/file")

# same as `if not is_sound_playing(sound)`
if not sound.is_playing():
	# Play it; same as `sound_play(sound)`
	sound.play()

# Unload from memory; same as `unload_sound(sound)`
sound.unload()
```

### RayMath

When added to the binding, it includes all functions in the raymath header.

### RLGL

When added to the binding, it includes all functions in the rlgl header.

### Documentation

You can generate API reference for all symbols wrapped by the generator. For some examples,
check out the markdown files in the _output_ folder.

## Using the python binding

Please, note that this binding does not include any raylib binary file. You can grab the binary 
from the C Raylib repo in the releases page. By default is expected the binary files to be
located the binding libpath.

Try to run the binding python file directly to know the exact path where the binary is expected
to be located or change the path with the generation options.
