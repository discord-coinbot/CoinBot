
@bot.command()
async def about(message):
  desc = "Created by **Razi** and **Thajan**. Suvheet, as our biggest user, gives us ideas and Aadish offered to reduce lag."
  name = "About"
  embed = discord.Embed(title=name,
                        description=desc,
                        color=discord.Color.random())
  await message.reply(embed=embed)
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1
