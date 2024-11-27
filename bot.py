# Imports
import discord
from discord.utils import get
import os
import dbm
import re

# Declare shorthands
intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

# Global vars
global userid_regex
global emoji
global channels

# Global Constants
global TOKEN

# Declare Inital Variables
channels = open("ChannelID.cfg", 'r').read().split(', ')
userid_regex = re.compile('<@[0-9]*>')
emoji = '\N{THUMBS UP SIGN}'

# Declare Constant Values
TOKEN = open("Token.cfg", 'r').read()

# Functions
async def getid(idnum: int):
	user = await bot.fetch_user(idnum)
	return(user.name)

async def getmention(idnum: int):
	user = await bot.fetch_user(idnum)
	try:
		if user.nick:
			return(user.nick)
	except AttributeError:
		return(user.name)

async def get_sorted_leaderboard():
	leaderboard_dict = {}
	with dbm.open('quote_leaderboard', 'c') as db:
		for i in db.keys():
			leaderboard_dict[str(i)] = int(db.get(i))
	sorted_list = sorted(leaderboard_dict.items(), key=lambda x:x[1], reverse=True)
	return(dict(sorted_list))

async def get_formatted_leaderboard():
	return_string = ""
	in_leaderboard = await get_sorted_leaderboard()
	for i in in_leaderboard:
		j = i[2:-1]
		return_person_mention = await getmention(j)
		return_person = f'{return_person_mention}: {str(in_leaderboard[i])}'
		return_string += f'{return_person}\n'
	return(f'{return_string}')

def update_leaderboard(mention_list):
	with dbm.open('quote_leaderboard', 'c') as db:
		for i in mention_list:
			if not (f'{i.id}' in db):
				db[f'{i.id}'] = "0"
			db[f'{i.id}'] = str(int(db[f'{i.id}']) + 1)

# Events
@bot.event
async def on_ready():
	print(f"{bot.user} is ready and online!")
@bot.event
async def on_message(message):
	for i in range(len(channels)-1):
		channel = channels[i]
		if message.channel.id == channel:
			if message.author.id != bot.application_id:
				if userid_regex.search(message.content):
					print(f'{message.author.name} ({message.author.id}) quoted: \"{message.content}\"')
					update_leaderboard(message.mentions)
					await message.add_reaction(emoji)
#				await message.channel.send("**Quoted!** New totals:\n" + await get_formatted_leaderboard(), reference=message, silent=True, delete_after=5)
#			else:
#				to_delete_message = await message.channel.send("You didn't mention anyone. If this is a quote, please delete your message and send it again with the person's name mentioned. (This message will delete itself.)", reference=message, delete_after=15)	

# Slash commands
@bot.command(name="formatting-help", description="Show optimal formatting for quotes.")
async def showformatting(ctx):
	await ctx.respond("The only requirement for quotes in this channel is that the person/people being quoted are mentioned in the message. However, *optimal* formatting is as follows:\n\> Quote\n\\\- \@user\n\nThe greater than symbol formats the quotation as a Block Quote, and the backslash prevents Discord from formatting your attribution as a Bulleted List (•).", ephemeral=True)

@bot.command(name="set-count", description="Manually set a member's quote count.")
async def setcount(ctx, name: discord.Option(discord.Member), total: discord.Option(int)):
	with dbm.open('quote_leaderboard', 'c') as db:
		db[f'{name.id}'] = str(total)
		if int(db[f'{name.id}']) == total:
			await ctx.respond(f'Member {name.mention} has been updated to {total} quotes!', ephemeral=True)

@bot.command(name="get-leaderboard", description="Get the current leaderboard.")
async def getleaderboard(ctx):
	await ctx.respond("Leaderboard:\n" + await get_formatted_leaderboard(), ephemeral=True)

@bot.command(name="show-leaderboard", description="Get the current leaderboard.")
async def getleaderboard2(ctx):
	await ctx.respond("Leaderboard:\n" + await get_formatted_leaderboard(), ephemeral=True)

# Deferred run
bot.run(TOKEN)