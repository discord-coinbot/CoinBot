class invSort(Select):
  def __init__(self, user):
    self.user=user
    # Set the options that will be presented inside the dropdown
    options = [
      discord.SelectOption(label='All', description='All Items', emoji='🌈'),

      discord.SelectOption(label='Collectables',
                           description='Show Collectables Only',
                           emoji='🏅'),
      discord.SelectOption(label='Tools',
                           description='Show Tools Only',
                           emoji='🛠️'),
      discord.SelectOption(label='Craft Ingredients',
                           description='Show Craft Ingredients Only',
                           emoji='🛠️'),
      discord.SelectOption(label='Sellables',
                           description='Show Sellables Only',
                           emoji='💵'),
      discord.SelectOption(label='Lootboxes',
                           description='Show Lootboxes Only',
emoji='<:commonbox:1124999919988650076>'),
      discord.SelectOption(label='Potions',
                           description='Show Potions Only',
                           emoji='🧪'),
    ]
    super().__init__(placeholder='Choose filter...',
                     min_values=1,
                     max_values=1,
                     options=options)

  async def callback(self, interaction: discord.Interaction):
    userId = str(self.user)
    link = await bot.fetch_user(int(userId))
    embed = discord.Embed(title=f"",
                          description="",
                          color=discord.Color.green())
    embed.set_author(name=f"{str(link).split('#')[0]}'s Inventory",
                     icon_url=interaction.user.display_avatar.url)
    pageSaid = 1
    dictSort = {
      "Sellables": sellable.keys(),
      "Collectables": allcollectables,
      "Lootboxes": lootboxes.keys(),
      "Potions": potions,
      "Craft Ingredients": list(getitems.keys())+otherCraftItems,
      "Tools":tools,
    }
    new_lst1 = dict(db["inv" + userId])
    if str(self.values[0]) != "All":
      new_lst = {}
      for i, v in new_lst1.items():
        if i in dictSort[str(self.values[0])]:
          new_lst[i] = v
    else:
      new_lst = new_lst1
    num_pages = int(math.ceil(len(new_lst) / 12))
    pages = {}
    value = 0
    for i in range(num_pages):
      pages[f"page{i+1}"] = []
    for i in range(len(new_lst)):
      daitem = list(new_lst.keys())[i]
      if new_lst[daitem] > 0:
        if daitem in allitememojis:
          pages[f"page{(i // 12) + 1}"].append(
            f"**{allitememojis[daitem]} {daitem} - ** {new_lst[daitem]}")
        else:
          pages[f"page{(i // 12) + 1}"].append(
            f"**{daitem} - ** {new_lst[daitem]}")
      else:
        del db["inv" + userId][daitem]
    numberpages = 0
    for page, contents in pages.items():
      numberpages += 1
    page = []
    for i in range(1, int(numberpages)):
      page.append("page" + str(i))
    if "page" + str(pageSaid) in pages:
      thelist = pages["page" + str(pageSaid)]
    else:
      embed = discord.Embed(title=f"__Inventory__",
                            description=f"Page {pageSaid} does not exist!",
                            color=discord.Color.red())
      await interaction.response.edit_message(embed=embed)
    txt = ""
    for i in thelist:
      txt = txt + f"\n{i}"
    view = PaginationView(int(interaction.user.id), "Inventory", pageSaid, pages)
    view.add_item(invSort(userId))
    embed.add_field(name="", value=txt, inline=False)
    embed.set_footer(text=f"{pageSaid}/{numberpages}")
    await interaction.response.edit_message(embed=embed, view=view)

@bot.command(name="inventory", aliases=["inv"])
async def inventory(ctx):  # *, user=None, page=None):
  if mentions := ctx.message.mentions:
    user = mentions[0]
  else:
    user = ctx.author
  pageSaid = 1
  split_message = ctx.message.content.split()
  if split_message[-1].isdigit():  # Checks if last param is a digit
    pageSaid = int(split_message[-1])
  userId = str(user.id)
  if "inv" + userId not in db:
    db["inv" + userId] = {}
  link = await bot.fetch_user(int(userId))
  embed = discord.Embed(title=f"", description="", color=discord.Color.green())
  embed.set_author(name=f"{str(link).split('#')[0]}'s Inventory",
                   icon_url=user.display_avatar.url)
  #pages
  new_lst = db["inv" + userId]
  num_pages = int(math.ceil(len(new_lst) / 12))
  pages = {}
  value = 0
  for i in range(num_pages):
    pages[f"page{i+1}"] = []
  for i in range(len(new_lst)):
    daitem = list(new_lst.keys())[i]
    if new_lst[daitem] > 0:
      if daitem in allitememojis:
        pages[f"page{(i // 12) + 1}"].append(
          f"**{allitememojis[daitem]} {daitem} - ** {new_lst[daitem]}")
      else:
        pages[f"page{(i // 12) + 1}"].append(
          f"**{daitem} - ** {new_lst[daitem]}")
      if daitem in shop_items:
        value += int(shop_items[daitem]) * int(new_lst[daitem])
      elif daitem in sellable:
        value += int(sellable[daitem]) * int(new_lst[daitem])
      elif daitem in collectables_value:
        value += int(collectables_value[daitem]) * int(new_lst[daitem])
    else:
      del db["inv" + userId][daitem]
  numberpages = 0
  for page, contents in pages.items():
    numberpages += 1
  page = []
  for i in range(1, int(numberpages)):
    page.append("page" + str(i))
  if "page" + str(pageSaid) in pages:
    thelist = pages["page" + str(pageSaid)]
  else:
    embed = discord.Embed(title=f"__Inventory__",
                          description=f"Page {pageSaid} does not exist!",
                          color=discord.Color.red())
    await ctx.reply(embed=embed)
  txt = ""
  for i in thelist:
    txt = txt + f"\n{i}"
  view = PaginationView(ctx.author.id, "Inventory", pageSaid, pages)
  view.add_item(invSort(userId))
  embed.add_field(name="", value=txt, inline=False)
  embed.set_footer(
    text=f"Value: {add_commas(value)}\n{pageSaid}/{numberpages}")
  await ctx.reply(embed=embed, view=view)
  db["invval" + userId] = value
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1