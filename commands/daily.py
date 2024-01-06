
# DAILY
@bot.command()
async def daily(ctx):
  userId = str(ctx.author.id)
  if "dailytime" + userId not in db:
    db["dailytime" + userId] = 0
  if db["userlvl" + userId] < 3:
    return await ctx.reply(
      "You need to be at least Level 3 to claim your daily")
  if round(time.time()) - db["dailytime" + userId] > 64800:
    if round(time.time()) - db["dailytime" + userId] < 129600:
      db["streak" + userId] += 1
    else:
      db["streak" + userId] = 0
      await ctx.reply("You lost your streak.")
    if "prestige" + userId in db:
      num1 = int(db["prestige" + userId]) * 10000
    else:
      num1 = 0
    if "userlvl" + userId in db:
      num2 = int(db["userlvl" + userId]) * 1000
    else:
      num2 = 0
    if "streak" + userId in db:
      num3 = int(db["streak" + userId]) * 2000
    else:
      db["streak" + userId] = 0
      num3 = 0
    amount = num1 + num2 + num3 + 12000
    db["dailytime" + userId] = round(time.time())
    embed = discord.Embed(title="**__Daily__**",
                          description="You got:\n 12,000",
                          color=discord.Color.random())
    inventoryadd(userId, "daily", 1)
    embed.add_field(name="__Prestige__", value=f"+{add_commas(str(num1))}")
    embed.add_field(name="__Level__", value=f"+{add_commas(str(num2))}")
    embed.add_field(name="__Streak__", value=f"+{add_commas(str(num3))}")
    embed.set_footer(text=f"Total: {add_commas(str(amount))}")
    db[userId] += amount
    await ctx.reply(embed=embed)
  else:
    timeleft = (int(db["dailytime" + userId]) + 86400) - round(time.time())
    hours = timeleft // 3600
    timeleft = timeleft - (hours * 3600)
    minutes = timeleft // 60
    seconds = timeleft % 60
    msg = str(
      f"You can collect your next daily in {hours} hours {minutes} minutes and {seconds} seconds."
    )
    embed = discord.Embed(title="**__Cooldown__**",
                          description="",
                          color=discord.Color.red())
    embed.add_field(name=msg, value="")
    await ctx.reply(embed=embed)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1

