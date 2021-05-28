# Importing Required Modules
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QMovie
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWebEngineWidgets import * 
from PyQt5.QtPrintSupport import * 
from getWeather import GetWeather
import asyncGetWeather
import asyncio
import about
import time
import mainUi
import datetime
import json
import sys
import os

# About Class
# Inhering the UserInterface from about.py
class aboutWindow(QtWidgets.QMainWindow, about.Ui_MainWindow):
	def __init__(self, parent=None):
		super(aboutWindow, self).__init__(parent)
		self.setupUi(self)
		# Setting the window title
		self.setWindowTitle("About Me")
		# Setting the icon
		self.setWindowIcon(QtGui.QIcon('mainLogo.png'))
		# Styling labels using StyleSheetSyntax (CSS)
		self.creator.setStyleSheet('font-family: Free sans; background-color: cyan')
		self.createdByLabel.setStyleSheet('font-family: Monospace;')
		self.twitter.setStyleSheet('font-family: Free sans; background-color: lightblue')
		self.twitterLabel.setStyleSheet('font-family: Monospace;')
		self.instagram.setStyleSheet('font-family: Free sans; background-color: deeppink')
		self.instagramLabel.setStyleSheet('font-family: Monospace;')
		self.githubLabel.setStyleSheet('font-family: Monospace;')
		self.github.setStyleSheet('font-family: Free sans; background-color: black; color: white')
		# Setting qmovie anim(label)
		self.movie = QMovie("neko2.gif")
		self.anim.setMovie(self.movie)
		self.movie.start()


