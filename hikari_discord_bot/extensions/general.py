import hikari
import lightbulb

plugin = lightbulb.Plugin("GeneralCommands")




@plugin.command()
@lightbulb.command("ping", "You get a pong")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context):
    await ctx.respond("Pong!")


@plugin.command()
@lightbulb.command("avatar", "See your beautiful avatar")
@lightbulb.implements(lightbulb.SlashCommand)
async def avatar(ctx: lightbulb.Context):
    profile = hikari.Embed().set_image(ctx.author.avatar_url.url)
    await ctx.respond(profile)



def load(bot: lightbulb.BotApp): 
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)