#--------------------------------GAMES----------------------------------
# Guess The Number
@bot.command(pass_context=True)
@commands.cooldown(1, 6, commands.BucketType.user)
async def gtn(ctx, user_choice: str):
  val = random.randint(1, 10)
  user_choice = int(user_choice.lower())
  if user_choice not in range(1, 11):
    await ctx.reply("You can only pick a number between 1 and 10")
    return
  if user_choice == val:
    embed = discord.Embed(title="**__Guess The Number__**",
                          description="",
                          color=discord.Color.green())
    ans = str()
    embed.add_field(name=f"The number was {val}",
                    value="SO YOU GUESSED IT CORRECTLY")
    embed.add_field(name="", value=ans, inline=False)
    embed.set_footer(text="You got 500 coins!")
  else:
    embed = discord.Embed(title="**__Guess The Number__**",
                          description="",
                          color=discord.Color.red())
    result = str(f"Wrong.")
    embed.add_field(name=f"The number was {val}", value=result)
  await ctx.reply(embed=embed)
  if user_choice == val:
    user = str(ctx.author.id)
    if user not in db:
      db[user] = 0
    coins_to_add = int(500)
    db[user] += coins_to_add
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1


#Rock Paper scissors
@bot.command(pass_context=True)
@commands.cooldown(1, 3, commands.BucketType.user)
async def rps(ctx, user_choice: str):
  choices = ['rock', 'paper', 'scissors']
  user_choice.lower()
  if not user_choice in choices:
    await ctx.reply('Invalid choice. Please choose rock, paper, or scissors.')
    return
  embed = discord.Embed(title="**__Rock Paper Scissors__**",
                        description="",
                        color=discord.Color.green())
  bot_choice = random.choice(choices)
  embed.add_field(name=f"I chose {bot_choice}", value="")

  if user_choice == bot_choice:
    embed.color = discord.Color.dark_gray()
    embed.add_field(name="", value="Which means we tied.", inline=False)
    return await ctx.reply(embed=embed)
  elif user_choice == 'rock' and bot_choice == 'scissors':
    result = 'win'
  elif user_choice == 'paper' and bot_choice == 'rock':
    result = 'win'
  elif user_choice == 'scissors' and bot_choice == 'paper':
    result = 'win'
  else:
    embed.color = discord.Color.red()
    embed.add_field(name="", value="Which means I won.", inline=False)
    return await ctx.reply(embed=embed)

  if result == "win":
    embed.add_field(name="", value="Which means you won.", inline=False)
    embed.set_footer(text="You got 150 coins!")

    user = str(ctx.author.id)
    if not user in db:
      db[user] = 0

    db[user] += 150
  await ctx.reply(embed=embed)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1


# beg
@bot.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def beg(message):
  user = str(message.author.id)
  if random.randint(1, 10) != 1:
    if user not in db:
      db[user] = 0
    coins_to_add = random.randint(75, 150)
    responses = [
      f"You begged for a whole day. You got {coins_to_add} coins.",
      f"You were a bully and asked for the lunch money. You got {coins_to_add} coins.",
      f"You begged the old lady passing by and she gave you {coins_to_add} coins.",
      f"Elon Musk felt bad for you and gave you {coins_to_add} money",
      f"Andrew Tate came past and said,'DO MORE PUSHUPS!' and gave you {coins_to_add} coins cuz y not",
      f"Imagine begging. Here's {coins_to_add} coins to stop you from doing it again",
      "MrBeast saw you were subscibed to him when you were begging and gave you 1000",
      "YOU GOT THE LUCKY CHANCE AND GOT 100K! (0.1% chance)"
    ]
    number = random.randint(1, 1000)

    if number < 969:
      text = responses[number % (len(responses) - 2)]
    elif number <= 999:
      text = responses[6]
      coins_to_add = 1000
    else:
      text = responses[7]
      coins_to_add = 100000
    db[user] += coins_to_add
  else:
    item = await itemsGrind(user)
    text = f"You got a(n) {item} while begging"
  notechance = random.randint(1, 100)
  if notechance == 1:
    inventory_items = db["inv" + user]
    if "banknote" in inventory_items:
      inventory_items["banknote"] += 1
    else:
      inventory_items["banknote"] = 1
    text += "** and a passerby gave you a banknote**"
  collect = await collectables(user, "beg")
  text += collect
  embed = discord.Embed(title="**__Beg__**",
                        description=text,
                        color=discord.Color.random())
  await message.reply(embed=embed)
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1
  if "bpinfo" + str(message.author.id) in db:
    data = db["bpinfo" + str(message.author.id)]["quests"]
    for i in data.values():
      if "Begs Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Beg Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))
      if "Commands Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Commands Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))


