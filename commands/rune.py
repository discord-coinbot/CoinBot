@bot.command(name="rune", aliases=["runes"])
async def rune(ctx, task, item=None, thing=None, type=None, amount=None):
  user = str(ctx.author.id)
  if item != None:
    if "@<" in item:
      user = item.replace("<", "").replace("@", "").replace(">", "")
  if "shard" + user not in db:
    db["shard" + user] = {
      "digshards": 0,
      "gameshards": 0,
      "mineshards": 0,
      "studyshards": 0,
      "searchshards": 0,
      "unbreakingshards": 0,
      # "luckshards": 0, CHANGE AT COLLECTABLES UPDATE
    }
  if "rune" + user not in db:
    db["rune" + user] = {
      "dig": 0,
      "game": 0,
      "mine": 0,
      "study": 0,
      "search": 0,
      "unbreaking": 0,
      # "luck": 0, # CHANGE AT COLLECTABLES UPDATE
    }
  if "game" not in db["rune" + user]:
    db["rune" + user]["game"] = 0
  if "gameshards" not in db["shard" + user]:
    db["shard" + user]["gameshards"] = 0
  if 'runeequip' + user not in db:
    db['runeequip' + user] = "No Rune Equipped"
  rune_items = db["shard" + user]
  rune_lvls = db["rune" + user]
  link = await bot.fetch_user(user)
  if item == None and task != "view":
    await ctx.reply(
      "You need to use the format !rune upgrade/equip [rune] or !rune view")
  if task == "view":
    embed = discord.Embed(title=f"{link}'s runes and shards",
                          description="All your runes and shards",
                          color=discord.Color.random())
    embed.add_field(name="Your equipped rune", value=f"{db['runeequip'+user]}")
    for type, amount in rune_items.items():
      s = type.replace("shards", "")
      t = s.title()
      lvl = rune_lvls[s]
      amount_required = 25 * (2**(lvl + 2))
      amount_needed = amount_required - amount
      if amount_needed > 0:
        txt = f"You have {amount} shards.\nYou need {amount_needed} more shards to level up."
      else:
        txt = f"You have {amount} shards.\n__You can upgrade this rune right now!__"
      embed.add_field(name=f"** **\n{t} Rune {lvl}", value=txt, inline=False)
  elif task == "upgrade":
    userlvl = db["userlvl" + user]
    lvlsneeded = (db["rune" + user][item] + 1) * 5
    if db["shard" + user][item + "shards"] <= lvlsneeded * 20:
      return await ctx.reply("You do not have enough shards for that")

    def check(m):
      return str(ctx.author.id) == user

    checking = await discordinput(
      ctx, check,
      f"This will cost {lvlsneeded} levels. !yes to upgrade your {item} rune.",
      10.0)
    if checking != "!yes":
      return await ctx.reply("Cancelling...")
    db["userlvl" + user] -= lvlsneeded
    lvl = rune_lvls[item]
    amount_required = 25 * (2**(lvl + 2))
    db["rune" + user][item] = lvl + 1
    db["shard" +
       user][item + "shards"] = rune_items[item + "shards"] - amount_required
    embed = discord.Embed(
      title="**Upgrade**",
      description=f"Successfully upgraded {item} rune to level {lvl+1}",
      color=discord.Color.random())
    return await ctx.reply(embed=embed)
  elif task == "equip":
    if "rob" not in item:
      for rune, level in rune_lvls.items():
        if rune in item:
          runes = rune + " " + str(level)
          db["runeequip" + user] = runes
          break
    else:
      inventory_items = db["inv" + user]
      if "rob" in inventory_items:
        inventoryremove(user, "rob", 1)
        db["runeequip" + user] = "rob"

    embed = discord.Embed(title=f"{link}'s equiped rune'",
                          description=runes,
                          color=discord.Color.random())
  elif task == "unequip":
    db["runeequip" + user] = "No Rune Equipped"
    await ctx.reply("Unequipped the rune.")
  elif task == "set":
    if ctx.author.id == 469521741744701444 or user == "600411237561663498":
      person = item.replace("@", "").replace("<", "").replace(">", "")
      if type in db[thing + person].keys():
        db[thing + person][type] = int(amount)
      await ctx.reply("Done.")
    else:
      await ctx.reply("Not Admin")
  else:
    embed = discord.Embed(title="**Runes**",
                          description="That isn't a valid task",
                          color=discord.Color.random())
  await ctx.reply(embed=embed)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1