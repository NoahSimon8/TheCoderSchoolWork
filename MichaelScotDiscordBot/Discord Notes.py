"""
commands with messages:
.content  (The message that was sent)
.channel  (the channel it was sent in)
.author   (The person who send the message)
.send((insert message here)) (type and send)
.purge(limmit=1)  (Delete message)
Example:
if message.content.startswith("hello"):
    await message.channel.send("Hello "+ str(message.author))
    if str(message.author)=="BotsRWalrus.f#3190":
        await message.channel.send("YOOO!!!!")

"""


"""
Notes on Commands:
from discord.ext import commands

"""