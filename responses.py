import random

def get_response(message: str) -> str:
  p_message = message.lower()
  chance = random.randint(1,3)
  if p_message == 'talk':
    return "I am talking"
  elif 'hello' in p_message or 'hi ' in p_message or p_message == 'hi':
    numb = random.randint(0,1)
    ans = ["Hello!","Hi!","Greetings!"]
    return ans[numb]
  elif 'lol' in p_message:
    return 'very funny!'
  elif "eid" in p_message:
    return "https://tenor.com/view/aid-gif-21496698"
  elif p_message == "created by":
    return "Razi and Thajan"
  # This is to make sure people don't transfer -1000 and get coins
  elif "-" in p_message and ("!" in p_message or "." in p_message) and "lb" not in p_message and "https" not in p_message and "randomise" not in p_message and "/" not in p_message:
    responseslist=[
      "Don't try it. Just **don't**",
      "What are you trying to do? Well **don't** do it",
      "*Silly **goose**.*",
      "What is a **-**???",
      "Calling **FBI...**\n**FBI**:This is the FBI, how can i help?\n**ChatBot**: Hello we are reporting a case of duping money.",
      "You have to pay taxes *eventually*.",
      "Ok!",
      "Cool!",
      "what",
                  ]
    num = int(random.randint(1,len(responseslist)))
    return responseslist[num-1]
  elif "!test skyrocket " in p_message:
    g=p_message.replace("!test skyrocket ","")
    return f"{g.title()} skyrocketed."
  elif "!test crash " in p_message:
    g=p_message.replace("!test skyrocket ","")
    return f"{g.title()} crashed."
  return "not in code"