

# ADMIN COMMANDS
# GIVE
@bot.command()
async def give(ctx, person: discord.User, where, item, number: int = None):
  if number == None:
    number = 1
  person = str(person.id)
  user = str(ctx.author.id)
  if "469521741744701444" not in user and "600411237561663498" not in user:
    return await ctx.reply("Silly **goose**, you arent a mod.")
  if "inv" in where:
    usersinv = str("inv" + person)
    inv = db[usersinv]
    inventoryadd(person, item, number)
    await ctx.reply(f"Added {number} {item}(s) to <@{person}>'s inventory.")
  elif "rune" in where:
    usersrune = str("rune" + person)
    rune = db[usersrune]
    if number == 1:
      rune[item] = 1
    else:
      rune[item] += number
    await ctx.reply(f"added {person} {number} {item} to runes")
  else:
    await ctx.reply("not valid place")

