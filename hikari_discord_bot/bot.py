import lightbulb
import hikari
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.environ.get("TOKEN")
    intents = (hikari.Intents.GUILD_MEMBERS | hikari.Intents.GUILD_MESSAGES)
    bot = lightbulb.BotApp(token=TOKEN, intents=intents)
    bot.load_extensions_from("extensions")
    bot.run()