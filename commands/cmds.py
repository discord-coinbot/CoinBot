@bot.command(name="cmds")
async def cmds(ctx):
  db["cmds" + str(ctx.author.id)] = dict(
    sorted(db["cmds" + str(ctx.author.id)].items(),
           key=lambda x: x[1],
           reverse=True))
  txt = ""
  for i, v in db["cmds" + str(ctx.author.id)].items():
    txt += f"{i}: {v}\n"
  embed = discord.Embed(title="**Commands Ran**", description=txt)
  await ctx.reply(embed=embed)