import os
import random
import discord
import praw
from discord.ext import commands

reddit = praw.Reddit(client_id="id",
                     client_secret="secret",
                     username="username",
                     password="password",
                     user_agent="pythonpraw")

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.command()
async def d2(ctx):
    subreddit = reddit.subreddit("DestinyMemes")
    all_subs = []

    hot = subreddit.hot(limit=100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    emb = discord.Embed(title=name)

    emb.set_image(url=url)

    message = await ctx.send(embed=emb)
    await message.add_reaction("👍")
    await message.add_reaction("👎")

@bot.command()
async def food(ctx):
    subreddit = reddit.subreddit("food")
    all_subs = []

    hot = subreddit.hot(limit=100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    emb = discord.Embed(title=name)

    emb.set_image(url=url)

    message = await ctx.send(embed=emb)
    await message.add_reaction("😋")

@bot.command()
async def phasmo(ctx):
    subreddit = reddit.subreddit("PhasmophobiaGame")
    all_subs = []

    hot = subreddit.hot(limit=100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    emb = discord.Embed(title=name)

    emb.set_image(url=url)

    await ctx.send(embed=emb)

@bot.command()
async def commands(ctx):
    embed = discord.Embed(
        title='All the Commands:',
        description='Prefix is ;',
        colour=discord.Colour.blue())

    embed.set_footer(text='Enjoy!')
    embed.set_author(name='I just hooked you up!',
                     icon_url='https://media.discordapp.net/attachments/862411748074455050/862411771846590484/image0.png')
    embed.add_field(name='d2', value='Destiny Memes', inline=False)
    embed.add_field(name='food', value='Food', inline=False)
    embed.add_field(name='phasmo', value='Phasmophobia Memes', inline=False)
    await ctx.send(embed=embed)

bot.run("bot_token")
