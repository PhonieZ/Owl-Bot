# bot.py
# Made by PhonieZ Dev
import os
import random
import discord
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is ready to owl around.')
    channel = client.get_channel(channelidhere) 
    await channel.send('coo coo, owl is in town, again')
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
    if message.content == 'owl':
        response = random.choice(owlyness)
        await message.channel.send(response)
    elif message.content == 'go kill yourself owl':
        response = random.choice(angriness)
        await message.channel.send(response)
    elif message.content == 'are you ok owl':
        response = random.choice(sadiness)
        await message.channel.send(response)
    elif message.content == 'shutup owl':
        response = "no, you shutup,rude"
        await message.channel.send(response)
        
    elif message.content == 'help me owl':
        response = "ok then fine, you can ask me if i am okay by saying 'are you ok owl', tell me to kill myself by saying 'go kill yourself owl' and say 'owl' for, well owliness,'shutup owl' if you are rude, and 'help me owl' for help, now let me sleep"
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


    
client.run(TOKEN)
