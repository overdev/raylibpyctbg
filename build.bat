echo "GENERATING RAYLIB BINDING CODE"
py -3.10 raylibpyctbg input/rl500/global_config.json package/src/raylibpy/__init__.py

echo "BUILDING PACKAGE"

cd package
py -m build

echo "[RE]INSTALLING"
cd dist
py -3.10 -m pip install raylib_py-5.0.0b2-py3-none-any.whl --force-reinstall

cd ..\..

echo "DONE."
