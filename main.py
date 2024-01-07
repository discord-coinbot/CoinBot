import random, discord, asyncio, time, math, string, os, datetime, time, aiofiles
import responses
from discord.ext import commands, tasks
from discord.ui import Button, View, Select
from random import sample
from typing import Dict
import topgg
from webserver import keep_alive
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
# from database import *
# db=database.db
# with open("database.py", "r", encoding="windows-1252") as file:
#   content = file.read()
exec(open('database.py').read())
# from database import Database
# db=Database.db

secret_token = os.environ['secret_token']
TOKEN = secret_token

bot = commands.Bot(
  command_prefix=["!","."],
  intents=discord.Intents.all(),
  case_insensitive=True)
bot.remove_command('help')

cancelEmbed = discord.Embed(title="**__Cancel__**",
                            description="Cancelling...",
                            color=discord.Color.red())

for filename in os.listdir("commands"):
  try:
    exec(open(f'commands/{filename}').read())
    print("\033[34m\033[1m"+filename,"\033[0minitialised.")
  except Exception as e:
    print("\033[31m\033[1m"+filename,"\033[0mfailed to initialise.")
    print(e)

uri = "mongodb+srv://CoinBot:coinbot123@coinbot.nqsluqc.mongodb.net/CoinBot?retryWrites=true&w=majority"

mongo_client = MongoClient(uri)
data_link = mongo_client.CoinBot
mongo_link = data_link.Old

load = mongo_link.find_one({"_id": ObjectId("659ad14f86f746aa5da04320")})
db = dict(load)

async def embedify(name, description=None, color=None):
  if "**" not in name:
    name = "**" + name + "**"
  if description==None:
    description=""
  if color == None:
    embed = discord.Embed(title=name,
                          description=description,
                          color=discord.Color.red())
  else:
    embed = discord.Embed(title=name, description=description, color=color)
  return embed

def timeconvert(secondsGiven):
  secondsGiven = int(secondsGiven)
  hours = secondsGiven // 3600
  minutes = (secondsGiven % 3600) // 60
  seconds = (secondsGiven % 3600) % 60
  txt = ""
  if hours != 0:
    txt += f"{hours} hours, "
  if minutes != 0:
    txt += f"{minutes} minutes, "
  if seconds != 0:
    txt += f"{seconds} seconds, "
  return txt
      
async def discordinput(ctx, check, msg=None, timetoquit: int = None):
  if msg != None:
    embed = discord.Embed(title="",
                          description=msg,
                          color=discord.Color.random())
    await ctx.reply(embed=embeed)
  if timetoquit == None:
    timetoquit = 30
  try:
    prompt = await bot.wait_for('message', check=check, timeout=timetoquit)
    return prompt.content.lower()
  except asyncio.TimeoutError:
    return await ctx.reply(
      embed=await embedify("Took too long, cancelling...", ""))

admin = ["469521741744701444","600411237561663498"]
getitems = {
  "rabbit_foot": 50,
  "sugar": 100,
  "glitter": 150,
  "owl_eye": 200,
  "packet_of_blood": 250,
  "lamp": 300,
  "toothpick": 350,
  "cloak": 400,
  "sand": 600,
  "redstone": 650,
  "string": 750,
  "wood": 800,
  "pen": 850,
  "glue": 900,
  "paper": 950,
  "card": 1000,
  "motor": 1025,
  "slurp_juice": 1050,
  "ammo": 1075,
  "bait": 1100,
  "mini": 1200,
  "metal": 1250,
  "mechanical_part": 1275,
  "leather": 1350,
  "yellow_uno_reverse":1400,
  "green_uno_reverse":1450,
  "red_uno_reverse":1500,
  "blue_uno_reverse":1550,
  "gold_part":1570,#
  "+4_uno_card":1610,
  "stick":1800
}

collectable = {
  "hunt": ["golden_hunting_rifle"],
  "fish": ["golden_fishing_rod"],
  "dig": ["golden_shovel"],
  "game": ["golden_playstation"],
  "mine": ["golden_pickaxe"],
  "search": ["golden_shard"],
  "study": ["golden_cgp_textbook"],
  "find": ["golden_spy_glass"],
  "beg": ["golden_statue"],
}

async def collectables(user, command):
  cchance = random.randint(1, 1000000)
  emoji = ""
  obtain = ""
  if cchance == 1000000:
    obtain = "crown"
    emoji = "👑"
  elif cchance >= 999990:
    obtain = "trophy"
    emoji = "🏆"
  elif cchance >= 999890:
    obtain = "medal"
    emoji = "🎖️"
  elif cchance >= 998890:
    obtain = "coin"
    emoji = "🪙"
  if obtain != "":
    inventoryadd(user, obtain, 1)
    return f"\n## You got a {obtain} {emoji} !!!"
  inchance = random.randint(1, 1000)
  if inchance == 1:
    num = random.randint(1, len(collectable[str(command)]))
    item = collectable[command][num-1]
    inventoryadd(user, item, 1)
    return f"\n## You got a {item}. This is a 0.1% chance!!"
  return ""


