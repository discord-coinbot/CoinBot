
# PETS
petslist = {
  "Spider": "25,000",
  "Goldfish": "50,000",
  "Hamster": "100,000",
  "Frog": "250,000",
  "Squid": "500,000",
  "Snake": "1,000,000",
  "Dolphin": "2,500,000",
  "Dinosaur": "5,000,000 and 1 dino_fossil",
  "Dragon": "10,000,000 and 1 dragon_wing",
  "Megladon": "25,000,000 and 1 megalodon_tooth",
}

pets = [
  "spider", "goldfish", "hamster", "frog", "squid", "snake", "dolphin",
  "dinosaur", "dragon", "megalodon"
]

petss = [
  "Spider", "Goldfish", "Hamster", "Frog", "Squid", "Snake", "Dolphin",
  "Dinosaur", "Dragon", "Megalodon"
]
petslink = {
  "Spider":
  "https://cdn.discordapp.com/attachments/1096799510845468672/1096843464437665922/New_Project1.png",
  "Goldfish":
  "https://cdn.discordapp.com/attachments/1092022074781990944/1096842677129064458/images.jpg",
  "Hamster":
  "https://cdn.discordapp.com/attachments/1092022074781990944/1096843019145203722/cartoon_syrian_hamster_photo_sculpture_magnet-rb12e9ee8507e46289cef8a4b452e321d_x7sai_8byvr_630.png",
  "Frog":
  "https://cdn.discordapp.com/attachments/1092022074781990944/1096843195993817240/ac1acffaa7f87b31c94cfab729167efb.png",
  "Squid":
  "https://cdn.discordapp.com/attachments/1092022074781990944/1096843547996598312/latest.png",
  "Snake":
  "https://cdn.discordapp.com/attachments/1092022074781990944/1096843833003745412/7fgGRlMHzoAAAAAElFTkSuQmCC.png",
  "Dolphin":
  "https://cdn.discordapp.com/attachments/1092022074781990944/1096843951929036810/CuHSQAAAABJRU5ErkJggg.png",
  "Dinosaur":
  "https://cdn.discordapp.com/attachments/1092022074781990944/1096844159291228230/images.png",
  "Dragon":
  "https://cdn.discordapp.com/attachments/1092022074781990944/1096844672837632101/9k.png",
  "Megalodon":
  "https://cdn.discordapp.com/attachments/1092022074781990944/1096844873065308253/9k.png"
}

petsfeed = {
  "Spider": "250",
  "Goldfish": "500",
  "Hamster": "1,000",
  "Frog": "2,500",
  "Squid": "5,000",
  "Snake": "10,000",
  "Dolphin": "25,000",
  "Dinosaur": "50,000",
  "Dragon": "100,000",
  "Megalodon": "250,000",
}

petslist = {
  "Spider": "25,000",
  "Goldfish": "50,000",
  "Hamster": "100,000",
  "Frog": "250,000",
  "Squid": "500,000",
  "Snake": "1,000,000",
  "Dolphin": "2,500,000",
  "Dinosaur": "5,000,000 and 1 dino_fossil",
  "Dragon": "10,000,000 and 1 dragon_wing",
  "Megalodon": "25,000,000 and 1 megalodon_tooth"
}

feedable = {
  # huntable
  "ant": 250,
  "mouse": 500,
  "pigeon": 1000,
  "deer": 5000,
  "lion": 10000,
  "mammoth": 25000,
  # Fishable
  "seahorse": 250,
  "fish": 500,
  "salmon": 1000,
  "whale": 25000,
}

animals = [
  "ant",
  "mouse",
  "pigeon",
  "cow",
  "horse",
  "deer",
  "buffalo",
  "cheetah",
  "lion",
  "mammoth",
  "seahorse",
  "fish",
  "salmon",
  "stingray",
  "shark",
  "whale",
]


def checkfed(user):
  if "fedtime" + user in db:
    timelastfed = int(db["fedtime" + user])
    if timelastfed + 3600 <= time.time():
      timesince = time.time() - timelastfed + 3600
      hourssince = math.floor(timesince / 3600)
      percentremove = 100 - (hourssince * 1.5)
      hunger = int(db["fed" + user])
      newAmount = round((hunger / 100) * int(percentremove))
      db["fed" + user] = str(newAmount)
      db["fedtime" + user] = round(time.time())
      return newAmount
  else:
    if "pets" + user in db:
      if db["pets" + user] != "":
        db["fedtime" + user] = round(time.time())
        return "ok"
    else:
      db["pets" + user] = ""


