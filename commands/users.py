
@bot.command()
async def users(ctx):
  listed=[]
  newdict=dict(db).copy()
  for i, v in newdict.items():
    if i[0].isnumeric():
      listed+=[str(i)]
  txt=""
  for i in listed:
    txt+=f"<@{i}>\n"
  await ctx.send(txt)