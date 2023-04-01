
### Binging generation: full pythonic

```
py -3.10 raylibpyctbg --include rmath --include rlgl -pythonic -typeHint --out package/src/raylibpy/__init__.py --libBasedir "os.path.dirname(__file__), 'bin'" --markdown package/DOCS.md
```

### Build wheel

```
cd `package`
```
then

```
py -3.10 -m build
```

#### Install

```
cd package/dist
```
then

```
py -3.10 -m pip install raylib_py-4.5.0-py3-none-any.whl --force-reinstall
```