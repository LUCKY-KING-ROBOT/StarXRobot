from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from StarRobot import OWNER_ID, dispatcher
from StarRobot import pbot as client

Star = "https://te.legra.ph/file/0c07a4bd25195fb1f948c.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Star,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

╔═════ஜ۩۞۩ஜ════╗

🇮🇳 ᴏᴡɴᴇʀ ʙy [ʟᴜᴄᴋy](tg://user?id={OWNER_ID})🌹
  
╚═════ஜ۩۞۩ஜ════╝

**[{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username}) sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•✨ᴏᴡɴᴇʀ✨",f"tg://user?id={OWNER_ID}"
                    ),
                    InlineKeyboardButton(
                        "✨ɢʀᴏᴜᴩ✨",
                        url="https://t.me/DXinfo143",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "✨Rᴇᴩᴏ✨"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""
