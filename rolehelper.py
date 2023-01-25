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

@bot.command()
# pycord will figure out the types for you
async def add(ctx, subject: discord.Option(str), alert: discord.Option(str, choices=['-traps', '-quotas'])):
    # you can use them as they were actual integers
    subject = subject.upper()
    role = subject+alert
    print(role)
    try:
        assert len(subject) == 4
        await ctx.author.add_roles(discord.utils.get(discord.utils.get(bot.guilds, id=GUILD_ID).roles , name=role))
        await ctx.respond(f"Added role {role}")
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        await ctx.respond(f"Failed to find role {role}")
        
@bot.command()
# pycord will figure out the types for you
async def remove(ctx, subject: discord.Option(str), alert: discord.Option(str, choices=['-traps', '-quotas'])):
    # you can use them as they were actual integers
    subject = subject.upper()
    role = subject+alert
    print(role)
    try:
        assert len(subject) == 4
        await ctx.author.remove_roles(discord.utils.get(discord.utils.get(bot.guilds, id=GUILD_ID).roles , name=role))
        await ctx.respond(f"Removed role {role}")
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        await ctx.respond(f"Failed to find role {role}")
    
@bot.event
async def on_ready():
    game = discord.CustomActivity("/add or /remove")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/add or /remove"))

bot.run(TOKEN_2)