import sys
import os
import ctypes
import gc
import asyncio
import threading
from telegram import Bot
import discord
from datetime import datetime
import psutil
from dotenv import load_dotenv

load_dotenv()
__version__ = "1.3.1"

# Telegram
bot_token = os.getenv("TELEGRAM_TOKEN")
group_id = os.getenv("TELEGRAM_GROUP_ID")

users = ["trickymf", "tommy_nalichkareal"]

channel_ids = {
	#"honey":1376526834774052966, # honey shop
	#"weather":1387356915796938846,
	#"egg":1387356895957745714,
	#"stock":1387356877826031736, # regular stocks (gear/seed)
	#"summer":1387356978921214022, # summer event stock
	#"cosmetics":None
    "gag-stock":1384416057162203156
}

bot = Bot(token=bot_token)

# Discord
discord_token = os.getenv("DISCORD_TOKEN")


class memory_controller():
	def trim_memory(self):
		libc = ctypes.CDLL("libc.so.6")
		return libc.malloc_trim(0)

	async def execute_trim(self):
		loop = asyncio.get_event_loop()
		await loop.run_in_executor(None, self.trim_memory)

	async def get_ram(self):
		ram = await asyncio.get_event_loop().run_in_executor(None, lambda: psutil.Process().memory_info().rss / 1024**2)
		return ram
	
	async def ram_cleaner(self):
		while True:
			await asyncio.sleep(900)
			# Clear unused vars and return reserved memory to linux.
			gc.collect()
			await self.execute_trim()
			
			await log(f"RAM: {await self.get_ram():.2f}Mb")
			await log(f"Active threads: {threading.active_count()}")

