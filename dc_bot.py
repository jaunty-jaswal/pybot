# -*- coding: utf-8 -*-
"""
bot
"""

import discord
import os
import requests
import json
import random
from chatterbot.trainers import ChatterBotCorpusTrainer
import pandas as pd
from replit import db
from keep_alive import keep_alive
from dotenv import load_dotenv
from discord.ext import commands,tasks
from discord.utils import get
from discord import FFmpegPCMAudio as ff
from discord import TextChannel
from youtube_dl import YoutubeDL
import youtube_dl
import giphy_client
from giphy_client.rest import ApiException
import random
import asyncio
from datetime import date, datetime
import os, platform
import emoji
from chatterbot import ChatBot
import music
from PIL import Image
from io import BytesIO

import spacy

















try:
    import textacy.extract
except ImportError:
    try:
        if platform.system().lower().startswith('win'):
            os.system("pip install textacy")
        else:
            os.system("pip install textacy")
    except Exception as e:
        print("Error:", e)
        exit()

client = commands.Bot(command_prefix="!")
youtube_dl.utils.bug_reports_message = lambda: ''

@client.command(name = "wanted")
async def wanted(ctx,user:discord.Member = None):
  if user == None:
    user = ctx.author
  lt = ["want.jpg"]
  wanted = Image.open(random.choice(lt))
  asset = user.avatar_url_as(size = 128)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pfp = pfp.resize((380,331))
  wanted.paste(pfp,(107,242))
  wanted.save("lol.jpg")
  await ctx.send(file = discord.File("lol.jpg"))

@client.command(name="selmon",aliases = ["salmon","Selmon","Salmon","bhoi","bhai","Bhai","Bhoi","Selmon bhoi","Salmon bhoi"])
async def selmon(ctx):
  l = ["sel1.jpg","sel2.jpg","sel3.jpg","sel4.jpg","sel5.jpg","sel6.jpg","sel7.jpg","sel8.jpg","sel9.jpg","sel10.jpg","sel11.jpg","sel12.jpg","sg1.gif","sg2.gif","sg3.gif","sg4.gif","sg5.gif","sg6.gif","sg7.gif","sg8.gif","sg9.gif","sg10.gif","sg11.gif","sg12.gif","sg13.gif","sg14.gif","sg15.gif","sg16.gif","sg17.gif","sg18.gif","sg19.gif","sg20.gif"]
  with open(random.choice(l),"rb") as f:
    file = discord.File(f)
  await ctx.send(file=file)




st = ["soothing music","sounds in kitchen","traffic sounds","sleep music","my owners voice","your commands","nothing","universes secrets","har har mahadev","bhajan","dogs barking on road","cooker whistling"]



youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

@client.command(name="date")
async def _time(ctx):
  global times_used
  from datetime import date, datetime

  now = datetime.now()

  if (now.strftime("%H") <= "12"):
    am_pm = "AM"
  else:
    am_pm = "PM"

  datetime = now.strftime("%m/%d/%Y, %I:%M")

  await ctx.send("Current Time:" + ' '  + datetime + ' ' + am_pm)
  times_used = times_used + 1
def jokes():
  response = requests.get("https://api.chucknorris.io/jokes/random")
  
  json_data = json.loads(response.text)
  return(json_data['value'])
def motivate():
  response = requests.get("https://zenquotes.io/api/random")
  data = json.loads(response.text)
  return (data[0]['q'] +"  -said by - "+ data[0]['a'])

sad = ["sad","dukhi","Dukhi","Sad","bad","Bad","cry","pain","dead","bekar","not good"]
happy = ["kush ho jaa","Cheer up!!","no need to cry","everything is fine","we will rock someday","har andhere ke baad ujala aata hai "]
hello = ["hello","Hello","HELLO","hEllo"]
tatti = ["meri khaa le","karle jaake fir","abhi karke deta hoon","abe jaa hagedu","dast hai tu"]
word = ["tatti","Tatti","gu","dast","hagedu","haggu"]
reply = ["hello","hii","hii firend","wazz up","yo!!","hows ya?","kaise ho sir","hello mate","heya","hieeee"]
d = pd.read_csv("sen.txt",delimiter = ".")
import pandas as pd
search_text = " "
  
# creating a variable and storing the text
# that we want to add
replace_text = ","
  