# DICE
@bot.command()
async def diceroll(ctx):
  desc = "Your die rolled a " + str(random.randint(1, 6))
  embed = discord.Embed(title="**__Dice__**",
                        description=desc,
                        color=discord.Color.random())
  await ctx.reply(embed=embed)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1


# SEARCH
# items = {
#   "Minecraft World": {
#     "pic": 5,
#     "redstone": 20,
#     "string": 40,
#     "wood": 60,
#   },
#   "School": {
#     "pen":10,
#     "glue":20,
#     "paper":35,
#     "card":50,
#   },
#   "Fortnite Map": {
#     "motor": 5,
#     "slurp_juice": 15,
#     "ammo":30,
#     "mini":50,
#     "metal": 70,
#   }
# }

# class searchbuttons(discord.ui.View):
#   def __init__(self, user):
#     super().__init__()
#     self.user = user
#     self.value = None
#     user = self.user

#   async def interaction_check(self, inter: discord.MessageInteraction) -> bool:
#     if inter.user.id != self.user:
#       await inter.response.send_message(content="This isn't your command!",
#                                         ephemeral=True)
#       return False
#     return True

#   @discord.ui.button(label="Minecraft World", style=discord.ButtonStyle.green)
#   async def mcworld(self, interaction: discord.Interaction, button: discord.ui.Button):
#     chance = random.randint(1,items["Minecraft WORLD"])# HIIII
#     for i,k in items["Minecraft World"].items():
#       if chance < k:
#         found = i
#         break
#     inventoryadd(self.user,found,1)
#     embed=discord.Embed(title="**Search**",
#                        description=f"You found {found}",
#                        color=discord.Color.green())
#     await interaction.response.edit_message(embed=embed, view=None)

#   @discord.ui.button(label="School", style=discord.ButtonStyle.grey)
#   async def sch(self, interaction: discord.Interaction, button: discord.ui.Button):
#     chance = random.randint(1,50)
#     for i,k in items["School"].items():
#       if chance < k:
#         found = i
#         break
#     inventoryadd(self.user,found,1)
#     embed=discord.Embed(title="**Search**",
#                        description=f"You found {found}",
#                        color=discord.Color.green())
#     await interaction.response.edit_message(embed=embed, view=None)

#   @discord.ui.button(label="Fortnite Map", style=discord.ButtonStyle.blurple)
#   async def fnmap(self, interaction: discord.Interaction, button: discord.ui.Button):
#     chance = random.randint(1,70)
#     for i,k in items["Fortnite Map"].items():
#       if chance < k:
#         found = i
#         break
#     inventoryadd(self.user,found,1)
#     embed=discord.Embed(title="**Search**",
#                        description=f"You found {found}",
#                        color=discord.Color.green())
#     await interaction.response.edit_message(embed=embed, view=None)

