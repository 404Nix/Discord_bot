from ast import alias
import asyncio
from multiprocessing.sharedctypes import Value
from turtle import title
from unicodedata import name
import youtube_dl
import pafy
import discord
import random
import giphy_client
import animec
from giphy_client.rest import ApiException
from keep_alive import keep_alive
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">>", intents=intents)

#variables
punch_gifs = [
    "https://c.tenor.com/BoYBoopIkBcAAAAM/anime-smash.gif",
    "https://c.tenor.com/EvBn8m3xR1cAAAAM/toradora-punch.gif",
    "https://c.tenor.com/SwMgGqBirvcAAAAM/saki-saki-kanojo-mo-kanojo.gif",
    "https://c.tenor.com/UH8Jnl1W3CYAAAAM/anime-punch-anime.gif",
    "https://c.tenor.com/6a42QlkVsCEAAAAM/anime-punch.gif",
    "https://c.tenor.com/3CUBZHrDUvUAAAAM/punch-combo.gif",
    "https://c.tenor.com/57GPuhglLyEAAAAM/anime-retro-anime.gif"]
punch_names = ["Puched you"]

slap_gifs = [
    "https://c.tenor.com/E3OW-MYYum0AAAAM/no-angry.gif",
    "https://c.tenor.com/Ws6Dm1ZW_vMAAAAM/girl-slap.gif",
    "https://c.tenor.com/eU5H6GbVjrcAAAAM/slap-jjk.gif",
    "https://c.tenor.com/1-1M4PZpYcMAAAAM/tsuki-tsuki-ga.gif",
    "https://c.tenor.com/CAesvxP0KyEAAAAM/shinobu-kocho-giyuu-tomioka.gif",
    "https://c.tenor.com/PeJyQRCSHHkAAAAM/saki-saki-mukai-naoya.gif"]
slap_names = ["Slaped you"]

oppai_gifs = [
    "https://c.tenor.com/Y6B_ey6biK8AAAAM/maoyuu-yuusha.gif",
    "https://c.tenor.com/XzroZ5dr4OcAAAAM/maoyuu-yuusha.gif",
    "https://c.tenor.com/5UCFLeILBlgAAAAM/anime-oppai.gif",
    "https://c.tenor.com/H7NGv4lJScMAAAAM/oppai-anime.gif",
    "https://c.tenor.com/BJVTJAaBo2kAAAAM/high-school-of-the-dead-anime.gif",
    "https://c.tenor.com/kmr7MdW60jQAAAAM/anime-boobs.gif",
    "https://c.tenor.com/TUUkx4E9NLAAAAAM/danmachi-oppai.gif",
    "https://c.tenor.com/1H_U6YLslw4AAAAM/maoyuu-yuusha.gif",
    "https://c.tenor.com/Jwirb-GsUIsAAAAM/nisekoi-anime.gif",
    "https://c.tenor.com/xAQEUZBG2qkAAAAM/lucoa-oppai.gif"
]
oppai_names = ["Here's your oppai \n Enjoy !", "hehe horny boii >//<", "feeling horny or what?"]

kick_gifs = [
    "https://c.tenor.com/Lyqfq7_vJnsAAAAM/kick-funny.gif",
    "https://c.tenor.com/EcdG5oq7MHYAAAAM/shut-up-hit.gif",
    "https://c.tenor.com/4F6aGlGwyrwAAAAM/sdf-avatar.gif",
    "https://c.tenor.com/7te6q4wtcYoAAAAM/mad-angry.gif",
    "https://c.tenor.com/4zwRLrLMGm8AAAAM/chifuyu-chifuyu-kick.gif",
    "https://c.tenor.com/2U9tTXuO_gUAAAAM/kick-anime.gif",
    "https://c.tenor.com/Qs9NYCf1b4YAAAAM/shida-midori-midori.gif",
    "https://c.tenor.com/BvzQtBbJHBMAAAAM/jujutsu-kaisen-sukuna.gif",
    "https://c.tenor.com/J3Lc1VDcZ4UAAAAM/dbz-dragon-ball-z.gif",
    "https://c.tenor.com/D67kRWw_cEEAAAAM/voz-dap-chym-dap-chym.gif",
    "https://c.tenor.com/3i8E86ZksXYAAAAM/sanji-luffy.gif"]
kick__names = ["kicked you"]

kiss_gifs = [
    "https://c.tenor.com/16MBIsjDDYcAAAAM/love-cheek.gif",
    "https://c.tenor.com/wDYWzpOTKgQAAAAM/anime-kiss.gif",
    "https://c.tenor.com/hK8IUmweJWAAAAAM/kiss-me-%D0%BB%D1%8E%D0%B1%D0%BB%D1%8E.gif",
    "https://c.tenor.com/TnjL6WcdkkwAAAAM/anime-kiss.gif",
    "https://c.tenor.com/03wlqWILqpEAAAAM/highschool-dxd-asia.gif",
    "https://c.tenor.com/3zdH2jC6qCcAAAAM/love-anime.gif",
    "https://c.tenor.com/Ze6FyEgy4WAAAAAM/kiss-anime.gif",
    "https://c.tenor.com/BjwmxFVGKm0AAAAM/toloveru-unexpected.gif",
    "https://c.tenor.com/YeitcPAdSCYAAAAM/kyo-x-tohru-kiss.gif",
    "https://c.tenor.com/Fyq9izHlreQAAAAM/my-little-monster-haru-yoshida.gif",
    "https://c.tenor.com/0E_odieuKmwAAAAM/anime-zero.gif"
]
kiss_names = ["kissed you"]

