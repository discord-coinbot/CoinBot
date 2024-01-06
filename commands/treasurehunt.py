# MINIGAME - treasure hunt?
world = {
  "Maze": {
    "Encounters": {
      "Dragon": {
        "IMAGE":
        ["IMAGE", "You came across a sleeping dragon. What do you do?"],
        "Fight": {
          200:
          "You easily slayed the dragon, who looked way fiercer than it was.",
          800: "You tried fighting the dragon, but you were easily defeated."
        },
        "Run Past": [{
          600: "You ran past the dragon without waking it up"
        }, {
          200: "You woke the dragon up, and it burnt you to a crisp"
        }, {
          200:
          "You woke the dragon up and its thorny tail smashed into you and killed you."
        }],
        "End your adventure by Running Away":
        "You ended your adventure"
      },
      "Spynx": {
        "IMAGE":
        ["IMAGE", "You came across a sleeping dragon. What do you do?"],
        "Fight": {
          200:
          "You easily slayed the dragon, who looked way fiercer than it was.",
          800: "You tried fighting the dragon, but you were easily defeated."
        },
        "Run Past": [{
          600: "You ran past the dragon without waking it up"
        }, {
          200: "You woke the dragon up, and it burnt you to a crisp"
        }, {
          200:
          "You woke the dragon up and its thorny tail smashed into you and killed you."
        }],
        "End your adventure by Running Away":
        "You ended your adventure"
      },
      "Treasure Chest": {
        "IMAGE":
        ["IMAGE", "You came across a sleeping dragon. What do you do?"],
        "Fight": {
          200:
          "You easily slayed the dragon, who looked way fiercer than it was.",
          800: "You tried fighting the dragon, but you were easily defeated."
        },
        "Run Past": [{
          600: "You ran past the dragon without waking it up"
        }, {
          200: "You woke the dragon up, and it burnt you to a crisp"
        }, {
          200:
          "You woke the dragon up and its thorny tail smashed into you and killed you."
        }],
        "End your adventure by Running Away":
        "You ended your adventure"
      },
      "Paths": ""
    }
  },
  "Streets": {
    "Encounters": {
      "Person": {
        "IMAGE":
        ["IMAGE", "You came across a sleeping dragon. What do you do?"],
        "Fight": {
          200:
          "You easily slayed the dragon, who looked way fiercer than it was.",
          800: "You tried fighting the dragon, but you were easily defeated."
        },
        "Run Past": [{
          600: "You ran past the dragon without waking it up"
        }, {
          200: "You woke the dragon up, and it burnt you to a crisp"
        }, {
          200:
          "You woke the dragon up and its thorny tail smashed into you and killed you."
        }],
        "End your adventure by Running Away":
        "You ended your adventure"
      },
      "Dog": {
        "IMAGE":
        ["IMAGE", "You came across a sleeping dragon. What do you do?"],
        "Fight": {
          200:
          "You easily slayed the dragon, who looked way fiercer than it was.",
          800: "You tried fighting the dragon, but you were easily defeated."
        },
        "Run Past": [{
          600: "You ran past the dragon without waking it up"
        }, {
          200: "You woke the dragon up, and it burnt you to a crisp"
        }, {
          200:
          "You woke the dragon up and its thorny tail smashed into you and killed you."
        }],
        "End your adventure by Running Away":
        "You ended your adventure"
      },
      "Treasure Chest": {
        "IMAGE":
        ["IMAGE", "You came across a sleeping dragon. What do you do?"],
        "Fight": {
          200:
          "You easily slayed the dragon, who looked way fiercer than it was.",
          800: "You tried fighting the dragon, but you were easily defeated."
        },
        "Run Past": [{
          600: "You ran past the dragon without waking it up"
        }, {
          200: "You woke the dragon up, and it burnt you to a crisp"
        }, {
          200:
          "You woke the dragon up and its thorny tail smashed into you and killed you."
        }],
        "End your adventure by Running Away":
        "You ended your adventure"
      },
    }
  },
  "Forest": {
    "Encounters": {
      "Snake": {
        "IMAGE":
        ["IMAGE", "You came across a sleeping dragon. What do you do?"],
        "Fight": {
          200:
          "You easily slayed the dragon, who looked way fiercer than it was.",
          800: "You tried fighting the dragon, but you were easily defeated."
        },
        "Run Past": [{
          600: "You ran past the dragon without waking it up"
        }, {
          200: "You woke the dragon up, and it burnt you to a crisp"
        }, {
          200:
          "You woke the dragon up and its thorny tail smashed into you and killed you."
        }],
        "End your adventure by Running Away":
        "You ended your adventure"
      },
      "Monkey": {
        "IMAGE":
        ["IMAGE", "You came across a sleeping dragon. What do you do?"],
        "Fight": {
          200:
          "You easily slayed the dragon, who looked way fiercer than it was.",
          800: "You tried fighting the dragon, but you were easily defeated."
        },
        "Run Past": [{
          600: "You ran past the dragon without waking it up"
        }, {
          200: "You woke the dragon up, and it burnt you to a crisp"
        }, {
          200:
          "You woke the dragon up and its thorny tail smashed into you and killed you."
        }],
        "End your adventure by Running Away":
        "You ended your adventure"
      },
      "Temple": {
        "IMAGE":
        ["IMAGE", "You came across a sleeping dragon. What do you do?"],
        "Fight": {
          200:
          "You easily slayed the dragon, who looked way fiercer than it was.",
          800: "You tried fighting the dragon, but you were easily defeated."
        },
        "Run Past": [{
          600: "You ran past the dragon without waking it up"
        }, {
          200: "You woke the dragon up, and it burnt you to a crisp"
        }, {
          200:
          "You woke the dragon up and its thorny tail smashed into you and killed you."
        }],
        "End your adventure by Running Away":
        "You ended your adventure"
      },
      "Treasure Chest": {
        "IMAGE":
        ["IMAGE", "You came across a sleeping dragon. What do you do?"],
        "Fight": {
          200:
          "You easily slayed the dragon, who looked way fiercer than it was.",
          800: "You tried fighting the dragon, but you were easily defeated."
        },
        "Run Past": [{
          600: "You ran past the dragon without waking it up"
        }, {
          200: "You woke the dragon up, and it burnt you to a crisp"
        }, {
          200:
          "You woke the dragon up and its thorny tail smashed into you and killed you."
        }],
        "End your adventure by Running Away":
        "You ended your adventure"
      },
    }
  }
}

