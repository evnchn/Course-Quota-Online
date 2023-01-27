## RUN THIS WITH PYCORD ONLY!!! USE PIPENV!!!
import traceback
import discord
from dotenv import load_dotenv
import os
TOKEN_2 = os.getenv('DISCORD_TOKEN_2')
GUILD_ID = int(os.getenv('DISCORD_GUILD_ID'))
print(type(GUILD_ID))
print(GUILD_ID)
bot = discord.Bot()

async def list_search(ctx: discord.AutocompleteContext):
    """Return's A List Of Autocomplete Results"""
    return sorted([i for i in list(set((_.name.split("-")[0].upper() for _ in discord.utils.get(bot.guilds, id=GUILD_ID).roles))) if i.startswith(ctx.value.upper())])
    
@bot.command(description="Tests Asuna's reaction speed") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Reaction speed is {str(bot.latency*1000)[:3]}ms. \nSlower than Kirito, but faster than you!", ephemeral=True)
    
    
@bot.command(description="Add role for @mention")
# pycord will figure out the types for you
async def add(ctx, subject: discord.Option(str, autocomplete=list_search), alert: discord.Option(str, choices=['traps', 'quotas'])):
    # you can use them as they were actual integers
    subject = subject.upper()
    role = subject+"-"+alert
    print(role)
    try:
        assert len(subject) == 4
        if role not in [_.name for _ in ctx.author.roles]:
            await ctx.author.add_roles(discord.utils.get(discord.utils.get(bot.guilds, id=GUILD_ID).roles , name=role))
            await ctx.respond(f"Added role {role}", ephemeral=True)
        else:
            await ctx.respond(f"Already have role {role}", ephemeral=True)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        await ctx.respond(f"Failed to find role {role}", ephemeral=True)
        
@bot.command(description="Remove role from @mention")
# pycord will figure out the types for you
async def remove(ctx, subject: discord.Option(str), alert: discord.Option(str, choices=['-traps', '-quotas'])):
    # you can use them as they were actual integers
    subject = subject.upper()
    role = subject+alert
    print(role)
    try:
        assert len(subject) == 4
        if role in [_.name for _ in ctx.author.roles]:
            await ctx.author.remove_roles(discord.utils.get(discord.utils.get(bot.guilds, id=GUILD_ID).roles , name=role))
            await ctx.respond(f"Removed role {role}", ephemeral=True)
        else:
            await ctx.respond(f"Already removed role {role}", ephemeral=True)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        await ctx.respond(f"Failed to find role {role}", ephemeral=True)
    
@bot.event
async def on_ready():
    game = discord.CustomActivity("/add /remove or /ping")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/add or /remove"))

bot.run(TOKEN_2)