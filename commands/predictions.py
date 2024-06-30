@bot.command()
async def addpred(ctx):
  if ctx.author.id not in [600411237561663498, 802295496538193960, 868472825252552735]:
    return await ctx.reply("Silly **goose**, you cannot do this.")
  if "EUROS_PRED" not in db:
    db["EUROS_PRED"] = {}
  
  await ctx.send("Who v Who?")
  print(1)
  game = await discordinput(ctx)
  print("HERE")
  await ctx.send("Game start time? (24 hr format %d/%m/%Y %H:%M eg 30/06/2024 10:00)")
  times = await discordinput(ctx)
  print(2)
  realtime = time.mktime(datetime.datetime.strptime(times, "%d/%m/%Y %H:%M").timetuple())
  db["EUROS_PRED"][game] = {"PredStart": False, "StartTime": realtime-3600, "Game": game}
  await ctx.reply("Starting 3 hours before the match.")