hug_gifs = [
    "https://c.tenor.com/9e1aE_xBLCsAAAAM/anime-hug.gif",
    "https://c.tenor.com/2bWwi8DhDsAAAAAM/hugs-and-love.gif",
    "https://c.tenor.com/xgVPw2QK5n8AAAAM/sakura-quest-anime.gif",
    "https://c.tenor.com/DVOTqLcB2jUAAAAM/anime-hug-love.gif",
    "https://c.tenor.com/SPs0Rpt7HAcAAAAM/chiya-urara.gif",
    "https://c.tenor.com/qF7mO4nnL0sAAAAM/abra%C3%A7o-hug.gif",
    "https://c.tenor.com/2lr9uM5JmPQAAAAM/hug-anime-hug.gif",
    "https://c.tenor.com/jQ0FcfbsXqIAAAAM/hug-anime.gif",
    "https://c.tenor.com/mB_y2KUsyuoAAAAM/cuddle-anime-hug.gif",
    "https://c.tenor.com/XyMvYx1xcJAAAAAM/super-excited.gif",
    "https://c.tenor.com/nHkiUCkS04gAAAAM/anime-hug-hearts.gif",
    "https://c.tenor.com/qZiLC0qGROAAAAAM/anime-two-girls.gif"
]
hug_names = ["hugged you"]

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("with Zenitsu"))
    print(f"{bot.user.name} is ready.")

'''@bot.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(bot.get_all_channels(), name="mod-mail")

    if message.author == bot.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.display_name + "]")

            for file in files:
                await modmail_channel.send(file.url)
        else:
            await modmail_channel.send("[" + message.author.display_name + "] " + message.content)

    elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + message.author.display_name + "]")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send(mod_message)'''

        
class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.song_queue = {}

        self.setup()

    def setup(self):
        for guild in self.bot.guilds:
            self.song_queue[guild.id] = []

    async def check_queue(self, ctx):
        if len(self.song_queue[ctx.guild.id]) > 0:
            await self.play_song(ctx, self.song_queue[ctx.guild.id][0])
            self.song_queue[ctx.guild.id].pop(0)

    async def search_song(self, amount, song, get_url=False):
        info = await self.bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet" : True}).extract_info(f"ytsearch{amount}:{song}", download=False, ie_key="YoutubeSearch"))
        if len(info["entries"]) == 0: return None

        return [entry["webpage_url"] for entry in info["entries"]] if get_url else info

    async def play_song(self, ctx, song):
        url = pafy.new(song).getbestaudio().url
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)), after=lambda error: self.bot.loop.create_task(self.check_queue(ctx)))
        ctx.voice_client.source.volume = 0.5


    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            return await ctx.send("You are not connected to a voice channel, please connect to the channel you want the bot to join.")

        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

        await ctx.author.voice.channel.connect()

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client is not None:
            return await ctx.voice_client.disconnect()

        await ctx.send("I am not connected to a voice channel.")

    @commands.command()
    async def play(self, ctx, *, song=None):
        if ctx.author.voice is None:
            return await ctx.send("You are not connected to a voice channel, please connect to the channel you want the bot to join.")

        if song is None:
            return await ctx.send("You must include a song to play.")

        if ctx.voice_client is None:
            return await ctx.send("I must be in a voice channel to play a song.")

        # handle song where song isn't url
        if not ("youtube.com/watch?" in song or "https://youtu.be/" in song):
            await ctx.send("Sit tight!, you will hear your song in few sec.")

            result = await self.search_song(1, song, get_url=True)

            if result is None:
                return await ctx.send("Sorry, I could not find the given song, try using my search command.")

            song = result[0]

        if ctx.voice_client.source is not None:
            queue_len = len(self.song_queue[ctx.guild.id])

            if queue_len < 10:
                self.song_queue[ctx.guild.id].append(song)
                return await ctx.send(f"I am currently playing a song, this song has been added to the queue at position: {queue_len+1}.")

            else:
                return await ctx.send("Sorry, I can only queue up to 10 songs, please wait for the current song to finish.")

        await self.play_song(ctx, song)
        await ctx.send(f"Now playing: {song}")

    @commands.command()
    async def search(self, ctx, *, song=None):
        if song is None: return await ctx.send("You forgot to include a song to search for.")

        await ctx.send("Searching for song, this may take a few seconds.")

        info = await self.search_song(5, song)

        embed = discord.Embed(title=f"Results for '{song}':", description="*You can use these URL's to play an exact song if the one you want isn't the first result.*\n", colour=discord.Colour.red())
        
        amount = 0
        for entry in info["entries"]:
            embed.description += f"[{entry['title']}]({entry['webpage_url']})\n"
            amount += 1

        embed.set_footer(text=f"Displaying the first {amount} results.")
        await ctx.send(embed=embed)

    @commands.command()
    async def queue(self, ctx): # display the current guilds queue
        if len(self.song_queue[ctx.guild.id]) == 0:
            return await ctx.send("There are currently no songs in the queue.")

        embed = discord.Embed(title="Song Queue", description="", colour=discord.Colour.dark_gold())
        i = 1
        for url in self.song_queue[ctx.guild.id]:
            embed.description += f"{i}) {url}\n"

            i += 1

        embed.set_footer(text="You can add upto 10 songs in a queue")
        await ctx.send(embed=embed)