# @bot.command()
# async def searcher(ctx):
#   view = searchbuttons(ctx.author.id)
#   embed = discord.Embed(title="**Search**",
#                         description="Choose where you want to search",
#                         color=discord.Color.dark_grey())
#   await ctx.reply(embed=embed, view=searchbuttons(ctx.author.id))


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def search(message):
  text = "You got nothing..."
  user = str(message.author.id)
  getchance = random.randint(1, 20)
  if getchance >= 7:
    if "rune" + user not in db:
      db["shard" + user] = {
        "digshards": 0,
        "gameshards": 0,
        "mineshards": 0,
        "studyshards": 0,
        "unbreakingshards": 0,
        "searchshards": 0
      }
    if "game" not in db["rune" + user] and "prestige" + user in db:
      if db["prestige" + user] > 0:
        db["rune" + user]["game"] = 0
    if "game" in db["rune" + user]:
      runelist = {
        "digshards": 20,
        "gameshards": 40,
        "mineshards": 60,
        "studyshards": 80,
        "unbreakingshards": 100,
        "searchshards": 110
      }
      max = 110
    else:
      runelist = {
        "digshards": 20,
        "mineshards": 40,
        "studyshards": 60,
        "unbreakingshards": 80,
        "searchshards": 90
      }
      max = 90
    runes = db["shard" + user]
    num = random.randint(0, max)
    for i, j in runelist.items():
      if num <= j:
        shard = i
        amount = random.randint(1, 10)
        multi = None
        if "runeequip" + user in db:
          rune = db["runeequip" + user]
          if "search" in rune:
            lvl = int(rune[-1])
            multi = lvl / 4
            amount += round(multi * amount)
        shards = str(amount) + " " + shard
        break
    responses = [
      f"You looked under the couch. You found {shards}.",
      f"When you opened your fridge, you found {shards}.",
      f"You looked under the mat. You found {shards}.",
      f"When you were looking for your car keys you found {shards} in the drawer"
    ]
    text = random.choice(responses)
    runes[shard] += amount
    db["shard" + user] = runes
    if multi != None:
      more = multi * 100
      text += f", your search rune giving you {more}% more shards"
    if random.randint(1, 3) == 1:
      dropped = random.randint(50, 500)
      db[user] -= dropped
      text += f" and you accidentally dropped {dropped} when looking around."
  elif getchance >= 2:
    text = "You found nothing."
  else:
    item = await itemsGrind(user)
    text = f"You got a(n) {item} while searching"
  notechance = random.randint(1, 100)
  if notechance < 4:
    inventory_items = db["inv" + user]
    inventory_items.append("banknote")
    text += " ** and you found a banknote while searching**"
  collect = await collectables(user, "search")
  text += collect
  embed = discord.Embed(title="**__Search__ 🔍**",
                        description=text,
                        color=discord.Color.random())
  await message.reply(embed=embed)
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1
  if "bpinfo" + str(message.author.id) in db:
    data = db["bpinfo" + str(message.author.id)]["quests"]
    for i in data.values():
      if "Searches Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Search Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))
      if "Commands Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Commands Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))


# FIND
@bot.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def find(message):
  user = str(message.author.id)
  if random.randint(1, 10) != 1:
    if user not in db:
      db[user] = 0
    coins_to_add = random.randint(5, 200)
    responses = [
      f"You looked under the couch. You found {coins_to_add}.",
      f"When you opened your fridge, you found {coins_to_add}.",
      f"You looked under the mat. You found {coins_to_add}.",
      f"When you were looking for your car keys you found {coins_to_add} in the drawer"
    ]
    text = responses[random.randint(0, len(responses) - 1)]
    db[user] += coins_to_add
  else:
    item = await itemsGrind(user)
    text = f"You got a(n) {item} while looking around"
  notechance = random.randint(1, 100)
  if notechance == 1:
    inventory_items = db["inv" + user]
    inventory_items.append("banknote")
    text += "** and you found a banknote**"
  collect = await collectables(user, "find")
  text += collect
  embed = discord.Embed(title="**__Find__ 🔍**",
                        description=text,
                        color=discord.Color.random())
  await message.reply(embed=embed)
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1