async def itemsGrind(user):
  itchance = random.randint(1, 1900)
  for item, chance in getitems.items():
    if itchance <= chance:
      obtain = item
      break
  inventoryadd(user, obtain, 1)
  return obtain


def isfloat(num):
  try:
    float(num)
    return True
  except ValueError:
    return False


async def create_code(code=None):
  while True:
    letters = list(string.ascii_letters + string.digits)
    result_str = ''.join(random.choice(letters) for i in range(16))
    result_str = result_str.upper()
    if code != None and code != "":
      result_str = code
    if str(result_str) not in list(db["CODES"].keys()):
      prizes = [
        "commonbox", "commonbox", "commonbox", "commonbox", "rarebox",
        "rarebox", "rarebox", "epicbox", "epicbox", "legendarybox"
      ]
      prize = random.choice(prizes)
      db["CODES"][result_str] = prize
      break
  return result_str


async def THE_GREAT_RESET(message):
  for i in db.keys():
    await message.seend(i + " WAS DELETED")
    del db[i]

def add_commas(number):
  number_string = str(number)
  groups = []
  while number_string:
    groups.append(number_string[-3:])
    number_string = number_string[:-3]
  new_string = ",".join(reversed(groups))
  if "-," in new_string:
    new_string = new_string.replace("-,", "-")
  return new_string

def getDB(dbName):
  return str(db[dbName])

class Links(discord.ui.View):

  def __init__(self):
    super().__init__(timeout=30)
    log = discord.ui.Button(label='Update Log',
                            style=discord.ButtonStyle.url,
                            url='https://web.coin-bot.repl.co/5')
    self.add_item(log)
    commandWeb = discord.ui.Button(label='All Commands',
                                   style=discord.ButtonStyle.url,
                                   url='https://web.coin-bot.repl.co/commands')
    self.add_item(commandWeb)
    status = discord.ui.Button(
      label='Bot Status',
      style=discord.ButtonStyle.url,
      url='https://coinbot.ourdiscordreplbot.repl.co/')
    self.add_item(status)
    groupLink = discord.ui.Button(label='CoinBot Community',
                                  style=discord.ButtonStyle.url,
                                  url='https://discord.gg/6sKNYkRE64')
    self.add_item(groupLink)

@bot.event
async def on_ready():
  await bot.change_presence(
    status=discord.Status.online,
    activity=discord.Game(f"!help | {str(len(bot.guilds))} servers!"))
  print(f'{bot.user} is now running.')
  try:
    synced = await bot.tree.sync()
    bot.loop.create_task(lottery_task())
    # dbl_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEwOTIwMTkwNzI3MDQ3MjUwMTIiLCJib3QiOnRydWUsImlhdCI6MTY4ODkxNDgyOH0.ncuEGOkQOFxSx2DgHoq_bIbmiioXklJD-RoYgOwfwD4"  # set this to your bot's Top.gg token
    # bot.topggpy = topgg.DBLClient(bot, dbl_token, autopost=True, post_shard_count=True)
    #topgg.DBLClient(bot=bot, token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEwOTIwMTkwNzI3MDQ3MjUwMTIiLCJib3QiOnRydWUsImlhdCI6MTY4ODkxNDgyOH0.ncuEGOkQOFxSx2DgHoq_bIbmiioXklJD-RoYgOwfwD4",autopost=False)#guild=discord.Object(id=guild_id))
  except Exception as e:
    print(e)

#cooldown
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    timeleft = "{:.2f}".format(error.retry_after)
    minutes = int(timeleft[:-3]) // 60
    seconds = int(timeleft[:-3]) % 60
    if seconds == 0:
      seconds = 1
    if minutes == 0:
      msg = str(f"Your cooldown ends in {seconds} seconds.")
    else:
      msg = str(
        f"Your cooldown ends in {minutes} minutes and {seconds} seconds.")
    embed = discord.Embed(title="**__Cooldown__**",
                          description="",
                          color=discord.Color.red())
    embed.add_field(name=msg, value="")
    await ctx.reply(embed=embed)
    return "cooldown"
  else:
    print(f"\033[91m\033[1mError Detected:\033[0m\033[91m\n{error}\033[0m")

#db_check
def db_check(object):
  if object not in db:
    db[object] = 0

def inventorycheck(user, amount, item):
  inv=db["inv"+str(user)]
  if item in inv:
    if inv[item]>=amount:
      return True
    else:
      return False
  else:
    return False

def balcheck(user, amount):
  if db[user]>=amount:
    return True
  else:
    return False

#inventory add
def inventoryadd(user, item, amount):
  user=str(user)
  if item in db["inv" + user].keys():
    db["inv" + user][item] += amount
  else:
    db["inv" + user][item] = amount


def inventoryremove(user, item, amount):
  try:
    db["inv" + user][item] -= amount
  except:
    return "Does not have enough"


#!leaderboard
# Function to get the top 10 users based on their coins
def get_leaderboard(list, type):
  ok = {}
  for i in [key for key in db if key.startswith(type)]:
    if "lb" in type:
      a = i.replace(type, "")
      b = a
    else:
      a = i.replace(type, "")
      b = i
    if a in list:
      val = db[b]
      if int(val) != 0:
        ok[a] = int(val)
  leaderboard = sorted(ok.items(), key=lambda x: x[1], reverse=True)
  return leaderboard


