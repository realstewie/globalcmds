from discord.ext import commands
from discord import app_commands

class GlobalCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        """Ensure commands can be used in any server."""
        return True

    async def is_user_authorized(self, user):
        """Check if the user has the specific role in any server."""
        for guild in self.bot.guilds:
            member = guild.get_member(user.id)
            if member and any(role.id == 1246885462011023400 for role in member.roles):
                return True
        return False

    @app_commands.command(name="globalban", description="Globally ban a user from all servers.")
    async def globalban(self, interaction: app_commands.Interaction, user: str, *, reason: str = "No reason provided"):
        if not await self.is_user_authorized(interaction.user):
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
            return

        # Implement the global ban functionality
        await interaction.response.send_message(f"User `{user}` has been globally banned for: `{reason}`")

    @app_commands.command(name="globalunban", description="Globally unban a user from all servers.")
    async def globalunban(self, interaction: app_commands.Interaction, user: str):
        if not await self.is_user_authorized(interaction.user):
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
            return

        # Implement the global unban functionality
        await interaction.response.send_message(f"User `{user}` has been globally unbanned.")

    @app_commands.command(name="globalkick", description="Globally kick a user from all servers.")
    async def globalkick(self, interaction: app_commands.Interaction, user: str, *, reason: str = "No reason provided"):
        if not await self.is_user_authorized(interaction.user):
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
            return

        # Implement the global kick functionality
        await interaction.response.send_message(f"User `{user}` has been globally kicked for: `{reason}`")

async def setup(bot):
    await bot.add_cog(GlobalCommands(bot))
