import os

import discord
import youtube_dl as youtube_dl
from discord import channel
from discord.ext import commands
import random
import json
import logging
import math
from urllib import request
from datetime import datetime
import asyncio
import youtube_dl as ytdl
from discord.utils import find, get
from pathlib import Path

client = commands.Bot(command_prefix="p:")


YTDL_OPTS = {
    "default_search": "ytsearch",
    "format": "bestaudio/best",
    "quiet": True,
    "extract_flat": "in_playlist"
}


def _play_song(self, client, state, song):
    state.now_playing = song
    state.skip_votes = set()  # clear skip votes
    source = discord.PCMVolumeTransformer(
        discord.FFmpegPCMAudio(song.stream_url), volume=state.volume)

    def after_playing(err):
        if len(state.playlist) > 0:
            next_song = state.playlist.pop(0)
            self._play_song(client, state, next_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(),
                                             self.bot.loop)

    client.play(source, after=after_playing)


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


async def audio_playing(ctx):
    """Checks that audio is currently playing before continuing."""
    client = ctx.guild.voice_client
    if client and client.channel and client.source:
        return True
    else:
        raise commands.CommandError("Not currently playing any audio.")


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
        await ctx.send("Default Commands. Say p:help <utilpack> For More Info On that Specific Package."
                       "\n"
                       "\n p:help, p:post, p:play, p:leave, p:submit, p:submitsong, p:marketplace, p:subforum <name>")
    else:
        if command == "community":
            embed = discord.Embed(title="Community Commands", description="All Of the Basic Community Utilities")
            embed.add_field(name="Networks",
                            value="p:post\np:top_posts\np:view <post>\np:submit <util>\np:submitsong <url>")
            await ctx.send(embed=embed)


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


async def in_voice_channel(ctx):
    """Checks that the command sender is in the same voice channel as the bot."""
    voice = ctx.author.voice
    bot_voice = ctx.guild.voice_client
    if voice and bot_voice and voice.channel and bot_voice.channel and voice.channel == bot_voice.channel:
        return True
    else:
        raise commands.CommandError(
            "You need to be in the channel to do that.")


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


@client.command()
async def mailtomods(ctx, arg):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("Alright")
        code = random.randint(0, 12073691093281287983)
        mailchannel = client.get_channel(803061426050170880)
        await ctx.send(f"Started Session. Code: {code}.")
        await mailchannel.send(f"Started Session. Code: {code}.")


@client.command(aliases=["stop"])
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def leave(self, ctx):
    """Leaves the voice channel, if currently in one."""
    clienst = ctx.guild.voice_client
    state = self.get_state(ctx.guild)
    if client and clienst.channel:
        await clienst.disconnect()
        state.playlist = []
        state.now_playing = None
    else:
        await ctx.send("NOT IN A VOICE!!!")


@client.command()
@commands.check(audio_playing)
@commands.check(in_voice_channel)
async def skip(self, ctx):
    """Skips the currently playing song, or votes to skip it."""
    state = self.get_state(ctx.guild)
    client = ctx.guild.voice_client
    if ctx.channel.permissions_for(
            ctx.author).administrator or state.is_requester(ctx.author):
        # immediately skip if requester or admin
        client.stop()
    elif self.config["vote_skip"]:
        # vote to skip song
        channel = client.channel
        self._vote_skip(channel, ctx.author)
        # announce vote
        users_in_channel = len([
            member for member in channel.members if not member.bot
        ])  # don't count bots
        required_votes = math.ceil(
            self.config["vote_skip_ratio"] * users_in_channel)
        await ctx.send(
            f"{ctx.author.mention} voted to skip ({len(state.skip_votes)}/{required_votes} votes)"
        )
    else:
        raise commands.CommandError("Sorry, vote skipping is disabled.")


