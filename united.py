import random
from datetime import date

def get_united_tweet():
    today = date.today()
    formatted_date = today.strftime("%B %d")

    tweets = [
        f"🔴 United 🔁 training mode: All eyes on the weekend! #MUFC #GloryGloryManUnited",
        f"📅 On this day, {formatted_date} — Ronaldo’s iconic header vs Chelsea (2008). 🏆 #OTD #MUFC",
        f"💬 Ten Hag has plans cooking — tactical shake-up brewing for Old Trafford! 🔁⚽",
        f"🚨 Transfer whispers around United... Something brewing? 👀 #MUFC #Transfers",
        f"🎯 Rashford. Garnacho. Bruno. Who's YOUR player to watch this weekend? #ManUtd",
        f"📸 Scenes from Carrington today. Energy levels: 🔥🔥🔥 #TrainingDay #MUFC",
        f"🔙 Flashback: On this day {formatted_date}, Rooney scored a hat-trick in his debut! 🔥🔥🔥 #Legend",
        f"📣 Matchday loading… United vs Arsenal 🔜. Predictions? #MUFC #Matchday",
        f"🎉 Happy Birthday to United legend Ryan Giggs! 🐐 #MUFCHistory",
        f"📊 United unbeaten at home in the last 10 games. Fortress Old Trafford 🏟️ #RedStats"
    ]

    return random.choice(tweets)