def get_bar(num, outof):
  ok = round((num / outof) * 100, 1)

  if ok < 6.25:
    txt = "<:p1n:1113754910861840466><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p3n:1113753573164060732>"
  elif ok < 18.75:
    txt = "<:p1y:1113753834532114432><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p3n:1113753573164060732>"
  elif ok < 31.25:
    txt = "<:p1y:1113753834532114432><:p2y:1113753073249161287><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p3n:1113753573164060732>"
  elif ok < 43.25:
    txt = "<:p1y:1113753834532114432><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p3n:1113753573164060732>"
  elif ok < 56.25:
    txt = "<:p1y:1113753834532114432><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2n:1113753023693475901><:p2n:1113753023693475901><:p2n:1113753023693475901><:p3n:1113753573164060732>"
  elif ok < 68.75:
    txt = "<:p1y:1113753834532114432><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2n:1113753023693475901><:p2n:1113753023693475901><:p3n:1113753573164060732>"
  elif ok < 81.25:
    txt = "<:p1y:1113753834532114432><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2n:1113753023693475901><:p3n:1113753573164060732>"
  elif ok < 93.75:
    txt = "<:p1y:1113753834532114432><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p3n:1113753573164060732>"
  elif ok <= 100:
    txt = "<:p1y:1113753834532114432><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p2y:1113753073249161287><:p3y:1113782343539363960> "
  return txt


class PaginationView(View):
  def __init__(self, author, title, PageSaid, pages, link=None, pfplink=None):
    super().__init__()
    self.page = PageSaid - 1
    self.title = title
    self.pages = pages
    self.link = link
    self.pfplink = pfplink
    self.author = author
    if len(pages) == 1:
      button1 = [x for x in self.children if "prev" in x.custom_id][0]
      button2 = [x for x in self.children if "next" in x.custom_id][0]
      button1.disabled = True
      button2.disabled = True
    elif self.page == 0:
      button1 = [x for x in self.children if "prev" in x.custom_id][0]
      button1.disabled = True
    elif len(pages) - 1 == self.page:
      button2 = [x for x in self.children if "next" in x.custom_id][0]
      button2.disabled = True

  async def interaction_check(self, inter: discord.MessageInteraction) -> bool:
    if inter.user.id != self.author:
      await inter.response.send_message(content="This isn't your command!",
                                        ephemeral=True)
      return False
    return True

  @discord.ui.button(label="◀",
                     style=discord.ButtonStyle.green,
                     custom_id="prev")
  async def prev_button_callback(self, interaction: discord.Interaction,
                                 button: discord.ui.Button):
    button1 = [x for x in self.children if x.custom_id == "next"][0]
    button2 = [x for x in self.children if x.custom_id == "prev"][0]
    if self.page - 1 < len(self.pages) - 1:
      button1.disabled = False
    else:
      button1.disabled = True
    if self.page > 0:
      self.page -= 1
      if self.page > 0:
        button2.disabled = False
      else:
        button2.disabled = True
      if self.link == None:
        embed = discord.Embed(title=self.title,
                              description="",
                              color=discord.Color.green())
      else:
        embed = discord.Embed(title="",
                              description="",
                              color=discord.Color.green())
        embed.set_author(name=f"{self.link}'s Inventory",
                         icon_url=self.pfplink)
      thelist = self.pages["page" + str(self.page + 1)]
      txt = ""
      for i in thelist:
        txt = txt + f"\n{i}"
      embed.add_field(name="", value=txt, inline=False)
      embed.set_footer(text=f"{self.page+1}/{len(self.pages)}")
      await interaction.response.edit_message(embed=embed, view=self)

  @discord.ui.button(label="▶",
                     style=discord.ButtonStyle.green,
                     custom_id="next")
  async def next_button_callback(self, interaction: discord.Interaction,
                                 button: discord.ui.Button):
    button1 = [x for x in self.children if x.custom_id == "prev"][0]
    button2 = [x for x in self.children if x.custom_id == "next"][0]
    if self.page + 1 > 0:
      button1.disabled = False
    else:
      button1.disabled = True
    if self.page < len(self.pages) - 1:
      self.page += 1
      if self.page + 1 < len(self.pages):
        button2.disabled = False
      else:
        button2.disabled = True
      if self.link == None:
        embed = discord.Embed(title=self.title,
                              description="",
                              color=discord.Color.green())
      else:
        embed = discord.Embed(title="",
                              description="",
                              color=discord.Color.green())
        embed.set_author(name=f"{self.link}'s Inventory",
                         icon_url=self.pfplink)
      thelist = self.pages["page" + str(self.page + 1)]
      txt = ""
      for i in thelist:
        txt = txt + f"\n{i}"
      embed.add_field(name="", value=txt, inline=False)
      embed.set_footer(text=f"{self.page+1}/{len(self.pages)}")
      await interaction.response.edit_message(embed=embed, view=self)


