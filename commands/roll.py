@bot.command()
async def roll(ctx):
  async with ctx.typing():
    chance = random.randint(1, 8)
    await asyncio.sleep(chance)
    chance = random.randint(0, 6)
    responses = [
      "definetely yes", "Probably", "maybe...", "try again", "ask me later",
      "Probably not", "defintely no"
    ]
  await ctx.reply(responses[chance])
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1