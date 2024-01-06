async def lottery_task():
  while True:
    if db["theLottery"]["Time"]+86400<round(time.time()):
      if len(db["theLottery"]["Tickets"])==0:
        return
      tickets=dict(db["theLottery"]["Tickets"].items())
      ticketNums=0
      for i,v in tickets.items():
        ticketNums+=v
      deflate=(ticketNums*50000)-db["theLottery"]["Jackpot"]
      db["lotteryDeflation"]+=deflate
      ticketNum=0
      print(ticketNums)
      if ticketNums>0:
        winnerNum=random.randint(1,ticketNums)
        for i,v in tickets.items():
          ticketNum+=v
          if ticketNum>=winnerNum:
            winner=i
            break
      else:
        break
      inventoryadd(str(winner),"winning_lottery_ticket",1)
      embed=discord.Embed(title="**Lottery**", description=f"<@{winner}> WON THE LOTTERY JACKPOT OF {db['theLottery']['Jackpot']} COINS!\n\nUsers: `{len(tickets)}`\nTickets: `{ticketNums}`")
      db[str(winner)]+=db["theLottery"]["Jackpot"]
      db["theLottery"]["Time"]+=86400
      db["theLottery"]["Tickets"]={}
      db["theLottery"]["Jackpot"]=0
      channel = bot.get_channel(1130172015584759898)
      await channel.send(embed=embed)
    await asyncio.sleep(60)

@bot.command()
async def lottery(ctx, type=None, amount:int=None):
  user=str(ctx.author.id)
  if "theLottery" not in db:
    db["theLottery"]={
      "Tickets":{},
      "Time":1689458400,
      "Jackpot":0,
    }
  data=dict(db["theLottery"])
  if type==None:
    if user in data["Tickets"]:
      txt=f"You have {data['Tickets'][user]} tickets."
    else:
      txt="You have no tickets. Buy one now!"
    num=0
    for i,v in data['Tickets'].items():
      num+=v
    txt+=f"\n\nUsers: `{len(data['Tickets'])}`\nTickets: `{num}`"
    embed=await embedify("**Lottery**",f"Tickets cost **50,000** coins each\n\n{txt}\n\nCurrent Jackpot: {data['Jackpot']}")
    embed.set_footer(text="!lottery buy [amount]")
    await ctx.send(embed=embed)
  elif type.lower() in "buy":
    if amount==None:
      amount=1
    price=50000*amount
    if db[user]>=price:
      if user in data['Tickets']:
        data["Tickets"][user]+=amount
      else:
        data["Tickets"][user]=amount
      data["Jackpot"]+=round(price*0.75)
      db[user]-=price
      await ctx.reply(embed=await embedify(f"You successfully bought {amount} lottery tickets."))
    else:
      await ctx.reply(embed=await embedify("You do not ahve enought money for that many lottery tickets!"))
  if type.lower() in "deflate" and user in admin:
    await ctx.send(db["lotteryDeflation"])
  db["theLottery"]=data
