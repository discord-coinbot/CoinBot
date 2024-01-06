
@bot.command()
async def randomise(ctx, type, start, end):
  if end == None:
    end = ""
  if "num" in type:
    start = int(start)
    end = int(end)
    number = random.randint(start, end)
    await ctx.reply(number)
  elif "word" in type:
    choice = random.randint(1, 2)
    if choice == 1:
      await ctx.reply(start)
    elif choice == 2:
      await ctx.reply(end)
  elif "choices" in type:
    text = ctx.message.content
    text = text.replace(".randomise choices ", "")
    text = text.replace("!randomise choices ", "")
    thelist = list(text.split(" "))
    choice = random.randint(1, len(thelist))
    await ctx.reply(thelist[choice])
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1