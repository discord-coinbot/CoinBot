
@bot.command()
async def ping(ctx):
  await ctx.reply('Pong! {0}ms'.format(round(1000 * (bot.latency))))
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1

@bot.command()
async def type(ctx):
  async with ctx.typing():
    await asyncio.sleep(600)



# REVISE (NOT CONFIRMED)
wordlist = {"ist": "is", "er": "he"}


@bot.command()
async def revise(ctx, num: int = None):

  def check(m):
    return m.author.id == ctx.author.id and m.channel == ctx.channel

  for i in range(num):
    german_word = random.choice(list(wordlist.keys()))
    english_word = wordlist[german_word]
    ger_or_eng = random.randint(1, 2)
    if ger_or_eng == 1:
      prompt = await discordinput(ctx, check, german_word, 10)
      if prompt == "stop":
        embed = discord.Embed(title="**Stopped**",
                              description="",
                              color=discord.Color.red())
        await ctx.reply(embed=embed)
        break
      if prompt == english_word:
        embed = discord.Embed(title="**Correct**",
                              description="",
                              color=discord.Color.green())
        await ctx.reply(embed=embed)
      else:
        embed = discord.Embed(title="**ncorrect**",
                              description=f"It was {english_word}.",
                              color=discord.Color.red())
        await ctx.reply(embed=embed)
    else:
      prompt = await discordinput(ctx, check, english_word, 10)
      if prompt == "stop":
        embed = discord.Embed(title="**Stopped**",
                              description="",
                              color=discord.Color.red())
        await ctx.reply(embed=embed)
        break
      if prompt == german_word:
        embed = discord.Embed(title="**Correct**",
                              description="",
                              color=discord.Color.green())
        await ctx.reply(embed=embed)
      else:
        embed = discord.Embed(title="**Incorrect**",
                              description=f"It was {german_word}.",
                              color=discord.Color.red())
        await ctx.reply(embed=embed)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1

@bot.command()
async def sudoku(ctx):
  base = 3
  side = base * base

  def pattern(r, c):
    return (base * (r % base) + r // base + c) % side



  def shuffle(s):
    return sample(s, len(s))

  rBase = range(base)
  rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
  cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
  nums = shuffle(range(1, base * base + 1))

  board = [[nums[pattern(r, c)] for c in cols] for r in rows]

  squares = side * side
  empties = squares * 49 // 81
  for p in sample(range(squares), empties):
    board[p // side][p % side] = 0

  def expandLine(line):
    return line[0] + line[5:9].join([line[1:5] *
                                     (base - 1)] * base) + line[9:13]

  line0 = expandLine("╔═══╤═══╦═══╗")
  line1 = expandLine("║ . │ . ║ . ║")
  line2 = expandLine("╟───┼───╫───╢")
  line3 = expandLine("╠═══╪═══╬═══╣")
  line4 = expandLine("╚═══╧═══╩═══╝")

  symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  nums = [[""] + [symbol[n] for n in row] for row in board]
  txt = ""
  txt += line0 + "\n"
  for r in range(1, side + 1):
    txt += "".join(n + s for n, s in zip(nums[r - 1], line1.split(".")))
    txt += "\n"
    txt += [line2, line3, line4][(r % side == 0) + (r % base == 0)]
    txt += "\n"
  embed = discord.Embed(title="**Sudoku**", description=f"`\n{txt}`")
  await ctx.reply(embed=embed)


# DM
@bot.command()
async def DM(ctx, user: discord.User, *, message=None):
  message = message or "This Message is sent via DM"
  await user.send(message)


@bot.command()
async def send(ctx,msg,channell):
  if "469521741744701444" == str(ctx.author.id) or "600411237561663498" == str(ctx.author.id):
    channel = bot.get_channel(int(channell))
    if "_" in msg:
      msg = msg.replace("_"," ")
    print(msg)
    await channel.send(msg)


# REMOVE
@bot.command()
async def remove(ctx, person: discord.Member, item, number: int = None):
  if number == None:
    number = 1
  number = int(number)
  person = str(person.id)
  user = str(ctx.author.id)
  if "469521741744701444" not in user and "600411237561663498" not in user:
    return await ctx.reply("Silly **goose**, you arent a mod.")
  inventoryremove(user, item, number)
  await ctx.reply(f"Removed {number} {item}(s) from <@{person}>'s inventory.")


# SHOW
@bot.command()
async def show(ctx, person=None):
  user = str(ctx.author.id)
  if person != None:
    person.replace("<", "").replace("@", "").replace(">", "")
  await ctx.reply


# TEST AND # SET
@bot.command()
async def set(ctx, person, type, set):
  user = str(ctx.author.id)
  if user != "469521741744701444" and user != "600411237561663498":
    return await ctx.reply("NOT ADMIN")
  person = person.replace("<", "").replace("@", "").replace(">", "")
  if "int" in set:
    set = set.replace("int", "")
    set = int(set)
  if type + person in db:
    db[type + person] = set
    await ctx.reply(f"Set <@{person}> 's {type} to {set}")
  else:
    await ctx.reply("Not in db")
