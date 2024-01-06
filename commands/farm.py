
cropsupgrade = {
  "wheat": 1000,
  "tomato": 2500,
  "broccoli": 6500,
  "potato": 10000,
  "cabbage": 25000,
  "carrot": 65000,
  "pear": 100000,
  "apple": 250000,
  "orange": 650000,
  "peach": 2500000,
  "grape": 6500000,
  "banana": 10000000,
  "lemon": 25000000,
  "lettuce": 65000000,
  "onion": 100000000,
  "cucumber": 250000000,
  "aubergine": 650000000,
  "cauliflower": 1000000000,
  "berry": 2500000000,
  "watermelon": 5000000000,
}

crops = {
  "wheat": 120,
  "tomato": 300,
  "broccoli": 780,
  "potato": 1200,
  "cabbage": 3000,
  "carrot": 7800,
  "pear": 12000,
  "apple": 30000,
  "orange": 78000,
  "peach": 300000,
  "grape": 780000,
  "banana": 1200000,
  "lemon": 3000000,
  "lettuce": 7800000,
  "onion": 12000000,
  "cucumber": 30000000,
  "aubergine": 78000000,
  "cauliflower": 120000000,
  "berry": 300000000,
  "watermelon": 600000000,
}

cropscost = {
  "wheat": 100,
  "tomato": 250,
  "broccoli": 650,
  "potato": 1000,
  "cabbage": 2500,
  "carrot": 6500,
  "pear": 10000,
  "apple": 25000,
  "orange": 65000,
  "peach": 250000,
  "grape": 650000,
  "banana": 1000000,
  "lemon": 2500000,
  "lettuce": 6500000,
  "onion": 10000000,
  "cucumber": 25000000,
  "aubergine": 65000000,
  "cauliflower": 100000000,
  "berry": 250000000,
  "watermelon": 500000000,
}

cropemojifinished = {
  "berry": "🍒",
  "tomato": "🍅",
  "potato": "🥔",
  "onion": "🧅",
  "carrot": "🥕",
  "cucumber": "🥒",
  "aubergine": "🍆",
  "wheat": "🌾",
  "watermelon": "🍉",
  "peach": "🍑",
  "apple": "🍎",
  "pear": "🍐",
  "grape": "🍇",
  "banana": "🍌",
  "orange": "🍊",
  "lemon": "🍋",
  "broccoli": "🥦",
  "cabbage": "🥬",
  "lettuce": "🥬",
  "cauliflower": "💮",
}

cropemojiseeds = {
  "berry": "<:berry:1118612521339859075>",
  "tomato": "<:tomato:1118612489886777395>",
  "potato": "<:potato:1118612493892329572>",
  "onion": "<:onion:1118614334537478184>",
  "carrot": "<:carrot:1118612515774021906>",
  "cucumber": "<:cucumber:1118612586754228355>",
  "aubergine": "<:aubergine:1118612518269616149>",
  "wheat": "<:wheat:1118612488271970468>",
  "watermelon": "<:watermelon:1118612491216375952>",
  "peach": "<:peach:1118612494966083625>",
  "apple": "<:apple:1118612588910104576>",
  "pear": "<:pear:1118612590562639924>",
  "grape": "<:grape:1118612511030263838>",
  "banana": "<:banana:1118612585315565679>",
  "orange": "<:oranges:1118612507918090304>",
  "lemon": "<:lemon:1118612504873017416>",
  "broccoli": "<:broccoli:1118612503233044530>",
  "cabbage": "<:cabbage:1118612501861519420>",
  "lettuce": "<:lettuce:1118612497444909056>",
  "cauliflower": "<:cauliflower:1118612499252646070>",
}


