
@bot.command()
async def createcode(ctx, times: str = None):
  if "CODES" not in db:
    db["CODES"] = {}
  code = ""
  if times == None:
    times = 1
  elif times.isnumeric():
    times = int(times)
  else:
    code = times
    times = 1
  user = str(ctx.author.id)
  if user != "600411237561663498" and user != "469521741744701444" and user != "1092483157841940581":
    return await ctx.reply("L not mod")
  txt = ""
  for i in range(times):
    codes = await create_code(code)
    txt += codes + "\n"
  embed = discord.Embed(title="**New Codes**",
                        description=txt,
                        color=discord.Color.random())
  await ctx.reply(embed=embed)
  command = list(str(ctx.message.content).split(" "))[0]


@bot.command()
async def codes(ctx):
  user = str(ctx.author.id)
  if user != "600411237561663498" and user != "469521741744701444" and user != "1092483157841940581":
    return await ctx.reply("L not mod")
  txt = str(list(db['CODES'].keys())).replace("'",
                                              "").replace(",", "\n").replace(
                                                "[", "").replace("]", "")
  embed = discord.Embed(title="**Codes**",
                        description=txt,
                        color=discord.Color.random())
  await ctx.reply(embed=embed)


@bot.command()
async def redeem(ctx, code):
  user = str(ctx.author.id)
  if code in db["CODES"].keys():
    embed = discord.Embed(title="**Valid Code**",
                          description=f"You got a {db['CODES'][code]}.",
                          color=discord.Color.green())
    inventoryadd(user, str(db['CODES'][code]), 1)
    del db["CODES"][code]
    await ctx.reply(embed=embed)
  else:
    embed = discord.Embed(title="**Invalid Code**",
                          description="Not a real code.",
                          color=discord.Color.red())
    await ctx.reply(embed=embed)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1