# DIG
@bot.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def dig(message):
  user = str(message.author.id)
  users = str("inv" + user)
  inventory_items = db[users]
  break_chance = random.randint(1, 200)
  txt = ""
  broke = False
  if "ultimate_shovel" in inventory_items:
    shovel = 90  # 600k
    if break_chance == 1:
      inventoryremove(user, "ultimate_shovel", 1)
      broke = True
  elif "netherite_shovel" in inventory_items:
    shovel = 50  # 200k
    if break_chance < 3:
      inventoryremove(user, "netherite_shovel", 1)
      broke = True
  elif "diamond_shovel" in inventory_items:
    shovel = 17  # 20k
    if break_chance < 9:
      inventoryremove(user, "diamond_shovel", 1)
      broke = True
  elif "iron_shovel" in inventory_items:
    shovel = 10  # 10k
    if break_chance < 15:
      inventoryremove(user, "iron_shovel", 1)
      broke = True
  elif "wooden_shovel" in inventory_items:
    shovel = 4  # 1000
    if break_chance < 21:
      inventoryremove(user, "wooden_shovel", 1)
      broke = True
  else:
    shovel = "no shovel"
  if user not in db:
    db[user] = 0
  coins = db[user]
  if shovel != "no shovel":
    if random.randint(1, 10) != 1:
      coins_to_add = random.randint(25, 50) * shovel
      multi = 0
      if "runeequip" + user in db:
        rune = db["runeequip" + user]
        if "dig" in rune:
          lvl = int(rune[-1])
          multi = lvl / 2
          coins_to_add += round(multi * coins_to_add)
      coins += round(coins_to_add)
      db[user] = coins
      responses = [  #leave blank 
        f"<@{user}> brought out your shovel and dug down. You dug out {coins_to_add} coins.",
        f"<@{user}> dug out sand for a sandcastle and found {coins_to_add} coins.",
        f"<@{user}> dug out dirt and got {coins_to_add} coins.",
        f"<@{user}> DUG DOWN AND FOUND A DINO FOSSIL!!!! (this is a 0.4% chance)"
      ]
      number = random.randint(1, 1000)
      if number < 340:
        text = txt + responses[0]
      elif number < 670:
        text = txt + responses[1]
      elif number < 997:
        text = txt + responses[2]
      else:
        text = txt + responses[3]
        inventoryadd(user, "dino_fossil", 1)
      if multi != 0:
        more = round(int(multi * 100))
        text += f"\n__Your dig rune giving you {more}% more coins__"
      if broke:
        text += "** ... But you dug down so hard your shovel broke**"
      if "runeequip" + user in db:
        rune = db["runeequip" + user]
        if "unbreaking" in rune:
          lvl = int(rune[-1])
          number = 1000 / ((lvl + 1)**2) / 2
        chance = random.randint(1, 100000)
        if chance <= number:
          text = text + "**...and your shovel broke**"
          if chance <= 1000 and chance > number:
            text += "**YOUR RUNE SAVED YOUR SHOVEL FROM BREAKING**"
    else:
      item = await itemsGrind(user)
      text = f"You got a(n) {item} while digging"
    notechance = random.randint(1, 100)
    if notechance < 4:
      inventoryadd(user, "banknote", 1)
      text += " ** and you found a banknote in the dirt**"
    collect = await collectables(user, "dig")
    #await message.send(collect)
    text += collect
    embed = discord.Embed(title="**__Dig__**",
                          description=str(text),
                          color=discord.Color.random())
    await message.reply(embed=embed)
  else:
    await message.reply("You don't even have a shovel. Go buy one in the shop")
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1
  if "bpinfo" + str(message.author.id) in db:
    data = db["bpinfo" + str(message.author.id)]["quests"]
    for i in data.values():
      if "Digs Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Dig Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))
      if "Commands Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Commands Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))


# HUNT
huntable = {
  "ant": "750",  #1
  "mouse": "1,000",  #2
  "pigeon": "2,000",  #2.5 #10
  "deer": "10,000",  #12
  "lion": "20,000",  #26.66
  "mammoth": "50,000",  #40
  "dragon_wing": "200,000",  #100
}


@bot.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def hunt(message):
  user = str(message.author.id)
  users = str("inv" + user)
  inventory_items = db[users].keys()
  if user not in db:
    db[user] = 0
  if "hunting_rifle" not in inventory_items:
    await message.reply(
      "You require to aquire a hunting rifle first. Go buy one in the shop")
  else:
    if random.randint(1, 10) != 1:
      number = random.randint(1, 2000)
      if number < 500:  #800
        animal_to_add = "ant"
      elif number < 1300:  #500
        animal_to_add = "mouse"
      elif number < 1650:  #350
        animal_to_add = "pigeon"
      elif number < 1850:  #200
        animal_to_add = "deer"
      elif number < 1950:  #100
        animal_to_add = "lion"
      elif number < 1997:  #46
        animal_to_add = "mammoth"
      else:  #4
        animal_to_add = "dragon_wing"
      inventoryadd(user, animal_to_add, 1)
      worth = huntable[animal_to_add]
      responses = [
        f"<@{user}> went hunting and got a {allitememojis[animal_to_add]} {animal_to_add} which is worth {worth} coins.",
        f"<@{user}> spent a whole day hunting down a {allitememojis[animal_to_add]} {animal_to_add} worth {worth} and actually got it",
      ]
      if animal_to_add != "dragon_wing":
        text = responses[random.randint(0, 1)]
      else:
        text += f" **{responses[random.randint(0,1)]}**"
      number = 1000
      if "runeequip" + user in db:
        rune = db["runeequip" + user]
        if "unbreaking" in rune:
          lvl = int(rune[-1])
          number = 1000 / ((lvl + 1)**2) / 2
        chance = random.randint(1, 100000)
        if chance <= number:
          text = text + "**...and your hunting rifle broke**"
          inventoryremove(user, "hunting_rifle", 1)
        if chance <= 1000 and chance > number:
          text += "**YOUR RUNE SAVED YOUR RIFLE FROM BREAKING**"
    else:
      item = await itemsGrind(user)
      text = f"You got a(n) {item} while hunting"
    notechance = random.randint(1, 100)
    if notechance < 5:
      inventoryadd(user, "banknote", 1)
      text += "** and you found a banknote while looking for animals**"
    collect = await collectables(user, "hunt")
    text += collect
    embed = discord.Embed(title="**__Hunt__ 🔍**",
                          description=str(text),
                          color=discord.Color.random())
    await message.reply(embed=embed)
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1
  if "bpinfo" + str(message.author.id) in db:
    data = db["bpinfo" + str(message.author.id)]["quests"]
    for i in data.values():
      if "Hunts Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Dig Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))
      if "Commands Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Commands Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))