@bot.command(name="farm")
async def farm(ctx, type, item: str = None):
  userId = str(ctx.author.id)
  if "farm" + userId not in db:
    db["farm" + userId] = {
      "bal": 0,
      "crop": "wheat",
      "size": 3,
      "totalearned": 0,
      "time": 0,
      "planted": False,
    }
  data = db["farm" + userId]
  if "view" in type:
    farm = []
    emoji = "<:dirt:1118612486036389948>"
    txt = ""
    if data["planted"]:
      if data["time"] + 1800 < time.time():
        txt += "*You can harvest **right now***\n"
        emoji = cropemojifinished[data["crop"]]
      else:
        txt += f"You can harvest in **{timeconvert((data['time'] + 1800)-round(time.time()))}**\n"
        emoji = cropemojiseeds[data["crop"]]
    else:
      txt += "Plant a crop now by running, *!farm plant*\n"
    for i in range(data["size"]):
      for j in range(data["size"]):
        txt += emoji
      txt += "\n"
    embed = discord.Embed(title="**__Your Farm__**",
                          description=txt,
                          color=discord.Color.dark_green())
    #embed.add_field(name="Farm", value=txt, inline=False)
    await ctx.reply(embed=embed)
  elif "plant" in type:
    if data["planted"] == False:
      data["planted"] = True
      amount = cropscost[data["crop"]]
      size = int(data["size"])**2
      total_amount = size * amount
      if data["bal"] - total_amount > 0:
        data["bal"] -= total_amount
        data["time"] = round(time.time())
        embed = discord.Embed(
          title="**__Your Farm__**",
          description=
          f"You grw your crops and it costed you for {total_amount}",
          color=discord.Color.dark_green())
        await ctx.reply(embed=embed)
      else:
        embed = discord.Embed(
          title="**__Your Farm__**",
          description=
          f"Insufficent balance\nRun !farm add 69420 to add from your CoinBot balance.",
          color=discord.Color.dark_green())
        await ctx.reply(embed=embed)
  elif "harvest" in type:
    if data["time"] + 1800 < time.time() and data["planted"]:
      data["planted"] = False
      amount = crops[data["crop"]]
      size = int(data["size"])**2
      total_amount = size * amount
      data["totalearned"] += total_amount
      data["bal"] += total_amount
      embed = discord.Embed(
        title="**__Your Farm__**",
        description=f"You harvested your crops and sold it for {total_amount}",
        color=discord.Color.dark_green())
      await ctx.reply(embed=embed)
    else:
      embed = discord.Embed(
        title="**__Your Farm__**",
        description=
        f"You can harvest in **{timeconvert((data['time'] + 1800)-round(time.time()))}**\n",
        color=discord.Color.dark_green())
      await ctx.reply(embed=embed)
  elif "add" in type:
    if db[userId] > -int(item):
      db[userId] -= int(item)
      data["bal"] += int(item)
      await ctx.reply("Added!")
    else:
      await ctx.reply("Not enought CoinBot coins")
  elif "bal" in type.lower():
    embed = discord.Embed(title="**__Your Farm Stats__**",
                          description="",
                          color=discord.Color.dark_green())
    embed.add_field(name="Farm Revenue:", value=str(data["bal"]), inline=False)
    await ctx.reply(embed=embed)
  elif "upgrades" in type:
    embed = discord.Embed(title="**__Farm Upgrades__**",
                          description="",
                          color=discord.Color.dark_green())
    size = data['size']
    if size < 11:
      embed.add_field(
        name="Size",
        value=
        f"{size}x{size}\nUpgrade for {add_commas(((size**2)*(size**2)**2)*2)}")
    else:
      embed.add_field(name="Size",
                      value=f"{size}x{size}\nYou are at maximum size!")
    crop = data['crop']
    if crop != list(cropsupgrade.keys())[-1]:
      num = list(cropsupgrade.keys())[list(cropsupgrade.keys()).index(crop) +
                                      1]
      embed.add_field(
        name="Crop",
        value=
        f"**Crop**:{crop}\n**Next Crop**: {num}\nCost: {add_commas(cropsupgrade[num])}"
      )
    else:
      embed.add_field(
        name="Crop",
        value=f"**Crop**:{crop}\n**Next Crop**: You have the best crop")
    await ctx.reply(embed=embed)
  elif "upgrade" in type:
    embed = discord.Embed(title="**__Farm Upgrade__**",
                          description="",
                          color=discord.Color.dark_green())
    if "crop" in item:
      crop = data['crop']
      if crop != list(cropsupgrade.keys())[-1]:
        num = list(cropsupgrade.keys())[list(cropsupgrade.keys()).index(crop) +
                                        1]
        cost = cropsupgrade[num]
        if data["bal"] >= cost:
          embed.add_field(
            name="Crop",
            value=
            f"Upgraded to a {num} {cropemojifinished[num]} for {add_commas(cost)}"
          )
          data["bal"] -= cost
          data['crop'] = num
        else:
          embed.add_field(name="Crop", value=f"Not enough money to upgrade")
      else:
        embed.add_field(name="Crop", value=f"You have the best crop")
      await ctx.reply(embed=embed)
    elif "size" in item:
      size = data['size']
      cost = ((size**2) * (size**2)**2) * 2
      if size < 11:
        if data['bal'] >= cost:
          embed.add_field(
            name="Size",
            value=f"Upgraded size to {size+1}x{size+1} for {add_commas(cost)}")
          data['size'] += 1
          data['bal'] -= cost
        else:
          embed.add_field(name="Size", value=f"Not enough money to upgrade")
      else:
        embed.add_field(name="Size", value=f"You are at maximum size!")
      await ctx.reply(embed=embed)
    else:
      await ctx.reply("Invalid item to upgrade, choose from size and crop.")
  elif "profile" in type:
    pass
  db["farm" + userId] = data
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1

