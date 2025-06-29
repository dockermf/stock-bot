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


__version__ = "1.0.0"

# Telegram
<<<<<<< HEAD
bot_token = "***REMOVED***"

users = ["trickymf", "tommy_nalichkareal"]
group_id = ***REMOVED***
=======
bot_token = os.getenv("TELEGRAM_TOKEN")
group_id = os.getenv("TELEGRAM_GROUP_ID")

users = ["trickymf", "tommy_nalichkareal"]
>>>>>>> 2559992 (Import os)

channel_ids = {
	#"honey":1376526834774052966, # honey
	"weather":1387356915796938846, # weather
	"egg":1387356895957745714, # egg
	"stock":1387356877826031736, # stocks
	"summer":1387356978921214022, # summer stock
	"cosmetics":None
}

bot = Bot(token=bot_token)

# Discord
discord_token = "***REMOVED***"


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
			"Snow",
			"Windy"
		],
		
		"all_events":[
			"Rain",
			"Snow",
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
			"Chocolate"
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
		"Green Apple":"\u2757",
		"Avocado":"\u2757",
		"Banana":"\u2757",
		"Pineapple":"\u2757",
		"Kiwi":"\u2757",
		"Bell Pepper":"\u2757",
		"Prickly Pear":"\u2757",
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
		"Sugar Apple":"\u2757",
	
		"GEAR":"\U0001F6E0", # \U0001F6E0 => 🛠
		"Trowel":"",
		"Watering Can":"",
		"Basic Sprinkler":"",
		"Advanced Sprinkler":"",
		"Godly Sprinkler":"\u2757",
		"Master Sprinkler":"\u2757",
		"Tanning Mirror":"\u2757",
		"Recall Wrench":"",
		"Lightning Rod":"\u2757",
		"Favorite Tool":"",
		"Harvest Tool":"",
		"Friendship Pot":"\u2757",
		"Cleaning Spray":"",
	
		"EGG":"\U0001F95A", # \U0001F95A => 🥚
		"Common Egg":"",
		"Common Summer Egg":"",
		"Uncommon Egg":"",
		"Rare Egg":"",
		"Rare Summer Egg":"\u2757",
		"Legendary Egg":"\u2757",
		"Mythical Egg":"\u2757",
		"Paradise Egg":"\u2757",
		"Bug Egg":"\u2757",
		
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

		# Summer event
		"EVENT":"\U00002600", # \U00002600 => ☀️
		"Summer Seed Pack":"\u2757",
		"Delphinium":"",
		"Lily of the Valley":"\u2757",
		"Traveler's Fruit":"\u2757",
		"Mutation Spray Burnt":"",
		"Oasis Crate":"",
		"Oasis Egg":"\u2757",
		"Hamster":"\u2757"
		
		#"COSMETICS":"\U00002728" # \U00002728 => ✨
	}
	
	def trim_memory(self):
		libc = ctypes.CDLL("libc.so.6")
		return libc.malloc_trim(0)


	async def execute_trim(self):
		loop = asyncio.get_event_loop()
		await loop.run_in_executor(None, self.trim_memory)
	

	async def get_ram(self):
		ram = await asyncio.get_event_loop().run_in_executor(None, lambda: psutil.Process().memory_info().rss / 1024**2)
		return ram
	

	async def clear_discord_caches(self):
		if hasattr(self._connection, "_messages"):
			self._connection._messages.clear()
		if hasattr(self._connection, "_guilds"):
			self._connection._guilds.clear()
	

	async def ram_cleaner(self):
		while True:
			await asyncio.sleep(900)
			# Clear unused vars and return memory to linux.
			await self.clear_discord_caches()
			gc.collect()
			await self.execute_trim()
			
			await log(f"RAM: {await self.get_ram():.2f}Mb")
			await log(f"Active threads: {threading.active_count()}")
	
	
	async def report(self, message):
		channel = self.get_channel(1386397564282339398)
		await channel.send(message)
		
	
	async def on_ready(self):
		await log("on_ready(): started")
		self.loop.create_task(self.ram_cleaner())
	
	
	async def on_message(self, message):
		if message.author.name == "trickymf":
			if isinstance(message.channel, discord.DMChannel):
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
			if embed.title:
				event = embed.title
				is_worthy = True
				
				for ban in event_bans:
					if ban in event:
						is_worthy = False
				
				if is_worthy:
					text += event + "\n"
			
			if embed.fields:
				for field in embed.fields:
					type = field.name.strip("*").split()[0]
					items = {}
					is_worthy = False
					
					for line in field.value.split("\n"):
						amount = line.split()[-1]
						
						if "<:" in line:
							name = " ".join(line.split()[1:-1])
						else:
							name = " ".join(line.split()[:-1])
						
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
	severity = {0:"info", 1:"error"}
	log_entry = f"[{severity[level]}] {time}: {entry}\n"
	
	await asyncio.to_thread(sys.stdout.write, log_entry)


async def discord_send(message):
	try:
		await log("discord_send(): sending")
		await discord_bot.report(message)
		await log("discord_send(): finished")
	
	except Exception as e:
		await log(f"discord_send(): {e}", 1)


async def telegram_send(text):
	try:
		reserved_chars = ["_", "[", "]", "(", ")", "~", "`", ">", "#", "+", "-", "=", "|", "{", "}", ".", "!"]
		for char in reserved_chars:
			text = text.replace(char, f"\\{char}")
		
		await log("telegram_send(): sending")
		await bot.send_message(chat_id=group_id, text=text, parse_mode="MarkdownV2")
		await log("telegram_send(): finished")
	
	except Exception as e:
		await log(f"telegram_send(): {e}", 1)


async def main():
	
	await asyncio.gather(
		discord_bot.start(discord_token)
	)


if __name__ == "__main__":
	asyncio.run(main())