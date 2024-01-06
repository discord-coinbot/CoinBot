

@bot.command()
async def clan(ctx, type, word=None, word2=None):
  if "allclans" not in db:
    db["allclans"] = []
  user = str(ctx.author.id)
  for i in db["allclans"]:
    if user in db[i]["Members"]:
      clan = i
    else:
      no += 1
  if type.lower() == "create":
    if word == None:
      return await ctx.reply(embed=await embedify(
        "You need to do !clan create [name]. The name can not contain numbers.",
        ""))
    numcheck = False
    for i in word:
      if i.isnumeric():
        numcheck == True
        return await ctx.reply(embed=await embedify(
          "You need to do !clan create [name]. The name can not contain numbers.",
          ""))

    def check(m):
      return str(ctx.author.id) == user

    checking = await discordinput(
      ctx, check,
      f"**Are you sure you want to create a clan called __{word}__? This will cost you 50,000 coins.**"
    )
    db["clan" + word] = {
      "Members": [user],
      "Treasury": {
        "Coins": 0,
        "Items": []
      },
      "Army": [0, "Fist", "Normal Clothes"],
      "Buildings": {
        "Research Tower": 0
      }
    }
    db["allclans"].append("clan" + word)
    await ctx.reply(embed=await embedify(f"Created the clan {word}", ""))
  elif type.lower() == "join":
    if "clan" + word not in db:
      return await ctx.reply(
        embed=await embedify("Pick an existing clan to join", ""))
    if user in db["clan" + word]["Members"]:
      return await ctx.reply(
        embed=await embedify("You are already in that clan"))
    for i in db["allclans"]:
      if user in i["Members"]:
        return await ctx.reply(
          "You already in a clan. Leave that clan to join this one. Do !clan leave [clan] to leave"
        )
    owner = db["clan" + user]["Members"][0]

    def check(m):
      return str(ctx.author.id) == user

    checking = await discordinput(
      ctx, check, f"**Are you sure you want to join the clan {word}**")

    def check(m):
      return str(ctx.author.id) == owner

    checking = await discordinput(
      ctx, check,
      f"**<@{owner}>, do you want to let <@{user}> join your clan?**")
    db["clan" + user]["Members"].append(user)
    await ctx.reply(f"<@{user}> has joined the clan.")
  elif type.lower() == "leave":
    pass
  elif type.lower() == "upgrade":
    word = word.lower()
    if word not in weapons.keys() and word not in armour.keys(
    ) and word != "research_tower":
      return await ctx.reply(
        embed=await embedify("That is not an upgradable item", ""))
    if word == "research_tower":
      no = 0
      print(1)
      print(2)
      if no == len(db["allclans"]):
        return await ctx.reply(
          embed=await embedify("You are not in a clan yet.", ""))
      lvl = (db[clan]["Buildings"]["Research Tower"]) + 1
      print(3)
      coinsneeded = lvl * 500000
      if lvl >= 3:
        coinsneeded = (lvl - 2) * 2500000
      if lvl == 1:
        itemslist = research[1][1:]
      print(4)
      for i in range(1, len(itemslist)):
        if i % 2 != 0:
          continue
        item = itemslist[i]
        if item in db["inv" + user]:
          if db["inv" + user][item] >= itemslist[i + 1]:
            notenough = False
          else:
            notenough = True
            break
        else:
          notenough = True
          break
      print(5)
      if db[clan]["Treasury"]["Coins"] < coinsneeded:
        less = "coins"
      elif notenough:
        less = "items"
      else:
        less = None
      if less != None:
        return await ctx.reply(embed=await embedify(
          f"You don't have enough {less} to upgrade you research tower", ""))
      print(6)

      def check(m):
        return str(ctx.author.id) == user

      newlist = itemslist[1].append(itemslist[0]).append(itemslist[3]).append(
        itemslist[2]).append(itemslist[5]).append(itemslist[4])
      await ctx.reply(embed=await embedify(
        f"Are you sure you want to upgrade your Research Tower to level {lvl}? This will cost {coinsneeded} coins and {newlistlist}",
        ""))
      for i in itemslist:
        if i % 2 != 0:
          continue
        item = itemslist[i]
        db["inv" + user][i] -= itemslist[i + 1]
      print(7)
      db[clan]["Buildings"]["Research Tower"] += 1
      await ctx.reply(embed=await embedify(
        f"You have upgraded your research tower to level {lvl}", ""))
  elif type.lower() == "research":
    pass
  elif type.lower() == "donate":
    if word.isdigit():
      word = int(word)
      if db[user] >= word:
        db[user] -= word
        db[clan]["Treasury"]["Coins"] += word
        await ctx.reply(
          embed=await embedify(f"You donated {word} coins to the clan", ""))
      else:
        await ctx.reply(embed=await embedify(f"You don't have {word} coins"))