# Opening our text file in read only
# mode using the open() function
with open(r'sen.txt', 'r', encoding="utf8") as file:
  
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()
  
    # Searching and replacing the text
    # using the replace() function
    data = data.replace(search_text, replace_text)
  
# Opening our text file in write only
# mode to write the replaced content
with open(r'sen.txt', 'w', encoding="utf8") as file:
  
    # Writing the replaced data in our
    # text file
    file.write(data)

dat = pd.read_csv("sen.txt",delimiter = ",")
z = list()
for i in dat:
    z.append(i)



x = list()
for i in range(1,100):
  x.append(i)
pic = ["im1.jpg","im2.jpg","im3.jpg","im4.jpg","im5.jpg","im6.jpg","im7.jpg","im8.jpg","im9.jpg"]
pic_2=["vil/1.jpg","vil/2.jpg","vil/3.jpg","vil/4.jpg","vil/5.jpg","vil/6.jpg","vil/7.jpg","vil/8.jpg","vil/10.jpg","vil/11.jpg","vil/12.jpg","vil/13.jpg","vil/14.jpg","vil/15.jpg","vil/16.jpg","vil/17.jpg","vil/18.jpg","vil/19.jpg","vil/20.jpg","vil/21.jpg","vil/22.jpg","vil/23.jpg","vil/24.jpg","vil/25.jpg","vil/26.jpg","vil/27.jpg","vil/28.jpg","vil/31.jpg","vil/29.jpg","vil/30.jpg","vil/32.jpg","vil/33.jpg","vil/34.jpg","vil/35.jpg","vil/36.jpg","vil/41.jpg","vil/37.jpg","vil/38.jpg","vil/39.jpg","vil/40.jpg","vil/42.jpg","vil/44.jpg","vil/43.jpg","vil/51.jpg","vil/52.jpg","vil/53.jpg","vil/54.jpg","vil/45.jpg","vil/46.jpg","vil/47.jpg","vil/48.jpg","vil/49.jpg","vil/50.jpg"]
sound = ["sounds/1.mp3","sounds/2.mp3","sounds/3.mp3","sounds/4.mp3","sounds/5.mp3","sounds/6.mp3","sounds/7.mp3","sounds/8.mp3","sounds/9.mp3","sounds/10.mp3","sounds/11.mp3","sounds/12.mp3","sounds/13.mp3","sounds/14.mp3","sounds/15.mp3","sounds/16.mp3","sounds/17.mp3","sounds/18.mp3","sounds/19.mp3","sounds/20.mp3","sounds/21.mp3","sounds/22.mp3","sounds/23.mp3","sounds/24.mp3","sounds/25.mp3","sounds/26.mp3","sounds/27.mp3","sounds/28.mp3","sounds/29.mp3","sounds/30.mp3","sounds/31.mp3","sounds/32.mp3","sounds/33.mp3","sounds/34.mp3","sounds/35.mp3"]
@client.command(name = "perky")
async def perk(ctx):
 
  
  with open(random.choice(pic), 'rb') as f:
    picture = discord.File(f)
    await ctx.send(file=picture)
@client.command(name = "fam") 
async def family(ctx):
 
  
  with open(random.choice(pic_2), 'rb') as f:
    picture = discord.File(f)
    await ctx.send(file=picture)
@client.command(name="random")
async def _command(ctx):
    
       await ctx.send(random.choice(z)) 

  



