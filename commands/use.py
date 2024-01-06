@bot.command()
async def use(ctx, item, amount=None):
  if amount==None:
    amount=1
  amount = int(amount)
  user = str(ctx.author.id)
  users = str("inv" + user)
  if users not in db:
    db[users] = {}
    # banknote
  if item == "banknote":
    if db[users]["banknote"] >= amount:
      if "bankspace" + user not in db:
        db["bankspace" + user] = 5000
      totalgain = 0
      for i in range(amount):
        gain = random.randint(4000, 6000)
        totalgain += gain
      link = await bot.fetch_user(int(user))
      db["bankspace" + user] += totalgain
      inventoryremove(user, "banknote", amount)
      embed = discord.Embed(
        title=f"{link}'s bank",
        description=f"You used {amount} banknotes and gained {totalgain}",
        color=discord.Color.random())
      return await ctx.reply(embed=embed)
  userused = str("used" + user)
  if userused not in db:
    db[userused] = {"": 10}
  inventory_items = db[users].keys()
  if item in item_list:
    if item in inventory_items:
      inventoryremove(user, item, 1)
      currenttime = time.time()
      epochtime = round(currenttime)
      dict = db[userused]
      dict[item] = epochtime
      embed = discord.Embed(
        title="**Use**",
        description=f"You used an {item}, it will last 30 minutes",
        color=discord.Color.green())
      await ctx.reply(embed=embed)
    else:
      embed = discord.Embed(title="**Use**",
                            description=f"You don't own any {item}s",
                            color=discord.Color.red())
      await ctx.reply(embed=embed)
  else:
    embed = discord.Embed(title="**Use**",
                          description="That item doesn't exist",
                          color=discord.Color.red())
    await ctx.reply(embed=embed)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1

