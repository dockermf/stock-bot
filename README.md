# Description
Gets stock from [this](https://discord.gg/giftcard) discord server, then parses the contents, formats and re-sends it to your telegram group.
# Dependencies
## OS
Linux
## Libraries used
Listed in requirements.txt
## Required python version
\>= 3.8
<= 3.11
# Setup
It was designed to be deployed via a hosting service, but you can host it on your machine too.
## Steps:
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
### 3. Start the bot
Run in your terminal:
```bash
$ python3 main.py
```
***Note: if you close your terminal, the bot will stop working as it's tied to the terminal session it was started in.***
