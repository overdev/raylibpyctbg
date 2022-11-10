# Raylib Package Template

This package template allows you to build wheel files for local installation.

## Getting your package build-ready

As a template this package is missing the important stuff, like path configurations, the generated binding code and the binary files.

To get this done, please, follow the steps below.

### 1. Generate the binding code with your options and the right paths.

The first thing we need to set right is the path for the lib binaries.

The package is configured to allow 32 and 64 bit binaries to be loaded according to the system's architecture.

Looking to the package folder structure, you see the following disposition:

```
package/
    src/
        raylibpy/
            bin/
                32bit/
                64bit/
            __init__.py
    LICENCE
    pyproject.toml
    README.md
```

To set the path, make sure your Python binding is generated via CLI with the following congif:

```
--libBase "os.path.dirname(__file__), 'bin'"
```

Alternatively, you can change the `input/raylib_api.bind.json` file to set this value directly:

```json
{
  "CONFIG": {
    "libBasedir": "os.path.dirname(__file__), 'bin'",
    // other options..
  }
  // other stuff...
}
```

This will ensure the correct library to be loaded regardless of the platform and architecture.

Having the binding code generated, put a copy of the file in the `package/src` folder and
rename it to `__init__.py`

### 2. Copying the binary files

This repository does not hold any raylib binary, so you're expected to grab them in the
C [Raylib](https://github.com/raysan5/raylib)'s reposity.

With the binaries in _hand_, just put them in the `package/src/bin/*` folder respective to the
system architecture.

### 3. Building the python wheel file

To be able to build without troubles, is might be necessary to get Pip up to date.

First, let's upgrade Pip:

```
py -m pip install --upgrade pip
```

then:

```
py -m pip install --upgrade build
```

then, in the terminal, change to the `package/` where `pyproject.toml` is located and:

```
py -m build
```

When the build in done, you see a new foder, _dist/_, under `package/src`.

Inside this folder there are 2 files, a _*.tar.gz_ and a _*.whl_.

### 4. Installing the package

With the wheel package in _hands_, you're ready to install it with Pip:

```
py -m pip install path/to/the/wheel-file.whl
```

That's it! I hope you enjoy making games and whatnot with _raylibpy_!

You can learn more on creating python packages in the [Python Packaging site](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
