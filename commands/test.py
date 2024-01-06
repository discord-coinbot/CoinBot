
@bot.command()
async def test(message, type, answer: str = None):
  user = str(message.author.id)
  if "469521741744701444" in user or "600411237561663498" in user:
    if "money" in type:
      db[user] += int(answer)
      await message.reply(f"Given {answer} coins.")
    elif "THE_GREAT_RESET" in type:

      def check(m):
        return 1 == 1 and str(m.author.id).isnumeric()

      thajan = await discordinput(message, check, "<@600411237561663498>?")
      if thajan != "!yes":
        return await message.send("cancelling")
      razi = await discordinput(message, check, "<@469521741744701444>?")
      if razi != "!yes":
        return await message.send("cancelling")
      await message.send(
        # This is it then... The end of the first era of CoinBot. CoinBot was brought to you by Razi and Thajan, but was not possible without all of you, and a special thanks to Suvheet for his ideas. We hope you enjoy its second era (in which Aadish will also hopefully aid in the progress of CoinBot). And now the second era of CoinBot shall begin, with the eradication of all data of the first - the great reset"""
      )
      time.sleep(5)
      await THE_GREAT_RESET(message)
      await message.reply("# Everything has been reset")
    elif "reset" in type:
      if "<@" and ">" in answer:
        answer = answer.replace("<@", "")
        answer = answer.replace(">", "")
        if "coins" in type:
          db[answer] = 0
          link = await bot.fetch_user(answer)
          await message.reply(f"Reset {link}'s coins.")
        elif "inv" in type:
          users = "inv" + answer
          db[users].clear()
          link = await bot.fetch_user(answer)
          await message.reply(f"Reset {link}'s inventory")
        elif "bankspace" in type:
          db["bankspace" + answer] = 5000
          await message.reply(f"Reset {link}'s bankspace'")
        elif "ALLRUNES" in type:
          for i in db.keys():
            if "rune" or "shard" in i:
              del db[i]
              await message.send(f"Deleted {i}")
        elif "runes" in type:
          db["rune" + answer] = {
            "dig": 0,
            "mine": 0,
            "study": 0,
            "search": 0,
            "unbreaking": 0,
          }
          await message.reply(f"Reset {link}'s runes'")
        elif "shards" in type:
          db["shard" + answer] = {
            "digshards": 0,
            "mineshards": 0,
            "studyshards": 0,
            "searchshards": 0,
            "unbreakingshards": 0,
          }
          await message.reply(f"Reset {link}'s shards'")
      elif "market" in answer:
        db["CRYPTO_MARKET"] = {
          "dogecoin": 50,
          "etherium": 3000,
          "bitcoin": 30000
        }
        await message.reply("Reset the crypto markets.")
      elif "chat" in answer:
        txt = "**"
        for i in range(1, 665):  #no not 2k what is the limit
          txt = txt + " \n"
        txt = txt + "**"
        for i in range(1, 10):
          await message.reply(txt)
    elif "servers" in type:
      txt = ""
      for i in list(bot.guilds):
        txt = txt + "\n" + str(i)
      embed = discord.Embed(title="**__Servers__**",
                            description=txt,
                            color=discord.Color.random())
      await message.reply(embed=embed)
  else:
    await message.reply("You are not an admin.")  #hi