# RUNE
runes = [
  "digshards", "gameshards", "mineshards", "studyshards", "searchshards",
  "unbreakingshards"
]  # CHANGE AT COLLECTABLES UPDATE

allitememojis = {
  "wooden_shovel": "🛠️",
  "iron_shovel": "🛠️",
  "diamond_shovel": "🛠️",
  "netherite_shovel": "🛠️",
  "ultimate_shovel": "🛠️",
  "PS2": "🎮",
  "PS3": "🎮",
  "PS4": "🎮",
  "PS5": "🎮",
  "PS6": "🎮",
  "ps2": "🎮",
  "ps3": "🎮",
  "ps4": "🎮",
  "ps5": "🎮",
  "ps6": "🎮",
  "lock_pick": "🔓",
  "bolts": "🔓",
  "lock": "🔒",
  "padlock": "🔒",
  "chains": "🔗",
  "halver": "🌗",
  "doubler": "🌗",
  "textbook": "📖",
  "flashcards": "📰",
  "fifa_mobile": "🎮",
  "mario_kart": "🎮",
  "minecraft": "🎮",
  "fortnite": "🎮",
  "roblox": "🎮",
  "fifa23": "🎮",
  "gta4": "🎮",
  "gta5": "🎮",
  "gta6": "🎮",
  "pickaxe": "🪓",
  "excavator": ":tractor:",
  "hunting_rifle": "🔫",
  "fishing_rod": ":fishing_pole_and_fish:",
  "ultimate_flex": "💪",
  "crown": "👑",
  "trophy": "🏆",
  "medal": "🎖️",
  "coin": "🪙",
  "coal_ore": "🪨",
  "iron_ore": "<:iron_ore:1125016951631130624> ",
  "gold_ore": "<:gold_ore:1125016358170673223>",
  "diamond": "💎",  # 4%
  "saphire": "💍",  # 2%
  "dino_fossil": "🦖",  # 0.4%
  "dragon_wing": "🐲",
  "megalodon_tooth": "🦷",
  "ant": "🐜",
  "mouse": "🐭",
  "pigeon": ":bird:",
  "deer": "🦌",
  "lion": "🦁",
  "mammoth": "🦣",
  "seahorse": "🐎",
  "fish": "🐟",
  "salmon": "🐠",
  "whale": "🐳",
  "horse": "🐎",
  "shark": "🦈",
  "buffalo": "🦬",
  "cow": "🐮",
  "stingray": "🦈",
  "workbench": "⚒️",
  "workbench_lvl_1": "⚒️",
  "brewing_stand": "🧪",
  "craft_box": ":package:",
  "holy_craft_box": "<:holy_craft_box:1125511994758414548>",
  "commonbox": "<:commonbox:1124999919988650076>",
  "uncommonbox": "<:uncommonbox:1131542599707148328>",
  "rarebox": "<:rarebox:1125000949396672512>",
  "epicbox": "<:epicbox:1125001857035681802>",
  "legendarybox": "<:legendarybox:1125001202204168212>",
  "mythicbox": "<:mythicbox:1125000359627198464>",
  "prestigebox": "<:prestigebox:1125002908262465547>",
  "banknote": "🏦",
  "daily": "<:dailybox:1117146276799184986>",
  "green_play_button": "<:ytgreen:1117402510194389075>",
  "silver_play_button": "<:ytsilver:1117404640028397618>",
  "gold_play_button": "<:ytgold:1117402513352695808>",
  "diamond_play_button": "<:ytdiamond:1117404643929116672>",
  "ruby_play_button": "<:ytred:1117404642205237402>",
  "garbage_bag":"🗑️",
  "mop":"🧹",
  "big_mac":"🍔",
  "cutlery":"🍴",
  "driving_licence":"🪪",
  "whiteboard_pen":"🖋️",
  "bitcoin":"🪙",
  "football":"⚽",
  "tesla":"🚘",
  "twitter_logo":"<:twitter:1127163437894602872>",
  "inv_potion":"🧪",
  "strength_potion":"🧪",
  "night_vision_potion":"🧪",
  "speed_potion":"🧪",
  "jump_boost_potion":"🧪",
  "red_uno_reverse":"<:reduno:1130090061824790578>",
  "green_uno_reverse":"<:greenuno:1130090057898926131>",
  "blue_uno_reverse":"<:blueuno:1130090060063191101>",
  "yellow_uno_reverse":"<:yellowuno:1130090056510619708>",
  "bait":"<:bait:1130091461560508466>",
  "glue":"<:gluestick:1130092789728813136>",
  "card":"<:card:1130093170449989722>",
  "sand":"<:sand:1130093174040301640>",
  "redstone":"<:redstone:1130093172735889428>",
  "+4_uno_card":"<a:4uno:1130428534591082547>",
  "metal":"<:metal:1130097237905653781>",
  "string":"<:string:1130095539283841044>",
  "lamp":":diya_lamp:",
  "toothpick":"<:toothpick:1130095010667319337>",
  "cloak":":womans_clothes:",
  "slurp_juice":"<:shield:1130093175449600020>",
  "owl_eye":":owl:",
  "sugar":"<:sugar:1130093177857114193>",
  "paper":"<:paper:1130097494764830790>",
  "glitter":":sparkles:",
  "wood":":wood:",
  "packet_of_blood":"<:packetofblood:1130093179555827722>",
  "ammo":"<:ammo:1130097492558626889>",
  "rabbit_foot":":rabbit2:",
  "pen":"<:pen:1130097485738688573>",
  "stick":"<:Stick:1130097488460796055>",
  "rat":"✨🐀",
  "mechanical_part":"<:mechanicalpart:1130097490847350814>",
  "motor" : "<a:motor:1131334557749215322>",
  "mini" : "<:mini:1130097483448582215>",
  "leather" : "<:leather:1130097487194112000>",
  "gold_part" : ":coin:",
  "golden_fishing_rod" : "<:golden_fishing_rod:1131547290415415376>",
  "golden_shard"  : "<:golden_shard:1131546084838215700>",
  "golden_cgp_textbook"  : "📒",
  "golden_spy_glass"  : "<:golden_spy_glass:1131545001504014397>",
  "golden_pickaxe"  : "<:Gold_Pickaxe:1131335903269355562>",
  "golden_hunting_rifle"  : "<:golden_hunting_rifle:1131549224773894186>",
  "golden_shovel": "<:golden_shovel:1131543920669642822>",
  "golden_playstation": "<:golden_play_station:1131550436999049286>",
  "winning_lottery_ticket" : ":ticket:",
  "iron_ingot": "<:IronIngot:1130556416684458085>",
  "steel_ingot": "<:steelingot:1131333855907938344>",
  "bitcoin":"<:Bitcoin_Logo:1131336565679980596>",
  "wooden_log":"<:woodenlog:1131335435323445339>",
  "wooden_plank":"<:woodenplank:1131335600553869433>",
  
}

