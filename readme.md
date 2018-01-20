Python SimpleHTTPServer as an windows executable.    
https://github.com/maditnerd/WinSimpleHTTP/releases/download/1.1/web.exe

I always forgot which commands to run to use python simple http server, so I build it as an executable using pyinstaller.       
You can either 
* copy ***web.exe*** on the directory where it is needed 
* add ***web.exe*** in your [path](https://superuser.com/questions/143119/how-to-add-python-to-the-windows-path) to use it anywhere

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

```
web 42
```
Share the current folder on port 42

Source: https://docs.python.org/2/library/simplehttpserver.html
