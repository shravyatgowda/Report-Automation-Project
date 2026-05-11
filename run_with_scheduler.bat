:: For PROD environemnet
:: Warning: when setting the system variable, use double quote "" if there are space in the value

if exist "C:\Working Directory\Review Report Automation\" (
    cd C:\Working Directory\ Review Report Automation\
    SET log_file="C:\Working Directory\0_scheduler_log\Business Review Report Automation.txt"
    call C:\ProgramData\miniconda3\Scripts\activate.bat
    call activate Report_Automation
)

:: Shared commands
python run_with_failure_msg.py >> %log_file%
@REM Pause