allcollectables = ["golden_hunting_rifle", 
                   "golden_fishing_rod", 
                   "golden_shovel", 
                   "golden_playstation", 
                   "golden_pickaxe",
                   "golden_shard",
                   "golden_cgp_textbook",
                   "golden_spy_glass",
                   "golden_statue",
                   "garbage_bag",
                   "mop",
                   "big_mac",
                   "cutlery",
                   "driving_licence",
                   "whiteboard_pen",
                   "bitcoin",
                   "football",
                   "tesla",
                   "twitter_logo",
                   "coin",
                   "crown",
                   "trophy",
                   "medal",
]

potions=["inv_potion",
"strength_potion",
"night_vision_potion",
"speed_potion",
"jump_boost_potion"]

otherCraftItems=[
  "iron_ore",
  "coal_ore",
  "iron_ingot",
  "wooden_log",
  "wooden_plank",
  "steel_ingot",
]

tools = ["wooden_shovel",
         "iron_shovel",
         "diamond_shovel",
         "netherite_shovel",
         "ultimate_shovel",
         "PS2",
         "PS3","PS4","PS5","PS6","pickaxe","excavator","hunting_rifle","fishing_rod","textbook","flashcards","banknote"]

collectables_value={
                   "golden_hunting_rifle":1000000, 
                   "golden_fishing_rod":1000000, 
                   "golden_shovel":1000000, 
                   "golden_playstation":1000000, 
                   "golden_pickaxe":1000000,
                   "golden_shard":1000000,
                   "golden_cgp_textbook":1000000,
                   "golden_spy_glass":1000000,
                   "golden_statue":1000000,
                   "garbage_bag":300000,
                   "mop":300000,
                   "big_mac":300000,
                   "cutlery":300000,
                   "driving_licence":300000,
                   "whiteboard_pen":300000,
                   "bitcoin":300000,
                   "football":300000,
                   "tesla":300000,
                   "twitter_logo":300000,
                   "coin":300000,
                   "crown":10000000,
                   "trophy":3000000,
                   "medal":2500000,
}

# USE
item_list = {
  "inv_potion": 30,
  "speed_potion": 30,
  "night_vision_potion": 30,
  "jump_boost_potion": 30,
}


# SHOP
shop_items = {
  "wooden_shovel": 1000,
  "iron_shovel": 5000,
  "diamond_shovel": 20000,
  "netherite_shovel": 150000,
  "ultimate_shovel": 400000,
  "PS2": 700,
  "PS3": 4000,
  "PS4": 20000,
  "PS5": 150000,
  "PS6": 500000,
  "lock_pick": 50000,
  "bolts": 250000,
  "lock": 50000,
  "chains": 100000,
  "halver": 100000,
  "doubler": 100000,
  "pickaxe": 20000,
  "excavator": 200000,
  "textbook": 10000,
  "flashcards": 10000,
  "ultimate_flex": 1000000,
  "fifa_mobile": 10000,
  "mario_kart": 15000,
  "minecraft": 20000,
  "fortnite": 25000,
  "roblox": 30000,
  "fifa23": 40000,
  "gta4": 50000,
  "gta5": 100000,
  "gta6": 1000000,
  "hunting_rifle": 200000,
  "fishing_rod": 200000,
  "rob": 500000,
  "workbench": 500000,
}

