# MERCHANT

def changedeals(date):
  item_deal_list=list(shop_items.keys()).copy()
  item1 = random.choice(item_deal_list)
  item_deal_list.remove(item1)
  cost1 = shop_items[item1]
  discount1 = random.randint(3,20)
  lcost1 = int((cost1 - (discount1*(cost1/100))))
  if cost1 >= 500000:
    stock1 = random.randint(1,3)
  elif cost1 >= 100000:
    stock1 = random.randint(2,5)
  else:
    stock1 = random.randint(3,10)
  item2 = random.choice(item_deal_list) # why is this bugged?
  cost2 = shop_items[item2]
  discount2 = random.randint(1,20)
  lcost2 = int(cost2 - (discount2*(cost2/100)))
  if cost2 >= 500000:
    stock2 = random.randint(1,3)
  elif cost2 >= 100000:
    stock2 = random.randint(2,5)
  else:
    stock2 = random.randint(3,10)
  getlist = list(getitems.keys())
  num = random.randint(0,len(getlist) - 1)
  item3 = getlist[num]
  cost3 = 5000000 / (getitems[item3] - getitems[getlist[num-1]])
  discount3 = random.randint(0,10)
  lcost3 = int(cost3 - discount3*(cost3/100))
  if getitems[item3] >= 50:
    stock3 = random.randint(2,7)
  else:
    stock3 = random.randint(1,5)
  db["merchant"] = [ [item1,lcost1,discount1,stock1],[item2,lcost2,discount2,stock2],
[item3,lcost3,discount3,stock3] ,date]

@bot.command(name="merchant", aliases=["m"])
async def merchant(ctx,action=None,item=None,amount = None):
  user = str(ctx.author.id)
  t = time.localtime()
  current_time = int(time.strftime("%H:%M:%S", t).replace(":","")) + 10000
  date = datetime.date.today()
  date = str(date).replace("-","")
  if current_time >= 170000 and db["merchant"][3] != date:
    changedeals(date)
    await ctx.send("# The merchant has changed his trades.")
  if action == None or "deal" in action.lower():
    embed = discord.Embed(title="Merchant Deals",
                         description="",
                         color=discord.Color.blue())
    for i in range(3):
      off = ""
      if i != 2:
        off = f'(__{db["merchant"][i][2]}%__ off)'
      embed.add_field(name=db["merchant"][i][0],value=f'{db["merchant"][i][1]} {off} - __{db["merchant"][i][3]}__ in stock',inline = False)
    embed.set_footer(text="The merchant will change its deals at 5:00 PM")
    await ctx.reply(embed=embed)
  elif "buy" in action.lower():
    if item == None:
      return await ctx.reply(embed=await embedify("What are you buying?",""))
    if amount == None:
      amount = 1
    items = []
    for i in range(3):
      items.append(db["merchant"][i][0])
      if item == db["merchant"][i][0]:
        index = i
    if item not in items:
      return await ctx.reply(embed=await embedify("The merchant isn't selling that",""))
    if amount > db["merchant"][index][3]:
      return await ctx.reply(embed=await embedify("The merchant has no more of that item in stock",""))
    if db[user] < db["merchant"][index][1]:
      return await ctx.reply(embed=await embedify("You do not have enough to buy that item",""))
    db[user] -= db["merchant"][index][1] * amount
    db["merchant"][index][3] -= amount
    inventoryadd(user,item,amount)
    return await ctx.reply(embed=await embedify(f"You bought {amount} {item}(s) from the merchant.","")) # razi should i ping now