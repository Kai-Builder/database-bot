import os

import discord
import youtube_dl as youtube_dl
from discord import channel
from discord.ext import commands
import random
import json

from datetime import datetime
import asyncio
from discord.utils import find, get
from pathlib import Path

client = commands.Bot(command_prefix="p:")


async def status_task():
    while True:
        game = discord.Game(f"The Community Submitted Games!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game(f"USB Is so cool Right?")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name='kai-builder.github.io'))
        await client.change_presence(status=discord.Status.idle, activity=game)
        await asyncio.sleep(3)
        game = discord.Game(f"p:help, p:database, p:os, p:post, p:submit")
        await client.change_presence(status=discord.Status.idle, activity=game)


@client.event
async def on_ready():
    await client.loop.create_task(status_task())


@client.command()
async def register(ctx, name, dob, age, pw):
    await ctx.message.delete()
    print("User Called init")
    await ctx.send("Registering you...")
    os.mkdir(name)
    i = open(name + "/user.txt", 'w')
    i.write(name + "\n" + age + "\n" + dob + "\n" + pw)
    i.close()


@client.event
async def on_member_ban(guild, user):
    print(guild, user)


@client.command()
async def login(ctx, name, passw):
    print("User Called Log In")
    await ctx.message.delete()
    await ctx.send("Logging you In..")
    await asyncio.sleep(random.randint(0, 6))
    a = Path(name)
    if a.exists():
        member = ctx.message.author
        man = ctx.message.author
        await ctx.send("Logging you in!")
        await man.add_roles(discord.utils.get(man.guild.roles, name="Verified"))  # add the role
        i = open(name + "/user.txt")
        a = i.readlines()
        if passw == a[3]:

            await ctx.send("Found Your Account! Account Details:\nName: " + a[0] + "Dob: " + a[2] + " Age: " + a[1])
        else:
            await ctx.send("Password Login Failed. Try Again.")
    else:
        await ctx.send("You're Not Logged In On This Account/Server Sorry.")


@client.command()
async def itch(ctx):
    print("User Called itch")
    await ctx.send(
        "If you didn't already know, I (U$B) Is Hosting this bot myself, Bascially, The New Game I'm Developing (KMOD) Is Now available In Pre-releases & Source Releases.\nIt is also Optional TO Pay For the App To Get Full Beta Access.\nLink: https://kai-builder.itch.io/kais-sandbox#download \nTrailer: https://www.youtube.com/watch?v=f4WhDsu-lJM&t=4s ")


@client.command()
async def backup(ctx, account):
    print("User Called Backup_Password")
    await ctx.send("Backing Up Your Password...")
    s = open(account + "/accountbackup.txt", "w")
    a = random.randint(0, 11023132139137139127382)
    s.write(str(a))
    s.close()
    await ctx.send("Generated Backup Account Password.")
    await ctx.author.send(
        "Your Backup Is " + str(a) + ". DO NOT SHARE THIS WITH ANYBODY ELSE! THIS IS USED TO IDENTIFY YOUR ACCOUNT!")


@client.command()
async def login_backup(ctx, account, backup_):
    print("User Called Login Through Backup")
    await ctx.send("Alright!")
    await asyncio.sleep(2)
    await ctx.send("Getting Account Details...")


@client.event
async def on_guild_join(guild):
    general = find(lambda x: guild.system_channel, guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send("""
            
                                                                ▄▄                               
                ▀███▀▀▀██▄           ██           ▄██                               
                ██    ▀██▄         ██            ██                               
                ██     ▀██▄█▀██▄ ██████ ▄█▀██▄   ██▄████▄  ▄█▀██▄  ▄██▀███ ▄▄█▀██ 
                ██      ███   ██   ██  ██   ██   ██    ▀████   ██  ██   ▀▀▄█▀   ██
                ██     ▄██▄█████   ██   ▄█████   ██     ██ ▄█████  ▀█████▄██▀▀▀▀▀▀
                ██    ▄██▀█   ██   ██  ██   ██   ██▄   ▄████   ██  █▄   ████▄    ▄
                ▄████████▀ ▀████▀██▄ ▀████████▀██▄ █▀█████▀ ▀████▀██▄██████▀ ▀█████▀
                                                                    
                **The DataBase Discord Bot**

                ```c++
                printf("Thanks for Using my Bot!");
                ```

                This Bot was Made By U$B And Was Made For Fun. Use this for any purpose (For Commercial Servers DM Me 
                (U$B#5000)) Without Pay (other than Commercial). 

                Thank you for Putting My Bot Into your Server and I Hope you have fun with it!

                To Begin, Say p:help :)


                        ▄▄▄ .▐▄• ▄ ▄▄▄▄▄▄▄▄▄   ▄▄▄· .▄▄ ·  ▄▄ 
                        ▀▄.▀· █▌█▌▪▀•██ ▀▀▄ █·▐█ ▀█ ▐█ ▀.  ██▌
                        ▐▀▀▪▄ ·██·   ▐█.▪▐▀▀▄ ▄█▀▀█ ▄▀▀▀█▄ ▐█·
                        ▐█▄▄▌▪▐█·█▌  ▐█▌·▐█•█▌▐█▪ ▐▌▐█▄▪▐█ .▀ 
                        ▀▀▀ •▀▀ ▀▀  ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀▀   ▀     

                Database Is a Self-Hosted Bot With Some Pretty Cool Features. In my Mind :)

A Forum Page for Posting Global Messages.

Accounts! If your Server Comes With A Verified Role, Users will Have to Register And Log In To Their Accounts On the Server To Get the Verified Role!

Custom Moderation Features! If you want a Custom moderation Command, The Github Package Site Is Coming soon :)

You can Talk to friends over a server,

Custom Commands Are found Also in the Github Package!

    Now Happy Moderating!

                                                       

            """)


@client.command()
async def info(ctx):
    print("User Called info")
    await ctx.send(
        "This Bot Is Used By Kai's sandbox Development for Moderation Purposes.\nThis Bot Can not Be used by Other users Unless The Command, p:register & p:login Is Called.")
    await ctx.send("Say p:register <name> <dob> <age> <password> To Get Started.")
    await ctx.send("Think Your account is already In Our Database? Say p:login <Name> <pass> To Log in!")
    await ctx.send("(All information Is not used against any entities Using this Discord Bot.)")


@client.command()
@commands.has_role("Logged In")
async def downloads(ctx):
    print("User Called downloads")
    await ctx.send("downloads")


@client.command()
async def deleteaccount(ctx, accountname):
    print("User Called deleteaccount")
    await ctx.author.send("Waiting For Account BACKUP Password...")
    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    await ctx.send("Checking If " + msg + " Is in the class of your backup Password.")


@client.command()
async def id(ctx, number: int):
    await client.send_message(number)


@client.command()
async def post(ctx, *, message):
    print("User Called _POST_")
    await ctx.send("Posting...")
    a = datetime.today()

    i = open("posts\\post_user" + str(ctx.author) + str(random.randint(19, 121031829236715812938178)) + ".txt", "w")
    i.write(f"{message}")
    i.close()


@client.command()
async def post_page(ctx):
    print("User Called View")
    await ctx.send("Sending You A List of the forum Page.")
    await asyncio.sleep(2)
    await ctx.send("List Of Posts By Raw DataBase Name")
    await ctx.send("To View Posts Individually, Type p:view <postname> OR Type p:top posts")
    for filename in os.listdir('posts'):
        await ctx.send(filename)


@client.command()
async def view(ctx, name):
    print("User Called view")
    o = open("posts/" + name, "r+")
    k = o.readlines()
    await ctx.send(f"Found Post " + name + ". Post Details:\n\n" + k[0] + ".")


@client.command()
async def top_posts(ctx):
    print("User Called top_posts")
    await ctx.send("Alright!")
    for file in os.listdir('posts'):
        await ctx.send("Post Found!")
        f = open("posts/" + file)
        a = f.readlines()
        for line in a:
            await ctx.send(f"Post Contents: {line} ")


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    if not reason:
        await user.kick()
        await ctx.send(f"**{user}** has been kicked for **no reason**.")
    else:
        await user.kick(reason=reason)
        await ctx.send(f"**{user}** has been kicked for **{reason}**.")


@client.command()
@commands.has_permissions(administrator=True)
async def announce(ctx, channel: discord.TextChannel, *, message):
    print("User Called annoucne")
    await ctx.message.delete()
    await channel.send("@everyone")
    s = discord.Embed(title="Announcement", description=message)
    await channel.send(embed=s)


client.remove_command("help")


@client.command()
async def music(ctx):
    print("music Called")
    await ctx.send("This Bot Also Contains Music! How Lovely. Most Of the Songs Are powered By Our Users. So If you "
                   "want to submit a song, Learn How @ https://kai-builder.github.io/bots/db/docs")


@client.command(pass_context=True)
async def ban(ctx, user: discord.Member, *, reason):
    print("Banned")
    await user.ban(reason=reason)
    await ctx.send(f"Banned @{user} With Reason Of {reason}")


@client.command()
async def play(ctx, url: str):
    global name
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
            print('Removed current song.')
    except PermissionError:
        print('Error in deleting song file. (Song in use.)')
        await ctx.send('Unable to request song. (Song already in use.)')
        return

    await ctx.send('Preparing song. Please wait.')
    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('Downloading audio now.\n')
        ydl.download([url])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print(f'Renamed File: {file}.')
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print(f'{name} has finished playing.'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.06

    nname = name.rsplit('-', 2)
    await ctx.send(f'Now playing {name}.')
    print('Now playing.\n')


@client.command()
async def marketplace(ctx):
    print("marketplace Called")
    os.mkdir("MarketPlace")
    await ctx.send("Loading the MarketPlace. . .")
    await asyncio.sleep(random.randint(0, 10))
    for filename in os.listdir("MarketPlace"):
        print("Loaded MarketPlace")


@client.command()
async def community(ctx):
    print("community Called")
    await ctx.send("You guys Control Me!\n\nYou can Submit Bot Extensions, Accounts, Custom Prefixes, And Much "
                   "More.\nYou can Submit Posts And More Via p:post!\nYou can Submit Links and More!"
                   "\n You can Also Submit SONGS Using the p:songrequest <link> !"
                   "\n To Submit Extensions Or Posts, Use p:post Or p:submit <extname> <Usage>")


@client.command()
async def subforum(ctx):
    print("subforum Called")
    await ctx.send("subforum")


@client.command()
async def help(ctx, command=None):
    print("heloin")
    if command is None:
        print("nonecomd")
        await ctx.send("Commands"
                       "\n"
                       "\n p:help, p:post, p:play, p:leave, p:submit, p:submitsong, p:marketplace, p:subforum <name>")
    else:
        a = open('doc/' + command, "r+")
        i = a.readlines()
        a = ''.join(i)
        embe = discord.Embed(title=command, description=f"This is the Utility's {command} Read me.")
        await ctx.send(embed=embe)
        for line in a:
            await ctx.send(line)


@client.command()
async def partycreate(ctx, ispub, code, *, partyname):
    print("party Called")
    await ctx.message.delete()
    await ctx.send(f"Creating a Party With the Name Of {partyname}. . .")
    await asyncio.sleep(2)
    os.mkdir(f"p/{partyname}")
    set = open('p/' + partyname + "/settings.ini", "w")
    if ispub == "yes":
        set.write(f"true")
    else:
        set.write(f"false\n{code}")
    set.close()
    await ctx.send("Created Party.")


@client.command()
async def publicparties(ctx):
    print("publicparties Called")
    x = 0
    x = x + 5
    for filename in os.listdir('p'):
        i = open("p/" + filename + "/settings.ini")
        f = i.readlines()
        if f[0] == "true":
            await ctx.send(filename)
        else:
            print("PrivateLobby")


@client.command()
async def joinparty(ctx, code: int, *, name):
    print("joinparty Called")
    await ctx.send(f"Joining {name}!")
    await asyncio.sleep(2)
    o = open('p/' + name + "/settings.ini")
    s = o.readlines()

    if code == s[1]:
        await ctx.send(f"Joined Party {name}")


sent_users = []


@client.event
async def on_message(message):

    if message.guild:  # ensure the channel is a DM
        return

    if message.author == client.user:
        return

    if message.author.id in sent_users:  # Ensure the intial message hasn't been sent before
        return

    modmail_channel = client.get_channel(803061426050170880)
    await modmail_channel.send("User Logged, Started MODMAIL")
    a = discord.Embed(title="ModMail")
    a.set_author(name="Mailer")
    a.add_field(name="How Does ModMail Work?",
                    value="Modmail Is a Discord Bot That Eases The Process Of Sending DMs To Mods Using Tokens and Stuff. I Don't understand Either."
                    )
    a.add_field(name="Mailing Commands",
                    value="mailto, mailtomods, joinmodparty")
    a.add_field(name="Shoutouts",
                    value="DKradicat, Kinetic_Unicornz, Echo_, Brop, USB (me) (Obviously), And All of my Other friends!")
    await message.author.send(embed=a)

    def check(m):
            if m.content == "mailtomods":
                sessionid = random.randint(0, 100002112312)


                await message.author.send(f"Starting Your Session With Id, {sessionid}")
                await modmail_channel.send(f"SessionID, {sessionid} Has Started.")

    msg = await client.wait_for('message', check=check)


@client.command()
async def check(ctx, arg):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send(arg)
client.run("ODAyMTg5NzQ4MTIyNjgxMzU2.YArnaw.M8K_kLBNmw6cUc3sI6saAUQIosY")