# FISH
fishable = {
  "seahorse": "750",
  "fish": "1,500",  #3
  "salmon": "5,000",  #4
  "whale": "50,000",  #100
  "megalodon_tooth": "1,000,000",  #300
}


@bot.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def fish(message):
  user = str(message.author.id)
  users = str("inv" + user)
  inventory_items = db[users].keys()
  if user not in db:
    db[user] = 0
  if "fishing_rod" not in inventory_items:
    await message.reply(
      "You require to aquire a fishing rod first. Go buy one in the shop")
  else:
    if random.randint(1, 10) != 1:
      number = random.randint(1, 1000)
      if number < 300:  # 300
        animal_to_add = "seahorse"
      if number < 700:  # 400
        animal_to_add = "fish"
      elif number < 950:  #250
        animal_to_add = "salmon"
      elif number < 1000:
        animal_to_add = "whale"  #50
      else:
        animal_to_add = "megalodon_tooth"
      inventoryadd(user, animal_to_add, 1)
      worth = fishable[animal_to_add]
      responses = [
        f"<@{user}> went fishing and got a {allitememojis[animal_to_add]} {animal_to_add} which is worth {worth} coins.",
        f"<@{user}> were fishing and when you pulled out a {allitememojis[animal_to_add]} {animal_to_add} worth {worth}",
      ]
      if animal_to_add != "megalodon_tooth":
        text = responses[random.randint(0, 1)]
      else:
        text = f" **{responses[random.randint(0,1)]}**"
      number = 1000
      if "runeequip" + user in db:
        rune = db["runeequip" + user]
        if "unbreaking" in rune:
          lvl = int(rune[-1])
          number = 1000 / ((lvl + 1)**2) / 2
        chance = random.randint(1, 100000)
        if chance <= number:
          text = text + "**...and your fishing rod broke**"
          inventoryremove(user, "fishing_rod", 1)
        if chance <= 1000 and chance > number:
          text += "**YOUR RUNE SAVED YOUR ROD FROM BREAKING**"
    else:
      item = await itemsGrind(user)
      text = f"You got a(n) {item} while fishing"
    notechance = random.randint(1, 100)
    if notechance < 5:
      inventoryadd(user, "banknote", 1)
      text += "** and you fished out a :bank: banknote**"
    collect = await collectables(user, "fish")
    text += collect
    embed = discord.Embed(title="**__Fish__ 🔍**",
                          description=str(text),
                          color=discord.Color.random())
    await message.reply(embed=embed)
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1
  if "bpinfo" + str(message.author.id) in db:
    data = db["bpinfo" + str(message.author.id)]["quests"]
    for i in data.values():
      if "Fishes Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Fish Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))
      if "Commands Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Commands Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))


games = [
  "fifa_mobile", "mario_kart", "minecraft", "fortnite", "roblox", "fifa23",
  "gta4", "gta5", "gta6"
]