class discord_client(discord.Client):
	def __init__(self):
		super().__init__(
			max_messages=5,
			chunk_guilds_at_startup=False,
			member_cache_flags=discord.MemberCacheFlags.none()
		)
	
	prefs = {
		"event_bans":[
			"Rain",
			"Frost",
			"Windy"
		],
		"all_events":[
			"Rain",
			"Frost",
			"Windy",
			"Thunder",
			"Tornado",
			"Heatwave",
			"Night",
			"Blood",
			"Meteor",
			"Disco",
			"Jandelstorm",
			"Blackhole",
			"Volcano",
			"Chocolate",
			"Aurora"
		],
		"SEEDS":"\U0001F331", # \U0001F331 => 🌱
		"Carrot":"",
		"Strawberry":"",
		"Daffodil":"",
		"Apple":"",
		"Tomato":"",
		"Cauliflower":"",
		"Orange Tulip":"",
		"Blueberry":"",
		"Pumpkin":"",
		"Watermelon":"",
		"Rafflesia":"",
		"Green Apple":"",
		"Avocado":"",
		"Banana":"",
		"Pineapple":"",
		"Kiwi":"",
		"Bell Pepper":"",
		"Prickly Pear":"",
		"Feijoa":"\u2757",
		"Loquat":"\u2757",
		"Bamboo":"",
		"Corn":"",
		"Coconut":"",
		"Cactus":"",
		"Dragon Fruit":"",
		"Mango":"\u2757", # \u2757 => ❗
		"Grape":"",
		"Mushroom":"\u2757",
		"Pepper":"\u2757",
		"Cacao":"\u2757",
		"Beanstalk":"\u2757",
		"Ember Lily":"\u2757",
		"Pitcher Plant":"\u2757",
		"Sugar Apple":"\u2757",	
        "Burning Bud":"\u2757",
        "Giant Pinecone":"\u2757",
		
		"GEAR":"\U0001F6E0", # \U0001F6E0 => 🛠
		"Trowel":"",
        #"Lightning Rod":"\u2757",
		"Watering Can":"",
		"Recall Wrench":"",
		"Basic Sprinkler":"",
		"Advanced Sprinkler":"",
        "Medium Toy":"\u2757",
        "Medium Treat":"\u2757",
		"Godly Sprinkler":"\u2757",
        "Magnifying Glass":"",
		"Tanning Mirror":"\u2757",
		"Master Sprinkler":"\u2757",
        "Cleaning Spray":"",
		"Favorite Tool":"",
		"Harvest Tool":"",
		"Friendship Pot":"\u2757",
        "Levelup Lollipop":"\u2757",
	
		"EGG":"\U0001F95A", # \U0001F95A => 🥚
		"Common Egg":"",
		"Common Summer Egg":"",
		"Uncommon Egg":"",
		"Rare Egg":"",
		"Rare Summer Egg":"\u2757",
		"Legendary Egg":"\u2757",
		"Mythical Egg":"\u2757",
		"Paradise Egg":"\u2757",
		"Bee Egg":"\u2757",
		"Bug Egg":"\u2757",
		
		# Bizzy bee event
		#"HONEY":"\U0001F36F", # \U0001F36F => honey pot emoji
		#"Flower Seed Pack":"\u2757",
		#"Honey Sprinkler":"\u2757",
		#"Bee Crate":"",
		#"Bee Egg":"\u2757",
		#"Nectarine":"\u2757",
		#"Hive Fruit":"\u2757",
		#"Honeysuckle":"\u2757",
		#"Lumira":"\u2757",
		#"Dandelion":"\u2757",
		#"Nectarshade":"\u2757",
		#"Manuka Flower":"\u2757",
		#"Lavender":"",
		#"Pollen Radar":"\u2757",
		#"Honey Comb":"",
		#"Nectar Staff":"\u2757",
		#"Honey Torch":"",
		#"Bee Chair":"",
		#"Honey Walkway":""

		# Summer harvest event
		#"EVENT":"\U00002600", # \U00002600 => ☀️
		#"Summer Seed Pack":"\u2757",
		#"Delphinium":"",
		#"Lily of the Valley":"\u2757",
		#"Traveler's Fruit":"\u2757",
		#"Mutation Spray Burnt":"",
		#"Oasis Crate":"",
		#"Oasis Egg":"\u2757",
		#"Hamster":"\u2757"
		
		# Zen event
		"EVENT":"\U0000262F", # \U0000262F => ☯
		"Zen Seed Pack":"\u2757",
		"Zen Egg":"\u2757",
		"Hot Spring":"",
		"Zen Sand":"",
		"Tranquil Radar":"",
		"Zenflare":"",
		"Zen Crate":"",
		"Soft Sunshine":"",
		"Koi":"\u2757",
		"Zen Gnome Crate":"",
		"Spiked Mango":"\u2757",
		"Pet Shard Tranquil":"\u2757"

		#"COSMETICS":"\U00002728" # \U00002728 => ✨
	}
	
	async def on_ready(self):
		await log(f"on_ready(): started. v{__version__}")
		controller = memory_controller()
		self.loop.create_task(controller.ram_cleaner())
	
	async def report(self, message):
		channel = self.get_channel(1386397564282339398)
		await channel.send(message)
	
	async def on_message(self, message):
		if isinstance(message.channel, discord.DMChannel):
			if message.author.name == "trickymf":
				await change_prefs(message.content)
		
		if message.author.name == "Sapphire":
			return
		
		if message.channel.id in channel_ids.values():
			content = await parse_message(message)
			if content != "":
				for user in users:
					content += f"@{user} "

				await log("on_message(): calling telegram_send()")
				await telegram_send(content)

discord_bot = discord_client()

