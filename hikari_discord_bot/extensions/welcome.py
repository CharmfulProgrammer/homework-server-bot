import lightbulb
import hikari

plugin = lightbulb.Plugin("WelcomePlugin")


@plugin.listener(hikari.events.MemberCreateEvent)
async def welcome(event: hikari.events.MemberCreateEvent):
    # will plan something
    pass


def load(bot: lightbulb.BotApp): 
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)