# GAME   # CHANGE LATER TO ADD BREAK CHANCE
@bot.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def game(message):
  user = str(message.author.id)
  if db["prestige" + user] < 1:
    return await message.send(
      "You can only game after prestiging once. Go prestige to become a gamer!"
    )
  users = str("inv" + user)
  inventory_items = db[users].keys()
  break_chance = random.randint(1, 200)
  broke = False
  if "xbox_mini_fridge" in inventory_items:
    shovel = 75
  elif "PS6" in inventory_items:
    shovel = 60  # 500k
    if break_chance == 1:
      inventory_items.remove("PS6")
      broke = True
  elif "PS5" in inventory_items:
    shovel = 24  # 100k
    if break_chance < 3:
      inventory_items.remove("PS5")
      broke = True
  elif "PS4" in inventory_items:
    shovel = 12  # 10k
    if break_chance < 9:
      inventory_items.remove("PS4")
      broke = True
  elif "PS3" in inventory_items:
    shovel = 4  # 2.5k
    if break_chance < 15:
      inventory_items.remove("PS3")
      broke = True
  elif "PS2" in inventory_items:
    shovel = 2  # 500
    if break_chance < 21:
      inventory_items.remove("PS2")
      broke = True
  else:
    shovel = "no console"
  numb = 1
  for i in games:
    if shovel != "no console":
      if i in inventory_items:
        shovel += int(numb)
        numb += 1

  user = str(message.author.id)
  if user not in db:
    db[user] = 0
  multi = 0
  coins = db[user]
  if shovel != "no console":
    if random.randint(1, 10) != 1:
      coins_to_add = round(random.randint(25, 50) * shovel)
      if "runeequip" + user in db:
        rune = db["runeequip" + user]
        if "game" in rune:
          lvl = int(rune[-1])
          multi = lvl / 2
          coins_to_add += round(multi * coins_to_add)
      responses = [
        f"<@{user}> grinded up to level 250 and sold his account for {coins_to_add} coins",
        f"<@{user}> farmed some potatoes in minecraft and sold them for {coins_to_add} coins",
        f"<@{user}> cranked some 90s and earned {coins_to_add} coins",
        f"<@{user}> tried playing fortnite but got sniped and earned nothing",
      ]
      number = random.randint(0, len(responses) - 1)
      text = responses[number]
      if "nothing" not in text:
        coins += coins_to_add
        db[user] = coins
      if "xbox_mini_fridge" in inventory_items and (number == 3
                                                    or number == 2):
        text = f"<@{user}> drank some PRIME ENERGY from his *xbox_mini_fridge*\nIt powered him to get {coins_to_add} in his new ESports career."
      elif "469521741744701444" in user and number == 3:  # RAZI
        text = f"<@{user}> tried playing some bios but got tripled sprayed"
      elif "1048148583196676106" in user and number == 1:
        text = f"<@{user}> beamed everyone he saw while standing still and earned {coins_to_add} coins"  # KAI
      elif "868472825252552735" in user and number == 3:  # SUVHEET
        text = f"<@{user}> did the griddy for too long and died"
      elif "935562487481372732" in user and number == 3:  # RYAN
        text = f"<@{user}> 1 pumped someone in a wager and won {coins_to_add} coins"
      elif "600411237561663498" in user and number == 3:  # THAJAN
        letters = list(string.ascii_letters + string.digits +
                       string.punctuation)
        result_str = ''.join(random.choice(letters) for i in range(4039))
        text = "<@600411237561663498> GAVE UP\n**Game Chat: **" + result_str + str(
          coins_to_add)
      if multi != 0:
        more = int(multi) * 100
        text += f"  __Your game rune giving you {more}% more coins__"
      if broke:
        text += "... and after losing a match you threw your console so hard it broke"
    else:
      item = await itemsGrind(user)
      text = f"You got a(n) {item} while searching"
    notechance = random.randint(1, 100)
    if notechance < 4:
      inventoryadd(user, "banknote", 1)
      text += "** and you got a banknote from winning a game**"
    collect = await collectables(user, "game")
    text += collect
    embed = discord.Embed(title="**__Game__ 🎮**",
                          description=str(text),
                          color=discord.Color.random())
    await message.reply(embed=embed)
  else:
    await message.reply("You don't even have a console. Go buy one in the shop"
                        )
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1


