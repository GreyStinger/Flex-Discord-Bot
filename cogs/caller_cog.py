from discord.ext import commands
from configs import STATIC_NAMES, PREFIX


class Caller(commands.Cog):
    def __init__(self, bot, embed_manager):
        self.bot = bot
        self.embed_dict = embed_manager.embed_dict

    # Create Command Call For All Static Items In Embed Config
    @commands.command(aliases=STATIC_NAMES)
    async def caller_(self, ctx):
        await ctx.send(embed=self.embed_dict[ctx.message.content[len(PREFIX):].split(' ')[0].capitalize()])
