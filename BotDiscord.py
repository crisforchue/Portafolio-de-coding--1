from discord_easy_commands import EasyBot
import pyjokes
import discord
import random ##Todas las importanciones 

token = 'MTI4ODY3MjUwNzAzMjc2ODU1Ng.GELGCS.-xkUv8feP5sEK97tw2qm_9As-Z5cnSI-u58RGc'

jokes = pyjokes.get_jokes(language='en', category='all')
intents = discord.Intents.all()
bot = EasyBot(intents=intents)

def random_joke():
    joke = random.choice(jokes)
    return joke

bot.setCommand("!youtube", 'https://www.youtube.com')
bot.setCommand("!x", 'https://x.com/home')
bot.setCommand("!jokes", random_joke())

bot.run(token)

print("corriendo...")
