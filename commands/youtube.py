
# YOUTUBE
ytitems = [
  "camera",
  "microphone",
  "pc",
  "monitor",
  "mouse",
  "keyboard",
  "headset",
  "green_screen",
]

yttypes = [
  "dirt",
  "plastic",
  "copper",
  "steel",
  "iron",
  "gold",
  "diamond",
  "emerald",
  "saphire",
]

ytupgrade = {
  "dirt": 100,
  "plastic": 200,
  "copper": 400,
  "steel": 800,
  "iron": 1600,
  "gold": 3200,
  "diamond": 6400,
  "emerald": 12800,
  "saphire": "Best",
}


@bot.command(name="youtube", aliases=["yt"])
async def youtube(ctx, type, item: str = None):
  if item == None:
    item = ""
  user = ctx.author.id
  if "youtube" not in db[user]:  #total subs
    db[user]["youtube"]["subs"] = 0  #total subs
    db[user]["youtube"]["views"] = 0  #total views
    db[user]["youtube"]["vidamount"] = 0  #total videos
    db[user]["youtube"]["ytvidtime"] = 0
    db[user]["youtube"]["ytlikes"] = 0  #total bal
    db[user]["youtube"]["ytbank"] = 0  #total bal
    db[user]["youtube"]["videos"] = {}  # videos list
    db[user]["youtube"]["stream"] = {}  # streams list
    db[user]["youtube"]["streamamount"] = 0  # streams amount
    db[user]["youtube"]["ytplaques"] = {
      "<:ytgreen:1117402510194389075>": [False, 1000],
      "<:ytsilver:1117404640028397618>": [False, 100000],
      "<:ytgold:1117402513352695808>": [False, 1000000],
      "<:ytdiamond:1117404643929116672>": [False, 10000000],
      "<:ytred:1117404642205237402>": [False, 1000000000],
    }
    db[user]["youtube"]["ytitems"] = {
      "camera": "dirt",
      "microphone": "dirt",
      "pc": "dirt",
      "monitor": "dirt",
      "mouse": "dirt",
      "keyboard": "dirt",
      "headset": "dirt",
      "green_screen": "dirt",
    }
  db[user]["youtube"]["ytplaques"]["<:ytred:1117404642205237402>"][1] = 100000000
  convertdict = {
    "<:ytgreen:1117402510194389075>": "green_play_button",
    "<:ytsilver:1117404640028397618>": "silver_play_button",
    "<:ytgold:1117402513352695808>": "gold_play_button",
    "<:ytdiamond:1117404643929116672>": "diamond_play_button",
    "<:ytred:1117404642205237402>": "ruby_play_button",
  }
  convertlink = {
    "<:ytgreen:1117402510194389075>":
    "https://cdn.discordapp.com/attachments/1092060572369039400/1117401769836818503/New_Project_58.png",
    "<:ytsilver:1117404640028397618>":
    "https://cdn.discordapp.com/attachments/1092060572369039400/1117882049269858405/New_Project_62.png",
    "<:ytgold:1117402513352695808>":
    "https://cdn.discordapp.com/attachments/1092060572369039400/1117401770306584576/New_Project_56.png",
    "<:ytdiamond:1117404643929116672>":
    "https://cdn.discordapp.com/attachments/1092060572369039400/1117404355683950612/New_Project_60.png",
    "<:ytred:1117404642205237402>":
    "https://cdn.discordapp.com/attachments/1092060572369039400/1117404218848989204/New_Project_61.png",
  }
  buttonlink = "https://cdn.discordapp.com/attachments/1092060572369039400/1117401770835050526/New_Project_54.png"
  ytplaques = dict(db[user]["youtube"]["ytplaques"])
  for i, v in ytplaques.items():
    if v[0] == False:
      if db[user]["youtube"]["subs"] > v[1]:
        db[user]["youtube"]["ytplaques"][i][0] = True
        inv = db[user]["inv"]
        if convertdict[i] in inv:
          db[user]["inv"][convertdict[i]] += 1
        else:
          db[user]["inv"][convertdict[i]] = 1
        await ctx.reply(f"{ctx.author.mention} got a {convertdict[i]}!")
    else:
      buttonlink = convertlink[i]
  if db[user]["youtube"]["subs"] == 0:
    await ctx.reply(
      "You must pay 10,000 CoinBot Coins to create a youtube channel and accept that you will be paid minimuum pages before you do viral, do you accept? (!yes)"
    )

    def check(m):
      return m.author == ctx.author

    prompt = await discordinput(ctx, check)
    if (prompt == "!yes" or prompt == ".yes") and db[user]["bal"] >= 10000:
      db[user]["youtube"]["subs"] += 1
      db[user]["bal"] -= 10000
      await ctx.reply("Congratulations, you now have a YouTube Channel")
    else:
      return await ctx.reply("cancelling")
  if len(db[user]["youtube"]["videos"]) > 9:
    for key in db[user]["youtube"]["videos"].keys():
      keys = list(db[user]["youtube"]["videos"].keys()).index(key)
      if keys >= 9:
        del db[user]["youtube"]["videos"][key]
  if "videos" in type.lower():
    if "<@" in item:
      pass
    else:
      embed = discord.Embed(title="**__Your Channel__**",
                            description="Your videos",
                            color=discord.Color.red())
      for i, v in db[user]["youtube"]["videos"].items():
        v = str(v).replace(", ",
                           "\n").replace("ObservedDict(value={",
                                         "").replace("'",
                                                     "**").replace("})", "")
        embed.add_field(name=f"__{i}__", value=v, inline=True)
      embed.set_thumbnail(url=buttonlink)
      await ctx.reply(embed=embed)
  elif "streams" in type.lower():
    if "<@" in item:
      pass
    else:
      embed = discord.Embed(title="**__Your Channel__**",
                            description="Your streams",
                            color=discord.Color.red())
      for i, v in db[user]["youtube"]["stream"].items():
        v = str(v).replace(", ",
                           "\n").replace("ObservedDict(value={",
                                         "").replace("'",
                                                     "**").replace("})", "")
        embed.add_field(name=f"__{i}__", value=v, inline=True)
      await ctx.reply(embed=embed)
  elif "profile" in type.lower():
    if "<@" in item:
      user = int(item.replace("<@", "").replace(">", ""))
    else:
      user = ctx.author.id
    link = await bot.fetch_user(user)
    embed = discord.Embed(title="", description="", color=discord.Color.red())
    embed.set_author(name=f"{str(link).split('#')[0]}'s channel",
                     icon_url=ctx.author.display_avatar.url)
    embed.set_thumbnail(url=buttonlink)
    embed.add_field(name="Subscribers:",
                    value=add_commas(str(db[user]["youtube"]["subs"])),
                    inline=False)
    embed.add_field(name="Total Views:",
                    value=add_commas(str(db[user]["youtube"]["views"])),
                    inline=False)
    embed.add_field(name="Videos:",
                    value=add_commas(str(db[user]["youtube"]["vidamount"])),
                    inline=False)
    embed.add_field(name="Total Likes:",
                    value=add_commas(str(db[user]["youtube"]["ytlikes"])),
                    inline=False)
    await ctx.reply(embed=embed)
  elif "bal" in type.lower():
    embed = discord.Embed(title="**__Your Channel__**",
                          description="Your Stats",
                          color=discord.Color.red())
    embed.add_field(name="Youtube Bank:",
                    value=str(db[user]["youtube"]["ytbank"]),
                    inline=False)
    embed.set_thumbnail(url=buttonlink)
    await ctx.reply(embed=embed)
  elif "upload" in type.lower():
    db[user]["youtube"]["ytvidtime"] = int(db[user]["youtube"]["ytvidtime"])
    if db[user]["youtube"]["ytvidtime"] + 300 > round(time.time()):
      timeleft = "000" + str(
        int(db[user]["youtube"]["ytvidtime"] + 300) - round(float(time.time())))
      minutes = int(timeleft) // 60
      seconds = int(timeleft) % 60
      embed = discord.Embed(
        title="**Cooldown**",
        description=f"Cooldown until {minutes} minutes and {seconds} seconds!",
        color=discord.Color.red())
      embed.set_thumbnail(url=buttonlink)
      return await ctx.reply(embed=embed)
    await ctx.reply("What would you like to name this video?")

    def check(m):
      return str(m.author.id) == str(
        ctx.author.id) and m.channel == ctx.channel

    try:
      response = await bot.wait_for('message', check=check, timeout=20.0)
      if response != "":
        name = response.content
        if name in db[user]["youtube"]["videos"]:
          await ctx.reply("This video title already exists! Choose another")
        elif "upload" in name.lower():
          return await ctx.reply("Bro thought")
        else:
          multi = 1
          for i in db[user]["ytitems"]:
            item = list(ytupgrade.keys()).index(db[user]["ytitems"][i])
            multi += item / random.randint(12, 17)
          luck = random.randint(1, 4)
          if luck == 4:
            multi *= 3
          elif luck == 3:
            multi *= 2
          elif luck == 2:
            multi *= 1.5
          view = round(multi * (db[user]["youtube"]["subs"] / 10 + 20))
          if db[user]["youtube"]["subs"] < 1000:
            subs = round((view / random.randint(3, 5))) + 1
          elif db[user]["youtube"]["subs"] < 5000000:
            subs = round((view / random.randint(5, 9))) + 1
          else:
            subs = round((view / random.randint(50, 70))) + 1
          likes = round(subs * (1 + (random.randint(10, 100) / 100)))
          coins = round(subs * (1 + (random.randint(-50, 50) / 100)))
          if coins > view:
            coins = view
          txt = ""
          viral = random.randint(1, 100)
          if viral == 100:
            if db[user]["youtube"]["subs"] < 5000000:
              view *= 10
              subs *= 10
              coins *= 10
            else:
              view *= 2
              subs *= 2
              coins *= 2
            txt = "🔴YOUR VIDEO WENT VIRAL🔴\n\n"
          elif viral == 99:
            view *= -1
            subs *= -1
            coins *= -1
            txt = "🔴YOUR VIDEO GOT YOU CANCELLED🔴\n\n"
          dict1 = {
            name: {
              "Views": view,
              "Subscribers": subs,
              "Likes": likes,
              "Revenue": coins
            }
          }
          db[user]["youtube"]["videos"] = {**dict1, **db[user]["youtube"]["videos"]}
          txtdict = {
            name: {
              "Views": add_commas(view),
              "New Subscribers": add_commas(subs),
              "Likes": add_commas(likes),
              "Revenue": add_commas(coins)
            }
          }
          txt += str(
            txtdict[name]).replace(", ", "\n").replace("}", "").replace(
              "{", "").replace("'", "").replace("Views", "**Views**").replace(
                "New Subscribers", "**Subscribers**").replace(
                  "Revenue", "**Revenue**").replace("Likes", "**Likes**")
          embed = discord.Embed(title=f"__{name}__",
                                description=txt,
                                color=discord.Color.red())
          embed.set_thumbnail(url=buttonlink)
          db[user]["youtube"]["vidamount"] += 1
          db[user]["youtube"]["subs"] += subs
          db[user]["youtube"]["views"] += view
          db[user]["youtube"]["ytbank"] += coins
          db[user]["youtube"]["ytlikes"] += likes
          db[user]["youtube"]["ytvidtime"] = round(int(time.time()))
          await ctx.reply(embed=embed)
    except asyncio.TimeoutError:
      return await ctx.reply(
        embed=await embedify("Took too long, cancelling...", ""))
  elif "stream" in type.lower():
    #return
    await ctx.reply("What would you like to name your stream?")

    def check(m):
      return str(m.author.id) == str(
        ctx.author.id) and m.channel == ctx.channel

    try:
      response = await bot.wait_for('message', check=check, timeout=10.0)
      if response != "":
        name = response.content
        if name in db[user]["youtube"]["stream"]:
          await ctx.reply("This stream title already exists! Choose another")
        else:
          chance1 = (db[user]["youtube"]["views"] / 100) * random.randint(-5, 15)
          view = round(db[user]["youtube"]["views"] + chance1)
          subs = round(view / (random.randint(7, 20)) + 5)
          donations = 0
          donators = 0
          donatorss = ""
          for i in range(1,
                         (db[user]["youtube"]["views"] // 1000 + random.randint(-1, 2))):
            chance = random.randint(1, 100)
            if chance > 50:
              donations += round(view // random.randint(500, 2000) *
                                 (random.randint(10, 30) / 100))
              donators += 1
            elif chance == 1:
              donations += 5000
              donatorss = "MR BEAST"
              donators += 1
          chance = random.randint(1, 100)
          if chance == 1:
            donations += 5000
          coins = round((view * (random.randint(3, 7) / 10))) + round(
            subs / random.randint(200, 400)) + donations
          text = ""
          if donatorss == "MR BEAST":
            text += " and Mr Beast donated 5,000 coins."
            donatorss = ""
          streamdict = {
            name: {
              "Views": view,
              "Subscribers": subs,
              "Donations":
              f"{donators} donated {donations} coins in total" + text,
              "Revenue": coins
            }
          }
          db[user]["youtube"]["stream"] = {**streamdict, **db[user]["youtube"]["stream"]}
          txt = ""
          txtdict = {
            name: {
              "Views":
              add_commas(view),
              "Subscribers":
              add_commas(subs),
              "Donations":
              f"{add_commas(donators)} donated {add_commas(donations)} coins in total"
              + text,
              "Revenue":
              add_commas(coins)
            }
          }
          txt += str(txtdict[name]).replace(", ", "\n").replace(
            "}", "").replace("{", "").replace("'", "").replace(
              "Views",
              "**Views**").replace("Subscribers", "**Subscribers**").replace(
                "Revenue", "**Revenue**").replace("Donations", "**Donations**")
          embed = discord.Embed(title=f"__{name}__",
                                description=txt,
                                color=discord.Color.red())
          db[user]["youtube"]["streamamount"] += 1
          db[user]["youtube"]["ytbank"] += coins
          db[user]["youtube"]["subs"] += subs
          db[user]["youtube"]["ytbank"] += coins
          embed.set_thumbnail(url=buttonlink)
          await ctx.reply(embed=embed)
    except asyncio.TimeoutError:
      return await ctx.reply(
        embed=await embedify("Took too long, cancelling...", ""))
  elif "setup" in type.lower():
    embed = discord.Embed(title="**Youtube Shop**",
                          description="All items you can buy for youtube",
                          color=discord.Color.red())
    embed.set_thumbnail(url=buttonlink)
    if item != "":
      user = item.replace("<", "").replace("@", "").replace(">", "")
    for i in db[user]["youtube"]["ytitems"]:
      item = db[user]["youtube"]['ytitems'][i]
      amount = ytupgrade[item]
      i = i.title()
      embed.add_field(name=f"__{i}__",
                      value=f"**Type:**{item}\n**Upgrade:**${amount}",
                      inline=True)
      #txt+=f"__**{i}**__\n**Type**:{item}\n**Upgrade**:${amount}\n** **"
    #embed.add_field(name="",value=txt,inline=False)
    await ctx.reply(embed=embed)
  elif "upgrade" in type.lower():
    item = item.lower()
    if item in ytitems:
      amountNeeded = ytupgrade[db[user]["youtube"]['ytitems'][item]]
      if db[user]["youtube"]["ytbank"] >= amountNeeded:
        db[user]["youtube"]["ytbank"] -= amountNeeded
        num = yttypes.index(db[user]["youtube"]['ytitems'][item]) + 1
        db[user]["youtube"]['ytitems'][item] = yttypes[num]
        embed = discord.Embed(
          title="**Youtube Upgrade**",
          description=f"Upgraded {item} to a {yttypes[num]} {item}",
          color=discord.Color.green())
        embed.set_thumbnail(url=buttonlink)
        await ctx.reply(embed=embed)
      else:
        embed = discord.Embed(title="**Youtube Upgrade**",
                              description=f"Not enough money.",
                              color=discord.Color.red())
        embed.set_thumbnail(url=buttonlink)
        await ctx.reply(embed=embed)
    else:
      await ctx.reply("Not an item.")
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1
  # elif "transfer" in type.lower():
  #   try:
  #     item = int(item)
  #   except:
  #     embed = discord.Embed(title="__Youtube__", description="You have to give an amount to transfer!", color=discord.Color.red())
  #     embed.set_thumbnail(url=buttonlink)
  #     return await ctx.reply(embed=embed)
  #   if db[user]["youtube"]["ytbank"] >= item:
  #     embed = discord.Embed(title="__Youtube__", description=f"Are you sure you want to transfer {item} youtube coins into {item*10} CoinBot coins? This can **not** be undone.", color=discord.Color.red())
  #     embed.set_thumbnail(url=buttonlink)
  #     await ctx.reply(embed=embed)
  #     def check(m):
  #       return str(m.author.id) == ctx.author.id and m.channel == ctx.channel
  #     try:
  #       response = await bot.wait_for('message', check=check, timeout=10.0)
  #       if response.content.lower() not in ("!yes") and response.content.lower() not in (".yes"):
  #         return await ctx.reply(embed=cancelEmbed)
  #       else:
  #         db[user]["youtube"]["ytbank"] -= item
  #         db[user]["bal"] += item*10
  #         await ctx.reply(f"<@{user}> has transfered {item*10} Youtube coins into CoinBot coins")
  #     except asyncio.TimeoutError:
  #       return await ctx.reply(embed=await embedify("Took too long, cancelling...",""))


