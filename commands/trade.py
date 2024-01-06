@bot.command()
async def trade(ctx, person: discord.Member, one, two, three=None, four=None):
  my_user=str(ctx.author.id)
  my_amount=0
  my_item=None
  their_user=str(person.id)
  their_amount=0
  their_item=None
  if three==None:
    if one.isnumeric():
      my_amount=int(one)
      their_amount=1
      their_item=str(two)
    elif two.isnumeric():
      their_amount=int(two)
      my_amount=1
      my_item=str(one)
    else:
      my_amount=1
      my_item=one
      their_amount=1
      their_item=two
  elif four==None:
    if not two.isnumeric():
      my_item=two
      my_amount=int(one)
      their_amount=int(three)
    else:
      my_amount=int(one)
      their_amount=int(two)
      their_item=three
  else:
    my_amount=int(one)
    my_item=two
    their_amount=int(three)
    their_item=four
  txt=f"{my_item} {my_amount}\n{their_item} {their_amount}"
  def check(m):
    return str(m.author.id) == str(person.id) and m.channel == ctx.channel
  if my_item==None and their_item!=None:
    my_check=balcheck(my_user, my_amount)
    other_check=inventorycheck(their_user, their_amount, their_item)
    if my_check==True and other_check==True:
      embed=discord.Embed(title="Trade",description=f"""
Do you want to trade
{ allitememojis[their_item]} {their_amount}x {their_item}(s)
**FOR**
{my_amount} Coins

(!yes)""", color=discord.Color.green())
      await ctx.send(f"{person.mention}",embed=embed)
      prompt=await discordinput(ctx, check)
      if prompt not in ["!yes",".yes"]:
        return await ctx.send("Cancelling")
      db[my_user]-=my_amount
      db[their_user]+=my_amount
      inventoryadd(my_user, their_item, their_amount)
      inventoryremove(their_user, their_item, their_amount)
      await ctx.reply(embed=await embedify("Trade",f"{ctx.author.mention} traded {my_amount} Coins to {person.mention} for {allitememojis[their_item]} {their_amount}x {their_item}(s)"))
    elif my_check==True:
      await ctx.reply("The other person does no have the items/money.")
    elif other_check==True:
      await ctx.reply("You do not have the items/money.")
  elif their_item==None and my_item!=None:
    my_check=inventorycheck(my_user, my_amount, my_item)
    other_check=balcheck(their_user, their_amount)
    if my_check==True and other_check==True:
      embed=discord.Embed(title="Trade",description=f"""
Do you want to trade
{their_amount} Coins
**FOR**
{allitememojis[my_item]} {my_amount}x {my_item}(s)

(!yes)""", color=discord.Color.green())
      await ctx.send(f"{person.mention}",embed=embed)
      prompt=await discordinput(ctx, check)
      if prompt not in ["!yes",".yes"]:
        return await ctx.send("Cancelling")
      db[their_user]-=their_amount
      db[my_user]+=their_amount
      inventoryadd(their_user, my_item, my_amount)
      inventoryremove(my_user, my_item, my_amount)
      await ctx.reply(embed=await embedify("Trade",f"{ctx.author.mention} traded {allitememojis[my_item]} {my_amount}x {my_item}(s) to {person.mention} for {their_amount} Coins"))
    elif my_check==True:
      await ctx.reply("The other person does no have the items/money.")
    elif other_check==True:
      await ctx.reply("You do not have the items/money.")
  else:
    my_check=inventorycheck(my_user, my_amount, my_item)
    other_check=inventorycheck(their_user, their_amount, their_item)
    if my_check==True and other_check==True:
      embed=discord.Embed(title="Trade",description=f"""
Do you want to trade
{allitememojis[their_item]} {their_amount}x {their_item}(s)
**FOR**
{allitememojis[my_item]} {my_amount}x {my_item}(s)

(!yes)""", color=discord.Color.green())
      await ctx.send(f"{person.mention}",embed=embed)
      prompt=await discordinput(ctx, check)
      if prompt not in ["!yes",".yes"]:
        return await ctx.send("Cancelling")
      inventoryadd(their_user, my_item, my_amount)
      inventoryremove(my_user, my_item, my_amount)
      inventoryadd(my_user, their_item, their_amount)
      inventoryremove(their_user, their_item, their_amount)
      await ctx.reply(embed=await embedify("Trade",f"{ctx.author.mention} traded {allitememojis[my_item]} {my_amount}x {my_item}(s) to {person.mention} for {allitememojis[their_item]} {their_amount}x {their_item}(s)"))
    elif my_check==True:
      await ctx.reply("The other person does no have the items/money.")
    elif other_check==True:
      await ctx.reply("You do not have the items/money.")
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1


@trade.error
async def trade_error(ctx, error):
  embed=discord.Embed(title="**Error**",
                      description="Try use one of the following commands\n\n`!trade @user amount my_item amount their_item`\n`!trade @user money amount their_item`\n`!trade @user amount my_item money`")
  await ctx.reply(embed=embed)