Dragon = [
  "You came across a sleeping dragon. What do you do?", "IMAGE", {
    "Run Past": [
      80,
      [
        "You swiftly ran past the sleeping dragon",
        "You ran past without making a sound"
      ], None
    ],
    "Fight": [
      20,
      [
        "You somehow overpowered a dragon with your elite karate skills!",
        "You barely managed to kill it, but you killed the dragon."
      ], "Dragon killed"
    ]
  }
]

maze_encounters = {
  200: Dragon,
  500: "Sphynx",
  600: "Minotaur",
}


# STRUCTURE
# Creature = [What it says first, Image, [{CHOICE1:[PROB OF SURVIVE,[RESPONSE1,RESPONSE2]]},CHOICE2:PROB OF SURVIVE,[RESPONSE1,RESPONSE2]]]
async def choices(message):
  pass  # DO


async def respond(mes1, mes2=None):
  pass  # DO


@bot.command()
async def th(ctx):
  user = ctx.author.id

  def check(m):
    return m.author.id == ctx.author.id

  place = discordinput(message, check, "Do you want to start an adventure?")
  chance = random.randint(1000)
  ended = False
  while not ended:
    if place == "Maze":
      if chance < x:  # Dragon
        encounter = maze_encounters[x]
        image = encounter[1]
        respond(encounter[0])
        if len(list(encounter[2].keys())) == 2:
          all_choices = list(encounter[2].keys())[0], list(
            encounter[2].keys())[1], "End Adventure"
        elif len(list(encounter[2].keys())) == 3:
          all_choices = list(encounter[2].keys())[0], list(
            encounter[2].keys())[1], list(
              encounter[2].keys())[2], "End Adventure"
        choice = choices(all_choices)
        chance2 = random.randint(1, 100)
        if choice == all_choices[0]:
          if chance2 <= 10:
            respond(
              "You somehow overpowered a dragon with your elite karate skills. You got a dragon wing!",
              "You barely managed to kill it, but you killed the dragon. You got a dragon wing!"
            )
          else:
            respond(
              "The dragon instantly burnt you to a crisp when you tried fighting it",
              "The dragon swung its thorned tail and it killed you")
            ended = True
        elif choice == "Run Past":
          if chance2 <= 70:
            respond("You swiftly ran past the sleeping dragon",
                    "You ran past without making a sound")
          else:
            respond(
              "You accidentally tripped on its tail which woke it up. The dragon instantly killed you.",
              "You made too much noise and woke the dragon up and it killed you."
            )
            ended = True
      if not ended:
        path()
      elif chance <= 500:
        pass