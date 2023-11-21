echo off
if "%~1"=="" (
    echo "No Python version provided; defaulting to 3.10"
    set pyversion=3.10
) else (
    set pyversion=%1
)
if "%~2"=="" (
    echo "No target Raylib version provided; defaulting to 5.0.0"
    set rlversion=5.0.0
) else (
    set rlversion=%2
)

echo "GENERATING RAYLIB BINDING CODE"
py -3.10 raylibpyctbg --in input/rl500 --include rmath --include rlgl -pythonic -typeHint --out package/src/raylibpy/__init__.py --libBasedir "os.path.dirname(__file__), 'bin'" --markdown package/DOCS.md
cd package
echo "BUILDING PACKAGE"
py -m build
if "%~3"=="install" (
    cd dist
    echo "INSTALLING"
    py -%pyversion% -m pip install raylib_py-%rlversion%-py3-none-any.whl
) else (
    if "%~3"=="reinstall" (
        cd dist
        echo "REINSTALLING"
        py -%pyversion% -m pip install raylib_py-%rlversion%-py3-none-any.whl --force-reinstall
    ) else (
        echo "Package will not be [re]installed. Add 'install' to force package [re]installation"
    )
)

cd ..