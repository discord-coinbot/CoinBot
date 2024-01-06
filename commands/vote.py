
async def on_dbl_vote(data):
  print(data)
  print("hu")
  channel = bot.get_channel(1096799510845468672)
  embed = discord.Embed(title="**__vote__**",
                        description="voted",
                        color=discord.Color.random())
  await channel.send(embed=embed)



class voteLinks(discord.ui.View):
  def __init__(self):
    super().__init__()
    topgglink = discord.ui.Button(label='top.gg',
                            style=discord.ButtonStyle.url,
                            url='https://top.gg/bot/1092019072704725012')
    self.add_item(topgglink)

@bot.command()
async def vote(ctx, claim=None):
  if claim==None:
    embed=discord.Embed(title="**Vote**", description="""**__Vote Rewards:__**
1 Vote Box
50,000 Coins
5 Banknotes""")
    await ctx.send(embed=embed,view=voteLinks())
  else:
    pass

