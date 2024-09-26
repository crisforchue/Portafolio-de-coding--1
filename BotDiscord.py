from discord_easy_commands import EasyBot
import pyjokes
import discord
import random ##Todas las importanciones 

token = 'MTI4ODY3MjUwNzAzMjc2ODU1Ng.GELGCS.-xkUv8feP5sEK97tw2qm_9As-Z5cnSI-u58RGc'

jokes = pyjokes.get_jokes(language='en', category='all') #Va a darnos una lista de chistes para el usuario
intents = discord.Intents.all() #Nos da varios intentos para usar el bot
bot = EasyBot(intents=intents) #Crea una instancia para el robot

def random_joke():
    joke = random.choice(jokes)
    return joke #Nos da una broma random cada vez (no funciona, revisar)

bot.setCommand("!youtube", 'https://www.youtube.com') #Cuando se nos da el comando "youtube", nos devolvera el link a la pagina principal de youtube. lo mismo con los otros comandos.
bot.setCommand("!x", 'https://x.com/home')
bot.setCommand("!jokes", random_joke())

bot.run(token) #Comienza a correr el bot
