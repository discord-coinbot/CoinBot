
# work
#work apply
workitems={
  "garbage_man": "garbage_bag",
  "janitor": "mop",
  "mcdonalds_waiter": "big_mac",
  "professional_cook": "cutlery",
  "chauffeur": "driving_licence",
  "professor": "whiteboard_pen",
  "business_man": "bitcoin",
  "cristopher_ronaldo": "football",
  "vice_captain_of_tesla": "tesla",
  "elon_musks_son": "twitter_logo",
}

work_jobs = {
  "garbage_man": 1,
  "janitor": 2,
  "mcdonalds_waiter": 3,
  "professional_cook": 4,
  "chauffeur": 5,
  "professor": 6,
  "business_man": 7,
  "cristopher_ronaldo": 8,
  "vice_captain_of_tesla": 9,
  "elon_musks_son": 10,
}

page1work = {
  "Garbage_Man": 1,
  "Janitor": 2,
  "Mcdonalds_Waiter": 3,
  "Professional_Cook": 4,
  "Chauffeur": 5,
}

page2work = {
  "Professor": 6,
  "Business_Man": 7,
  "Cristopher_Ronaldo": 8,
  "Vice_Captain_Of_Tesla": 9,
  "Elon_Musks_Son": 10,
}


@bot.command()
async def work(ctx, type=None, job=None):
  user = str(ctx.author.id)
  userworklvl = str("worklvl" + user)
  userworkxp = str("workxp" + user)
  usercurrentwork = str("job" + user)
  userworktime = str("worktime" + user)
  if userworklvl not in db:
    db[userworklvl] = 0
  if usercurrentwork not in db:
    db[usercurrentwork] = ""
  if userworkxp not in db:
    db[userworkxp] = 0
  if userworktime not in db:
    db[userworktime] = 0
  if type == "apply":
    if int(db[userworklvl]) == 0:
      await ctx.reply(
        "To get a job, you must pay 5000 to convince you are a hard working man dedicated to working. Would you like to? [!yes or !no]"
      )

      def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

      try:
        response = await bot.wait_for('message', check=check, timeout=10.0)
        if response.content.lower() != "!yes":
          return await ctx.reply(embed=cancelEmbed)
        else:
          user = str(ctx.author.id)
          if user not in db:
            db[user] = 0
          if db[user] >= 5000:
            db[user] -= 5000
            db[userworklvl] = 1
            return await ctx.reply(
              f"{ctx.author.mention} sucessfully unlocked work level 1.")
          else:
            await ctx.reply("You dont have 5000 coins.")
      except asyncio.TimeoutError:
        return await ctx.reply(
          embed=await embedify("Took too long, cancelling...", ""))
    jobs = str(job)
    jobs = jobs.lower()
    jobs = jobs.replace(" ", "")
    if str(jobs) in work_jobs:
      if db[usercurrentwork] == "":
        if int(work_jobs[jobs]) <= int(db[userworklvl]):
          db[usercurrentwork] = str(jobs)
          await ctx.reply(f"Congratulations! You now work as a {job}!")
          work.reset_cooldown(ctx)
        else:
          await ctx.reply("You don't have that job unlocked!")
          work.reset_cooldown(ctx)
      else:
        await ctx.reply("You already have a job, resign from it first!")
        work.reset_cooldown(ctx)
    else:
      await ctx.reply("Choose a job from !work list")
      work.reset_cooldown(ctx)
  content = ctx.message.content.lower()
  user = str(ctx.author.id)
  userworklvl = str("worklvl" + user)
  userworkxp = str("workxp" + user)
  usercurrentwork = str("job" + user)
  userworktime = str("worktime" + user)
  if userworklvl not in db:
    db[userworklvl] = 0
  if usercurrentwork not in db:
    db[usercurrentwork] = ""
  if userworkxp not in db:
    db[userworkxp] = 0
  if userworktime not in db:
    db[userworktime] = 0
  if type==None:
    if db[usercurrentwork] != "":
      if int(db[userworktime]) + 3600 <= round(time.time()) or str(ctx.author.id) == "600411237561663498":
        db[userworktime] = str(round(time.time()))
        num1 = random.randint(10, 30)
        num2 = random.randint(10, 30)
        num3 = random.randint(10, 30)
        embed1 = discord.Embed(
          title="**__Work__**",
          description=str(f"What is {str(num1)}-{str(num2)}+{str(num3)}?"),
          color=discord.Color.random())
        await ctx.reply(embed=embed1)

        def check(m):
          return m.author == ctx.author and m.channel == ctx.channel

        ans = int(num1 - num2 + num3)
        ans = str(ans)
        try:
          response = await bot.wait_for('message', check=check, timeout=10.0)
          if ans not in response.content.lower():
            embeds = discord.Embed(title="**__Incorrect__**",
                                   description=str(f"You got nothing"),
                                   color=discord.Color.red())
            return await ctx.reply(embed=embeds)
          else:
            lvl = int(work_jobs[db[usercurrentwork]])
            coins = 1000 * (lvl**2 - lvl + 5)
            txt=f"You got {add_commas(str(coins))}. "
            if random.randint(1,15)==15:
              itemFound=workitems[db[usercurrentwork]]
              txt+=f"\n\nYou also found a {allitememojis[itemFound]} {itemFound}"
              inventoryadd(ctx.author.id,itemFound,1)
            embeds = discord.Embed(
              title="**__Correct__**",
              description=txt,
              color=discord.Color.green())
            db[user] += int(coins)
            num=round(0.03 * (11 - int(db[userworklvl])),2)
            db[userworkxp] = float(num)+float(round(float(db[userworkxp]),2))
            if int(db[userworkxp]) >= 1 and int(db[userworklvl]) < 11:
              await ctx.reply("You leveled up!")
              db[userworkxp] = 0
              db[userworklvl] += 1
            return await ctx.reply(embed=embeds)
        except:
          await ctx.reply("You took too long.")
      else:
        timeleft = (int(db[userworktime]) + 3600) - round(time.time())
        minutes = timeleft // 60
        seconds = timeleft % 60
        msg = str(
          f"Your cooldown ends in {minutes} minutes and {seconds} seconds.")
        embed = discord.Embed(title="**__Cooldown__**",
                              description="",
                              color=discord.Color.red())
        embed.add_field(name=msg, value="")
        await ctx.reply(embed=embed)
    else:
      await ctx.reply("Get a job to work.")
  elif "apply" in type.lower() and job==None:
    await ctx.reply("Please tell us a job from the list you are applying for")
  elif "resign" in type.lower():
    if db[usercurrentwork] != "":
      db[usercurrentwork] = ""
      await ctx.reply(
        "You resigned from your job. Wait an hour to apply for another.")
    else:
      await ctx.reply("But u don't even have a job.")
  elif "list" in type.lower():
    page1 = discord.Embed(title="**__Work List__**",
                          description="Jobs",
                          color=0xFF5733)
    for item, level in page1work.items():
      lvl = int(level)
      price = 1000 * (lvl**2 - lvl + 5)
      page1.add_field(
        name=item,
        value=f"Salary: {add_commas(str(price))}\nWork Level: {level}",
        inline=False)
    page1.set_footer(text=f"You are level {db[userworklvl]}\n1/2")
    page2 = discord.Embed(title="**__Work List__**",
                          description="Jobs",
                          color=0xFF5733)
    for item, level in page2work.items():
      lvl = int(level)
      price = 1000 * (lvl**2 - lvl + 5)
      page2.add_field(name=item,
                      value=f"Salary: {price}\nWork Level: {level}",
                      inline=False)
    page2.set_footer(text=f"You are level {db[userworklvl]}\n2/2")
    pages = [page1, page2]
    message = await ctx.reply(embed=page1)
    await message.add_reaction('◀')
    await message.add_reaction('▶')

    def check(reaction, user):
      return user == ctx.author

    i = 0
    reaction = None
    while True:
      if str(reaction) == '◀':
        if i > 0:
          i -= 1
          await message.edit(embed=pages[i])
      elif str(reaction) == '▶':
        if i < 2:
          i += 1
          await message.edit(embed=pages[i])
      try:
        reaction, user = await bot.wait_for('reaction_add',
                                            timeout=30.0,
                                            check=check)
        await message.remove_reaction(reaction, user)
      except:
        break

    await message.clear_reactions()
    work.reset_cooldown(ctx)
    command = list(str(ctx.message.content).split(" "))[0]
    if command in db["cmds" + str(ctx.author.id)]:
      db["cmds" + str(ctx.author.id)][command] += 1
    else:
      db["cmds" + str(ctx.author.id)][command] = 1
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1

