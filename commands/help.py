
@bot.command()
async def help(ctx):
  embed = discord.Embed(
    title="**Help**",
    description="**type !help [command] for help on that command**",
    color=discord.Color.random())
  embed.add_field(name="Rock Paper Scissors(!rps [choice])",
                  value="Play Rock Paper Scissors against a bot!",
                  inline=False)
  embed.add_field(name="Guess The Number(!gtn [choice])",
                  value="Play Guess the Number against a bot!",
                  inline=False)
  embed.add_field(name="Dice Roll (!diceroll)",
                  value="Roll A Die!",
                  inline=False)
  embed.add_field(name="Find function (!find)",
                  value="Search around for some coins! Cooldown is 10 secs",
                  inline=False)
  embed.add_field(
    name="Dig function (!dig)",
    value=
    "Dig for some coins! The better shovel you have, the more coins you can get.",
    inline=False)
  embed.add_field(
    name="Game function (!game)",
    value=
    "Game for some coins! The better console you have, the more coins you can get.",
    inline=False)
  embed.add_field(
    name="Mine function (!mine)",
    value=
    "Mine for some ores with a pickaxe or for more ores an excavator (buy one in the shop) After your done, sell them from your inventory or keep the very rare ones...",
    inline=False)
  embed.add_field(
    name="Study function (!study)",
    value=
    "Study and the better grade you get the more coins you get! Textbooks and flashcards always help! (you get more coins if you buy them)",
    inline=False)
  embed.add_field(name="Beg function (!beg)",
                  value="Beg people for some coins! Cooldown is 10 secs.",
                  inline=False)
  embed.add_field(name="Balance function (!bal/!balance [user])",
                  value="Look at your Balance!",
                  inline=False)
  embed.add_field(name="Shop function (!shop)",
                  value="Look at the shop!",
                  inline=False)
  embed.add_field(name="Buy function (!buy [item] [amount])",
                  value="Buy from the shop!",
                  inline=False)
  embed.add_field(name="Sell function (!sell)",
                  value="Sell to the shop!",
                  inline=False)
  embed.add_field(name="Inventory function (!inventory/inv [user])",
                  value="Look at your or someone else's inventory!",
                  inline=False)
  embed.add_field(name="Leaderboard function (!leaderboard/lb)",
                  value="Look at the server coins leaderboard!",
                  inline=False)
  embed.add_field(name="Rob function (!rob [user])",
                  value="Rob People!",
                  inline=False)
  embed.add_field(name="Slots function (!slots [amount])",
                  value="Gamble your money with slots!",
                  inline=False)
  embed.add_field(
    name=
    "Invest function (!invest !invest view !invest [buy/sell] [item] [amount])",
    value="Invest your money!",
    inline=False)

  embed.add_field(name="Hunt function (!hunt)",
                  value="Buy a hunting_rifle in the shop and go hunting!",
                  inline=False)

  embed.add_field(name="Fish function (!fish)",
                  value="Buy a fishing_rod in the shop and go fishing!",
                  inline=False)

  embed.add_field(
    name="Pet list (!pet list)",
    value="Look at what pets you can adopt and how much they cost",
    inline=False)

  embed.add_field(
    name=
    "Pet adopting and disowning (!pet adopt [pet] to adopt and !pet disown [pet] to disown)",
    value=
    "Adopt a pet and it will give u up to 2% of what it costs every single day when you pet it (!pet pet [pet])",
    inline=False)

  embed.add_field(name="Pet feed (!pet feed [animal])",
                  value="Feed your pet, or it will run away!",
                  inline=False)

  embed.add_field(name="Pet feed list (!pet feed list)",
                  value="Find out how much food each pet needs",
                  inline=False)

  embed.add_field(
    name="Pet feed list (!pet feedable list)",
    value="Find out how much food each animal you feed your pet gives!",
    inline=False)

  embed.add_field(
    name="Pet profile (!pet profile)",
    value=
    "Look at your pet's profile, which shows how hungry your pet is and when it can next be petted",
    inline=False)
  embed.set_footer(text="Created by Razi and Thajan")
  await ctx.reply(embed=embed)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1
