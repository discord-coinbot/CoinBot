
class fightbuttons(View):

  def __init__(self, attacker, defender):
    super().__init__()
    self.value = None
    self.attacker = attacker
    self.defender = defender

  @discord.ui.button(label="Shadow Spike", style=discord.ButtonStyle.grey)
  #  if db["moveequipped"+attacker] == "Shadow Spike":
  async def shadow_spike(self, interaction: discord.Interaction,
                         button: discord.ui.Button):
    damage = 30 * db["fightmovelevel" + attacker]["Shadow Spike"]
    await interaction.response.send_message(
      f"You conjured a spike from the shadows and sent it {self.defender}'s way, which dealt {damage}."
    )


@bot.command()
async def fight(ctx, type, other=None):
  person = str(ctx.author.id)
  if "fight" == person:
    pass

  if "@<" in type:  # 1V1
    player = type.replace("<", "").replace("@", "").replace(">", "")
    for i in range(2):
      if "fightmovelevel" + person not in db:
        db["fightmovelevel" + str(ctx.author.id)] = {
          "Shadow Spike": 0,
          "Shadow Sword": 0,
          "Demon Charge": 0,
          "Side Step": 0,
          "Shadow Shield": 0,
          "Shadow Walk": 0,
          "Disarm": 0,
          "Shadow Hold": 0,
          "Darkness": 0,
          "Death Touch": 0,
          "Fire Stream": 0,
          "Choke": 0,
          "Wrath Of The Wind": 0,
          "Double Jump": 0,
          "Gust": 0,
          "Stone Henge": 0,
          "Water Splash": 0,
          "Vine Grip": 0,
          "Tsunami": 0,
          "Nature's Blessing": 0,
        }
      person = player
    view = fightbuttons(str(ctx.author.id), player)

  elif "unequip" in type:  # UNEQUIP
    if other == None:
      return await ctx.reply(
        "It's !fight equip [move] to equip a move and !fight unequip [move] to unequip a move"
      )
    if other in necromancer or other in adept:
      if "fightequipmove" + user in db and len(
          db["movesequipped" + user]) >= 1:
        db["fightequipmove" + user].remove(other)
      else:
        db["fightequipmove" + user] = []
        return ctx.send("You don't have any moves to unequip")
    else:
      return await ctx.reply("That is not a valid move")

  elif "equip" in type:  # EQUIP
    if other == None:
      return await ctx.reply(
        "It's !fight equip [move] to equip a move and !fight unequip [move] to unequip a move"
      )
    if other in necromancer or other in adept:
      if "fightequipmove" + user not in db:
        db["fightequipmove" + user] = []
      if len(db["fightequipmove" + user]) <= 4:
        db["fightequipmove" + user].append(other)
      else:
        return await ctx.reply("You have already equipped the max of 4 moves.")
    else:
      return await ctx.reply("That is not a valid move")

  elif "profile" in type:  #PROFILE
    embed = discord.Embed(title="**Fight**",
                          description="",
                          color=discord.Color.random())
    link = await bot.fetch_user(member.id)
    link = str(link).split("#")[0]
    embed = discord.Embed(title=f"",
                          description="",
                          color=discord.Color.random())
    embed.set_author(name=f"{link}", icon_url=member.display_avatar.url)
    user = str(member.id)
    embed.set_thumbnail(url=member.display_avatar.url)
    lvl = str(db['fightlvl' + user])
    xp = db['fightxp' + user]
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1