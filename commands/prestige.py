
@bot.command()
async def prestige(ctx, yes=None):
  if yes == None:
    yes = "no"
  userId = str(ctx.author.id)
  if "prestige" + userId in db:
    prestigeLvl = db["prestige" + userId]
  else:
    db["prestige" + userId] = 0
    prestigeLvl = 0
  moneyToPrestige = str(1000000 * prestigeLvl + 1000000)
  invToPrestige = str(1000000 * prestigeLvl + 2000000)
  lvlToPrestige = str(prestigeLvl * 15 + 25)
  if prestigeLvl == 3:
    await ctx.reply("You are max prestige level.n\n**Treat Worthy!**")
  if "yes" not in yes:
    embed = discord.Embed(
      title="**__Prestige__**",
      description=str("To Prestige you need the following:"),
      color=discord.Color.random())
    embed.add_field(name=f"**-{moneyToPrestige} Coins**",
                    value="",
                    inline=False)
    embed.add_field(name=f"**-Level {lvlToPrestige}**\n** **",
                    value="",
                    inline=False)
    embed.add_field(name=f"**-{invToPrestige} Inventory Value**\n** **",
                    value="",
                    inline=False)
    embed.add_field(name="__:warning:WARNING:warning:__",
                    value="",
                    inline=False)
    embed.add_field(
      name="__Prestiging will take away __EVERYTHING__ from you__.",
      value="",
      inline=False)
    embed.add_field(name="",
                    value="Except your pet and job levels and runes.\n** **",
                    inline=False)
    embed.add_field(name="**__Benefits__**", value="", inline=False)
    embed.add_field(name="",
                    value="-Have access to prestige locked features!",
                    inline=False)
    embed.add_field(name="",
                    value="-Gain a higher bank interest!",
                    inline=False)
    embed.add_field(name="",
                    value="-Start with a new starter pack!",
                    inline=False)
    embed.add_field(name="",
                    value="-Gain a prestige exclusive Prestige Lootbox!",
                    inline=False)
    embed.set_footer(text="!prestige yes to prestige")
    await ctx.reply(embed=embed)
  else:
    if int(db[userId]) >= int(moneyToPrestige) and int(
        db["userlvl" + userId]) >= int(lvlToPrestige) and int(
          db["invval" + userId]) >= int(invToPrestige):
      await ctx.reply(
        "Are you sure you want to prestige? (!yes)\n-You **__WILL__** be **__RESET__**\n-You will only keep your pet and job and runes."
      )

      def check(m):
        return str(m.author.id) == str(
          ctx.author.id) and m.channel == ctx.channel

      try:
        response = await bot.wait_for('message', check=check, timeout=10.0)
        if response.content.lower() not in (
            "!yes") and response.content.lower() not in (".yes"):
          return await ctx.reply(embed=cancelEmbed)
        else:
          prompt = await discordinput(ctx, check,
                                      "You can keep one item, what is it")
          if prompt not in db["inv" + userId]:
            return await ctx.reply("invaild item, redo")
          else:
            for i in dict(
                filter(lambda item: item[0].endswith(str(userId)),
                       db.items())).keys():
              if userId not in i:
                pass
              elif "job" in i or "cmds" in i or "work" in i or "pet" in i or "prestige" in i or "rune" in i or "shard" in i:
                pass
              elif str(userId) in str(i):
                del db[i]
            db["inv" + userId] = {
              "prestigebox": 1,
              "PS2": 1,
              "diamond_shovel": 1,
              "textbook": 1,
              "hunting_rifle": 1,
              "fishing_rod": 1,
              str(prompt): 1,
            }
            db[userId] = 1000
            db["prestige" + userId] += 1
            await ctx.reply(f"<@{ctx.author.id}> HAS PRESTIGED")
      except asyncio.TimeoutError:
        return await ctx.reply(
          embed=await embedify("Took too long, cancelling...", ""))
    else:
      await ctx.reply("You don't meet the requirements")
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1

