
# BUY
@bot.command()
async def buy(ctx, item, times=None):
  if times == None:
    times = "1"
  user = str(ctx.author.id)
  users = str("inv" + user)
  if users not in db:
    db[users] = {}
  inventory_items = db[users]
  if "ps" in item:
    item = item.replace("ps", "PS")
  if item in shop_items:
    times = int(times)
    price = int(times) * int(shop_items[item])
    user = str(ctx.author.id)
    if price < db[user] or price == db[user]:
      embed = discord.Embed(
        title="**Buy**",
        description=
        f"{ctx.author.mention}, do you want to buy {allitememojis[item]} {times} {item}(s) for {price} coins? Type !yes to confirm.",
        color=discord.Color.random())
      await ctx.reply(embed=embed)

      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

      try:
        response = await bot.wait_for('message', check=check, timeout=10.0)
        if response.content.lower() not in (
            "!yes") and response.content.lower() not in (".yes"):
          return await ctx.reply(embed=cancelEmbed)
        else:
          user = str(ctx.author.id)
          #inventory_items.extend(list(times*[item]))
          inventoryadd(user, item, int(times))
          #new_items=list(times*[item])+list(inventory_items)
          # for i in range(0, times):
          #   inventory_items.append(item)
          if user not in db:
            db[user] = 0
          db[user] -= price
          embed = discord.Embed(
            title="**Buy**",
            description=
            f"{ctx.author.mention} has bought {allitememojis[item]} {times} {item}",
            color=discord.Color.green())
          return await ctx.reply(embed=embed)
      except asyncio.TimeoutError:
        return await ctx.reply(
          embed=await embedify("Took too long, cancelling...", ""))
    else:
      embed = discord.Embed(
        title="**Buy**",
        description=f"Not enough coins for a {allitememojis[item]} {item}",
        color=discord.Color.red())
      await ctx.reply(embed=embed)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1
