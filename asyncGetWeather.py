# WARNING: A Prototype testing module
import aiohttp
import asyncio

async def asyncWeather(api_key, city_name):

	async with aiohttp.ClientSession() as session:
		baseUrl = 'http://api.openweathermap.org/data/2.5/weather?'
		mainUrl = baseUrl + "q=" + city_name + "&appid=" + api_key
		async with session.get(mainUrl) as resp:
			weatherData = await resp.json()
			if weatherData["cod"] != "404":
				return weatherData;
  
			else:
				return "error"

