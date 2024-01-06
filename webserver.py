from flask import Flask, render_template
from threading import Thread
app = Flask('')

def run():
  app.run(host="0.0.0.0", port=8080)

text="k"
def keep_alive(txt):
  if txt=="yes":
    text="🟢ONLINE"
  else:
    text="🔴OFFLINE"

  @app.route('/')
  def home():
    return '''<html>
    <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.4/dist/jquery.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
    <title>CoinBot Status</title>
    <link rel="icon" type="image/x-icon" href="https://cdn.discordapp.com/attachments/1092022074781990944/1104423324710359070/New_Project_40_1.png")}}">
    <style>

    .topnav {
      background-color: #0e1525;
      background-image: linear-gradient(#151F37,#0F1626);
      overflow: hidden;
    }

    .topnav a {
      float: left;
      color: #f2f2f2;
      text-align: center;
      text-decoration: none;
      font-size: 17px;
      font-weight: bold;
    }
    .topnav a.normal {
      padding: 14px 16px;
    }
    .topnav a.active {
      text-align: center;
      background-color: #04AA6D;
      background-image: linear-gradient(#00EA94, #00603D);
      padding: 6px 10px;
      color: white;
      border-radius: 25px;
    }
    .topnav-left {
      padding: 8px 16px;
      float: left;
    }
    h1 {
      font-weight: bold;
    }
    h2 {
      color: #202434;
    }
    </style>
    </head>
    <body style="background-color:#151F37;color:white;">
    <div class="topnav">
      <a class="normal" href="https://coinbotupdates.ourdiscordreplbot.repl.co/"><img src="https://cdn.discordapp.com/attachments/1092022074781990944/1104682809941037096/New_Project_42.png" width="26px" height="26px" id=logo alt="Logo image"/> </a>
      <div class="topnav-left">
      <a class="active" href="https://coinbotupdates.ourdiscordreplbot.repl.co/"><b>&lt;Go To Update Logs</b></a>
      </div>
    </div>
    <center><h2 style="font-size:100px:">.</h2></center>


    <center><h1 style="font-size:100px;"><u>CoinBot Status</u></h1></center>
    <center><h1 style="font-size:80px;">'''+text+'''</h1></center>
    </body>
    </html>'''

  t = Thread(target=run)
  t.start()
