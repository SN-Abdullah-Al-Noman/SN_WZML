# (c) @LCUBOTS

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", ""))
	API_HASH = os.environ.get("API_HASH", "")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "")) #id starts with -100
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "")) #Id
	DATABASE_URL = os.environ.get("DATABASE_URL", "")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "") #username without @
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "") #id starts with -100
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
**🔅 Cloud Store Bot 🔅**

🔸🤖 **My Name: [US Cloud Store Bot](https://telegram.me/{BOT_USERNAME}) **

🔹📝 **Language: [Pʏᴛʜᴏɴ](https://www.python.org) **

🔸📚 **Library: [Pʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org) **

🔹📡 **Hosted On: VPS **

🔸 🚩**Version : 1.0 [Stable] **

🔹👨‍💻 **Developer: [Logesh](https://telegram.me/) **

**🔅  Urlshorten.in  🔅**
"""
	ABOUT_DEV_TEXT = f"""
**🌐 My Father is [ LOGESH ](https://telegram.me/) **  

Powered by @urlshortenlink
"""	
	HELP_TEXT = """**How to Connect Your api with Bot :**

**Step 1 :** Just click **Get api 🔗** button and copy your Api Token from Website.

**Step 2 :** Then come again here and use **/api** to connect your api with bot.

**Example :** `/api 5d9603650f2b1fd15f543acb1fb0a0764403ba5c`"""
	
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\n I am site.in Telegram Cloud Storage Bot.

**What i can store,**

1. Files : Supported upto 4GB.
2. Videos : Supported upto 4GB.
3. Post 
4. Image with captions

**Note : Please connect with api first.**

**Example :** `/api 5d9603650f2b1fd15f543acb1fb0a0764403ba5c` 
"""
