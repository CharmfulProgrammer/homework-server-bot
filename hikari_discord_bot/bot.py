import lightbulb
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.environ.get("TOKEN")
    bot = lightbulb.BotApp(token=TOKEN)
    bot.load_extensions_from("extensions")
    bot.run()