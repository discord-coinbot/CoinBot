@bot.command()
async def update(ctx):
  txt = "** **"
  if "bot" in str(ctx.message.content):
    txt = "<@&1118613436444704979>"
  embed = discord.Embed(
    title="__**Merchant + Lottery + Trade**__",
    description=
    "This update announces many new commands! \n* **!lottery** to enter the lottery \n* **!trade** trading revamp \n* **!merchant** to see the latest deals\nFor more infomation, check the full update logs below! (We **advise** you to check out the full update logs as this isnt all of it and it goes through some things not meantioned here.)\n\nMake sure to join the CoinBot Communinty Server too!\nhttps://discord.gg/6sKNYkRE64",
    color=discord.Color.random())  
  await ctx.reply(txt, embed=embed, view=Links())
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1