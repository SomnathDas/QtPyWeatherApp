# QtPy WeatherApp
>A Simple Demonstration of using PyQT and APIs in Python
> 
<div align="center">
<a href="https://ibb.co/7yJ3799"><img src="https://i.ibb.co/s3vTLBB/Screenshot-from-2021-05-28-12-08-20.png" alt="Screenshot-from-2021-05-28-12-08-20" border="0"></a>
<a href="https://ibb.co/3rTYY7J"><img src="https://i.ibb.co/Rvg4495/Screenshot-from-2021-05-28-12-09-15.png" alt="Screenshot-from-2021-05-28-12-09-15" border="0"></a>
</div><br/>
<br/>

*Make sure you have `PyQT5`, `Pyuic5`, `aiohttp-3.7.4.post0`, `request`, `` installed in your system before using this*

# Install some required packages
Paste the command in the terminal or powershell
```cmd
> sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev python-tk python3-tk tk-dev pyqt5 aiohttp-3.7.4.post0 request pyuic5
```

# GET API KEYS

## Openweathermap [FREE]
1. <a href="https://openweathermap.org/api" target="_blank"> Get API_KEY from Open Weather Map </a>
2. Paste your API_KEY on *line 111* in the file named "app.py" for openweathermap

## Windy [FREE]
1. <a href="https://api.windy.com/" target="_blank"> Get API_KEY from Windy </a>
2. Paste your API_KEY on *line 174* in the file named "app.py" for windy

# Usage

### Running the app
```cmd
python3 app.py
```

### Compiling the .ui file into .py
```cmd
pyuic5 file_name.ui -o file_name.py
```
