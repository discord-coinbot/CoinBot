
@bot.command(name="restaurant", aliases=["diner", "cafe"])
async def restaurant(ctx, type=None):
  user = str(ctx.author.id)
  if "restaurant" + user not in db:
    db["restaurant" + user] = {
      "Level": 1,
      "Money": 0,
      "Style": "Default",
      "Waiters": 1,
      "Cooks": 1,
      "Floors": 1,
      "Size": 10,
      "Rating": 1,
      "Customers Served": 0,
      "Time": 1688150415,
      "Total Earned": 0,
    }
  data = db["restaurant" + user]
  for i, v in data.items():
    if isfloat(v):
      data[i] = round(v)
    else:
      pass
  if "Cookers" in data.keys():
    db["restaurant" + user]["Cooks"] = db["restaurant" + user]["Cookers"]
    del db["restaurant" + user]["Cookers"]
  if data["Time"] + 3600 < time.time():
    num = (round(time.time()) - (data["Time"])) // random.randint(1400, 2500)
    served = round(num * data["Floors"] * data["Size"] *
                   (random.randint(15, 20) / 10))
    revenue = round(served * data["Rating"] *
                    (1.15**data["Level"])) * random.randint(10, 20)
    w = random.randint(70, 100)*(served/70)
    c = random.randint(70, 100)*(served/70)
    wcosts = 0
    ccosts = 0
    ecosts = round(data["Size"] * random.randint(3, 7) * data["Floors"] *
                   data["Rating"] * num * (random.randint(65, 95) / 100))
    for i in range(0, data["Waiters"]):
      wcosts += w
      w *= (random.randint(35, 55)) / 100
      w = round(w)
    for i in range(0, data["Cooks"]):
      ccosts += c
      c *= (random.randint(35, 65)) / 100
      c = round(c)
    tcosts = wcosts + ccosts + ecosts
    embed = discord.Embed(title="**Your Restaurant**",
                          description="What happened while you were gone.")
    embed.add_field(name="Customers Served:", value=add_commas(served))
    embed.add_field(name="Revenue:", value=add_commas(revenue))
    embed.add_field(
      name="Costs:",
      value=
      f"{add_commas(wcosts)} - Waiters\n{add_commas(ccosts)} - Cooks\n{add_commas(ecosts)} - Electricity"
    )
    embed.add_field(name="Net Costs:", value=f"{add_commas(tcosts)}")
    embed.add_field(name="Net Profit:", value=f"{add_commas(revenue-tcosts)}")
    await ctx.reply(f":wave: Hey, {ctx.author.mention}!", embed=embed)
    data["Customers Served"] += served
    data["Money"] += revenue - tcosts
    data["Total Earned"] += revenue - tcosts
    data["Time"] = round(time.time()) - 3600
  link = await bot.fetch_user(int(user))
  theLink = ctx.author.display_avatar.url
  if type == None:
    embed = discord.Embed(
      title="",
      description=
      "**                                                         **",
      color=discord.Color.red())
    embed.set_author(name=f"{str(link).split('#')[0]}'s restaurant",
                     icon_url=theLink)
    embed.set_thumbnail(url=theLink)
    embed.set_image(url=restaurantImages[data["Style"]])
    await ctx.reply(embed=embed)
  elif "profile" in type.lower():
    embed = discord.Embed(title="", description="", color=discord.Color.red())
    embed.set_author(name=f"{str(link).split('#')[0]}'s restaurant",
                     icon_url=theLink)
    embed.set_thumbnail(url=theLink)
    embed.add_field(name="Level:", value=data["Level"])
    txt = ""
    for i in range(0, round(data["Rating"])):
      txt += "<:star:1124639847424991253>"
    embed.add_field(name=f"Rating: {data['Rating']}", value=str(txt))
    embed.add_field(name="Waiters:", value=data["Waiters"])
    embed.add_field(name="Cooks:", value=data["Cooks"])
    embed.add_field(name="Customers Served:", value=data["Customers Served"])
    embed.add_field(name="Total Earned:", value=data["Total Earned"])
    await ctx.reply(embed=embed)
  elif "upgrades" in type.lower():
    pass
  elif "bal" in type.lower():
    embed = discord.Embed(title="**__Your Restaurant__**",
                          description="Y",
                          color=discord.Color.red())
    embed.add_field(name="Youtube Bank:",
                    value=str(data['Money']),
                    inline=False)
    embed.set_thumbnail(url=theLink)
    await ctx.reply(embed=embed)
  db["restaurant" + user] = data