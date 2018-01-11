Python SimpleHTTPServer as an windows executable.    

I always forgot which commands to run to use python simple http server, so I build it as an executable using pyinstaller.       
You can either 
* copy ***web.exe*** on the directory where it is needed 
* add ***web.exe*** in your path

Compile:
```
pip install pyinstaller
pyinstaller web.py --onefile
```

Usage:
```
web
```
Share the current folder on port 8000.

https://github.com/maditnerd/WinSimpleHTTP/releases/download/1.0/web.exe
