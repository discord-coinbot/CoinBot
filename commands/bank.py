
# BANK
@bot.command()
async def bank(ctx, type=None, amount: str = None):
  if amount == None:
    amount = ""
  if type == None:
    type = "bal"
  userId = str(ctx.author.id)
  if "bankspace" + userId not in db:
    db["bankspace" + userId] = 5000
  db["bank" + userId] = round(db["bank" + userId])
  if "bank" + userId not in db:
    db["bank" + userId] = 0
  if "bankinterest" + userId not in db:
    db["bankinterest" + userId] = 0
  userBal = db[userId]
  userBankBal = db["bank" + userId]
  # withdraw
  if type == "withdraw":
    if int(userBankBal) >= int(amount):
      db["bank" + userId] -= int(amount)
      db[userId] += int(amount)
      await ctx.reply(f"Withdrawed {amount} coins.")
    else:
      await ctx.reply(f"You dont have {amount} coins in your bank.")
    # deposit
  if type == "deposit":
    if amount == "max":
      if db["bankspace" + userId] - db["bank" + userId] >= db[userId]:
        amount = db[userId]
      else:
        amount = db["bankspace" + userId] - db["bank" + userId]
    if int(userBal) >= int(amount):
      if db["bankspace" + userId] >= int(amount) + db["bank" + userId]:
        db[userId] -= int(amount)
        db["bank" + userId] += int(amount)
        await ctx.reply(f"Deposited {amount} coins.")
      else:
        await ctx.reply("You don't have enough bank space.")
    else:
      await ctx.reply(f"You dont have {amount} coins.")
    # view
  if type == "view" or type == "bal" or type == "wallet":
    link = await bot.fetch_user(userId)
    name = str(link).split("#")[0]
    embed = discord.Embed(title=f"",
                          description="",
                          color=discord.Color.random())
    embed.set_author(name=f"{name}'s Bank",
                     icon_url=ctx.author.display_avatar.url)
    embed.add_field(
      name="Bank:",
      value=f"{add_commas(str(userBankBal))} / {db['bankspace'+userId]}")
    await ctx.reply(embed=embed)
    # interest
  if type == "interest":
    userBankInterest = int(db["bankinterest" + userId])
    if int(userBankInterest) < int(round(time.time())):
      if "prestige" + userId not in db:
        db["prestige" + userId] = 0
      add = (userBankBal / 100) * (db["prestige" + userId] + 1)
      embed = discord.Embed(title="**__Bank Interest__**",
                            description="",
                            color=discord.Color.red())
      embed.add_field(name="Previous Balance",
                      value=add_commas(userBankBal),
                      inline=False)
      db["bank" + userId] += round(add)
      embed.add_field(name="New Balance",
                      value=add_commas(db["bank" + userId]),
                      inline=False)
      db["bankinterest" + userId] = round(time.time()) + 86400
      await ctx.reply(embed=embed)
    else:
      timeleft = (int(db["bankinterest" + userId])) - round(time.time())
      hours = timeleft // 3600
      timeleft = timeleft - (hours * 3600)
      minutes = timeleft // 60
      seconds = timeleft % 60
      msg = str(
        f"You can collect your bank interest in {hours} hours {minutes} minutes and {seconds} seconds."
      )
      embed = discord.Embed(title="**__Cooldown__**",
                            description="",
                            color=discord.Color.red())
      embed.add_field(name=msg, value="")
      await ctx.reply(embed=embed)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1

