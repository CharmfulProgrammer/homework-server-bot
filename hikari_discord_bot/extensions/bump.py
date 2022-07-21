import lightbulb
import hikari

plugin = lightbulb.Plugin("TrackBumpPlugin")

@plugin.listener(hikari.events.GuildMessageCreateEvent)
async def track_bump(event: hikari.events.GuildMessageCreateEvent):
    if str(event.channel_id) != "757114175381176362" and event.author_id != "302050872383242240":
        return

    bump_image = "https://disboard.org/images/bot-command-image-bump.png"

    try:
        # implement a database and scoreboard in futute
        if event.embeds[0].image.url == bump_image:
            pass
    except AttributeError:
        pass

def load(bot: lightbulb.BotApp): 
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)