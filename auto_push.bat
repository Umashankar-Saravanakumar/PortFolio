@echo off
setlocal
echo ========================================================
echo Auto Git Push Script
echo ========================================================

:: Check if git is installed
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo Git could not be found. Please ensure Git is installed and in your PATH.
    pause
    exit /b 1
)

:: Get commit message
set "msg=%~1"
if "%msg%"=="" (
    set "msg=Auto commit: %date% %time%"
)

echo Adding files...
git add .

echo Committing files...
git commit -m "%msg%"

echo Pushing to repository...
git push

if %errorlevel% equ 0 (
    echo.
    echo ========================================================
    echo SUCCESS! Changes pushed successfully.
    echo ========================================================
) else (
    echo.
    echo ========================================================
    echo ERROR: Failed to push changes. Check the output above.
    echo ========================================================
)

endlocal
pause