class Video:
    """Class containing information about a particular video."""

    def __init__(self, url_or_search, requested_by):
        """Plays audio from (or searches for) a URL."""
        with ytdl.YoutubeDL(YTDL_OPTS) as ydl:
            video = self._get_info(url_or_search)
            video_format = video["formats"][0]
            self.stream_url = video_format["url"]
            self.video_url = video["webpage_url"]
            self.title = video["title"]
            self.uploader = video["uploader"] if "uploader" in video else ""
            self.thumbnail = video[
                "thumbnail"] if "thumbnail" in video else None
            self.requested_by = requested_by

    def _get_info(self, video_url):
        with ytdl.YoutubeDL(YTDL_OPTS) as ydl:
            info = ydl.extract_info(video_url, download=False)
            video = None
            if "_type" in info and info["_type"] == "playlist":
                return self._get_info(
                    info["entries"][0]["url"])  # get info for first video
            else:
                video = info
            return video

    def get_embed(self):
        """Makes an embed out of this Video's information."""
        embed = discord.Embed(
            title=self.title, description=self.uploader, url=self.video_url)
        embed.set_footer(
            text=f"Requested by {self.requested_by.name}",
            icon_url=self.requested_by.avatar_url)
        if self.thumbnail:
            embed.set_thumbnail(url=self.thumbnail)
        return embed


@client.command(brief="Plays audio from <url>.")
async def play(self, ctx, *, url):
    """Plays audio hosted at <url> (or performs a search for <url> and plays the first result)."""

    clients = client.guild.voice_client
    state = clients.get_state(ctx.guild)  # get the guild's state

    if clients and clients.channel:
        try:
            video = Video(url, ctx.author)
        except youtube_dl.DownloadError as e:
            logging.warn(f"Error downloading video: {e}")
            await ctx.send(
                "There was an error downloading your video, sorry.")
            return
        state.playlist.append(video)
        message = await ctx.send(
            "Added to queue.", embed=video.get_embed())
        await self._add_reaction_controls(message)
    else:
        if ctx.author.voice is not None and ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel
            try:
                video = Video(url, ctx.author)
            except youtube_dl.DownloadError as e:
                await ctx.send(
                    "There was an error downloading your video, sorry.")
                return
            client = await channel.connect()
            self._play_song(client, state, video)
            message = await ctx.send("", embed=video.get_embed())
            await self._add_reaction_controls(message)
            logging.info(f"Now playing '{video.title}'")
        else:
            await ctx.send("Failed To Play Video.")


async def on_reaction_add(self, reaction, user):
    """Respods to reactions added to the bot's messages, allowing reactions to control playback."""
    message = reaction.message
    if user != self.bot.user and message.author == self.bot.user:
        await message.remove_reaction(reaction, user)
        if message.guild and message.guild.voice_client:
            user_in_channel = user.voice and user.voice.channel and user.voice.channel == message.guild.voice_client.channel
            permissions = message.channel.permissions_for(user)
            guild = message.guild
            state = self.get_state(guild)
            if permissions.administrator or (
                    user_in_channel and state.is_requester(user)):
                client = message.guild.voice_client
                if reaction.emoji == "⏯":
                    # pause audio
                    self._pause_audio(client)
                elif reaction.emoji == "⏭":
                    # skip audio
                    client.stop()
                elif reaction.emoji == "⏮":
                    state.playlist.insert(
                        0, state.now_playing
                    )  # insert current song at beginning of playlist
                    client.stop()  # skip ahead
            elif reaction.emoji == "⏭" and self.config[
                "vote_skip"] and user_in_channel and message.guild.voice_client and message.guild.voice_client.channel:
                # ensure that skip was pressed, that vote skipping is
                # enabled, the user is in the channel, and that the bot is
                # in a voice channel
                voice_channel = message.guild.voice_client.channel
                self._vote_skip(voice_channel, user)
                # announce vote
                channel = message.channel
                users_in_channel = len([
                    member for member in voice_channel.members
                    if not member.bot
                ])  # don't count bots
                required_votes = math.ceil(
                    self.config["vote_skip_ratio"] * users_in_channel)
                await channel.send(
                    f"{user.mention} voted to skip ({len(state.skip_votes)}/{required_votes} votes)"
                )


client.run("")