itememojis = {
  "wooden_shovel": "🛠️",
  "iron_shovel": "🛠️",
  "diamond_shovel": "🛠️",
  "netherite_shovel": "🛠️",
  "ultimate_shovel": "🛠️",
  "workbench":"🛠️",
  "PS2": "🎮",
  "PS3": "🎮",
  "PS4": "🎮",
  "PS5": "🎮",
  "PS6": "🎮",
  "lock_pick": "🔓",
  "bolts": "🔓",
  "lock": "🔒",
  "chains": "🔗",
  "halver": "🌗",
  "doubler": "🌗",
  "textbook": "📖",
  "flashcards": "📰",
  "fifa_mobile": "🎮",
  "mario_kart": "🎮",
  "minecraft": "🎮",
  "fortnite": "🎮",
  "roblox": "🎮",
  "fifa23": "🎮",
  "gta4": "🎮",
  "gta5": "🎮",
  "gta6": "🎮",
  "pickaxe": "🪓",
  "excavator": "🎮",
  "hunting_rifle": "🔫",
  "fishing_rod": ":fishing_pole_and_fish:",
  "ultimate_flex": "💪",
  #"rob":"💰"
  # "crown": "👑",
  # "trophy": "🏆",
  # "medal": "🎖️",
  # "coin": "🪙",
}

sellable = {
  "coal_ore": 500,
  "iron_ore": 1000,
  "gold_ore": 2500,
  "diamond": 20000,  # 4%
  "saphire": 50000,  # 2%
  "dino_fossil": 250000,  # 0.4%
  "dragon_wing": 500000,
  "megalodon_tooth": 1000000,
  # 0.2%
  # Huntable
  "ant": 750,
  "mouse": 1000,
  "pigeon": 2000,
  "deer": 10000,
  "lion": 20000,
  "mammoth": 50000,
  # Fishable
  "seahorse": 750,
  "fish": 1500,
  "salmon": 5000,
  "whale": 50000,  # 0.1%
}



sellallitems = {
  "coal_ore": 500,
  "iron_ore": 1000,
  "gold_ore": 2500,
  "diamond": 20000,
  "saphire": 50000,
  "ant": 750,
  "mouse": 1000,
  "pigeon": 2000,
  "cow": 3000,
  "horse": 5000,
  "deer": 7000,
  "buffalo": 10000,
  "cheetah": 13000,
  "lion": 20000,
  "mammoth": 50000,
  "seahorse": 750,
  "fish": 1500,
  "salmon": 2000,
  "stingray": 3000,
  "shark": 7500,
  "whale": 50000,
}





gearitems1 = {
  "Pocket":
  "**5 Leather, 3 String, 100,000 coins**\nDoubles the amount stolen",
  "Bag": "**30 Leather, 10 String, 500,000 coins**\n5x more coins stolen",
}


gearitems = {
  "pocket":{"leather":5,
           "string":3,
           "Coins":200000,
           "description":"Doubles the amount stolen."},
  "bag":{"leather":30,
        "string":10,
        "Coins":500000,
        "description":"5x more coins stolen"},
  "lock_pick":{"toothpick":3,
              "pen":3,
              "Coins":200000,
              "description":"Makes you 2x more likely to succeed"},
  "bolts":{"mechanical_part":5,
           "gold_part":1,
          "Coins":500000,
          "description":"Makes you 5x more likely to succeed"
            },
  "jet":{"mechanical_part":5,
        "motor":1,
         "metal":10,
        "Coins":500000,
        "description":"Makes you 5x less likely to get caught by the police"},
  "uno_skip":{"bait":3,
             "+4_uno_card":3,
             "Coins":350000,
             "description":"Skips the uno reverse"},
  "uno_reverse":{"yellow_uno_reverse":1,
                "blue_uno_reverse":1,
                "green_uno_reverse":1,
                "red_uno_reverse":1,
                "Coins":500000,
                "description":"Play the ultimate uno reverse"},
  "lock":{"metal":5,
          "mechanical_part":1,
         "Coins":250000,
         "description":"Makes the robber 2x less coins"},
  "chains":{"metal":10,
           "glue":5,
           "Coins":350000,
           "description":"Makes the robber get 3x less coins"},
  "vault":{"metal":25,
          "mechanical_part":5,
          "Coins":500000,
          "description":"Makes the robber 5x more likely to fail"},
  "guard_dog":{"police_badge":1,
              "bone":5,
              "Coins":250000,
              "description":"Makes the robber 2x more likely to get caught by the police"},
  "alarm":{"redstone":25,
          "mechaincal_part":5,
          "Coins":500000,
          "description":"Makes the robber 3x more likely to get caught by the police",
          },
}


xp_commands = ["beg", "fish", "hunt", "dig", "game", "mine", "study", "work"]

xp_messages = {}


# CRAFT

