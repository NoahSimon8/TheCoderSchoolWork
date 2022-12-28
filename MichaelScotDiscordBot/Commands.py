import discord
from discord.ext import commands
client=commands.Bot(command_prefix="$")
@client.command()
async def repeat(ctx, *arg):
    print(ctx.author)
    print(ctx.message) #Info about message
    print(ctx.guild)
    str=""
    for i in arg:
        str+=i+" "
    if str!="":
        await ctx.send(str)


client.run("Nzg0Mjg3OTE0OTM0NjY1MjU3.X8nHCg.XuH5DoS63Z0ObWAEPr81i1Ek-uY")
