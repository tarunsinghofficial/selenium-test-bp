@echo off
REM Cross Browser Testing Script (Chrome & Firefox)

set PYTHON_EXE=.venv\Scripts\python.exe

echo Cross Browser Testing
echo ============================
echo.

if "%1"=="test-local" goto :test_local
if "%1"=="test-grid" goto :test_grid
if "%1"=="status" goto :check_status

:show_help
echo Usage: cross_browser_test.bat [command]
echo.
echo Commands:
echo   test-local    - Run Chrome+Firefox tests locally
echo   test-grid     - Run Chrome+Firefox tests on Selenium Grid
echo   status        - Check Selenium Grid status
echo.
goto :end

:check_status
echo Checking Grid status...
curl -s http://localhost:4444/status | %PYTHON_EXE% -m json.tool
goto :end

:test_local
echo Running cross browser tests locally (Chrome, Firefox).
echo Make sure demo app is running at http://localhost:8000
set HEADLESS=1
set USE_GRID=0
%PYTHON_EXE% -m pytest tests/test_cross_browser.py -v -s
goto :end

:test_grid
echo Running cross browser tests on Selenium Grid (Chrome, Firefox).
echo Start Grid with: java -jar selenium-server-4.35.0.jar standalone
set HEADLESS=1
set USE_GRID=1
set GRID_URL=http://localhost:4444
%PYTHON_EXE% -m pytest tests/test_cross_browser.py -v -s
goto :end

:end
echo.