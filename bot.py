# Don't Remove Credit Tg - @Whosekirito
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @Whosekirito

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

class Bot(Client):

    def __init__(self):
        super().__init__(
            "techvj login",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="TechVJ"),
            workers=200,
            sleep_threshold=5
        )


    async def start(self):

        await super().start()
        print('Bot Started Powered By @Whosekirito')

    async def stop(self, *args):

        await super().stop()
        print('Bot Stopped Bye')

Bot().run()

# Don't Remove Credit Tg - @Whosekirito
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @Whosekirito