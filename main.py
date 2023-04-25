# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>>', intents=intents)

@bot.event
async def on_ready():
    print("Ready")

#Hello
@bot.command()
async def good(ctx):
    await ctx.send("Hello")

# 利用規則
ID_CHANNEL_README=1099917400704548894
ID_ROLE_GOOD=1099914039162847232
@bot.event
async def on_raw_reaction_add(payload):
  channel=bot.get_channel(payload.channel_id)
  if channel.id != ID_CHANNEL_README:
      return
  guild = bot.get_guild(payload.guild_id)
  member = await guild.fetch_member(payload.user_id)
  role = guild.get_role(ID_ROLE_GOOD)
  await member.add_roles(role)

bot.run(os.environ["DISCORD_TOKEN"])
