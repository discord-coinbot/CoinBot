@bot.command(name="balance", aliases=["bal"])
async def balance(message, member: discord.Member = None):
  if member == None:
    member = message.author
  person = str(member.id)
  link = await bot.fetch_user(person)
  db_check(person)
  db_check("lb-" + person)
  if "inv" + person not in db:
    db["inv" + person] = {}
  coins = str(db[person])
  embed = discord.Embed(title="", description="", color=discord.Color.random())
  name = str(link).split("#")[0]
  embed.set_author(name=f"{name}'s Balance",
                   icon_url=member.display_avatar.url)
  embed.add_field(name="Coins", value=add_commas(coins), inline=True)

  invval = "invval" + person
  bank = "bank" + person
  net = "net" + person
  if bank in db:
    embed.add_field(name="Bank", value=add_commas(str(db[bank])), inline=True)
  embed.add_field(name="", value="", inline=False)
  if invval in db:
    embed.add_field(name="Inventory Value",
                    value=add_commas(str(db[invval])),
                    inline=True)
  db_check(bank)
  if net in db:
    embed.add_field(name="Net Worth",
                    value=add_commas(str(db[net])),
                    inline=True)
  await message.reply(embed=embed)
  db[person] = round(db[person])
  db[net] = db[invval] + db[bank] + int(coins)
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1