
async def send_message(message, user_message, is_private):
  try:
    user = str(message.author.id)
    response = responses.get_response(user_message)
    if response != "not in code":
      if db["responses" + user] == "on" and "1103357482023268514" not in str(
          message.channel.id):
        await message.reply(response)
        return "sent"
  except Exception as e:
    print(e)


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.channel.id == 1120413286786142258:
    msg = message.content
    channel = bot.get_channel(1017156210329407518)
    await channel.send(msg)
  if message.author.id == "GET NIKHIL ID":
    await ctx.reply("poo")
  if str(
      message.author.id) in db and "cmds" + str(message.author.id) not in db:
    db["cmds" + str(message.author.id)] = {}
  ewds = await bot.get_context(message)
  #if ewds.valid:
    # if message.author.id!=600411237561663498 and message.author.id!=469521741744701444 and message.author.id!=868472825252552735:
    #   embed=discord.Embed(title="**__Maintenance__**",
    #                      description="CoinBot is currently down to prepare for the upcoming update. \n\nETA: 10mins\n\nSee you soon!",
    #                      color=discord.Color.dark_grey())
    #   if str(message.content)[0]=="!" or str(message.content)[0]==".": 
    #     return await message.reply(embed=embed)
  if "1103357482023268514" in str(message.channel.id):
    if message.author.id == 1104712133670875228 or message.author.id == 469521741744701444 or message.author.id == 600411237561663498 or message.author.id == 1066483366007947385:
      if str(message.content).isnumeric() == True:
        num = int(message.content)
        await message.reply(f"{num+1}")
  await bot.process_commands(message)
  async with aiofiles.open("database.py", "w") as db_file:
    await db_file.write("db = " + repr(db))
  if "inv" + str(message.author.id) in db:
    for i, v in db["inv" + str(message.author.id)].items():
      if v == 0:
        del db["inv" + str(message.author.id)][i]
  if not isinstance(message.channel, discord.channel.DMChannel):
    if message.guild.name != "A.R.K":
      print(
        f'\033[32m{str(message.author)}\033[0m said: \033[34m"{str(message.content)}"\033[35m ({str(message.channel)})--({message.guild.name})\033[0m '
      )
  if "sendmsg" in str(message.content) or "i need 4k" in str(message.content):
    return
  user = str(message.author.id)
  userxp = "userlvlxp" + user
  userlvl = "userlvl" + user
  if userxp not in db and user in db:
    db[userxp] = 0
  if userlvl not in db and user in db:
    db[userlvl] = 1
  if "responses" + user not in db:
    db["responses" + user] = "off"
  if "469521741744701444" in user or "600411237561663498" in user:
    if "invest change" in str(message.content):
      event = change_invest()
      await message.channel.reply("Markets have been changed early")
  command = await bot.get_context(message)
  if str(message.content).replace("!", "").replace(
      ".", "") in xp_commands and command.valid:
    if "!" in message.content or "." in message.content:
      if "prestige" + user in db:
        num = 10 * db["prestige" + user]
      else:
        num = 0
      db[userxp] += int(random.randint(15, 25) + num)
      if db[userlvl] * 150 <= db[userxp]:
        db[userlvl] += 1
        db[userxp] = 0
        await message.reply(f"<@{user}> Leveled up to Level {db[userlvl]}")
#  if shush == False
  if db["responses" + user] == "on":
    p = ""
    user_message = str(message.content)
    loweredmsg = user_message.lower()
    if loweredmsg == "ok" and str(message.author.id) != "1089163941063704626":
      author_id = str(message.author.id)
      text = "Ok <@" + author_id + ">!"
      await message.reply(text)
    else:
      p = await send_message(message, user_message, is_private=False)
    if p == "sent":
      return
