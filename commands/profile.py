@bot.command(name="profile", aliases=["ich"])
async def profile(ctx, member: discord.Member = None):
  txt = ""
  if member == None:
    member = ctx.author
  link = await bot.fetch_user(member.id)
  link = str(link).split("#")[0]
  embed = discord.Embed(title=f"",
                        description="",
                        color=discord.Color.random())
  embed.set_author(name=f"{link}", icon_url=member.display_avatar.url)
  user = str(member.id)
  embed.set_thumbnail(url=member.display_avatar.url)
  lvl = str(db['userlvl' + user])
  xp = db['userlvlxp' + user]

  embed.add_field(
    name="Level",
    value=
    f"Level: {lvl}\nExperience: {xp}/{int(lvl)*150}\n{get_bar(xp,int(lvl)*150)}",
    inline=True)
  if "bpinfo"+user in db:
    embed.add_field(name="",value=f"**Battlepass Level**: {db['bpinfo'+user]['lvl']}")
    embed.add_field(name="",value=f"",inline=False)
  if "prestige" + user in db and db["prestige" + user] != 0:
    prestige = db["prestige" + user]
    txt = ""
    if prestige == 1:
      txt = "<:i_:1120409267208466433>"
    elif prestige == 2:
      txt = "<:ii:1120409264490557580>"
    elif prestige == 3:
      txt = "<:iii:1120409262993190912>"
    embed.add_field(name="",
                    value=f"{txt}** Prestige:** {db['prestige'+user]}",
                    inline=True)
  embed.add_field(name="", value="", inline=False)
  if user in db:
    bal = db[user]
    embed.add_field(name="__Balance__",
                    value=add_commas(str(bal)),
                    inline=True)
  bank = 0
  if "bank" + user in db:
    bank = db["bank" + user]
    embed.add_field(
      name="Bank",
      value=
      f"{add_commas(str(db['bank'+user]))}/{add_commas(str(db['bankspace'+user]))}",
      inline=True)
  embed.add_field(name="", value="", inline=False)
  if "invval" + user in db:
    invval = db["invval" + user]
    embed.add_field(name="__Inventory Worth__",
                    value=add_commas(str(invval)),
                    inline=True)
  net = int(bal) + int(bank) + int(invval)
  embed.add_field(name="__Net Worth__",
                  value=add_commas(str(net)),
                  inline=True)
  embed.add_field(name="", value="", inline=False)
  if "job" + user in db:
    val = db["job" + user]
    if val != "":
      vals = val.replace("_", " ")
      val = vals.title()
      embed.add_field(name="__Job__", value=f"Works as a {val}", inline=True)
  if "pets" + user in db:
    val = db["pets" + user]
    if val != "" and val != "disowned":
      embed.add_field(name="__Pet__", value=f"Has a {val}", inline=True)
  embed.add_field(name="", value="", inline=False)
  if "subs" + user in db:
    val = db["subs" + user]
    inv = list(db["inv" + user].keys())
    emoji = "<:youtube:1117402516645236828>"
    if "ruby_play_button" in inv:
      emoji = "<:ytred:1117404642205237402>"
    elif "diamond_play_button" in inv:
      emoji = "<:ytdiamond:1117404643929116672> "
    elif "gold_play_button" in inv:
      emoji = "<:ytgold:1117402513352695808> "
    elif "silver_play_button" in inv:
      emoji = "<:ytsilver:1117404640028397618> "
    elif "green_play_button" in inv:
      emoji = "<:ytgreen:1117402510194389075> "
    embed.add_field(name=f"__{emoji} Youtube__",
                    value=f"Subscribers: {val}",
                    inline=True)
  if "cmds" + user in db:
    num = 0
    db["cmds" + str(ctx.author.id)] = dict(
      sorted(db["cmds" + str(ctx.author.id)].items(),
             key=lambda x: x[1],
             reverse=True))
    for i in db['cmds' + user].values():
      num += i
    db['cmdstotal' + user] = num
    most_used = list(db["cmds" + str(ctx.author.id)].keys())[0]
    embed.add_field(name=f"__Commands Ran__",
                    value=f"{num}\nMost Used: {most_used}",
                    inline=True)
  await ctx.reply(embed=embed)
  db["net" + user] = str(net)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1