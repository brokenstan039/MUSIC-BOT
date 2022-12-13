import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "1AZWarzwBuwZTbkHcFLip-nqNtQDhUlBtCaxoZLy4HqjpUlfDB8vDql_Up5AomnSuYy9vMPdbO2rkR81eDsICZiNpmtpbHTJFmnNRQnjJiuSq1hGMo2D7NdhhB1uOckRXpPo1NNv6EpH6CImK0CrdIHmlQhJW3gG9_V5Ovj57MrCvCw-nhGxW-3XinH3yCR8M-kSlwIRbmkeLmV3Qh_3QZfAfW0uvBMG0yiDwYLOxvqH1d-e91dODu5Y02F5m2xp1hL50cvyZgY1GxVsNh4nqdACCNzaxEs4JMA0bSuIfhEbIdu9CssJhDL9MzUuvmZLup6BsUVokR8ZXumYqF6M2LEJ5w4BfmlM=")
BOT_TOKEN = getenv("BOT_TOKEN", "5945087760:AAEsdI-SRg0EdYpV1TCrlsWhvaOJtQlv-40")
BOT_NAME = getenv("BOT_NAME", "F4R MUSIC BOT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LaylaBots")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {}
API_ID = int(getenv("API_ID", "29653892"))
API_HASH = getenv("API_HASH", "9a9c203c27ccb3a6d3982ecdab9c54ad")
BOT_USERNAME = getenv("BOT_USERNAME", "F4R_MUSICAL_STAR_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "HEVAAN_PC")
OWNER_NAME = getenv("OWNER_NAME", "HEVAAN_PC")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "FRIENDS_FOR_REALL")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlaybot2.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/brokenstan039/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", FRIENDS_FOR_REALL)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5663329994").split()))
