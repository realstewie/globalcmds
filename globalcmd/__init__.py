from .globalcmds import GlobalCommands

async def setup(bot):
    await bot.add_cog(GlobalCommands(bot))
