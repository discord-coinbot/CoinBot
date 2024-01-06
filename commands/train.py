# train
class trainbuttons(discord.ui.View):

  def __init__(self):
    super().__init__()
    self.value = None

  global choice
  global choices
  choices = ["Left", "Middle", "Right"]
  choice = random.choice(choices)

  @discord.ui.button(label="Check", style=discord.ButtonStyle.green)
  async def check(self, interaction: discord.Interaction,
                  button: discord.ui.Button):
    embed = discord.Embed(title="**Check**",
                          description=f"CHOICE = {choice}",
                          color=discord.Color.random())
    await interaction.response.edit_message(embed=embed, view=trainbuttons)

  if choice == "Left":

    @discord.ui.button(label="Left", style=discord.ButtonStyle.green)
    async def left(self, interaction: discord.Interaction,
                   button: discord.ui.Button):
      embed = discord.Embed(title="**hi**",
                            description="CORRECT",
                            color=discord.Color.random())
      await interaction.response.edit_message(embed=embed, view=trainbuttons)
  else:

    @discord.ui.button(label="Left", style=discord.ButtonStyle.red)
    async def left(self, interaction: discord.Interaction,
                   button: discord.ui.Button):
      embed = discord.Embed(title="**Train**",
                            description="You missed.",
                            color=discord.Color.random())
      await interaction.response.edit_message(embed=embed, view=None)

  if choice == "Middle":

    @discord.ui.button(label="Middle", style=discord.ButtonStyle.green)
    async def middle(self, interaction: discord.Interaction,
                     button: discord.ui.Button):
      embed = discord.Embed(title="**hi**",
                            description="CORRECT",
                            color=discord.Color.random())
      await interaction.response.edit_message(embed=embed, view=trainbuttons())
  else:

    @discord.ui.button(label="Middle", style=discord.ButtonStyle.red)
    async def middle(self, interaction: discord.Interaction,
                     button: discord.ui.Button):
      embed = discord.Embed(title="**Train**",
                            description="You missed.",
                            color=discord.Color.random())
      await interaction.response.edit_message(embed=embed, view=None)

  if choice == "Right":

    @discord.ui.button(label="Right", style=discord.ButtonStyle.green)
    async def right(self, interaction: discord.Interaction,
                    button: discord.ui.Button):
      embed = discord.Embed(title="**hi**",
                            description="CORRECT",
                            color=discord.Color.random())
      await interaction.response.edit_message(embed=embed, view=trainbuttons())
  else:

    @discord.ui.button(label="Right", style=discord.ButtonStyle.red)
    async def right(self, interaction: discord.Interaction,
                    button: discord.ui.Button):
      embed = discord.Embed(title="**Train**",
                            description="You missed.",
                            color=discord.Color.random())
      await interaction.response.edit_message(embed=embed, view=None)
      
@bot.command()
async def train(ctx):
  view = trainbuttons()
  await ctx.reply(view)
  embed = discord.Embed(title="**Training**",
                        description="You started a training session",
                        color=discord.Color.dark_grey())
  await ctx.reply(embed=embed, view=view)
  command = list(str(ctx.message.content).split(" "))[0]
  if command in db["cmds" + str(ctx.author.id)]:
    db["cmds" + str(ctx.author.id)][command] += 1
  else:
    db["cmds" + str(ctx.author.id)][command] = 1
  # xp = level*10
  # embed=discord.Embed(name="Training",
  # description=text,
  # color=discord.Color.random())