# MINE
@bot.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def mine(message):
  user = str(message.author.id)
  users = str("inv" + user)
  if user not in db:
    db[user] = 0
  inventory_items = db[users].keys()
  if "pickaxe" in inventory_items or "excavator" in inventory_items:
    if int(random.randint(1, 10)) != 1:
      times = 1
      break_chance = random.randint(1, 100)
      if "excavator" in inventory_items:
        chance = random.randint(1, 100)
        if chance < 20:
          times = 1
        elif chance < 60:
          times = 2
        elif chance < 85:
          times = 3
        elif chance < 100:
          times = 4
        else:
          times = 5
      multi = 1
      if "runeequip" + user in db:
        rune = db["runeequip" + user]
        if "mine" in rune:
          lvl = int(rune[-1])
          if lvl == 1:
            runechance = random.randint(1, 100)
            if runechance > 50:
              multi = 2
          elif lvl != 0:
            multi = random.randint(1,2**(lvl - 1))
      responses = [
        f"<@{user}> found {allitememojis['coal_ore']} {times*multi} coal ore while mining",
        f"<@{user}> found {allitememojis['iron_ore']} {times*multi} iron ore while mining",
        f"<@{user}> found {allitememojis['gold_ore']} {times*multi} gold ore while mining",
        f"<@{user}> found {allitememojis['diamond']} {times*multi} diamond while mining",
        f"<@{user}> found {allitememojis['saphire']} {times*multi} saphire while mining"
      ]
      number = random.randint(1, 100)
      amount = times * multi
      if amount > 10:
        amount = 10
      if number < 3:
        text = responses[4]
        inventoryadd(user, "saphire", amount)
      elif number < 8:
        text = responses[3]
        inventoryadd(user, "diamond", amount)
      elif number < 28:
        text = responses[2]
        inventoryadd(user, "gold_ore", amount)
      elif number < 57:
        text = responses[1]
        inventoryadd(user, "iron_ore", amount)
      else:
        text = responses[0]
        inventoryadd(user, "coal_ore", amount)
      if times == 5 and "saphire" in text:
        await message.reply(
          "You got **5 saphires** that is **0.02%** chance. If you see this message - then you are literally just... just insanely lucky"
        )
      if multi != 1:
        text += f", your rune letting you mine {multi} times more"

      if "excavator" in inventory_items:
        number = 1000
        if "runeequip" + user in db:
          rune = db["runeequip" + user]
          if "unbreaking" in rune:
            lvl = int(rune[-1])
            number = 1000 / ((lvl + 1)**2) / 2
          chance = random.randint(1, 100000)
          if chance <= number:
            text = text + "**...and your excavator broke**"
            inventoryremove(user, "excavator", 1)
          if chance <= 1000 and chance > number:
            text += "**YOUR RUNE SAVED YOUR EXCAVATOR FROM BREAKING**"
        else:
          if random.randint(1, 100) == 1:
            inventoryremove(user, "excavator", 1)
            text += "**...and you excavator broke"
      elif "pickaxe" in inventory_items:
        number = 2000
        if "runeequip" + user in db:
          rune = db["runeequip" + user]
          if "unbreaking" in rune:
            lvl = int(rune[-1])
            number = 2000 / ((lvl + 1)**2) / 2
          chance = random.randint(1, 100000)
          if chance <= number:
            text = text + "**...and your pickaxe broke**"
            inventoryremove(user, "excavator", 1)
          if chance <= 1000 and chance > number:
            text += "**YOUR RUNE SAVED YOUR PICKAXE FROM BREAKING**"
        else:
          if random.randint(1, 100) < 3:
            inventoryremove(user, "pickaxe", 1)
            text += "**...and you pickaxe broke"
    else:
      item = await itemsGrind(user)
      text = f"You got a(n) {item} while mining"
    notechance = random.randint(1, 100)
    if notechance == 1:
      inventoryadd(user, "banknote", 1)
      text += "** and you also found a banknote**"
    collect = await collectables(user, "mine")
    text += collect
    embed = discord.Embed(title="**__Mine__**",
                          description=str(text),
                          color=discord.Color.random())
    await message.reply(embed=embed)
  else:
    await message.reply("You don't even have a pickaxe. Go buy one in the shop"
                        )
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1

  if "bpinfo" + str(message.author.id) in db:
    data = db["bpinfo" + str(message.author.id)]["quests"]
    for i in data.values():
      if "Mines Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Mine Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))
      if "Commands Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Commands Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))


