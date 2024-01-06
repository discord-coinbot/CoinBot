
@bot.command()
async def shop(ctx, pageSaid: int = None):
  if pageSaid == None:
    pageSaid = 1
  else:
    pageSaid = int(pageSaid)
  embed = discord.Embed(title="**Shop**",
                        description="",
                        color=discord.Color.green())
  new_lst = itememojis
  num_pages = int(math.ceil(len(itememojis) / 9))
  pages = {}
  for i in range(num_pages):
    pages[f"page{i+1}"] = []
  for i in range(len(new_lst)):
    daitem = list(new_lst.keys())[i]
    pages[f"page{(i // 9) + 1}"].append(
      f"**{new_lst[daitem]}{daitem} - ** {shop_items[daitem]}")
  numberpages = 0
  for page, contents in pages.items():
    numberpages += 1
  page = []
  for i in range(1, int(numberpages)):
    page.append("page" + str(i))
  if "page" + str(pageSaid) in pages:
    thelist = pages["page" + str(pageSaid)]
  else:
    embed = discord.Embed(title=f"__Shop__",
                          description=f"Page {pageSaid} does not exist!",
                          color=discord.Color.red())
    await ctx.reply(embed=embed)
  txt = ""
  for i in thelist:
    txt = txt + f"\n{i}"
  embed.add_field(name="", value=txt, inline=False)
  embed.set_footer(text=f"{pageSaid}/{numberpages}")
  await ctx.reply(embed=embed,
                  view=PaginationView(ctx.author.id, "Shop", pageSaid, pages))
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1
