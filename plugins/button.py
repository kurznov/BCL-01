# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if FORCE_SUB_CHANNEL:
        buttons = [
            [
                InlineKeyboardButton(text="ᴏʀᴅᴇʀ ᴠɪᴘ", url=f"https://t.me/CumAgent")
            ],
        ]
        return buttons


def fsub_button(client,message):
    if FORCE_SUB_CHANNEL:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink)
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ʀᴇsᴛᴀʀᴛ ʙᴏᴛ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
