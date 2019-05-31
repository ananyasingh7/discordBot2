import discord
import mysql.connector
import time
import requests, json 
from discord.ext import commands

# Function to convert temperature 
def Kelvin_to_Fahrenheit(K): 
  #(K − 273.15) × 9/5 + 32      
  return (32 + (9.0/5.0) * (K-273.15))

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.command()
async def weather(ctx):
  #OpenWeatherMap
  api_key = "OPENWEATHERMAP API GOES HERE"
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  city_name = "Newark"
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  response = requests.get(complete_url)
  x = response.json()
  y = x["main"]
  current_temperature = y["temp"]
  z = x["weather"]
  weather_description = z[0]["description"]
  temp = Kelvin_to_Fahrenheit(current_temperature)
  await ctx.send("The current temperature is: " + str(temp) + " and the weather is: " + str(weather_description))



@client.command()
async def points(ctx, *, arg):
  s = "SELECT points from pointsDB.points WHERE name='"+arg+"'"
  str(s)
  cnx = mysql.connector.connect(host='localhost', user='admin', password='password', database='pointsDB')
  cursor = cnx.cursor(buffered=True)
  cursor.execute(s)
  result = cursor.fetchall()
  await ctx.send("Hey " + str(arg) + ", you have these many points for the semester: " + str(result[0][0]))
  cnx.commit()
  cnx.close()
  


client.run(DISCORD_TOKEN GOES HERE)
