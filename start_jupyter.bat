@echo off
echo ============================================
echo   Activating rise_env and starting Jupyter
echo ============================================

REM Activate venv
call rise_env\Scripts\activate

REM Run Jupyter directly in this window
jupyter notebook

REM Once Jupyter stops (via Ctrl+C or Quit button), deactivate
call deactivate

echo ============================================
echo   Jupyter stopped, rise_env deactivated
echo ============================================

pause