craftitems = {
  "iron_ingot": {
    "iron_ore": 1,
    "coal_ore": 1,
    "crafted_item": [1, "iron_ingot"]
  },
  "steel_ingot": {
    "iron_ingot": 2,
    "coal_ore": 1,
    "crafted_item": [2, "steel_ingot"]
  },
  "wooden_log": {
    "wood": 1,
    "stick": 4,
    "crafted_item": [2, "wooden_log"]
  },
  "wooden_plank": {
    "wooden_log": 10,
    "crafted_item": [3, "wooden_plank"]
  },
  "wooden_shovel": {
    "wooden_log": 5,
    "crafted_item": [1, "wooden_shovel"]
  },
  "brewing stand": {
    "blaze_rod": 1,
    "wooden_plank": 2,
    "stick": 10,
    "blaze_powder": 3,
    "crafted_item": [1, "brewing_stand"]
  },
  "level1workbench": {
    "iron_ingot": 100,
    "steel_ingot": 75,
    "wooden_log": 50,
    "wooden_plank": 25,
    "crafted_item": [1, "workbench_lvl_1"]
  },
}
# "Hunting_Rifle":"20 wooden_plank + 20 iron_ingot + ??? -> 1 hunting_rifle",
# "Fishing_Rod":"20 wooden_plank + 20 iron_ingot + ??? -> 1 fishing_rod",
# "Pickaxe":"20 wooden_plank + 20 steel_ingot -> pickaxe"}
craftitems1 = {
  "pickaxe": {
    "wooden_plank": 10,
    "steel_ingot": 20,
    "crafted_item": [1, "pickaxe"]
  },
  "hunting_Rifle": {
    "wooden_plank": 20,
    "iron_ingot": 50,
    "steel_ingot": 50,
    "crafted_item": [1, "hunting_rifle"]
  },
  "fishing_Rod": {
    "wooden_plank": 20,
    "iron_ingot": 20,
    "string": 10,
    "crafted_item": [1, "fishing_rod"]
  },
  "excavator": {
    "motor": 1,
    "metal": 3,
    "redstone": 3,
    "crafted_item": [1, "excavator"]
  },
}
craftitems2 = {
  "fs": {
    "iron_ore": 1,
    "coal": 1,
    "crafted_item": [3, "iron_ingot"]
  },
  "ef": {
    "erwtn": 34,
    "4etg": 1,
    "rdbfht": 2,
    "crafted_item": [2, "iron"],
  },
}
craftitems3 = {
  "as": {
    "iron_ore": 1,
    "coal": 1,
    "crafted_item": [3, "iron_ingot"]
  },
  "cs": {
    "erwtn": 34,
    "4etg": 1,
    "rdbfht": 2,
    "crafted_item": [2, "iron"],
  },
}

craftpotions = {
  "bottle": {
    "sand": 2,
    "coal_ore": 1,
    "crafted_item": [1, "bottle"]
  },
  "inv_potion": {
    "glitter": 1,
    "cloak": 1,
    "bottle": 1,
    "crafted_item": [1, "inv_potion"]
  },
  "strength_potion ": {
    "blood": 1,
    "toothpick": 1,
    "bottle": 1,
    "crafted_item": [1, "strength_potion"]
  },
  "night_vision_potion": {
    "lamp": 1,
    "owl_eye": 1,
    "bottle": 1,
    "crafted_item": [1, "night_vision_potion"]
  },
  "speed_potion": {
    "soap": 1,
    "sugar": 1,
    "bottle": 1,
    "crafted_item": [1, "speed_potion"]
  },
  "jump_boost_potion": {
    "shoes": 1,
    "rabbit_foot": 1,
    "bottle": 1,
    "crafted_item": [1, "jump_boost_potion"]
  },
}


# FIGHT
# def necromancer():
#   global Necromancer
#   Necromancer = {"Attacks":{"Shadow Spike":[3,20,f"{attacker} conjured a spike from the shadows and sent it {defender}'s' way"],
#                           "Shadow Sword":[5,50,f"{attacker} created a shadow sword and sent it at {defender}."],
#                           "Demon Charge":[7,70,f"{attacker}'s' shadows charged {defender} and tore into {defender}, not affected by any defence"]},
#               "Defence":{"Side Step":[3,20,f"{defender} Side Stepped, moving out of the way saving themself {defence} damage"],
#                          "Shadow Shield": [5,50,f"{defender} created a shield from their shadows quick enough, which absorbed {defence} damage"],
#                          "Shadow Walk":[7,100,f"{defender} Shadow Walked away, making {attacker}'s attack miss."]},
#               "Other":{"Disarm":[3,0,f"{attacker} used their shadows to disarm {defender}, making their next turn 50% less effective."],
#                        "Shadow Hold":[4,20,f"{attacker}'s shadows wrapped around {defender}, and dealing 20 damage and making
# {defender} unconscious and lose a turn."],
#                        "Darkness":[5,0,f"{attacker}'s shadows engulfed {defender} blinding them and making them loose 3 energy and 20 health."]},
#               "Special":{"Death Touch":[7,99,f"{attacker} released a bubble and brought it back into himself, (nearly) killing everyone it touched."]}}
# NOTE: demon charge and shadow walk, demon charge still does damage

# elemental = {"Attacks":{"Fire Stream":[],
#                         "Choke":[],
#                         "Wrath Of The Wind":[]},
#              "Defence":{"Double Jump":[],
#                         "Gust":[],
#                         "Stone Henge":[]},
#              "Other":{"Water Splash":[],
#                       "Vine Grip":[],
#                       "Tsunami":[]},
#              "Special":{"Nature's blessing":[]}

