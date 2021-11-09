import discord
import random
from discord import channel
from discord.ext import commands
from discord import DMChannel

client = commands.Bot(command_prefix="%")

@client.event
async def on_ready():
    print("Logged in as " + client.user.name)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='To Your Words'))


#Sends an error message when a nonexistant command is run
@client.event
async def on_command_error(ctx, error):
    embed=discord.Embed(title="Error", description="This command does not exist or you do not have nessesary permissions. Use the help command if you need assistance.", color=discord.Color.red())
    await ctx.send(embed=embed)

@client.command(
    help="Set the channel ID that the social credit notices are reported to.",
    brief="Set the reporting channel for sc"
)
@commands.has_permissions(administrator=True)
#This command lets anyone with the specified role to change the reporting channel ID
async def setchannelID(ctx, cID):
        global channelId
        channelId=int(cID)
        await ctx.channel.send("The reporting channel ID for infractions is now set as: "+cID)

#These are all the phrases that can trigger a response, copy and paste within the function and change the wording to add more
@client.event
async def on_message(message):
    if message.content.startswith('china commits'):
        channel = client.get_channel(channelId)
        content=message.content
        await message.channel.send('**MESSAGE REPORTED**')
        await channel.send('ILLEGAL KEYWORD DETECED BY:')
        await channel.send(message.author)
        await channel.send("MESSAGE: "+content)

    if message.content.startswith('taiwan is a country'):
        channel = client.get_channel(channelId)
        content=message.content
        await message.channel.send('**MESSAGE REPORTED**')
        await channel.send('ILLEGAL KEYWORD DETECED BY:')
        await channel.send(message.author)
        await channel.send("MESSAGE: "+content)

    if message.content.startswith('something happened in tianamen square in 1989'):
        channel = client.get_channel(channelId)
        content=message.content
        await message.channel.send('**MESSAGE REPORTED**')
        await channel.send('ILLEGAL KEYWORD DETECED BY:')
        await channel.send(message.author)
        await channel.send("MESSAGE: "+content)

    if message.content.startswith('something happened in tianamen square'):
        channel = client.get_channel(channelId)
        content=message.content
        await message.channel.send('**MESSAGE REPORTED**')
        await channel.send('ILLEGAL KEYWORD DETECED BY:')
        await channel.send(message.author)
        await channel.send("MESSAGE: "+content)

    if message.content.startswith('david sucks'):
        channel = client.get_channel(channelId)
        content=message.content
        await message.channel.send('**MESSAGE REPORTED**')
        await channel.send('ILLEGAL KEYWORD DETECED BY:')
        await channel.send(message.author)
        await channel.send("MESSAGE: "+content)

    if message.content.startswith('david is great'):
        channel = client.get_channel(channelId)
        content=message.content
        await message.channel.send('**POSITIVE MESSAGE REPORTED**')
        await channel.send('POSITIVE KEYWORD DETECED BY:')
        await channel.send(message.author)
        await channel.send("MESSAGE: "+content)

    if message.content.startswith('i love david'):
        channel = client.get_channel(channelId)
        content=message.content
        await message.channel.send('**POSITIVE MESSAGE REPORTED**')
        await channel.send('POSITIVE KEYWORD DETECED BY:')
        await channel.send(message.author)
        await channel.send("MESSAGE: "+content)

    if message.content.startswith('hail the ccp'):
        channel = client.get_channel(channelId)
        content=message.content
        await message.channel.send('**POSITIVE MESSAGE REPORTED**')
        await channel.send('POSITIVE KEYWORD DETECED BY:')
        await channel.send(message.author)
        await channel.send("MESSAGE: "+content)

    if message.content.startswith('hail the CCP'):
        channel = client.get_channel(channelId)
        content=message.content
        await message.channel.send('**POSITIVE MESSAGE REPORTED**')
        await channel.send('POSITIVE KEYWORD DETECED BY:')
        await channel.send(message.author)
        await channel.send("MESSAGE: "+content)

    if message.content.startswith('china is the best'):
        channel = client.get_channel(channelId)
        content=message.content
        await message.channel.send('**POSITIVE MESSAGE REPORTED**')
        await channel.send('POSITIVE KEYWORD DETECED BY:')
        await channel.send(message.author)
        await channel.send("MESSAGE: "+content)

    if message.content.startswith('hail david'):
        channel = client.get_channel(channelId)
        content=message.content
        await message.channel.send('**POSITIVE MESSAGE REPORTED**')
        await channel.send('POSITIVE KEYWORD DETECED BY:')
        await channel.send(message.author)
        await channel.send("MESSAGE: "+content)

    await client.process_commands(message)
        
client.run('BOT TOKEN HERE')
