import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7807552195:AAGzBSvBoN8HNSLUy5QRX5yT6bJWUyKDAiM")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23572045"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6bf81dff6563e3f1fb3c7d23a6872291")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7577853954"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sumitsajwan135:gameno01@cluster0.ja0i0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
