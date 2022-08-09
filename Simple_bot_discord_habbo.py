import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time



bot = commands.Bot(command_prefix='!', description="ayuda bot") #Prefijo para el comando !sticker
bot.remove_command("help") # Borra el comando por defecto !help




####
#Programado Por Jose89fcb
#Twitter: twitter.com/jose89fcb
####
@bot.command()
async def habbo(ctx, habbonombre): #Comando "habbo"
    await ctx.message.delete() #Borramos el comando para no dejar sucio el chat xD
    await ctx.send("Generando avatar habbo...", delete_after=0)
    time.sleep(3) #Añadimos un tiempo para que sea borrado

   

   
    

    
    
   
    
    url = f"https://www.habbo.es/habbo-imaging/avatarimage?user={habbonombre}&action=std&direction=2&head_direction=2&gesture=std&size=l" #url
    imagen = Image.open(io.BytesIO(requests.get(url).content))

   
    
    


    
    


    print(f"Habbo Nombre: {habbonombre}") #Esto lo puedes quitar si quieres




    
    with io.BytesIO() as imagen_binary:
        imagen.save(imagen_binary, 'PNG')
        imagen_binary.seek(0)
       
        
        await ctx.send(file=discord.File(fp=imagen_binary, filename=f'keko_{habbonombre}.png'))

  
 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
     
bot.run('') 