def petcheck(user):
  if "pettime" + user in db:
    if int(db["pettime" + user]) + 3600 <= time.time():
      return "yes"
    else:
      return "no"
  else:
    db["pettime" + user] = 0
    return "yes"


@bot.command()
async def pet(ctx, action=None, item=None):
  if item == None:
    item = ""
  if action == None:
    action = "profile"
  user = str(ctx.author.id)
  if user not in db:
    db[user] = 0
  if "pets" + user not in db:
    db["pets" + user] = ""
  amount = checkfed(user)
  if amount != None:
    if amount <= 0:
      db["pets" + user] = ""
      del db["fedtime" + user]
      return await ctx.reply("Your pet ran away as you didn't feed it.")
  usercoins = db[user]
  inventory_items = db["inv" + user].keys()
  if "feedable" in action:
    if "list" in item:
      embed = discord.Embed(
        title="**Pet Feedable List**",
        description=
        "Here are how much hunger each animal can give a pet when fed",
        color=discord.Color.random())
      for i, k in feedable.items():
        i = str(i)
        k = str(k)
        if i.lower() in allitememojis:
          i = allitememojis[i.lower()] + " " + i
        embed.add_field(name=i, value=k, inline=False)
      embed.set_footer(text="You can get these animals by hunting or fishing")
      await ctx.reply(embed=embed)
  elif "feed" in action:
    if "list" in item:
      embed = discord.Embed(
        title="**Pet Feeding List**",
        description="Here are what all the pets need to be fed every 3 days",
        color=discord.Color.random())
      for i, k in petsfeed.items():
        i = str(i)
        k = str(k)
        if i.lower() in allitememojis:
          i = allitememojis[i.lower()] + " " + i
        embed.add_field(name=i, value=k, inline=False)
      embed.set_footer(
        text=
        "If you forget to feed your pet it will have an increasingly higher chance to run away"
      )
      await ctx.reply(embed=embed)
    else:
      user = str(ctx.author.id)
      userss = str("pets" + user)
      if userss not in db or db[userss] == "":
        await ctx.reply("You don't even have a pet")
      else:
        users = "inv" + user
        inventory_items = db["inv" + user].keys()
        pet = db["pets" + user]
        fed = int(db["fed" + user])
        item = item.lower()
        if item in feedable.keys():
          if item in inventory_items:
            value = int(feedable[item])
            pet = pet.title()
            full = petsfeed[pet].replace(",", "")
            if int(fed) + value >= int(full):
              fed = full
            else:
              fed += int(value)
            inventoryremove(user, item, 1)
            db["fed" + user] = fed
            embed = discord.Embed(
              title="**Pet Feeding**",
              description=
              f"You fed you {pet} a(n) {allitememojis[item]} {item}.",
              color=discord.Color.random())
            embed.set_footer(text=f"Hunger:{fed}")
            await ctx.reply(embed=embed)
          else:
            await ctx.reply(f"You don't have a {item}.")
        else:
          await ctx.reply("You cant feed your pet that.")
  elif "pet" in action:
    print(0)
    check_time = petcheck(user)
    print(1)
    if check_time == "yes":
      user = str(ctx.author.id)
      inventory_items = db["inv" + user].keys()
      if user not in db:
        db[user] = 0
      print(2)
      if str(db["pets" + user]).title() in petslist:
        chance = random.randint(1, 3)
        k = petslist[db["pets" + user].capitalize()]
        k = k.replace(",", "")
        if "and" in k:
          x = k.split(" and")
          k = x[0]
        k = int(k)
        if k <= 250000:
          times = 1
        elif k <= 2500000:
          times = 2
        else:
          times = 3
        text = ""
        box = 0
        for a in range(times):
          chance1 = random.randint(1, 100)
          if chance1 < 20:
            lootbox = "no"
          elif chance1 < 50:  #5
            lootbox = "commonbox"
          elif chance1 < 70:  #10
            lootbox = "uncommonbox"
          elif chance1 < 90:  #25
            lootbox = "rarebox"
          elif chance1 < 100:  #50
            lootbox = "epicbox"
          else:  #100
            lootbox = "legendarybox"
          if lootbox != "no":
            inventoryadd(user, lootbox, 1)
            if box == 0:
              text += f" and it also found a {lootbox}"
              box = 1
            else:
              text += f"and a {lootbox}"
        earnt = int(int(k) / 200) * chance
        if "runeequip" + user in db:
          rune = db["runeequip" + user]
          if "pet" in rune:
            lvl = int(rune[-1])
            multi = lvl / 2
            earnt += round(multi * earnt)
        db[user] += earnt
        db["pettime" + user] = str(round(time.time()))
        await ctx.reply(
          f"You have petted your {db['pets' + user]} and it gave you {earnt}{text}"
        )
    else:
      timeleft = (int(db["pettime" + user]) + 3600) - round(time.time())
      minutes = timeleft // 60
      seconds = timeleft % 60
      msg = str(
        f"Your cooldown ends in {minutes} minutes and {seconds} seconds.")
      embed = discord.Embed(title="**__Cooldown__**",
                            description="",
                            color=discord.Color.red())
      embed.add_field(name=msg, value="")
      await ctx.reply(embed=embed)
  elif "adopt" in action:
    userss = str("pets" + user)
    if userss not in db:
      db[userss] = ""
    db[userss] = ""
    hi = str(db[userss])
    if hi != "":
      await ctx.reply("You still have a pet. !pet disown [pet] to disown it")
    else:
      pet = item.lower()
      if pet in pets:
        petss = pet.capitalize()
        cost = petslist[petss]
        if "and" in cost:
          if "dino" in cost:
            cost = cost[0:9]
          else:
            cost = cost[0:10]
        costs = cost.replace(",", "")
        cost = int(costs)
        if int(cost) <= int(usercoins):
          db[userss] = str(petss)
          db[user] -= cost
          await ctx.reply(f"You have now adopted a {petss}")
          feed = round(int(petsfeed[petss].replace(",", "")) / 2)
          db["pets" + user] = item
          if "fed" + user not in db:
            db["fed" + user] = feed
          if "fedtime" + user not in db:
            db["fedtime" + user] = round(time.time())
        else:
          await ctx.reply("You don't have enough coins to adopt that pet")
      else:
        await ctx.reply(
          "That is not a pet. If you want to adopt a pet do !pet buy [pet]")
  elif "disown" in action:
    pet = db["pets" + user]
    items = item.capitalize()
    if items in pet:
      pet = pet.lower()
      if pet in pets:
        db["pets" + user] = ""
        await ctx.reply(f"You have disowned your {items}")
      else:
        await ctx.reply("That isn't a pet")
    else:
      await ctx.reply(f"You don't have a {items}")
  elif "list" in ctx.message.content and "feed" not in ctx.message.content:
    if "aadish" in (ctx.message.content).lower() or "kai" in (ctx.message.content).lower():
      errorlol
    embed = discord.Embed(title="**Pet List**",
                          description="Here are all the pets",
                          color=discord.Color.random())

    for item, price in petslist.items():
      embed.add_field(name=item, value=f"Price: {price}", inline=False)

    embed.set_footer(text="Do !pet adopt [pet] to buy a pet")
    await ctx.reply(embed=embed)
  elif "profile" in action:
    print(1)
    user = str(ctx.author.id)
    users = ctx.author
    link = await bot.fetch_user(user)
    pet = db[str("pets" + user)]
    print(2)
    if "pets" + user in db:
      if pet.lower() in pets:
        embed = discord.Embed(title=f"{link} 's pet {pet}",
                              description="",
                              color=discord.Color.random())
        pet = pet.capitalize()
        need_feed = petsfeed[pet].replace(",", "")
        url1 = petslink[pet]
        if "fed" + user in db:
          fed = db["fed" + user]
        else:
          fed = need_feed
          db["fed"+user] = fed
        if int(fed) > int(need_feed):
          fed = need_feed
        print(3)
        if int(fed) < 0:
          fed = 0
          db["fed" + user] = fed
        embed.set_thumbnail(url=url1)
        embed.add_field(
          name="__Hunger__",
          value=f"{fed}/{need_feed}\n{get_bar(int(fed),int(need_feed))}",
          inline=False)
        print(4)
        if "pettime" + user not in db:
          db["pettime"+user] = time.time()
        thetime = round(int(db["pettime" + user]) + 3600 - time.time())
        min = str(thetime // 60)
        sec = str(thetime % 60)
        print(5)
        if "-" not in str(min):
          embed.add_field(
            name="__Petting__",
            value=
            f"You can pet your {pet} in {min} minutes and {sec} seconds.",
            inline=False)
        else:
          embed.add_field(name="__Petting__",
                          value=f"You can pet your {pet} right now.",
                          inline=False)
        await ctx.reply(embed=embed)
      else:
        await ctx.reply("You don't have a pet")
    else:
      await ctx.reply("You don't have a pet")
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1