# coding=utf8
emoj = ['✢', '✣', '✤', '✥', '✦', '✧', '★', '☆', '✯', '✡︎', '✩', '✪', '✫', '✬', '✭', '✮', '✶', '✷', '✵', '✸', '✹', '→', '⇒', '⟹', '⇨', '⇾', '➾', '⇢', '☛', '☞', '➔', '➜', '➙', '➛', '➝', '➞', '♠︎', '♣︎', '♥︎', '♦︎', '♤', '♧', '♡', '♢', '♚', '♛', '♜', '♝', '♞', '♟', '♔', '♕', '♖', '♗', '♘', '♙', '⚀', '⚁', '⚂', '⚃', '⚄', '⚅', '🂠', '⚈', '⚉', '⚆', '⚇', '𓀀', '𓀁', '𓀂', '𓀃', '𓀄', '𓀅', '𓀆', '𓀇', '𓀈', '𓀉', '𓀊', '𓀋', '𓀌', '𓀍', '𓀎', '𓀏', '𓀐', '𓀑', '𓀒', '𓀓', '𓀔', '𓀕', '𓀖', '𓀗', '𓀘', '𓀙', '𓀚', '𓀛', '𓀜', '𓀝❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '💔', '❣️', '💕', '💞', '💓', '💗', '💖', '💘', '💝', '💟', '☮️', '✝️', '☪️', '🕉', '☸️', '✡️', '🔯', '🕎', '☯️', '☦️', '🛐', '⛎', '♈️', '♉️', '♊️', '♋️', '♌️', '♍️', '♎️', '♏️', '♐️', '♑️', '♒️', '♓️', '🆔', '⚛️', '🉑', '☢️', '☣️', '📴', '📳', '🈶', '🈚️', '🈸', '🈺', '🈷️', '✴️', '🆚', '💮', '🉐', '㊙️', '㊗️', '🈴', '🈵', '🈹', '🈲', '🅰️', '🅱️', '🆎', '🆑', '🅾️', '🆘', '❌', '⭕️', '🛑', '⛔️', '📛', '🚫', '💯', '💢', '♨️', '🚷', '🚯', '🚳', '🚱', '🔞', '📵', '🚭', '❗️', '❕', '❓', '❔', '‼️', '⁉️', '🔅', '🔆', '〽️', '⚠️', '🚸', '🔱', '⚜️', '🔰', '♻️', '✅', '🈯️', '💹', '❇️', '✳️', '❎', '🌐', '💠', 'Ⓜ️', '🌀', '💤', '🏧', '🚾', '♿️', '🅿️','🈳', '🈂️', '🛂', '🛃', '🛄', '🛅', '🚹', '🚺', '🚼', '⚧', '🚻', '🚮', '🎦', '📶', '🈁', '🔣', 'ℹ️', '🔤', '🔡', '🔠', '🆖', '🆗', '🆙', '🆒', '🆕', '🆓', '0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟', '🔢', '#️⃣', '*️⃣', '⏏️', '▶️', '⏸', '⏯', '⏹', '⏺', '⏭', '⏮', '⏩', '⏪', '⏫', '⏬', '◀️', '🔼', '🔽', '➡️', '⬅️', '⬆️', '⬇️', '↗️', '↘️', '↙️', '↖️', '↕️', '↔️', '↪️', '↩️', '⤴️', '⤵️', '🔀', '🔁', '🔂', '🔄', '🔃', '🎵', '🎶', '➕', '➖', '➗', '✖️', '♾', '💲', '💱', '™️', '©️', '®️', '〰️', '➰', '➿', '🔚', '🔙', '🔛', '🔝', '🔜', '✔️', '☑️', '🔘', '🔴', '🟠', '🟡', '🟢', '🔵', '🟣', '⚫️', '⚪️', '🟤', '🔺', '🔻', '🔸', '🔹', '🔶', '🔷', '🔳', '🔲', '▪️', '▫️', '◾️', '◽️', '◼️', '◻️', '🟥', '🟧', '🟨', '🟩', '🟦', '🟪', '⬛️', '⬜️', '🟫', '🔈', '🔇', '🔉', '🔊', '🔔', '🔕', '📣', '📢', '👁🗨', '💬', '💭', '🗯', '♠️', '♣️', '♥️', '♦️', '🃏', '🎴', '�⌚️', '📱', '📲', '💻', '⌨️', '🖥', '🖨', '🖱', '🖲', '🕹', '🗜', '💽', '💾', '💿', '📀', '📼', '📷', '📸', '📹', '🎥', '📽', '🎞', '📞', '☎️', '📟', '📠', '📺', '📻', '🎙', '🎚', '🎛', '🧭', '⏱', '⏲', '⏰', '🕰', '⌛️', '⏳', '📡', '🔋', '🔌', '💡']
x = list()
i = 0
      
jj = ["Jaunty","jaunty","Shantanu","SRJ","srj","Shantanu"]

# To get the exception

#@client.command(name = "say it")
#async def _command(ctx):
    # code
 #   try:
  #      msg = await client.wait_for("message", check=check, timeout=30) # 30 seconds to reply
   # except asyncio.TimeoutError:
    #    await ctx.send("Sorry, you didn't reply in time!") 
  
def func(c,d):
        c.append(d)
       
c_ = 0
import math
@client.command(name = "clear")
@commands.has_permissions(manage_messages=True)
async def clear(ctx,am =0):
  await ctx.channel.purge(limit = am+1)
@client.command(name="ping")
async def _ping(ctx):
  x = client.latency
  await ctx.send(f"Ping: {math.trunc(x*1000)}ms")
r = ["sond.jpg","sond2.jpg"]

@client.event
async def on_ready():
  change.start()
  print("{0.user} is ready".format(client))
@client.event
async def on_message(message):
      if message.author == client.user:
        return
      if (  message.author.bot): 
        return
      if message.content.startswith('hello'):
        await message.channel.send("hello there!!")
      if message.content.startswith('hi'):
        await message.channel.send("hello friend!!")
      if message.content.startswith('hey'):
        await message.channel.send("hola")
      if message.content.startswith('hii'):
        await message.channel.send("hiiiii!!")  
      if message.content.startswith('!cn'):
        joke = jokes()
        await message.channel.send(joke)
      if message.content.startswith('!quote'):

        jk = motivate()
        await message.channel.send(jk)
      l = ["soondhi","mishti","mishthi","Mishthi","Mishti","Soondhi","Adhvika","adhvika","sondhi","Sondhi"] 
      if any(i in message.content for i in l):
        with open(random.choice(r), 'rb') as f:
          picture = discord.File(f)
        await message.channel.send(file=picture)
      if any(i in message.content for i in jj):
        with open("j.gif", 'rb') as f:
          picture = discord.File(f)
        await message.channel.send(file=picture)
      if message.content.startswith("selmon bhoi"):
        await message.channel.send("stay away from footpath!!")
      if any(i in message.content for i in sad):
        await message.channel.send(random.choice(happy))
      gm = ["gm","Gm","GM","Goodmorning","goodmorning","Good morning","good night","Goodnight","good morning"]
      af = ["Good afternoon","good afternoon","goodafternoon","Goodafternoon"]
      gn = ["Goodnight","gn","Gn","GN","goodnight","good night","Goodnight"]
      if any(i in message.content for i in word):
        await message.channel.send(random.choice(tatti))
      if any(i in message.content for i in hello):
        await message.channel.send(random.choice(reply))
      if message.content.startswith("name"):
        await message.channel.send(f"my name  = {client.user.name} or u can call me super poochoo!!")
      if message.content.startswith("poochoo"):
        await message.channel.send("hehe...hello")
      if message.content.startswith("number"):
        await message.channel.send(random.choice(x))
      if any(i in message.content for i in gm):
        await message.channel.send(f" good morning {message.author.name} ")
      if any(i in message.content for i in af):
        await message.channel.send(f"good afernoon  {message.author.name}")
      if any(i in message.content for i in gn):
        await message.channel.send(f"good night  {message.author.name} ")
      if message.content.startswith('sorry'or "Sorry"):
        await message.channel.send("koi na")
        await message.add_reaction(emoji = random.choice(emoj))
      await client.process_commands(message)
      s = ["!sounds","!sound"]
      if any (i in message.content for i in s):
        with open(random.choice(sound) , "rb") as f:
          file = discord.File(f)
        await message.channel.send(file = file)
      sit = ["perky/sit_2.jpg","perky/sit_3.jpg","perky/sit.jpg"]
      sleep = ["perky/sleep.jpg","perky/sleep_2.jpg"]
      if message.content.startswith("perky sit"):
        global c
        if c==3:
          await message.content.send("i sleeping do not disturb")
          c=0
        else:
          with open(random.choice(sit) ,"rb") as f:
            file = discord.File(f)
       
          await message.channel.send("ok i m sitting now")
          await message.channel.send(file = file)     
 
       
      if message.content.startswith("perky sleep"):
        
       
        c = c+1  
        with open(random.choice(sleep) ,"rb") as f:
          file = discord.File(f)
        
        await message.channel.send("ok i m sleeping now, goodnight!")
        

        await message.channel.send(file = file)
      cod = ["The coderpedia","Coderpedia","coderpedia","the coderpedia"]
      cod_2 = ["cod.jpg","cod2.jpg"]
      dd = ["sirji","sirji zindabad","xhivam!!","ole maata","chingum","sibum"]
      if any(i  in message.content for i in cod):
        with open(random.choice(cod_2),"rb") as f:
          file = discord.File(f)
        await message.channel.send(file = file)
        
        await message.channel.send(random.choice(dd))
      chela = ["rishu","tidda","chela","dast chela","noob chela","hagedu chela","bahut jayada hagne waala-->rishu" ]
      cc = ["chela","Chela","Chele","chele"]
      cc_1 = ["chela.jpg"]
      if any(i in message.content for i in cc):
        await message.channel.send(random.choice(chela))
        with open(random.choice(cc_1),"rb") as f:
          pic = discord.File(f)
        await message.channel.send(file = pic)
      async def on_member_join(member):
        c = discord.utils.get(member.guild.channels,name = 'general')
        await c.send(f"Welcome {member.mention}!!! to Anthem...use '!info' for help")

@tasks.loop(seconds = 120)
async def change():
  await client.change_presence(activity = discord.Activity(type=discord.ActivityType.listening,name = random.choice(st)))
c1 = 0
@client.command(name= "sleep")
async def sleep(ctx):
  sleep = ["perky/sleep.jpg","perky/sleep_2.jpg"]
  global c1
  print(c1)
  if c1<1:
    
    c1 = c1+1
    await ctx.send("sleep time!!")
    with open(random.choice(sleep),"rb") as f:
      file = discord.File(f)
    global c_
    c_ = c_+1  
    await ctx.send(file = file)
    await ctx.send("sleeping for 10 seconds straight")
    await ctx.message.add_reaction(emoji = random.choice(emoj))
    await asyncio.sleep(10)
    c1 = 0
    await ctx.send("i m awake and ready to play 🐕🐕🐕 !!")
    c_ = 0
  else:
    await ctx.send(r"sleeping😴💤💤💤💤")
wag = ["wag_2.gif","wag.gif"]
c2 = 0
ll = [" i m tired 😩","please hold on 🥺","thakk gaya hoon 🥵sabar karo","hold on i m tires🤧","aah, i m exhausted😿","wait plzzzz🤒","hey !!i m tired🐶"," its making me feel drowsy😵‍💫","time plzz,i wanna fart😮‍💨,‍💨💨💨💨💨💨💨"]
@client.command(name = "sit")
async def sit(ctx):
  sit = ["perky/sit_2.jpg","perky/sit_3.jpg","perky/sit.jpg"]
  global c_
  if(c_<1):
       
    global c2
    c2 = c2+1
    if c2==3:
      
      await ctx.send(random.choice(ll))
      await asyncio.sleep(10)
      c2=0
      with open(random.choice(wag),"rb") as f:
        file = discord.File(f)
      await ctx.send("i m pumped up!!")  
      await ctx.send(file = file)
      await ctx.send("lets playaaaayyyy!!")
    elif c2>=4:
      return
    else:
      await ctx.send("im sitting!!") 
      with open(random.choice(sit),'rb') as f:
        file = discord.File(f)
      
      await ctx.send(file = file)
  else:
    await ctx.send(r"😴😴😴😴😴😴😴") 
    await asyncio.sleep(10)
    
    
    c_ = 0  
@client.command(name = "emoji")
async def em(ctx):
  await ctx.send(random.choice(emoj))      
@client.command(name ="support")
async def c(ctx):

    await ctx.send("!ping = for knowing the user ping\n!fam-->for family photos\n!perky = for viewing my photos\n!random-->for any random sentence\n!cn = for chuck norris jokes\n!quote-->for motivational quotes\nperky sit = i will sit\nperky stand = i will stand\n!gif for random gifs")

mq =[]


@client.command("gif")
async def gif(ctx,*,q="ye lo gif"):

    api_key="mPABYJBnybZ4vnY4CSHCvN0O74FWKfgD"
    api_instance = giphy_client.DefaultApi()

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)



