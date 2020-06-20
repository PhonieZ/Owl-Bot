# bot.py
# Made by PhonieZ Dev
# You also need to get the dotenv and discord library for this to work
#importing stuff here
import os
import random
import discord
from dotenv import load_dotenv
load_dotenv()
#put the discord bot token in the .env file, so it works
TOKEN = os.getenv('DISCORD_TOKEN')
#defining stuff here
client = discord.Client()
version = "1.1"
congacount = 1
#these are the events
@client.event
async def on_ready():
    #this for debugging
    print(f'{client.user} is ready to owl around.')
    #put the channel id in the brackets,so it works
    channel = client.get_channel()
    #announcing its presence, also noting version
    await channel.send('coo coo, owl is in town, again, owl v'+version+" to be exact")
#whena  member joins, owl sends thema  greeting,ez
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'coo coo {member.name},i owl, welcome to my place,i live in parliament, coo coo'
        )
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    owlyness = ['DID SOMEBODY SAY OWL?','O W L','coo coo , owl is awoke','coo?','Owl, what owl?','Owl is here, no drink beer,only coo, i can rhyme ish oo','huh?'
    ]
    angriness = ['no u','COOOOOOOOOOOOOOOOO YOU MAKE ME SAD,COOOOOOOOOOOOOOOOOOOOOOOO','well i am off to hang myself, actually, nah, i go coo','why','owl sad','N O'
    ]
    sadiness = ['yes','no','coo?','OWL','Y E S','N O','dunno i owl','wha?']
    #if you say owl, you can say any other words to get certain responses, also it case insensitive, so now it more human like and cooler.
    if "owl".lower() in message.content.lower():
        if "kill".lower() in message.content.lower() and "yourself".lower() in message.content.lower():
            response = random.choice(angriness)
            await message.channel.send(response)
        elif "are".lower() in message.content.lower() and "you".lower() in message.content.lower() and "ok".lower() in message.content.lower():
            response = random.choice(sadiness)
            await message.channel.send(response)
        elif "shut".lower() in message.content.lower()and "up".lower() in message.content.lower():
            response = "no, you shutup,rude"
            await message.channel.send(response)
        elif "help".lower() in message.content.lower() and "me".lower() in message.content.lower() or "help".lower() in message.content.lower():
            response = "ya know what, just ask my owner for help, i improved now."
            await message.channel.send(response)
        else:
            response = random.choice(owlyness)
            await message.channel.send(response)
        #this conga feature, if u want u can submit a working bit for it, cuz it doesn't work for me
        #if "conga".lower() in message.content.lower() and "time".lower() in message.content.lower():
            #if congacount == 1:
                #response = "conga conga conga!"
                #await message.channel.send(response)
                #congacount = congacount + 1
            #else:
                #if "conga".lower() in message.content.lower():
                    #response = "conga conga conga!"
                    #await message.channel.send(response)
                    #congacount = congacount + 1
                #else:
                    #response = "aww, no more conga :( ,well at least we kept the conga going for "+str(congacount)+" congas, or whatever."
                    #await message.channel.send(response)
                    #congacount = 0
    #i gonna reimplement this or remove this later
    #elif message.content == 'raise-exception':
        #raise discord.DiscordException
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


    
client.run(TOKEN)
