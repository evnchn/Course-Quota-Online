## RUN THIS WITH PYCORD ONLY!!! USE PIPENV!!!

import discord
from dotenv import load_dotenv
import os
TOKEN_2 = os.getenv('DISCORD_TOKEN_2')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')
print(GUILD_ID)
bot = discord.Bot()

@bot.command()
# pycord will figure out the types for you
async def add(ctx, subject: discord.Option(str), alert: discord.Option(str, choices=['-traps', '-quotas'])):
    # you can use them as they were actual integers
    role = subject+alert
    print(role)
    try:
        await ctx.author.add_roles(discord.utils.get(discord.utils.get(bot.guilds, id=GUILD_ID).roles , name=role))
        await ctx.respond(f"Added role {role}")
    except:
        await ctx.respond(f"Failed to find role {role}")
    #print(role)
    #await ctx.respond(f"The role of {first} and {second} is {role}.")
    
    
    

bot.run(TOKEN_2)