async def change_prefs(text):
	if (len(text.split()) < 3) or (text.lower() in channel_ids):
		await discord_send(f"Syntax for stocks: weather/stock <name> <on/off>\nSyntax for channel settings: channel <name> <id>")
		return
	
	prefix = text.split()[0].lower()
	
	if prefix == "weather":
		event_bans = discord_client.prefs["event_bans"]
		all_events = discord_client.prefs["all_events"]
		action = text.split()[-1]
		event_input = " ".join(text.split()[1:-1])

		valid = False
		for event in all_events:
			if event.lower() == event_input.lower():
				valid = True
				break
		
		if not valid:
			await discord_send(f"{event_input} is not valid.\nAll event names: {all_events}")
			return

		if action.lower() == "on":
			found = False
			for event in event_bans:
				if event.lower() == event_input.lower():
					event_bans.remove(event)
					found = True
					await discord_send(f"{event} -> on")
					return
			if not found:
				await discord_send(f"{event_input.lower()} is already enabled.")

		elif action.lower() == "off":
			for event in all_events:
				if event.lower() == event_input.lower():
					for ban in event_bans:
						if ban.lower() == event_input.lower():
							await discord_send(f"{ban} is already disabled.")
							return
					
					event_bans.append(event)
					await discord_send(f"{event} -> off.")
					return
		else:
			await discord_send(f"{action} has to be on/off.")
			return
	
	elif prefix == "stock":
		action = text.split()[-1]
		item_input = " ".join(text.split()[1:-1])
		prefs = discord_client.prefs

		for key in prefs:
			if key.lower() == item_input.lower():
				if action.lower() == "off":
					if prefs[key] == "":
						await discord_send(f"{key} is already disabled.")
						return
					
					prefs[key] = ""
					await discord_send(f"{key} -> off")
					return
				elif action.lower() == "on":
					if prefs[key] == "\u2757":
						await discord_send(f"{key} is already enabled.")
						return
					
					prefs[key] = "\u2757"
					await discord_send(f"{key} -> on")
					return
				else:
					await discord_send(f"{action} has to be on/off")
					return
		
		exclude = ["event_bans", "all_events", "SEEDS", "GEAR", "EGG"]
		await discord_send(f"{item_input} is invalid.\nItems: {[x for x in prefs if x not in exclude]}")
	
	elif prefix == "channel":
		id = text.split()[-1]
		name_input = " ".join(text.split()[1:-1]).lower()

		if name_input in channel_ids:
			await discord_send(f"Changing from {channel_ids[name_input]} to {id}")
			channel_ids[name_input] = id
		else:
			await discord_send(f"{name_input} is not valid. Options: {[x for x in channel_ids]}")
	else:
		await discord_send(f"Syntax for stocks: weather/stock <name> <on/off>\nSyntax for channel settings: channel <name> <id>")

async def parse_message(message):
	prefs = discord_client.prefs
	event_bans = prefs["event_bans"]
	text = ""

	if not message.embeds:
		text += message.content + "\n"
	else:
		for embed in message.embeds:
			if embed.description:
				lines = embed.description.split("\n")
				event = lines[0]
				duration = lines[2]
				is_worthy = True
				for ban in event_bans:
					if ban in event:
						is_worthy = False
				if is_worthy:
					text += event + "\n" + duration + "\n"
			
			if embed.fields:
				for field in embed.fields:
					type = field.name.strip("*").split()[0]
					items = {}
					is_worthy = False

					for line in field.value.split("\n"):
						# Detects if there is an emoji being used and removes it if needed.
						if "<:" in line:
							name = " ".join(line.split()[1:-1])
						else:
							name = " ".join(line.split()[:-1])
						
						amount = line.split()[-1]
						# Check if the item is wanted by the user.
						if prefs[name] != "":
							is_worthy = True
							items[name] = amount
					
					if is_worthy:
						text += f"{prefs[type]} **{type} STOCK** {prefs[type]}" + "\n"
					
					for item in items:
						if prefs[item] != "":
							text += f"• {prefs[item]}{item} — {items[item]}" + "\n"
	return text

async def get_time():
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

async def log(entry, level=0):
	time = await get_time()
	severity = {0:"info", 1:"error", 2:"debug"}
	log_entry = f"[{severity[level]}] {time}: {entry}\n"
	
	await asyncio.to_thread(sys.stdout.write, log_entry)

async def discord_send(message):
	try:
		await discord_bot.report(message)
		await log("discord_send(): sent")
	except Exception as e:
		await log(f"discord_send(): {e}", 1)

async def telegram_send(text):
	try:
		# Send the following characters raw without triggering markdown to prevent errors.
		reserved_chars = ["_", "[", "]", "(", ")", "~", "`", ">", "#", "+", "-", "=", "|", "{", "}", ".", "!"]
		for char in reserved_chars:
			text = text.replace(char, f"\\{char}")
		await bot.send_message(chat_id=group_id, text=text, parse_mode="MarkdownV2")
		await log("telegram_send(): sent")
	except Exception as e:
		await log(f"telegram_send(): {e}", 1)

async def main():
	loop = asyncio.get_event_loop()
	await loop.create_task(discord_bot.start(discord_token))

if __name__ == "__main__":
	asyncio.run(main())
