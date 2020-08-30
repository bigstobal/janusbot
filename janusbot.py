import os
import discord
from discord.ext import commands

janus = commands.Bot(command_prefix='!')

@janus.event
async def on_ready():
    print("janusbot is ready")

# Updating PaperMC

@janus.command()
async def paper(ctx, ver, tag):
    await ctx.send("Updating Paper...")
    os.system("curl -o /home/minecraft/bigjanus/server.jar https://papermc.io/api/v1/paper/" + ver + "/" + tag + "/download")
    await ctx.send("**Done.** Updated Paper to build `" + tag + "` for version `" + ver + "`.")

@paper.error
async def paper_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("**Usage:** `!paper [Minecraft version] [Paper build number]`\n**Example:** `!paper 1.16.2 163`")

# Starting the minecraft server

@janus.command()
async def start(ctx):
    await ctx.send("Starting the Bigjanus Minecraft server...")
    os.system("screen -S bigjanus -d -m java -Xms3291M -Xmx3291M -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar /home/minecraft/bigjanus/server.jar nogui")
    await ctx.send("**Done.** Server will be ready in 60s.")

# Get januswiki link

def fix_url(argument):
    return argument.replace(" ", "_")

@janus.command()
async def januswiki(ctx, *, content: fix_url):
    await ctx.send("https://bigjanus.ga/wiki/" + content)

@januswiki.error
async def januswiki_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("**Usage:** `!januswiki [title of januswiki article]`\n**Example:** `!januswiki chicken nugget`")

janus.run("TOKEN")
