

@bot.command(name="battlepass", aliases=["bp"])
async def battlepass(ctx, type=None):
  user = str(ctx.author.id)
  if "bpinfo" + user not in db:
    a = random.choice(list(bpquests.keys()))
    b = random.choice(list(bpquests.keys()))
    c = random.choice(list(bpquests.keys()))
    questGiven = {
      1: [a, bpquests[a][0]],
      2: [b, bpquests[b][1]],
      3: [c, bpquests[c][2]],
    }
    db["bpinfo" + user] = {
      "quests": questGiven,
      "points": 0,
      "lvl": 0,
    }
  data = db["bpinfo" + user]
  if type == None:
    embed = discord.Embed(
      title="**Battlepass**",
      description=
      f"**Battlepass Level:** {data['lvl']}\n\n**Total Points:** {data['points']}",
      color=discord.Color.random())
    text = ""
    txt = ""
    for i, v in data["quests"].items():
      if int(i) == 1:
        txt = "<:i_:1120409267208466433> "
      elif int(i) == 2:
        txt = "<:ii:1120409264490557580> "
      elif int(i) == 3:
        txt = "<:iii:1120409262993190912> "
      else:
        txt = str(i)
      text += txt + str(v[1]) + " " + v[0] + "\n"
    embed.add_field(name="Quests", value=text)
    await ctx.reply(embed=embed)
  elif "upgrade" in type:
    pointCost = math.ceil((data["lvl"] + 1) / 25)
    if data["points"] >= pointCost:
      data["lvl"] += 1
      data["points"] -= pointCost
      txt = ""
      if data["lvl"] in bpRewards:
        for i in bpRewards[data["lvl"]]:
          if i in allitememojis:
            txt += f" You also got a {allitememojis[i]} {i}."
            inventoryadd(user, i, 1)
          else:
            txt += f". You also got a {i}"
            inventoryadd(user, i, 1)
      embed = discord.Embed(
        title="**Battlepass**",
        description=
        f"Upgraded to level {data['lvl']} for {pointCost} points!{txt}",
        color=discord.Color.random())
      await ctx.reply(embed=embed)
    else:
      embed = discord.Embed(
        title="**Battlepass**",
        description=
        f"You dont have enought points to level up\n\nYou have: {data['points']}\n\nPoints Required: {pointcost}",
        color=discord.Color.red())
      await ctx.reply(embed=embed)
