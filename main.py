import os
from typing import Any
from keep_alive import keep_alive

keep_alive()

import discord
from discord.ext import commands

from cogs import COMMANDS, EVENT_HANDLERS
from bot_utilities.config_loader import config

class AIBot(commands.AutoShardedBot):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        if config['AUTO_SHARDING']:
            super().__init__(*args, **kwargs)
        else:
            super().__init__(shard_count=1, *args, **kwargs)

    async def setup_hook(self) -> None:
        for cog in COMMANDS:
            cog_name = cog.split('.')[-1]
            discord.client._log.info(f"Loaded Command {cog_name}")
            await self.load_extension(f"{cog}")
        for cog in EVENT_HANDLERS:
            cog_name = cog.split('.')[-1]
            discord.client._log.info(f"Loaded Event Handler {cog_name}")
            await self.load_extension(f"{cog}")
        print('If syncing commands is taking longer than usual you are being ratelimited')
        await self.tree.sync()
        discord.client._log.info(f"Loaded {len(self.commands)} commands")

bot = AIBot(command_prefix=[], intents=discord.Intents.all(), help_command=None)

bot.run('MTIzMjU5ODYxNTU3OTY4ODk3MA.GnKPc5.fvdt_IVxaUPubg5uaFE7LvqW9BZg5Qx5nBhZd4')