@client.command(name = "credit")
async def credit(ctx):
  await ctx.send("made by = SRJ\nfor = ANthem Clan\ncoded in = Python")

@client.command(name='join')                 
async def join(ctx):
   
    if not ctx.message.author.voice:
      await ctx.send(f"{ctx.message.author} connect to a voice channel first")
    else :
      channel = ctx.message.author.voice.channel
      if ctx.voice_client is None:
        await channel.connect()
        await ctx.send(f"successfully connected to {channel}")
      else :
       await ctx.voice_client.move_to(channel)
       await ctx.send(f"successfully moved to {channel}")
    


@client.command(name = "dc",aliases = ["leave","disconnect"])
async def disconnect(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send(f"successfully disconnected from voice channel")





    
FFMPEG_OPTIONS = {'options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn' }

YDL_OPTIONS = {
  
  'format': 'bestaudio/best',
  'restrictfilenames': True,
  'noplaylist': True,
  'nocheckcertificate': True,
  'ignoreerrors': False,
  'logtostderr': False,
  'quiet': True,
  'out':'%(extractor)s-%(id)s-%(title)s.%(ext)s',
  'no_warnings': True,
  'default_search': 'auto',
  'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
    }
ytdl = youtube_dl.YoutubeDL(YDL_OPTIONS)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
            loop = loop or asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

            if 'entries' in data:
                # take first item from a playlist
                data = data['entries'][0]

            filename = data['url'] if stream else ytdl.prepare_filename(data)
            return cls(discord.FFmpegPCMAudio(filename, **FFMPEG_OPTIONS), data=data)
songs = []
counter = 0
@client.command(name = "play",aliases = ["p", " p"])
async def play(ctx,*,url):

  
        global songs
        #main part here
        server = ctx.message.guild
        voice_channel = server.voice_client
        songs.append(url) 
        await ctx.send(f"`{url}` added to queue..")
        async with ctx.typing():
          global counter
          
          for c in range(counter,len(songs)):
            
            
            player = await YTDLSource.from_url(url = songs[c],loop = client.loop)
            server.voice_client.play(player,after = lambda e:print("error:") if e else None)
            del(songs[0])
          await ctx.send(f"****now playing {player.title} ***")
            
            
            










  

     
@client.command(name = "skip")
async def skip(ctx):
  #global songs
  global counter
  counter = counter + 1
  
  ctx.send("skipping")
  

@client.command(name ="pause")
async def pause(ctx):
  await ctx.send("paused ⏸️")
  await ctx.voice_client.pause()
  

@client.command(name ="resume")
async def res(ctx):
  await ctx.send("resumed 🎶")
  await ctx.voice_client.resume()
  
@client.command(name = "stop")
async def stop(ctx):
  await ctx.send("stopping...")
  global counter 
  counter = 0
  
  await ctx.voice_client.stop()

@client.command(name = 'remove',aliases =["r","del"])
async def remove(ctx,number):
  global songs
  try:
    del(songs[int(number)])
    await ctx.send(f"remaining queue `{songs}`")
  except:
    ctx.send("queue already empty or number out of range")
@client.command(name = "q",aliases = ["vq","queue","view"])
async def view(ctx):
  global songs
  await ctx.send(f"`{songs}`")


@client.command(name = "tell",aliases = ['t'])
async def tell(ctx,*,word):
  
  

  # Load the large English NLP model
  nlp = spacy.load('en_core_web_md')

  # The text we want to examine
  text = str(word)
  doc1 = nlp(text)
  s = "PERSON:      People, including fictional.\nNORP:        Nationalities or religious or political groups.\nFAC:         Buildings, airports, highways, bridges, etc.\nORG:         Companies, agencies, institutions, etc.\nGPE:         Countries, cities, states.\nLOC:         Non-GPE locations, mountain ranges, bodies of water.\nPRODUCT:     Objects, vehicles, foods, etc. (Not services.)E\nVENT: Named hurricanes, battles, wars, sports events, etc.\nWORK_OF_ART: Titles of books, songs, etc.\nLAW:         Named documents made into laws.\nLANGUAGE:    Any named language.\nDATE:        Absolute or relative dates or periods.\nTIME:        Times smaller than a day.\nPERCENT:     Percentage, including ”%“.\nMONEY:       Monetary values, including unit.\nQUANTITY:    Measurements, as of weight or distance.\nORDINAL:     “first”, “second”, etc.\nCARDINAL:    Numerals that do not fall under another type."
  # Parse the text with spaCy. This runs the entire pipeline.
  await ctx.send("i will tell what your sentence contains")
  for i in range(0,3):
    await asyncio.sleep(2)

    await ctx.send(".")
  await ctx.send(f"refer to __>\n{s}")
  await ctx.send("######################################## ")
  for i in range(0,4):
    await ctx.send(".")
  await ctx.send("your sentece contains>>>>>>>>")
  for entity in doc1.ents:
    await ctx.send(f"{entity.text} ({entity.label_})")
  await ctx.send("i hope they are right")
  
keep_alive()
client.run(os.getenv('code'))

