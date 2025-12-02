@echo off
echo ============================================
echo   Setting up Python 3.11.9 venv + RISE
echo ============================================

REM Upgrade pip, wheel, setuptools (system-wide)
python -m pip install --upgrade pip wheel setuptools

REM Create virtual environment with Python 3.11
py -3.11 -m venv rise_env

REM Activate venv
call rise_env\Scripts\activate

REM Install requirements
pip install -r requirements.txt

REM Enable RISE in Jupyter
jupyter-nbextension install rise --py --sys-prefix
jupyter-nbextension enable rise --py --sys-prefix

echo ============================================
echo   Setup complete! Use start_jupyter.bat next.
echo ============================================
pause
