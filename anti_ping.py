import discord

# Admin ctrls
default_call = 'n!'
client = discord.Client()
token = '---'
icon = "https://cdn.discordapp.com/emojis/435912920702910464.png?v=1"
noping = []

# Fill in your user id here:
auth = []

# Random vars
txt = ""
msg = ""

def findGuild(guild: str):
    global noping
    for i in range(len(noping)):
        if noping[i]["guild"] == guild:
            return i
    noping.append({"guild": guild, "members": []})


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="out for pings"))

@client.event
async def on_message(message):
    global txt, msg, noping, auth
    if message.author.bot:
        pass
    else:
         if str(message.author.id) not in auth:
            for i in range(len(auth)):
                if ("<@!" + str(auth[i]) + ">") in str(message.content) or ("<@" + str(auth[i]) + ">") in str(message.content):
                    await message.delete()
                    msg = discord.Embed(title="Error",
                                        description=str(message.author.mention) + ", you cannot ping <@!" + str(auth[i]) + ">",
                                        color=discord.Color.red())
                    msg.set_author(name="NoPing")
                    msg.set_thumbnail(url=icon)
                    await message.channel.send(embed=msg)
                    txt = discord.Embed(title="Announcement📢",
                                        description=str(message.author.mention) + " pinged you in <#" + str(message.channel.id) + "> with message: \n\n" + str(message.content),
                                        color=discord.Color.red())
                    msg.set_author(name="NoPing")
                    msg.set_thumbnail(url=icon)
                    await client.get_user(int(auth[i])).send(embed=txt)


client.run(token)
