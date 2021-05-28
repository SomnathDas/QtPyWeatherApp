# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}  

#base_url = "http://api.openweathermap.org/data/2.5/weather?"

# import required modules
import requests
import json
import asyncio

class GetWeather:
	def __init__(self, api_key, city_name):
		self.apiKey = api_key
		self.baseUrl =  "http://api.openweathermap.org/data/2.5/weather?"
		self.cityName = city_name;
		self.mainUrl = self.baseUrl + "q=" + self.cityName + "&appid=" + self.apiKey
	
	def getWeather(self):
		# Sending GET Request to fetch the data
		response = requests.get(self.mainUrl)
		# Converting the data into JSON format
		weatherData = response.json()
		# Checking if there's an error
		if weatherData["cod"] != "404":
			# If NO error then returning the weather data
			return weatherData;
  
		else:
			# If there's an error, returning a string with value of "error"
			return "error"

