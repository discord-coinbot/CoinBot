@bot.command()
async def bar(ctx, num1, num2):
  await ctx.reply(get_bar(int(num1), int(num2)))
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1