# Adept = {"Attacks":{"Sword Swipe":[],
#                     "Energy Throw":[],
#                     "Sacred Stab":[]},
#           "Defence":{"Block":[],
#                      "Self Heal":[],
#                      "Mirror":[]},
#           "Other":{"Illusion":[],
#                    "Gravity Flip":[],
#                    "":[]},
#          "Special": {"Clone":[]}

necromancer = [
  "Shadow Spike", "Shadow Sword", "Demon Charge", "Side Step", "Shadow Shield",
  "Shadow Walk", "Disarm", "Shadow Hold", "Darkness", "Death Touch"
]
elemental = [
  "Fire Stream",
  "Choke",
  "Wrath Of The Wind",
  "Double Jump",
  "Gust",
  "Stone Henge",
  "Water Splash",
  "Vine Grip",
  "Tsunami",
  "Nature's Blessing",
]  # idk if u can




restaurantImages = {
  "Default":
  "https://cdn.discordapp.com/attachments/1124968161117212684/1124968698323681290/normal.png",
  "McDonalds":
  "https://cdn.discordapp.com/attachments/1124968161117212684/1124968697216385097/ok1.png",
  "Modern":
  "https://cdn.discordapp.com/attachments/1124968161117212684/1124968697979752468/ok.png",
  "Hell":
  "https://cdn.discordapp.com/attachments/1124968161117212684/1124968696788570122/ok2.png",
  "Heaven":
  "https://cdn.discordapp.com/attachments/1124968161117212684/1124968696448815194/ok3.png",
  "Nightmare":
  "https://cdn.discordapp.com/attachments/1124968161117212684/1124968697627414589/dark.png",
}

bpquests = {
  "Commands Ran": [30, 60, 80],
  "Digs Ran": [30, 60, 80],
  "Begs Ran": [30, 60, 80],
  "Fishes Ran": [30, 60, 80],
  "Mines Ran": [30, 60, 80],
  "Studies Ran": [30, 60, 80],
  "Hunts Ran": [30, 60, 80],
  "Searches Ran": [30, 60, 80],
}

bpRewards = {}
for i in range(1, 100):
  if i % 100 == 0:
    bpRewards[i] = [
      "xbox_mini_fridge", "legendarybox", "holy_craft_box", "craft_box"
    ]
  elif i % 50 == 0:
    bpRewards[i] = ["legendarybox", "holy_craft_box", "craft_box"]
  elif i % 25 == 0:
    bpRewards[i] = ["legendarybox"]
  elif i % 15 == 0:
    bpRewards[i] = ["rarebox"]
  elif i % 5 == 0:
    bpRewards[i] = ["craft_box"]
  elif i > 62:
    bpRewards[i] = ["commonbox"]
  elif i > 30 and i % 2 == 0:
    bpRewards[i] = ["commonbox"]



# CLANS
weapons = {"wooden_sword": [100, 25000]}
armour = {"leather_armour": [100, 25000]}
research = {1: [250000, "redstone", 5, "brick", 10, "mechanical_part", 3]}


# # This example uses topggpy's webhook system.
# bot.topgg_webhook = topgg.WebhookManager(bot).dbl_webhook("/dblwebhook", "password")

# # The port must be a number between 1024 and 49151.
# bot.topgg_webhook.run(5000)  # this method can be awaited as well





# @bot.event
# async def on_dbl_vote(data):
#     print("here")
#     """An event that is called whenever someone votes for the bot on Top.gg."""
#     try:
#       if data["type"] == "test":
#           # this is roughly equivalent to
#           # `return await on_dbl_test(data)` in this case
#           return bot.dispatch("dbl_test", data)
    
#       print(f"Received a vote:\n{data}")
#     except:
#       user_id = int(data['user'])
#       user = bot.get_user(user_id)

#       if user:
#           await user.send("Thank you for voting! Your support is greatly appreciated.")


# @bot.event
# async def on_dbl_test(data):
#     """An event that is called whenever someone tests the webhook system for your bot on Top.gg."""
#     print(f"Received a test vote:\n{data}")

# This example uses topggpy's webhook system.
# bot.topgg_webhook = topgg.WebhookManager(bot).dbl_webhook("/dblwebhook", "password")

# # The port must be a number between 1024 and 49151.
# bot.topgg_webhook.run(5000)  # this method can be awaited as well


# @bot.event
# async def on_dbl_vote(data):
#     """An event that is called whenever someone votes for the bot on Top.gg."""
#     if data["type"] == "test":
#         # this is roughly equivalent to
#         # `return await on_dbl_test(data)` in this case
#         return bot.dispatch("dbl_test", data)

#     print(f"Received a vote:\n{data}")


# @bot.event
# async def on_dbl_test(data):
#     """An event that is called whenever someone tests the webhook system for your bot on Top.gg."""
#     print(f"Received a test vote:\n{data}")
# RUN BOT
keep_alive("yes")
bot.run(TOKEN)
