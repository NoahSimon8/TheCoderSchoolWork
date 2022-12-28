import discord

thatswhatshesaid=["why is it so small",
            "it's small",
            "its small",
           "it is huge",
           "it's huge",
           "come inside",
           "that is really hard",
           "can you go all day long?",
           "you always left me satisfied",
           "why is it so big",
           "you already did me",
           "i can't stay on top of you",
           "can you make that straighter",
           "that job looks hard",
           "I need two men on this",
           "I want you to think about it long and hard",
           "you are hardly my first",
           "you're hardly my first",
           "lets put this matter to bed",
           "easy to get in, hard to rise up",
           "hold it in your mouth and swallow",
           "let's blow this party off",
            "let's just blow this party off"
           "why is this so hard",
           "get out of my nook",
           "when things get hard",
           "this is huge",
           "it squeeks when you bang it",
           "you were directly under her the entirer time",
           "come again",
           "you need to get back on top",
           "you screwed me",
           "give me a hard one",
           "don't make it harder than it was to",
           "you are making this harder",
           "im not saying it won't be hard",
           "you came",
           "that's big",
           "thats big",
           "put your mouth on that",
           "racism",
           "that's hard"
                  "thats hard",
            "that's really hard"]

hahafunny=["pee pee poo poo",
           "pp",
           "poopoo",
           "poo poo",
           "finn dumb",
           "finn's dumb",
           "l bad"]
no=["game?",
    "hello",
    "like?",
    "like it?"]
client=discord.Client()
@client.event
async def on_message(message):
    message.content=message.content.lower()
    if message.author== client.user:
        return
    for i in thatswhatshesaid:
        if i in message.content:
            await message.channel.send("That's what she said")
    for i in hahafunny:
        if i in message.content:
            await message.channel.send("Haha, Funny")

    for i in no:
        if i in message.content:
            await message.channel.send("No")


client.run("Nzg0Mjg3OTE0OTM0NjY1MjU3.X8nHCg.XuH5DoS63Z0ObWAEPr81i1Ek-uY")
