import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "28356026"))
    API_HASH = os.environ.get("API_HASH", "5fea2d52ca31906c83cf6ca8fc8a4449")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7040863690:AAHKLfJZ5EnbA5YfbgEKmjROZtYK_dFewh8")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Myprsnabot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 6790808572))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
