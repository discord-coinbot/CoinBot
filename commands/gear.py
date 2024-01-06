# GEAR
@bot.command()
async def gear(ctx, type=None, person=None):
  if person == None or "equip" in type.lower() or "unequip" in type.lower():
    user = str(ctx.author.id)
  elif isinstance(person, discord.Member):
    user = str(person.id)
  else:
    user = str(ctx.author.id)
  check = db["gear"+user]["items"]
  try:
    check.append(1)
    dictistrue = False
    check.remove(1)
  except:
    dictistrue = True
  if "gear" + user not in db or dictistrue:
    await ctx.send("CHANGING (dw this is meant to be here)")
    db["gear" + user] = {"Attack": "Nothing Equipped", "Defence": "Nothing Equipped", "items":[]}
  if type.lower() == "items":
    embed = discord.Embed(title="**Gear Items**",
                          description="",
                          color=discord.Color.random())
    for a, b in gearitems.items():
      txt=""
      for i,v in b.items():
        if i!="description":
          txt+=f"{v} {i} "
        else:
          txt+=f"\n {v}"
      embed.add_field(name=a, value=txt,inline=False)
    await ctx.reply(embed=embed)
  elif type.lower() == "view" or type==None:
    embed = discord.Embed(title="**Gear View**",
                          description="Gear Equipped",
                          color=discord.Color.random())
    embed.add_field(name="Attack", value=str(db["gear" + user]["Attack"]))
    embed.add_field(name="Defence", value=str(db["gear" + user]["Defence"]))
    await ctx.reply(embed=embed)
  elif "unequip" in type.lower():
    await ctx.send("UNEUWIQPPF")
    print(0)
    if person.lower() == "attack":
      print(1)
      db["gear"+user]["Attack"] = "Nothing Equipped"
      print(2)
    elif person.lower() == "defence":
      db["gear"+user]["Defence"] = "Nothing Equipped"
  elif "equip" in type.lower():
    print("equip")
    if "defence" in type.lower():
      type = "Defence"
      gearlist = ["lock", "chains","uno_reverse","vault","guard_dog","alarm"]
    elif "attack" in type.lower():
      type = "Attack"
      gearlist = ["pocket", "bag", "lock_pick", "bolts","jet","uno_skip"]
    else:
      return await ctx.reply(embed=await embedify("That is not a valid type of gear. There is attack and defence.",""))
    print(1)
    if db["gear"+user][type] != "Nothing Equipped":
      return await ctx.reply(embed=await embedify("You still have something equipped. Unequip that to equip a new item",""))
    person = str(person.lower())
    print(2)
    if person not in gearlist:
      return await ctx.reply(embed=await embedify(f"Not a valid gear {type} item", ""))
    print(2.5)
    if person not in db["gear"+user]["items"]:
      return ctx.reply(embed=await embedify(f"You don't have (a) {person}",""))
    print(3)
    db["gear" + user][type] = person
    print(4)
    await ctx.reply(embed=await embedify(f"Equipped a {person}", ""))
  elif "buy" in type.lower():
    if person.lower() in gearitems.keys():
      txt=f"Are you sure you want to buy a {person.title()} for:**"
      for i,v in gearitems[person.lower()].items():
        if i!="description":
          if i=="Coins":
            if db[str(ctx.author.id)]<v:
              return await ctx.send("Insufficient Balance")
              txt+=f"\n{v} {i}"
          else:
            if i not in db["inv"+str(ctx.author.id)]:
              return await ctx.send("You do not have all the required items.")
            else:
              if db["inv"+str(ctx.author.id)][i]<v:
                return await ctx.send("You do not have all the required items.")
            txt+=f"\n{v} {i}"
      txt+="**\n(!yes)"
      await ctx.reply(txt)
      def check(m):
        return m.author.id == ctx.author.id
      prompt=await discordinput(ctx, check)
      if prompt=="!yes" or prompt==".yes":
        for i,v in gearitems[person.lower()].items():
          if i!="description":
            if i=="Coins":
              db[str(ctx.author.id)]-=v
            else:
              db["inv"+str(ctx.author.id)][i]-=v
        db["gear"+user]["items"].append(person.lower())
        await ctx.reply(f"You bought a {person.lower()}")
    else:
      await ctx.reply("Invalid Item!")
  elif type.lower() == "inv":
    embed = discord.Embed(title="Your gears",
                       description="",
                       color=discord.Color.random())
    for i in db["gear"+user]["items"]:
      embed.add_field(name=i,value="",inline=False)
    await ctx.reply(embed=embed)
