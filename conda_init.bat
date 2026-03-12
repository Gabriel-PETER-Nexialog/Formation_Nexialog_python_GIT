@echo off
CALL C:\Users\%USERNAME%\anaconda3\Scripts\activate.bat
:: ==============================================
::  Conda Environment Management Script
:: ==============================================

SETLOCAL ENABLEDELAYEDEXPANSION

:: Default variables
SET "ENV_NAME=default_env"
SET "REQUIREMENTS_FILE=requirements.txt"
SET "ENV_FILE=environment_development.yaml"
SET "PYTHON_VERSION=3.12.11"

echo ----------------------------------------
set /p ENV_NAME= Enter the Conda environment name:
set /p PYTHON_VERSION= Enter the Python version (e.g., 3.12.11):

echo ----------------------------------------
echo [1] Checking if the environment "%ENV_NAME%" exists...
CALL conda env list | FINDSTR /C:"%ENV_NAME%" >nul

:: If the environment exists, remove it
IF %ERRORLEVEL%==0 (
    echo [2] Environment "%ENV_NAME%" already exists. Removing...
    CALL conda deactivate >nul 2>nul
    CALL conda env remove -n %ENV_NAME% -y
) ELSE (
    echo [2] Environment "%ENV_NAME%" does not exist.
)

:: Check if the YAML file exists
IF EXIST "%ENV_FILE%" (
    echo [3] YAML file "%ENV_FILE%" found. Verifying environment name...

    :: Extract the 'name:' line from YAML
    FOR /F "tokens=2 delims=:" %%A IN ('FINDSTR /B "name:" "%ENV_FILE%"') DO SET YAML_ENV_NAME=%%A
    :: Remove leading/trailing spaces
    SET YAML_ENV_NAME=!YAML_ENV_NAME:~1!

    IF /I "!YAML_ENV_NAME!"=="%ENV_NAME%" (
        echo [4] YAML environment name matches "%ENV_NAME%". Creating environment from YAML...
        CALL conda env create -f "%ENV_FILE%" -n "%ENV_NAME%"

    ) ELSE (
        echo [4] YAML environment name "!YAML_ENV_NAME!" does not match "%ENV_NAME%". Skipping YAML creation.
        echo [5] Creating a new environment with Python %PYTHON_VERSION%...

        CALL conda create -n "%ENV_NAME%" python=%PYTHON_VERSION% -y
        CALL conda activate %ENV_NAME%

        IF EXIST "%REQUIREMENTS_FILE%" (
            echo [6] Installing dependencies from "%REQUIREMENTS_FILE%"...
            CALL pip install -r "%REQUIREMENTS_FILE%"
        ) ELSE (
            echo [6] File "%REQUIREMENTS_FILE%" not found. No dependencies installed.
        )
    )
) ELSE (
    echo [3] YAML file "%ENV_FILE%" not found. Creating a new environment...
    CALL conda create -n "%ENV_NAME%" python=%PYTHON_VERSION% -y
    CALL conda activate %ENV_NAME%

    IF EXIST "%REQUIREMENTS_FILE%" (
        echo [4] Installing dependencies from "%REQUIREMENTS_FILE%"...
        CALL pip install -r "%REQUIREMENTS_FILE%"
    ) ELSE (
        echo [4] File "%REQUIREMENTS_FILE%" not found. No dependencies installed.
    )
)

:: Reactivate environment
echo [7] Final activation of environment "%ENV_NAME%"...
CALL conda activate %ENV_NAME%

:: Export environment to YAML
echo [8] Exporting environment to "%ENV_FILE%"...
CALL conda env export --from-history > "%ENV_FILE%"

echo ----------------------------------------
echo  Environment "%ENV_NAME%" is ready to use!
echo  YAML file saved as "%ENV_FILE%"
echo ----------------------------------------
echo [INFO] : You need to pick the env compiler for our IDE (On Pycharm go to the settings)

cmd /k

REM Easter EGGS 🐣 : Congratulations 🎉 you find the easter eggs !! Enjoy and send the Emoji 🐱‍💻 to : www.linkedin.com/in/gabriel-peter-dev-logiciel  🎉🎉🎉