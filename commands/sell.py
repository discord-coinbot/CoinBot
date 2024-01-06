
# SELL
@bot.command()
async def sell(ctx, item, times=None):
  if times == None:
    times = "1"
  user = str(ctx.author.id)
  users = "inv" + user
  if users not in db:
    db[users] = {}
  amountHave = 0
  inventory_items = db[users]

  if times == "all":
    times = inventory_items[item]
  if item in inventory_items or item == "all":
    if item in shop_items.keys():
      times = int(times)
      price = round(int((times) * 75 * (shop_items[item] / 100)))
    elif item in sellable.keys():
      times = int(times)
      price = round(int((times) * sellable[item]))
    elif item == "all":
      if times == "ores":
        coal = 0
        iron = 0
        gold = 0
        for i in inventory_items:
          if "ore" in i:
            if "coal" in i:
              coal += 1
            elif "iron" in i:
              iron += 1
            elif "gold" in i:
              gold += 1
        price = int(coal * 500 + iron * 1000 + gold * 2500)
        if price == 0:
          embed = discord.Embed(title="**Sell**",
                                description="You don't have any ores",
                                color=discord.Color.red())
          await ctx.reply(embed=embed)
          return None
      elif times == "animals":
        pass  # DO LATER
      elif times == "1":
        embed = discord.Embed(title="**__Sell All__**",
                              description="",
                              color=discord.Color.green())
        lists = []
        no = ["diamond", "saphire", "whale", "mammoth"]
        for i in inventory_items:
          if i in sellallitems and i not in no:
            if inventory_items[i] > 0:
              lists = list(lists) + list([i] * inventory_items[i])
        counts = {}
        for element in lists:
          if element in counts:
            counts[element] += 1
          else:
            counts[element] = 1
        txt = ""
        for element, count in counts.items():
          txt = f"{txt}\n{allitememojis[element]} {element} (x{count})"
        embed.add_field(name="", value=txt, inline=False)
        val = 0
        for i in lists:
          val += sellallitems[i]
        taxLottery=round(val/6)
        embed.set_footer(text=f"Worth {val}. (!yes)")
        await ctx.reply(embed=embed)

        def check(m):
          return m.author == ctx.author and m.channel == ctx.channel

        try:
          response = await bot.wait_for('message', check=check, timeout=10.0)
          if response.content.lower() not in (
              "!yes") and response.content.lower() not in (".yes"):
            return await ctx.reply(embed=cancelEmbed)
          else:
            my_dict = {}
            for item in lists:
              if item in my_dict:
                my_dict[item] += 1
              else:
                my_dict[item] = 1
            for i, v in my_dict.items():
              inventory_items[i] -= v
            db[user] += val
            db["theLottery"]["Jackpot"]+=taxLottery
            embed = discord.Embed(title="**__Sale__**",
                                  description=f"<@{user}> sold all for {val}.",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)
        except asyncio.TimeoutError:
          return await ctx.reply(
            embed=await embedify("Took too long, cancelling...", ""))
    else:
      times = int(times)
      price = 0
    for i in db[users].keys():
      if i == item:
        amountHave = db[users][i]
    items = item
    if times == "ores" or amountHave >= times:
      if item == "all":
        items = "all"
        item == "all coal_ore, iron_ore and gold_ore"
      embed = discord.Embed(
        title="**Sell**",
        description=
        f"{ctx.author.mention}, do you want to sell {times} {allitememojis[items]} {items} for {price} coins? Type !yes to confirm or !no to cancel.",
        color=discord.Color.green())
      await ctx.reply(embed=embed)

      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

      try:
        response = await bot.wait_for('message', check=check, timeout=10.0)
        if response.content.lower() not in (
            "!yes") and response.content.lower() not in (".yes"):
          return await ctx.reply(embed=cancelEmbed)
      #if they say yes...
        else:
          user = str(ctx.author.id)
          if items == "all" and times == "ores":
            ores = ["coal_ore", "iron_ore", "gold_ore"]
            for i in ores:
              if "coal" in i:
                repeat = coal
              if "iron" in i:
                repeat = iron
              if "gold" in i:
                repeat = gold
              for ii in range(0, repeat):
                inventory_items.remove(i)
          else:
            inventory_items[items] -= times
          if user not in db:
            db[user] = 0
          db[user] += price
          db["theLottery"]["Jackpot"]+=round(price/6)
          embed = discord.Embed(
            title="**Sell**",
            description=
            f"{ctx.author.mention} has sold {times} {allitememojis[items]} {items}(s).",
            color=discord.Color.green())
          await ctx.reply(embed=embed)
      except asyncio.TimeoutError:
        return await ctx.reply(
          embed=await embedify("Took too long, cancelling...", ""))

    else:
      embed = discord.Embed(
        title="**Sell**",
        description=
        f"You don't have {allitememojis[items]} {times} {items}(s). You have {allitememojis[items]} {amountHave} {items}(s).",
        color=discord.Color.red())
      await ctx.reply(embed=embed)
  else:
    await ctx.reply("You don't own that item")
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1
