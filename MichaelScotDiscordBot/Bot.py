from DunderBowlClasses import*
import time
from discord.ext import commands
Dundies=False
Bowl=False
DundiePlayers=[]

BowlPlayers=[]
BowlClasses=["dwight", "jim", "stanley", "kevin"]
BowlPhase=0

client=commands.Bot(command_prefix="$")

@client.command()
async def helpplease(ctx):
    await ctx.send('Welcome to the Michael Scott bot! \nThis bot contains funny jokes like, "Thats what she said!", and games. Thats pretty much it \nCommands start with $ because yes, Dunder Miflin is a business. They include: \ndundies \ndunderbowl! ')



@client.command()
async def dunderbowl(ctx):
    global Bowl
    await  ctx.send('WELCOME TO THE DUUUNNNDDDEEERR BOOOWWWLLL!\nWhat is the DUNDER BOWL you may ask? Well, its the newest, hottest, turn based attack game of this discord server. \nTo get started, we need two competitors. Choose an Office Worker (class) from the following to join the fight (Note: Do not select same person twice): \nDwight, Jim, Stanley, Kevin')
    Bowl=True



@client.command()
async def dundies(ctx):
    global Dundies
    await ctx.send("The Dundies have begun,")
    time.sleep(1)
    await ctx.send("oh what cheer!")
    time.sleep(1)
    await ctx.send("Time for a game,")
    time.sleep(1)
    await ctx.send("in this fine year!")
    time.sleep(1)
    await ctx.send("To join the games,")
    time.sleep(1)
    await ctx.send('you should type "Here Here!"')
    time.sleep(1)
    await ctx.send('Should everyone be in play,')
    time.sleep(1)
    await ctx.send('type "hasta la vista" and the game will be away! ')
    Dundies=True




thatswhatshesaid=["why is it so small",
            "come here",
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
           "don't make it harder than it has to",
           "you are making this harder",
           "im not saying it won't be hard",
           "you came",
           "that's big",
           "thats big",
            "that's hard"
            "thats hard"
           "put your mouth on that",
           "racism",
           "that's hard",
                  "thats hard",
            "that's really hard",
            "guess i'm on top"]

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

@client.event
async def on_message(message):
    global Bowl, Dundies, BowlPhase, BowlPlayers
    message.content=message.content.lower()
    if message.author== client.user:
        return
    if Dundies==True:
        if message.content=="here here!":
            await message.channel.send(str(message.author)+" has joined the Dundies!")

        if message.content=="hasta la vista":
            await message.channel.send('Hurray Hurray,')
            time.sleep(1)
            await message.channel.send('the Dundies are up, up and away!')


    elif Bowl==True:
        if len(BowlPlayers)<2:
            if message.content =="jim":
                BowlPlayers.append(Jim())
            if message.content == "dwight":
                BowlPlayers.append(Dwight())
            if message.content ==  "stanley":
                BowlPlayers.append(Stanley())
            if message.content == "kevin":
                BowlPlayers.append(Kevin())

            if len(BowlPlayers)==2:
                BowlPlayers[0].opponent.append(BowlPlayers[1].name)
                BowlPlayers[0].opponent.append(BowlPlayers[1].job)
                BowlPlayers[1].opponent.append(BowlPlayers[0].name)
                BowlPlayers[1].opponent.append(BowlPlayers[0].job)
                BowlPhase=1
                BowlPlayers.sort(key=lambda x: x.agility, reverse=True)
                await message.channel.send("Good good, we have our competitors. Now, the rules are simple. You will take turns attacking one another until one of you loses. In addition, there is no stopping the DUNDER BOWL once it begins. Good luck! ")

        if len(BowlPlayers)==2:


            option=bowlFunc(message)
            if option[0]=="dm list":

                for i in option[1]:
                    await message.author.send(i)
            elif option[0]=="dm string":
                await message.author.send(option[1])

            else:
                await message.channel.send(option[0])


                if BowlPhase==1 or BowlPhase==2:
                    await message.channel.send(BowlPlayers[0].name + " HP: " + str(BowlPlayers[0].HP))
                    await message.channel.send(BowlPlayers[1].name + " HP: " + str(BowlPlayers[1].HP))
                    await message.channel.send(bowlFunc(message)[0])
            n=None
            for i in BowlPlayers:
                if i.HP<=0:
                    if n==None:
                        await message.channel.send("We have a winner! Congratulations %s on your victory. Please, take this Dundie, you've earned it. If you would like to make a speach you may"%BowlPlayers[1].name)
                    else:
                        await message.channel.send("We have a winner! Congratulations %s on your victory. Please, take this Dundie, you've earned it. If you would like to make a speach you may"%BowlPlayers[0].name)

                    BowlPlayers=[]
                    BowlPhase=0
                    Bowl=False
                n=1




    else:
        for i in thatswhatshesaid:
            if i in message.content:
                await message.channel.send("That's what she said")
        for i in hahafunny:
            if i in message.content:
                await message.channel.send("Haha, Funny")

        for i in no:
            if i in message.content:
                await message.channel.send("No")
        await client.process_commands(message)

