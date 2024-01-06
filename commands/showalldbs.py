@bot.command()
async def showalldbs(ctx):
  if ctx.author.id != 469521741744701444 or ctx.author.id == 600411237561663498:
    return await ctx.reply("NOT ADMIN")
  for i in db.keys():
    if "shard" in i:
      await ctx.reply(f"{i} = {db[i]}t")