import lightbulb
import hikari
import os
import urllib.parse

plugin = lightbulb.Plugin("WelcomePlugin")

KEY = os.environ.get("SOME_RANDOM_API_KEY")

@plugin.listener(hikari.events.MemberCreateEvent)
async def welcome(event: hikari.events.MemberCreateEvent):
    user = event.user
    guild = await plugin.bot.rest.fetch_guild(756961365200994314)

    data = {"type": "join", "username": user.username, "discriminator": user.discriminator, "guildName": guild.name, "textcolor": "white", "memberCount": guild.approximate_member_count}
    params = urllib.parse.urlencode(data)

    welcome_image = "https://some-random-api.ml/welcome/img/6/night?" + params + "&avatar=" +  (user.avatar_url.url or user.default_avatar_url.url) + "&key=" + KEY

    embed = hikari.Embed()
    embed.set_image(welcome_image)
    await plugin.bot.rest.create_message(757071112206286929, embed=embed)


@lightbulb.add_checks(lightbulb.owner_only)
@plugin.command()
@lightbulb.command("guildid", "the the guild id")
@lightbulb.implements(lightbulb.SlashCommand)
async def guildid(ctx: lightbulb.Context):
    await ctx.respond(ctx.guild_id)


def load(bot: lightbulb.BotApp): 
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)