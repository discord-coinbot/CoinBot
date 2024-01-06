
@bot.command()
async def transfer(ctx, recipients: discord.Member, amount,free=None):
  recipient = str(recipients.id) 
  sender = str(ctx.author.id)
  if sender not in db:
    db[sender] = 0
  sender_balance = str(db[sender])
  if "-" not in amount:
    if int(sender_balance) >= int(amount):
      if "." not in amount:
        if recipient not in db:
          db[recipient] = 0
        amount=int(amount)
        amountNew = round(int(amount)*0.9)
        if free != None:
          if sender in admin and free == "taxfree":
            amountNew = amount
        db[sender] -= amount
        db[recipient] += amountNew
        db["theLottery"]["Jackpot"]+=round(int(amount)*0.05)
        embed = discord.Embed(
          title="**__Transfer__**",
          description=f"<@{sender}> has given {amountNew} to {recipients.mention}",
          color=discord.Color.random())
        embed.set_footer(text=f"{round(amount*0.1)} tax")
        await ctx.reply(embed=embed)
      else:
        await ctx.reply(f"{sender} atleast send a whole number of coins")
    else:
      await ctx.reply(f"{sender} doesn't even have {amount}")
  else:
    await ctx.reply(
      f"<@{sender}> what are you trying to do? You can't send someone negative coins"
    )
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1