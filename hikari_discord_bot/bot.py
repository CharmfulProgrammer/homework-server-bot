import lightbulb
import hikari
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.environ.get("TOKEN")
    OWNER_ID = 593537214231609357
    intents = (hikari.Intents.GUILD_MEMBERS | hikari.Intents.GUILD_MESSAGES)
    bot = lightbulb.BotApp(token=TOKEN, intents=intents, owner_ids=[OWNER_ID])
    bot.load_extensions_from("extensions")
    bot.run()