# Raylib CTypes Binding Generator Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [3.0.0]

Third version of the binding generator. The generated binding code is far superior to last version, it keeps the organization between libraries and modules, each thing is its proper place.

The new generator misses a few things, like documentation generation. This is intended to be done in a post stable release.

### Added

- A specialized class to write python code and get rid of excessive use of templates and format strings
- Ability to bind more than one library in a single binding
- rlgl_api.bind.json (binding extra information)
- argument/return tranformation customization per function in `*.bind.json`
- raylibpyctbg can now generate the binding, build the package and install it for you with a single command (make sure you pip installed **build** first)

### Changed

- Less use of templates, which reduced code complexity a lot
- Moved customization options to a config file (`input/rl500/global_config.json`)
- Moved helper classes to a separate source file (`core.py`)
- Updated the `*.bind.json` files to include better information on how to wrap stuff
- Better type annotation/hinting

### Removed

- Almost all command line options

### Fixed

- Functions with varargs now work (with some requirements)
- Structural problem preventig third party extensions (like physac) from being wrapped.
- Better return values for functions returning pointers: the return values are cast to array, instead of added to `list`s.


## [2.0.0] - 2022-11-07

Rewrite of the generator to get things a little more organized, but the code is still very messy (specially one week after I wrote it).

### Changed

- Move some constants to proper places.
- Less messier code

### Added

- Customization to the code generation
- Abuse of command line options


## [1.0.0] - 2022-08-29

First write of the generator based on the binding data provided by Raymon's (C Raylib Author) parser.

### Added

Mostly everything. The code was written in the hurry of excitement.
