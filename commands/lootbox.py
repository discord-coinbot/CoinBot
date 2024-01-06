# OPEN
commonbox = ["1000", "wooden_shovel", "PS2", "coal_ore", "ant", "seahorse"]
uncommonbox = ["10000", "iron_shovel", "PS3", "mouse", "pigeon", "fish"]
rarebox = [
  "20000", "diamond_shovel", "PS4", "salmon", "cow", "horse", "flashcards",
  "textbook"
]
epicbox = [
  "50000", "netherite_shovel", "PS5", "lock_pick", "fifa23", "lock",
  "stingray", "shark", "deer", "buffalo"
]
legendarybox = [
  "100000", "fishing_rod", "hunting_rifle", "bolts", "halver", "doubler"
]

prestigebox = [
  "25000", "pickaxe", "fifa23", "netherite_shovel", "PS5", "lock_pick",
  "fifa23", "lock", "stingray", "shark", "deer", "buffalo"
]

daily = [
  "2500", "fish", "seahorse", "ant", "mouse", "coal_ore", "iron_ore", "diamond"
]

lootboxes = {
  "commonbox": ["1000", "wooden_shovel", "PS2", "coal_ore", "ant", "seahorse"],
  "uncommonbox": ["10000", "iron_shovel", "PS3", "mouse", "pigeon", "fish"],
  "rarebox": [
    "20000", "diamond_shovel", "PS4", "salmon", "cow", "horse", "flashcards",
    "textbook"
  ],
  "epicbox": [
    "50000", "netherite_shovel", "PS5", "lock_pick", "fifa23", "lock",
    "stingray", "shark", "deer", "buffalo"
  ],
  "legendarybox":
  ["100000", "fishing_rod", "hunting_rifle", "bolts", "halver", "doubler"],
  "daily": [
    "2500", "fish", "seahorse", "ant", "mouse", "coal_ore", "iron_ore",
    "diamond"
  ],
  "prestigebox": [
    "25000", "pickaxe", "fifa23", "netherite_shovel", "PS5", "lock_pick",
    "fifa23", "lock", "stingray", "shark", "deer", "buffalo"
  ],
  "craft_box": [
    "rabbit_foot", "sugar", "glitter", "owl_eye", "packet_of_blood", "lamp",
    "toothpick", "paper", "glue", "card", "pen"
  ],
  "holy_craft_box": [
    "slurp_juice", "motor", "ammo", "bait", "redstone", "mini",
    "mechanical_part"
  ],
}


@bot.command(name="open")
async def open_command(ctx, item, number: int = None):
  if number == None:
    number = 1
  user = str(ctx.author.id)
  inventory_items = db["inv" + user]
  if item not in lootboxes:
    return await ctx.reply(
      embed=await embedify("Open", f"{item} is not a valid item."))
  if item in inventory_items:
    if inventory_items[item] < number:
      return await ctx.reply(
        embed=await embedify("Open", f"You don't have {number} {item}s"))
  else:
    return await ctx.reply(
      embed=await embedify("Open", f"You don't have {number} {item}s"))
  link = await bot.fetch_user(user)
  embed = discord.Embed(title=f"{link} opened {number} {item}",
                        description="**You got:**",
                        color=discord.Color.random())
  txt = ""
  listOfItems={}
  for i in range(number):
    itemsGot = random.randint(1, 3)
    for i in range(itemsGot):
      itemfromLoot = random.choice(lootboxes[item])
      if itemfromLoot.isnumeric():
        db[user] += int(itemfromLoot)
        if "Coins" in listOfItems:
          listOfItems["Coins"]+=int(itemfromLoot)
        else:
          listOfItems["Coins"]=int(itemfromLoot)
      else:
        if itemfromLoot in sellable:
          amountofitem = random.randint(1, 5)
        else:
          amountofitem = 1
        if itemfromLoot in listOfItems:
          listOfItems[itemfromLoot]+=amountofitem
        else:
          listOfItems[itemfromLoot]=amountofitem
        # if itemfromLoot in allitememojis:
        #   txt += allitememojis[itemfromLoot] + " "
        # txt += str(amountofitem) + " " + itemfromLoot + "\n"
        inventoryadd(user, itemfromLoot, amountofitem)
  for i,v in listOfItems.items():
    if i in allitememojis:
      txt += allitememojis[i]+" "+str(v)+" "+i+"\n"
    elif i=="Coins":
      txt+=f":moneybag: {v} Coins\n"
    else:
      txt+=f"{v} {i}\n"
  inventoryremove(user, item, number)
  embed.add_field(name="", value=txt)
  await ctx.reply(embed=embed)
