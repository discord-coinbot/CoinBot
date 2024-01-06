
thesettings = ["responses"]


# SETTINGS
@bot.command()
async def settings(ctx, type: str = None, switch: str = None):
  user = str(ctx.author.id)
  if type == None:
    embed = discord.Embed(title="**__Settings__**",
                          description="Here are the settings options",
                          color=discord.Color.dark_grey())
    for i in thesettings:
      if i + user not in db:
        db[i + user] = "on"
      if db[i + user] == "on":
        emoji = ":white_check_mark:"
      else:
        emoji = ":negative_squared_cross_mark:"
      embed.add_field(
        name=f"Responses{emoji}",
        value="Turn this off if you dont want the bot to respond to you.",
        inline=False)
      if user == "469521741744701444":
        embed.add_field(name="Sendmsg", value=db["sendmsg"], inline=False)
    await ctx.reply(embed=embed)
  else:
    type = type.lower()
    if type in thesettings:
      # if switch==None:
      #   if db[type+user]=="on":
      #     db[type+user]=="off"
      #   else:
      #     db[type+user]=="on"
      if "on" in switch:
        db[type + user] = "on"
        text = "😀"
      elif "off" in switch:
        db[type + user] = "off"
        text = "😭"
      await ctx.reply(f"Set {type} to {db[type+user]} {text}")
    else:
      await ctx.reply("Not a Vaild Setting")
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1
