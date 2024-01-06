@bot.command(name="embed")
async def embed(ctx, title, desc):
  embed = discord.Embed(title=title.replace("`", " "),
                        description=desc.replace("`", " test"),
                        color=discord.Color.green())
  await ctx.reply(embed=embed)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1