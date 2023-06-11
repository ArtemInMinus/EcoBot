import discord, random, os, requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

balls = 0

@bot.command()
async def get(ctx, count_bottles):
    global balls
    balls = balls + int(count_bottles)
    ran = random.randint(1, 2)
    if ran == 1:
        await ctx.send(f"Вы получили {count_bottles} экобалл(-а)(-ов)!")
    if ran == 2:
        await ctx.send(f"Вы получили {count_bottles} экобалл(-а)(-ов), вы большой молодец!")

@bot.command()
async def points(ctx):
    global balls
    await ctx.send(balls)

@bot.command()
async def sort(ctx):
    await ctx.send("Нужно уметь сортировать мусор, обычно это указано на мусорных баках.")

@bot.command()
async def tips(ctx):
    await ctx.send("Выкидывайте пластик и пластиковые бутылки в специальные контейнеры для переработки пластика, пропишите /example чтобы узнать как они выглядят.")

@bot.command()
async def example(ctx):
    ecom = random.choice(os.listdir("images"))
    with open(f"images\{ecom}", 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run(token)
