
@bot.command()
async def craft(ctx, item: str = None, times: int = None):
  user = str(ctx.author.id)
  inv = db["inv" + user]
  if "workbench" not in inv:
    embed = discord.Embed(title="**Craft**",
                          description="You don't own a workbench🛠️.",
                          color=discord.Color.red())
    return await ctx.reply(embed=embed)
  craftinfo = craftitems
  if "workbench_lvl_1" in inv:
    craftinfo = craftinfo.copy()
    craftinfo.update(craftitems1)
  if "workbench_lvl_2" in inv:
    craftinfo = craftinfo.copy()
    craftinfo.update(craftitems2)
  if "workbench_lvl_3" in inv:
    craftinfo = craftinfo.copy()
    craftinfo.update(craftitems3)
  if "brewing_stand" in inv:
    craftinfo = craftinfo.copy()
    craftinfo.update(craftpotions)
  if item == None:
    page = 0
  elif item.isnumeric():
    page = int(item) - 1
  else:
    if times == None:
      times = 1
    if item in craftinfo:
      for i, v in craftinfo[item].items():
        if i != "crafted_item":
          if i in db["inv" +
                     user] and db["inv" +
                                  user][i] >= v * times:  # THAJAN CHECK
            db["inv" + user][i] -= v * times
          else:
            return await ctx.reply(embed=await embedify(
              "Craft",
              f"{item} is not a craftable as you do not have the required items. ({i})"
            ))
      if item in db["inv" + user]:
        db["inv" + user][item] += craftinfo[item]["crafted_item"][0] * times
      else:
        db["inv" + user][item] = craftinfo[item]["crafted_item"][0] * times
      await ctx.reply(
        embed=await embedify("Craft", f"Sucessfully crafted a {item}."))
    else:
      await ctx.reply(
        embed=await embedify("Craft", f"{item} is not a vaild craftable"))
  txt = ""
  var1 = list(craftinfo.keys())
  for i, v in craftinfo[var1[page]].items():
    if i != "crafted_item":
      txt += f" + {v} {i}"
    else:
      txt += f" => {v[0]} {v[1]}"
  txt = txt[2:]
  num = 0
  num_pages = int(math.ceil(len(craftinfo.keys()) / 9))
  pages = {}
  for i in range(num_pages):
    pages[f"page{i+1}"] = []
  for i in range(len(craftinfo)):
    daitem = list(craftinfo.keys())[i]
    make = str(craftinfo[daitem]).split(" 'crafted_item'")[0].replace(
      "{", "").replace(",", ") +").replace(": ", "(").replace("'", "").replace("("," (x")
    if make[-1]=="+":
      make=make[:-1]
    pages[f"page{(i // 9) + 1}"].append(f"**{daitem} -> ** {make}")
  numberpages = 0
  for pageybh, contents in pages.items():
    numberpages += 1
  pageList = []
  for i in range(1, int(numberpages)):
    pageList.append("page" + str(i))
  if "page" + str(page) in pages:
    thelist = pages["page" + str(page)]
  thelist = pages["page" + str(page + 1)]
  txt = ""
  for i in thelist:
    txt = txt + f"\n{i}"
  embed = discord.Embed(title="**Craft**",
                        description=txt,
                        color=discord.Color.green())
  #embed.add_field(name=f"{var1[page]}", value=txt, inline=False)
  message = await ctx.reply(embed=embed,
                            view=PaginationView(ctx.author.id, "Craft", page+1,
                                                pages))
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1

