@bot.command()
async def roundinv(ctx,person:discord.Member=None):
  if person == None:
    user = str(ctx.author.id)
  else:
    user = str(person.id)
  new = {}
  for i,k in db["inv"+user].items():
    new[i] = int(k)
  db["inv"+user] = new
  await ctx.reply(embed=await embedify("Done.",""))