
# FEEDBACK
@bot.command()
async def feedback(ctx):
  channel = bot.get_channel(1096799510845468672)
  message = str(ctx.message.content).replace("!feedback ", "")
  message = str(ctx.message.content).replace("!feedback", "")
  embed = discord.Embed(title="**__Feedback__**",
                        description=str(message),
                        color=discord.Color.random())
  name = str(await bot.fetch_user(ctx.author.id))
  embed.set_footer(text=f"From {name}")
  await ctx.reply("Feedback sent!")
  await channel.send(embed=embed)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1

