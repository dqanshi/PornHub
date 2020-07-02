"""Check if userbot alive or not . """
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from platform import python_version, uname

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
if ALIVE_PIC is None:
  CAT_IMG = "https://telegra.ph/file/4117e39218991cdd7379f.jpg"
else:
  CAT_IMG = ALIVE_PIC


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@rosebakthan"

cat_caption = "**MY BOT IS RUNNING SUCCESFULLY**\n\n"
cat_caption += f"☞`Telethon Version:` **{version.__version__}**\n"
cat_caption += f"☞`Python Version:` **{python_version()}**\n"
cat_caption += "☞**Always With You, My Master!**\n"
cat_caption += f"☞`Owner Name :` {DEFAULTUSER}\n"
cat_caption += "☞`Database Status :` Databases Functioning Normally!\n"
cat_caption += "☞`Modified by :` 𔒒K࿆I𝐝Ｉ𝕠⃤S𝓀α᳄☤👁‍🗨\n"
cat_caption += "☞`Created by :` snapdragon, anubis, sandeep\n\n"
cat_caption += "**[⚜️DEPLOY CATUSERBOT⚜️]**"


@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete()
    await borg.send_file(alive.chat_id, CAT_IMG, caption=cat_caption)