# Engine Class
# Inheriting the UserInterface from mainUi.py
class WeatherApp(QtWidgets.QMainWindow, mainUi.Ui_MainWindow):
	def __init__(self, parent=None):
		super(WeatherApp, self).__init__(parent)
		self.setupUi(self)
		# Setting the window title
		self.setWindowTitle("Weather App")
		# Setting the icon
		self.setWindowIcon(QtGui.QIcon('mainLogo.png'))
		# Connecting the buttons with respective functions
		self.getCityName.pressed.connect(self.getWeatherData)
		self.aboutButton.pressed.connect(self.on_Button_clicked)
		# Setting the Main Window Heigh & Width
		self.setFixedHeight(519)
		self.setFixedWidth(872)
		# Setting the progressBar
		self.progressBar.setValue(0)
		# Setting the webEngineView
		self.webEngineView = QWebEngineView()
		# Adding the widget webEngineView to vbox object
		self.vbox.addWidget(self.webEngineView)
		# Setting the weather image display QLabel, position and initial Text
		self.weatherPic = QtWidgets.QLabel(self.centralwidget)
		self.weatherPic.setGeometry(QtCore.QRect(20, 250, 61, 61))
		self.weatherPic.setText("Waiting...")
		
	# Function to open About window that is connected above to aboutButton 
	def on_Button_clicked(self):
		aboutWin = aboutWindow(self)
		aboutWin.show()

	# Note "progressBarAnim" function is just here to create an illusion that things are working so the GUI feel more alive
	# This function doesn't represent any actual progress of the work
	# I did this to make it a bit less complex  
	# This function is called when the Button (Get Data) getCityName is pressed
	def progressBarAnim(self):
		# A simple loop to set the value of the progress bar
		for i in range(101):
			# Sleeping to slow down the loop a bit
			time.sleep(0.01)
			# Setting the value to the progress bar
			self.progressBar.setValue(i)

	# Getting the city name from the text box
	def getCityValue(self):
		print(self.cityName.toPlainText())
		print(type(self.cityName.toPlainText()))

	# Main function to get Weather Data
	def getWeatherData(self):
		# Checking if text box isn't empty then executing the tasks
		if(self.cityName.toPlainText() != ""):
			# Setting time
			self.setTime()
			# Setting city
			self.setCity()
			# Setting date
			self.setDate()
			# Changing the statusValue text
			self.statusValue.setText("Working")
			# Changing the background color of statusLabel
			self.statusLabel.setStyleSheet("background-color: cyan")
			# Getting the weather data providing API_KEY and City Name value ( also converting it to plain text) then executing the getWeather() function
			self.data = GetWeather("Get APIKEY from openweathermap.org", self.cityName.toPlainText()).getWeather()
			# If there's an error received from the getWeather() function
			if(self.data == "error"):
				self.statusValue.setText("City not found")
				self.statusLabel.setStyleSheet("background-color: red");
				print("BOOM YOU LOOKIN FOR AN ERROR ?")
			# If there's no error then proceed
			else:
				# Getting the longitude value from 'data'
				longitude = self.data['coord']['lon']
				# Getting the latitude value from 'data'
				latitude = self.data['coord']['lat']
				# Setting the map providing the respective data
				self.setMap(latitude, longitude)
				# Starting progress bar animation
				self.progressBarAnim()
				# Assinging the data to results variable
				results = self.data
				# Changing the statusValue text
				self.statusValue.setText("Done!")
				# Setting all the required values received from openweathermap.org API
				self.setAllValues()
				# Changing the statusLabel
				self.statusLabel.setStyleSheet("background-color: lightgreen");
				# Setting the weather Image
				self.setWeatherImage()
				# Printing some stuffs on the console
				print(results['weather'][0]['main'])
				print(type(results['weather'][0]['main']))
		# If text box is empty
		else:
			self.statusValue.setText("Enter City Name")
			self.statusLabel.setStyleSheet("background-color: yellow")

	# A function to set time
	def setTime(self):
		currentTime = datetime.datetime.now().strftime("%H H %M M %S S")
		self.timeValue.setText(currentTime)

	# A function to set city
	def setCity(self):
		if(self.cityName.toPlainText() != ""):
			self.cityValue.setText(self.cityName.toPlainText())
		else:
			self.cityValue.setText("Blank")

	# A function to set date
	def setDate(self):
		today = datetime.date.today()
		currentDate = today.strftime("%d/%m/%Y")
		self.dateValue.setText(currentDate)

	# A function to set map
	def setMap(self, latitude, longitude):
		# Setting the "Absolute" file path while providing the file name of the required html file
		file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "wind_map.html"))
		# Assigning the converted QUrl
		local_url = QUrl.fromLocalFile(file_path)
		# Converting longitude and latitude values to string and concatenating em
		windUrl = "https://www.windy.com/?" + str(longitude) + ',' + str(latitude);
		# This is a google map url (Removed in the final stage and replaced it with windy API)
		mapUrl = "https://www.google.com/maps/search/?api=1&query=" + str(latitude) + ',' + str(longitude)	
		# Setting up the data to be written in the data.json file that will be used by the javascript in wind_map.html to generate the map by the windy API
		api = 'data = \'[{"apikey" : "Get APIKEY from windy.com"'
		lon = '"longitude": %f' %(longitude)
		lat = '"latitude": %f}]\'' %(latitude)

		# Concatenating the mainData
		mainData = api + ',' + lon + ',' + lat

		# Overwriting the whole file with new data each time this function gets executed
		with open("data.json", "w") as write_file:
			write_file.write(mainData);
			write_file.close()	

		#print(mapUrl)
		#print(windUrl)
		#self.loadPage()
		qurl1 = QUrl(mapUrl)
		qurl2 = QUrl(windUrl)
		#self.webEngineView.setUrl(qurl2)
		#self.webEngineView.setHtml("./wind_html.html")
		self.webEngineView.load(local_url)
	

	# Setting the weather image according to the data received
	def setWeatherImage(self):
		sky = self.data['weather'][0]['main']
		if(sky == "Clouds"):
			self.weatherPic.setPixmap(QtGui.QPixmap("clouds.png"))
			self.weatherPic.setObjectName("weatherPic")
		elif(sky == "Rain"):
			self.weatherPic.setPixmap(QtGui.QPixmap("rain.png"))
			self.weatherPic.setObjectName("weatherPic")
		elif(sky == "Clear"):
			self.weatherPic.setPixmap(QtGui.QPixmap("sun.png"))
			self.weatherPic.setObjectName("weatherPic")

	# Using formula to convert the received data which is in kelvin to celsius
	def kelvinToCelsius(self, kelvin):
		# Formula K − 273.15 = °C
		return str(round((kelvin - 273.15), 1))

	# A function to set all received values
	def setAllValues(self):
		currentTemp = self.data['main']['temp'];
		maxTemp = self.data['main']['temp_max'];
		minTemp = self.data['main']['temp_min'];
		feelsLikeTemp = self.data['main']['feels_like'];
		humidity = self.data['main']['humidity'];
		pressure = self.data['main']['pressure'];
		forecast = self.data['weather'][0]['description'];
		windSpeed = self.data['wind']['speed'];
		cloudiness = self.data['clouds']['all'];

		maxCelsius = self.kelvinToCelsius(maxTemp);
		minCelsius = self.kelvinToCelsius(minTemp);
		currentCelsius = self.kelvinToCelsius(currentTemp);
		feelsLikeCelsius = self.kelvinToCelsius(feelsLikeTemp);

		self.currentTemp.setText(str(currentCelsius)+" °C");
		self.currentTemp.setStyleSheet('font-family: Mono')
		self.tempMax.setText(str(maxCelsius)+" °C");
		self.tempMin.setText(str(minCelsius)+" °C");
		self.feelsLike.setText(feelsLikeCelsius+" °C");
		self.feelsLike.setText(
		self.humidity.setText(str(humidity)+"%");
		self.pressure.setText(str(pressure)+" hPa");
		self.forecast.setText(forecast);
		self.windSpeed.setText(str(windSpeed)+" m/s");
		self.cloudiness.setText(str(cloudiness)+"%");

# Main function that will execute the app
def main():
	app = QApplication(sys.argv)
	app.setApplicationName("Weather App QtPy")
	form = WeatherApp()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