subjects = [
  "Maths",
  "English",
  "Science",
  "Computing",
  "PE",
  "RE",
  "History",
  "Geography",
  "DT",
  "Music",
  "Art",
  "Economics",
  "Business",
  "German",
  "Spanish",
  "Biology",
  "Chemistry",
  "Physics",
  "Drama",
  "Cookery",
  "Algebra",
  "Quadratic Formula",
  "Arithmetic",
  "Probability",
  "Trignometry",
]


# STUDY
@bot.command()
@commands.cooldown(1, 7, commands.BucketType.user)
async def study(message):
  user = str(message.author.id)
  users = str("inv" + user)
  if user not in db:
    db[user] = 0
  coins = db[user]
  inventory_items = db[users]
  if random.randint(1, 10) != 1:
    if "runeequip" + user in db and "study" in str(db["runeequip" + user]):
      studyrune = str(db["runeequip" + user])[6:]
      cal = int(studyrune) * 22
      chance1 = 100 - cal
      chance2 = 100
      unlucky = random.randint(1, 3)
      if unlucky == 1:
        chance1 = 1
        chance2 = 100 - cal
      txt = "\n__Your Study Rune is giving a higher chance of success__"
    else:
      chance1 = 1
      chance2 = 100
      txt = ""
    multi = 1
    if "textbook" in inventory_items:
      if inventory_items["textbook"] > 0:
        multi += 1
    if "flashcards" in inventory_items:
      if inventory_items["flashcards"] > 0:
        multi += 1
    score = random.randint(chance1, chance2)
    grade = ""
    scoremulti = 0
    if score >= 98:
      grade = "A+"
      scoremulti = 20
    elif score >= 89:
      grade = "A"
      scoremulti = 10
    elif score >= 74:
      grade = "B"
      scoremulti = 8
    elif score >= 60:
      grade = "C"
      scoremulti = 6
    elif score >= 58:
      grade = "D"
      scoremulti = 4
    elif score >= 24:
      grade = "E"
      scoremulti = 2
    else:
      grade = "F"
      scoremulti = 0
    coins_to_add = int(30 * multi * scoremulti)
    coins += coins_to_add
    db[user] = coins
    thesubjectnumb = random.randint(1, len(subjects))
    subject = subjects[thesubjectnumb]
    runemulti = 1
    if "runeequip" + user in db:
      rune = db["runeequip" + user]
      if "study" in rune:
        lvl = int(rune[-1])
        runeulti = lvl / 2
        coins_to_add += round(runeulti * coins_to_add)
    responses = [
      "seecret",
      f"<@{user}>'s mom gave them {coins_to_add} coins for getting a {grade} in the {subject} test.",
      f"<@{user}>'s dad gave them {coins_to_add} coins for getting a {grade} in the {subject} test.",
    ]
    number = random.randint(1, len(responses) - 1)
    text = responses[number]
    if runemulti != 1:
      more = runemulti * 100
      text += f", your rune letting you get {more}% more coins"
  else:
    item = await itemsGrind(user)
    text = f"You got a(n) {item} while studying"
  notechance = random.randint(1, 100)
  if notechance < 4:
    inventoryadd(user, "banknote", 1)
    text += "** and you found a banknote in your revision notes**"
  collect = await collectables(user, "study")
  text += collect
  embed = discord.Embed(title="**__Study__**",
                        description=str(text + txt),
                        color=discord.Color.random())
  await message.reply(embed=embed)
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1
  if "bpinfo" + str(message.author.id) in db:
    data = db["bpinfo" + str(message.author.id)]["quests"]
    for i in data.values():
      if "Studies Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Study Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))
      if "Commands Ran" in i:
        num = int(list(data.values()).index(i)) + 1
        db["bpinfo" + str(message.author.id)]["quests"][str(num)][1] -= 1
        if int(data[str(num)][1]) - 1 == 0:
          await message.send(embed=await embedify(
            f"You completed your Commands Quest for {num} points!", ""))
          a = random.choice(list(bpquests.keys()))
          db["bpinfo" + user]["quests"][str(num)] = [a, bpquests[a][num - 1]]
          db["bpinfo" + user]["points"] += int(num)
          await message.send(
            embed=await embedify(f"New Quest!", f"{bpquests[a][num-1]} {a}"))
