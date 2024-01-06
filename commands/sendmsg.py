@bot.command()
async def sendmsg(ctx, msg, *, count: int = None, channel=None):
  if "_" in msg:
    msg = msg.replace("_", " ")
  msg = msg.replace("/n", "\n")
  if count == None:
    count = 1
  if "469521741744701444" == str(ctx.author.id) or "600411237561663498" == str(
      ctx.author.id):
    user = "admin"
  else:
    user = None  #str(ctx.author.id)
  if msg == "stop" and user == "admin":
    db["sendmsg"] = "OFF"
    await ctx.reply("Disallowing sendmsg")
  elif msg == "start" and user == "admin":
    db["sendmsg"] = "ON"
    await ctx.reply("Allowing sendmsg")
  count = int(count)
  if user == "admin":
    for i in range(count):
      await ctx.reply(msg)
      time.sleep(0.1)
  elif db["sendmsg"] == "ON":
    if count > 5:
      count = 5
    for i in range(count):
      await ctx.reply(msg)
      time.sleep(0.1)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1