#skip cmd here

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client.is_paused():
            return await ctx.send("I am already stopped.")

        ctx.voice_client.pause()
        await ctx.send("The current song has been stopped.")

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send("I am not connected to a voice channel.")

        if not ctx.voice_client.is_paused():
            return await ctx.send("I am already playing a song.")
        
        ctx.voice_client.resume()
        await ctx.send("The current song has been resumed.")


    @commands.command()
    async def anime(self,ctx,*,query):
        try:
            anime = animec.Anime(query)
        except:
            await ctx.send(embed=discord.Embed(description ="Anime not found",color= discord.Color.blue()))
            return
        embed=discord.Embed(title= anime.title_english,url = anime.url,description= f"{anime.description[:200]}...",color=discord.Color.red())
        embed.add_field(name= "Episodes",value = str(anime.episodes))
        embed.add_field(name= "Rating",value = str(anime.rating))
        embed.add_field(name= "Genre",value = str(anime.genres))
        embed.add_field(name= "Broadcast",value = str(anime.broadcast))
        embed.add_field(name= "NSFW",value = str(anime.is_nsfw()))
        embed.set_thumbnail(url = anime.poster)

        await ctx.send(embed=embed)

    @commands.command()
    async def char(self,ctx,*,query):
        try:
            char = animec.Charsearch(query)
        except:
            await ctx.send(embed=discord.Embed(description ="Anime Character not found",color= discord.Color.blue()))
            return
        embed =discord.Embed(title= char.title,url = char.url,color=discord.Color.red())
        embed.set_image(url= char.image_url)
        embed.set_footer(text = ",".join(list(char.references.keys())[:2]))
        await ctx.send(embed = embed)

    

    @commands.command()
    async def punch(self,ctx):
        embed = discord.Embed(
            color=(discord.Color.red()),
            description = f"{ctx.author.mention},{(random.choice(punch_names))}"
        )
        embed.set_image(url=(random.choice(punch_gifs)))

        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self,ctx):
        embed = discord.Embed(
            color=(discord.Color.red()),
            description = f"{ctx.author.mention},{(random.choice(slap_names))}"
        )
        embed.set_image(url=(random.choice(slap_gifs)))

        await ctx.send(embed=embed)   

    @commands.command()
    async def oppai(self,ctx):
        embed = discord.Embed(
            color=(discord.Color.red()),
            description = f"{ctx.author.mention},{(random.choice(oppai_names))}"
        )
        embed.set_image(url=(random.choice(oppai_gifs)))

        await ctx.send(embed=embed)  

    @commands.command()
    async def kick(self,ctx):
        embed = discord.Embed(
            color=(discord.Color.red()),
            description = f"{ctx.author.mention},{(random.choice(kick__names))}"
        )
        embed.set_image(url=(random.choice(kick_gifs)))

        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self,ctx):
        embed = discord.Embed(
            color=(discord.Color.red()),
            description = f"{ctx.author.mention},{(random.choice(kiss_names))}"
        )
        embed.set_image(url=(random.choice(kiss_gifs)))

        await ctx.send(embed=embed)
    
    @commands.command()
    async def hug(self,ctx):
        embed = discord.Embed(
            color=(discord.Color.red()),
            description = f"{ctx.author.mention},{(random.choice(hug_names))}"
        )
        embed.set_image(url=(random.choice(hug_gifs)))

        await ctx.send(embed=embed)

@bot.command(name="ping")
async def yo(ctx: commands.Context):
    await ctx.send(f'**Pong!** : {round(bot.latency * 1000)}ms')

@bot.command()
async def gif(ctx,*,q="Nezuko"):
    api_key="TwOuL3yltcQBuSmdrpJGJy7NXJCevy3j"
    api_instance = giphy_client.DefaultApi()
    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=10, rating='R')
        lst = list(api_response.data)
        giff = random.choice(lst)
        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@bot.command()
async def yo(ctx):

  responses = ['hey.', 'whats up?', 'how is it going?','yo!', 'howdy!', 'Gday!', 'Hi', 'Its nice to meet you.', 'Hello', 'its pleasure to meet you' ]
  await ctx.channel.send(random.choice(responses))

@bot.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

async def setup():
    await bot.wait_until_ready()
    bot.add_cog(Player(bot))

bot.loop.create_task(setup())
keep_alive()
bot.run("YourBotToken")
