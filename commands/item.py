
# !ITEM DESCRIPTIONS
@bot.command()
async def item(ctx, name: str):
  if name.lower() in itemsdesc:
    desc = itemsdesc[name.lower()]
    if name.lower() in shop_items:
      price = shop_items[name.lower()]
    elif name.lower() in sellable:
      price = sellable[name.lower()]
    name = "__" + name.replace("_", " ").title() + "__"
    embed = discord.Embed(title=name,
                          description=desc,
                          color=discord.Color.random())
    embed.add_field(name="", value=f"**Price:** {price}")
    await ctx.reply(embed=embed)

  elif "list" in name.lower():
    embed = discord.Embed(title="**__Items__**", color=discord.Color.random())
    txts1 = ""
    txts2 = ""
    txts3 = ""
    for item, desc in itemsdesc.items():
      if item in shop_items:
        price = shop_items[item]
      elif item in sellable:
        price = sellable[item]
      item = item.replace("_", " ").title()
      txt = f"__**{item}**__\n{desc}\n**Price:** {price}"
      if len(txts1) + len(txt) > 1024:
        if len(txts2) + len(txt) > 1024:
          txts3 += txt + "\n"
        else:
          txts2 += txt + "\n"
      else:
        txts1 += txt + "\n"
    embed.add_field(name="", value=txts1, inline=True)
    embed.add_field(name="", value=txts2, inline=True)
    embed.add_field(name="", value=txts3, inline=True)
    await ctx.reply(embed=embed)

  else:
    await ctx.reply(f"{name} is not a valid item")
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1