def dundieFunc(message,phase):
    pass

def bowlFunc(message):
    global BowlPhase, BowlPlayers
    #move selection
    print(BowlPhase,message.content)
    if BowlPhase%2==1:
        if BowlPhase==1:
            BowlPhase=3
            return [BowlPlayers[0].name+", type an option: attack.use (a, b, c), attack.summary, player.summary"]
        elif BowlPhase==3:
            if message.content.startswith("attack.use"):
                if message.content=="attack.use a":
                    effect=BowlPlayers[0].attack_a("attack")
                elif message.content=="attack.use b":
                    effect= BowlPlayers[0].attack_b("attack")
                elif  message.content=="attack.use c":
                    effect= BowlPlayers[0].attack_c("attack")


                BowlPlayers[1].HP-=effect[1]
                BowlPlayers[1].agility-=effect[2]
                BowlPlayers[1].strength-=effect[3]
                BowlPlayers[1].confidence-=effect[4]
                BowlPlayers.sort(key=lambda x: x.agility, reverse=True)
                BowlPhase=2
                return [effect[0]]
            elif message.content.startswith("attack.summary"):
                return ["dm list",BowlPlayers[0].attackSummary()]
            elif message.content.startswith("player.summary"):
                return ["dm string",BowlPlayers[0].summary()]

            else:
                return ["Invalid Option, please try again"]
        else:
            return ["there's been an issue"]
    if BowlPhase%2==0:
        if BowlPhase==2:
            BowlPhase=4
            return [BowlPlayers[1].name+", type an option: attack.use (a, b, c), attack.summary, player.summary"]
        elif BowlPhase==4:
            if message.content.startswith("attack.use"):
                if message.content=="attack.use a":
                    effect=BowlPlayers[1].attack_a("attack")
                elif message.content=="attack.use b":
                    effect= BowlPlayers[1].attack_b("attack")
                elif  message.content=="attack.use c":
                    effect= BowlPlayers[1].attack_c("attack")


                BowlPlayers[0].HP-=effect[1]
                BowlPlayers[0].agility-=effect[2]
                BowlPlayers[0].strength-=effect[3]
                BowlPlayers[0].confidence-=effect[4]
                BowlPlayers.sort(key=lambda x: x.agility, reverse=True)
                BowlPhase=1
                return [effect[0]]
            elif message.content.startswith("attack.summary"):
                return ["dm list",BowlPlayers[1].attackSummary()]
            elif message.content.startswith("player.summary"):
                return ["dm string",BowlPlayers[1].summary()]

            else:
                return ["Invalid Option, please try again"]


client.run("Nzg0Mjg3OTE0OTM0NjY1MjU3.X8nHCg.XuH5DoS63Z0ObWAEPr81i1Ek-uY")
