@bot.command(name="leaderboard", aliases=["lb"])
async def leaderboard(message):
  select = Select(min_values=1,
                  max_values=1,
                  placeholder="Choose a filter...",
                  options=[
                    discord.SelectOption(label="Coins",
                                         value="lb-",
                                         emoji="🪙",
                                         description="Balance Leaderboard"),
                    discord.SelectOption(label="Bank",
                                         value="bank",
                                         emoji="🏦",
                                         description="Bank Leaderboard"),
                    discord.SelectOption(label="Streak",
                                         value="streak",
                                         emoji="🗓️",
                                         description="Streak Leaderboard"),
                    discord.SelectOption(
                      label="Net Worth",
                      value="net",
                      emoji="💼",
                      description="Net Worth Leaderboard",
                    ),
                    discord.SelectOption(
                      label="Inventory",
                      value="invval",
                      emoji="🎒",
                      description="Inventory Leaderboard",
                    ),
                    discord.SelectOption(
                      label="Commands Ran",
                      value="cmdstotal",
                      emoji="👷‍♂️",
                      description="Commands Ran Leaderboard",
                    ),
                    discord.SelectOption(
                      label="Level",
                      value="userlvl",
                      emoji="🎚️",
                      description="Level Leaderboard",
                    ),
                    discord.SelectOption(
                      label="Subscribers",
                      value="subs",
                      emoji="<:youtube:1117402516645236828>",
                      description="Subscriber Count Leaderboard",
                    ),
                    discord.SelectOption(
                      label="Views",
                      value="views",
                      emoji="<:ytpurple:1117402508101435442>",
                      description="Youtube Views Leaderboard",
                    ),
                    discord.SelectOption(
                      label="Likes",
                      value="ytlikes",
                      emoji="<:ytgold:1117402513352695808>",
                      description="Youtube Likes Leaderboard",
                    ),
                  ])
  solvedict = {
    "subs": "Subscriber Count",
    "streak": "Streak",
    "bank": "Bank",
    "userlvl": "Level",
    "invval": "Inventory",
    "net": "Net Worth",
    "lb-": "Coins",
    "ytlikes": "Youtube Likes",
    "views": "Youtube Views",
    "cmdstotal": "Commands Ran",
  }

  valueType = {
    "subs": "Subscribers",
    "userlvl": "Level",
    "invval": "Coins",
    "net": "Coins",
    "lb-": "Coins",
    "streak": "Days",
    "bank": "Coins",
    "ytlikes": "Likes",
    "views": "Views",
    "cmdstotal": "Commands Ran",
  }

  async def my_callback(interaction):
    if interaction.user.id != message.author.id:
      return await interaction.response.send_message(
        content="This isn't your command!", ephemeral=True)

    type = select.values[0]
    peopleinserver = []
    for member in message.guild.members:
      peopleinserver.append(str(member.id))
    leaderboard = get_leaderboard(peopleinserver, type)
    output = ""
    for index, (user, coins) in enumerate(leaderboard):
      userss = "<@" + user + ">"
      output += f"{index + 1}.{userss} {add_commas(coins)} {valueType[select.values[0]]}\n"
    embed = discord.Embed(
      title=f"__{solvedict[str(select.values[0])]} Leaderboard__",
      description=output,
      color=discord.Color.random())
    await interaction.response.edit_message(embed=embed)

  select.callback = my_callback
  view = View()
  view.add_item(select)

  peopleinserver = []
  for member in message.guild.members:
    peopleinserver.append(str(member.id))
  leaderboard = get_leaderboard(peopleinserver, "lb-")
  output = ""
  for index, (user, coins) in enumerate(leaderboard):
    userss = "<@" + user + ">"
    output += f"{index + 1}.{userss} {add_commas(coins)}\n"
  embed = discord.Embed(title=f"__Coins Leaderboard__",
                        description=output,
                        color=discord.Color.random())
  await message.reply(embed=embed, view=view)
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1