import requests
import os
from datetime import datetime

api_key = '1e1d0c2feedace87fd5a227d0dcd1da6'
location = input("Enter the CITY NAME")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

city_temp = ((api_data['main']['temp']) - 273.15)
weather_type = api_data['weather'][0]['description']
humid = api_data['main']['humidity']
wind_spd = api_data ['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("------------------------------------------------")
print("Weather Stats for -{} || {}".format(location.upper(),date_time))
print("-------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(city_temp))
print("current weather type :", weather_type)
print("current humidity:", humid,'%')
print("current wind speed :",wind_spd,"kmph")

print("==========================================")


txtlist = [city_temp,weather_type, humid,wind_spd,date_time]
with open("textfile.txt" , mode= 'w' ,encoding= 'utf-8') as f :  
    f.write("-----------------------------------------\n")
    f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    f.write("\n ------------------------------------------------------------- \n")
    f.write("Current temperature is: {:.2f} deg C\n".format(txtlist[0]))
    
    f.write("{},{} \n".format("Current weather desc  :" ,txtlist[1]))
    f.write("{},{},{} \n".format("Current Humidity      :",txtlist[2],"%"))
    f.write("{},{},{} \n".format("Current wind speed    :",txtlist[3],"kmph"))
    f.write("====================================================")
