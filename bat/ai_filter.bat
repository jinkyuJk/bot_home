@Echo off
call "%HOMEPATH%\Anaconda3\Scripts\activate.bat" C:\Users\no100\Anaconda3\envs\py37_64
call python "%~dp0/../ai_filter.py" %1 %2
