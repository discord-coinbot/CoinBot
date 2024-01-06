
@bot.command()
async def button(ctx):
  pages = ["page1", "page2", "page3", "page4"]
  button1 = Button(label="<", style=discord.ButtonStyle.green)
  button2 = Button(label=">", style=discord.ButtonStyle.green)
  global page
  page = 0

  async def button1_callback(interaction, page):
    if page > 0:
      return await interaction.response.edit_message(content=pages[page - 1])
      page -= 1
    else:
      return

  async def button2_callback(interaction, page):
    if page < len(pages) - 1:
      return await interaction.response.edit_message(content=pages[page + 1])
      page += 1
    else:
      return

  button1.callback = button1_callback(interaction, page)
  button2.callback = button2_callback(interaction, page)
  view = View()
  view.add_item(button1)
  view.add_item(button2)
  await ctx.reply(pages[page], view=view)

  await bot.wait_for("button_click")

