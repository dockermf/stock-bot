# Description
Gets stock from [this](https://discord.gg/giftcard) discord server, then parses the contents, formats and re-sends it to your telegram group.

This is my first personal project I've been working on to learn new stuff, so I don't expect it to work flawlessly on your machine, since there are possible bugs I might not be aware of.
# Dependencies
## OS
Linux
## Libraries used
Listed in [requirements.txt](requirements.txt)
## Required python version
\>= 3.8
<= 3.11
# Setup
It was designed to be deployed via a hosting service, but you can host it on your machine too, either using docker or running it via python.
## For python follow the next steps:
### 1. Download
Run in your terminal:
```bash
git clone https://github.com/dockermf/stock-bot.git
```
Or just install zip archive and unzip it where you like.

After that, open the directory where you downloaded this and cd into stock-bot directory.
### 2. Install all required libraries
Run in your terminal:
```bash
$ pip install -r requirements.txt
```
Or, if you like, you can install them manually.
### 3. Prepare bots/group
Create a .env file, then copy/paste a template provided in [.env.example](.env.example) file. Those are gonna be used by the code.

*Discord*:
For all this to work, you'll have to get a real discord account's token (might be your alt, since it's against discord's ToS to self-bot). To get it, watch a youtube tutorial or ask an AI.
After you got the token, paste it into .env file.

*Telegram*:
First of all, create your bot and get it's token. Ask an AI if you don't know how.
After that, create a group in which you have to add your bot and then make sure the bot has all permissions required for sending messages. Then, get the group's chat id, and paste it into your .env file. You can now turn group's notifications off.

*IMPORTANT*
Change users variable in [main.py](main.py) file to include your group's member usernames, as the bot uses it to ping you whenever something good is on stock. Will be fixed later.
### 4. Start the bot
Run in your terminal:
```bash
$ python3 main.py
```
***Note: if you close your terminal, the bot will stop working as it's tied to the terminal session it was started in.***
## For docker:
### 1. Download (the same as above).
### 2. Build:
```bash
$ docker build -t <your container name> .
```
### 3. Run:
```bash
$ sudo docker run -e TELEGRAM_TOKEN=<YOUR_TOKEN> -e TELEGRAM_GROUP_ID=<YOUR_GROUP_ID> -e DISCORD_TOKEN=<YOUR_DISCORD_TOKEN> <your container>
```
