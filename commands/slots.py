
# SLOTS
@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def slots(message, amount):
  user = str(message.author.id)
  coins = int(db[user])
  if int(amount) < 1000:
    return await message.reply("Minimum to slot is 1000 coins")
  if coins < int(amount) * 3:
    return await message.reply("You can't bet more than 1/3 of your balance")
  emojis = {
    ":gem:": 100,
    ":coin:": 80,
    ":moneybag:": 60,
    ":hamburger:": 40,
    ":candy:": 20,
    ":pretzel:": -10,
    ":chocolate_bar:": -20,
    ":croissant:": -30,
    ":sandwich:": -40,
    ":cut_of_meat:": -50,
    ":poultry_leg:": -60,
    ":cooking:": -70,
    ":meat_on_bone:": -80,
    ":canned_food:": -90,
    ":rock:": -100,
  }
  random_item1 = random.choice(list(emojis.keys()))
  random_item2 = random.choice(list(emojis.keys()))
  random_item3 = random.choice(list(emojis.keys()))
  random_item1val = int(emojis[random_item1])
  random_item2val = int(emojis[random_item2])
  random_item3val = int(emojis[random_item3])
  percentagewon = int(random_item1val) + int(random_item2val) + int(
    random_item3val)
  amounts = int(int(amount) / 100)
  amounti = int(int(percentagewon) * int(amounts))
  amountwon = round(int(amounti))
  text = random_item1 + random_item2 + random_item3
  embed = discord.Embed(title="**__Slots__**",
                        description=text,
                        color=discord.Color.random())
  db[user] += amountwon
  if amountwon < 0:
    amounts = str(amountwon)
    amounts = amounts.replace("-", "")
    embed.add_field(name="Lost", value=f"You lost {amounts} coins.")
    embed.color = discord.Color.red()
  elif amountwon == 0:
    amounts = str(amountwon)
    amounts = amounts.replace("-", "")
    embed.add_field(name="Draw", value="You won nothing but lost nothing.")
    embed.color = discord.Color.dark_grey()
  elif amountwon > 0:
    amounts = str(amountwon)
    embed.add_field(name="Won", value=f"You won {amounts} coins.")
    embed.color = discord.Color.green()
  embed.set_footer(text=f"Net Won: {percentagewon}%")
  await message.reply(embed=embed)
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1
