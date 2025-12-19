import os
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv('config.env')
elif os.path.exists("sample.env"):
    load_dotenv("sample.env")

API_ID = os.getenv("26422668")
API_HASH = os.getenv("13853df234b2fbe18d9027a5985cc69e")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_DB_URI = os.getenv("mongodb+srv://villainravangaming:mikey_kun_781_@cluster0.fbgs1zz.mongodb.net/?retryWrites=true&w=majority")
STATUS_MSG_ID = os.getenv("STATUS_MSG_ID")
SCHEDULE_MSG_ID = os.getenv("SCHEDULE_MSG_ID")
CHANNEL_TITLE = os.getenv("CHANNEL_TITLE", "AnimeDex")
INDEX_CHANNEL_USERNAME = os.getenv("https://t.me/Fx_Anime_Group")
UPLOADS_CHANNEL_USERNAME = os.getenv("https://t.me/Fx_Anime_Group")
TECHZ_API_KEY = os.getenv("TECHZ_API_KEY")
COMMENTS_GROUP_LINK = os.getenv("COMMENTS_GROUP_LINK")
SLEEP_TIME = os.getenv("SLEEP_TIME", 60)

for k, v in {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "MONGO_DB_URI": MONGO_DB_URI,
    "STATUS_MSG_ID": STATUS_MSG_ID,
    "SCHEDULE_MSG_ID": SCHEDULE_MSG_ID,
    "INDEX_CHANNEL_USERNAME": INDEX_CHANNEL_USERNAME,
    "UPLOADS_CHANNEL_USERNAME": UPLOADS_CHANNEL_USERNAME,
    "TECHZ_API_KEY": TECHZ_API_KEY,
    "COMMENTS_GROUP_LINK": COMMENTS_GROUP_LINK,
}.items():
    if not v:
        raise Exception(f"{k} not found .env file, please add it to use AutoAnimeBot")
