import os
import sys
import config
from datetime import datetime
from DEADLYSPAM import  BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, SUDOERS
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events
hl = config.CMD_HNDLR

@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(event):
    if event.sender_id in SUDOERS:
        start = datetime.now()
        text = await event.reply(f"» ᴘᴏɴɢ!", parse_mode=None, link_preview=None)
        end = datetime.now()
        result = (end - start).microseconds / 1000
        await text.edit(f"» 𝗧𝗘𝗔𝗠 𝗔𝗚𝗢𝗥𝗔 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧𝗦  🔥\n\n💫 ᴀʙ ʙᴏʟ ʙʜᴀɪ ᴋɪsᴋᴇ ᴍᴀᴀ ᴄʜᴏᴅɴᴀ ʜᴀɪ: {result} ms🥀`")
