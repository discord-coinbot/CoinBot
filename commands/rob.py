
# ROB
@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def rob(message, user_mentioned: discord.Member):
  user = str(message.author.id)
  victim = str(user_mentioned.id)
  if victim not in db:
    db[victim] = 0
  if "gear" + user not in db:
    db["gear" + user] = {"Attack": "Nothing Equipped", "Defence": "Nothing Equipped", "items":{}}
  if "gear" + victim not in db:
    db["gear" + victim] = {"Attack": "Nothing Equipped", "Defence": "Nothing Equipped", "items":{}}
  victim_used = str("used" + victim)
  used = str("user" + user)
  if victim_used not in db:
    db[victim_used] = {"": 10}
    print(1)
  elif used not in db:
    db[used] = {"": 10}
  print(2)
  if True:
    pass
    print(3)
    victimval = db[victim]
    if str(victim) != str(user):
      if victimval > 1000:
        users = "inv" + user
        inventory_items = db["gear"+user]["Attack"]
        victiminv = "inv" + victim
        victim_inventory_items = db["gear"+victim]["Defence"]
        victim_used_items = db[victim_used]
        used_items = db[used]
        chance = 6
        special = 1
        print(4)
        caught = 10
        text = ""
        if "runeequip" + user in db:
          if "rob" in db["runeequip" + user]:
            chance = chance / 2
            special = special / 2
        if "bolts" in inventory_items:
          chance = chance / 5
        elif "lock_pick" in inventory_items:
          chance = chance / 2
        if "bag" in inventory_items:
          special = special / 5
        elif "pocket" in inventory_items:
          special = special / 2
        if "chains" in victim_inventory_items:
          chance = 3 * int(chance)
        elif "lock" in victim_inventory_items:
          chance *= 2 * int(chance)
        if "jet" in inventory_items:
          caught = caught * 5
        if "alarm" in victim_inventory_items:
          caught = int(caught/3)
        elif "guard_dog" in victim_inventory_items:
          caught = int(caught/2)
        if "chicken_wing" in inventory_items and "guard_dog" in victim_inventory_items:
          caught = 10
        uno = False
        if "uno_reverse" in victim_inventory_items:
          if "uno_skip" in inventory_items:
            text = "Your uno skip skipped the uno reverse"
          else:
            uno = True
        print(5)
        if chance > 9:
          chance = 9
        elif chance < 2:
          chance = 2
        continues = True
        print(6)

        if "inv_potion" in victim_used_items:
          print(7)
          thetime = int(victim_used_items["inv_potion"]) + 1800
          if int(thetime) > int(time.time()):
            if "night_vision_potion" not in used_items:
              embed = discord.Embed(
                title="**__Rob__**",
                description=
                f"<@{victim}> drank an invisibility potion and you couldn't find them.",
                color=discord.Color.random())
              embed.add_field(name="",
                              value=f"You failed to rob {user_mentioned}.")
              await message.reply(embed=embed)
              continues = False
            else:
              nighttime = int(used_items["night_vision_potion"]) + 1800
              if int(nighttime) > int(time.time()):
                await message.reply(
                  "Your right_vision_potion ran out and you couldn't find them.")
                used_items.pop("night_vision_potion", None)
                continues = False
              else:
                await message.reply(
                  embed=
                  "Your night_vision_potion let you see eventhough they had a invisibility_potion"
                )
                continues = True
          else:
            await message.reply(f"<@{victim}>'s invisibility ran out")
            victim_used_items.pop("inv_potion", None)
            continues = True
        else:
          pass
        print(7)
        if continues == True:
          if uno == True and random.randint(1,2) != 2:
            link = await bot.fetch_user(victim)
            text = f"{link}'s uno reverse REVERSED the rob!'"
            third = user
            user = victim
            victim = third
            print(8)
            user_mentioned = await bot.fetch_user(user)
          print(9)
          if "speed_potion" in used_items:
            chance / 2
            await message.send(
              "You speed potion gave you a 2x chance of robbing")
          chance = round(chance)
          rob_chance = random.randint(1, 10)
          lucky = random.randint(1, 7)
          multi = int(random.randint(2, 5))
          if lucky == 7:
            multi = int(random.randint(3, 10))
            text = f"You robbed {user_mentioned} and stole a fairly big chunk of "
          if "jump_boost_potion" in used_items:
            if int(victim_used_items["jump_boost_potion"]) + 1800 > int(
                time.time()):
              caught *= 4
            else:
              await message.reply("Your jump_boost_potion ran out")
              used_items.pop("jump_boost_potion")
          paychance = random.randint(1, caught)
          if rob_chance > chance:
            if victimval > 5000000:
              amount = 500
            elif victimval > 500000:
              amount = 200
            else:
              amount = 100
            amountrobnot = ((victimval / amount) * multi) / special
            amountrob = round(amountrobnot)
            db[victim] -= amountrob
            db[user] += amountrob
            amountrob = str(amountrob)
            coin = str(db[user])
            coins = coin
            coin = str(db[user])
            print(10)
            coins = coin
            if ".0" in coin:
              coins = coins.replace(".0", "")
            if ".0" in amountrob:
              amountrob = amountrob.replace(".0", "")
            if text == "":
              text = f"You robbed {user_mentioned} successfully and stole a bag of {amountrob} coins."
            else:
              text = text + f"{amountrob} coins."
            embed = discord.Embed(
              title="**__Rob__**",
              description=text,
              color=discord.Color.green())
            await message.reply(embed=embed)
          elif paychance == 1:
            payamount = int((victimval / 10000) * random.randint(1, 100))
            print("here")
            embed = discord.Embed(
              title="**__Rob__**",
              description=
              f"You got caught trying to rob {user_mentioned} and had to pay {payamount} to the police.",
              color=discord.Color.red())
            db[user] -= payamount
            await message.reply(embed=embed)
          else:
            embed = discord.Embed(
              title="**__Rob__**",
              description=f"You failed to rob {user_mentioned}.",
              color=discord.Color.red())
            await message.reply(embed=embed)
      else:
        await message.reply(
          "That user has under 1000 coins. Don't rob the poor.")
    else:
      await message.reply("You can't rob yourself.")
  command = list(str(message.message.content).split(" "))[0]
  if command in db["cmds" + str(message.author.id)]:
    db["cmds" + str(message.author.id)][command] += 1
  else:
    db["cmds" + str(message.author.id)][command] = 1

