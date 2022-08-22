# Raylib Ctypes Binding Generator

A very basic raylib binding generator for Python

This tool generates Python bindings for the awesome Raylib. It makes use of 
json files generated by the Raylib's header parser.

## Usage

Dowload and unzip it in a directory of you choosing, then, in the command line:
```
$ python path\to\raylib_wrapper path\to\raylib_api.json path\to\output\python\file
```

## Customization

You can then customize the output to fit any need you may have. One default
customization that this wrapper includes is the `Vector[2|3|4]` swizzling:

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

## Using the python binging

Please, note that this binding does not include any raylib binary file. You can grab the binary 
from the C Raylib repo in the releases page. By default is expected the binary files to be
located inside '/bin/32bit' or '/bin/64bit' relative to where the python binding is located.

Then, you can just:
```python
import raylib as rl
```