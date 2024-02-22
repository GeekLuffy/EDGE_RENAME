import re, os, time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", 7414019)
    API_HASH = os.environ.get("API_HASH", "d463ed3d695f5cd4164029405ad8388e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6585676928:AAFOa8imTZ-wnZGj1CdTQl-NX-9y6wqFPpk")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "pyro-botz")
    DB_URL = os.environ.get("DB_URL",
                            "mongodb+srv://owaisnae92:glassone1@zoro.zelrmhx.mongodb.net/?retryWrites=true&w=majority")

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/2a534b25a88d4c2e2b108.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in
             os.environ.get('ADMIN', '1350488685').split()]
    FORCE_SUB_1 = os.environ.get("FORCE_SUB_1", "EdgeBotSupport")
    FORCE_SUB_2 = os.environ.get("FORCE_SUB_2", "EdgeBots")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001863937035))
    DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", "-1002131803512"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))


class Txt(object):
    # part of text configuration
    START_TXT = """
<b>👋 ʜᴇʟʟᴏ {}!

🌟 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ! 🌟
📂 ᴡɪᴛʜ ᴛʜɪꜱ ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ ᴇᴀꜱɪʟʏ  ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ ᴀɴᴅ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟꜱ ᴀɴᴅ ᴄᴀᴘᴛɪᴏɴꜱ. 🖼️📝

🚀 ᴛʜɪꜱ ʙᴏᴛ ᴡᴀꜱ ᴄʀᴀꜰᴛᴇᴅ ʙʏ  <a href="https://t.me/GeekLuffy">ʟᴜꜰꜰʏ</a>
ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴀ ꜱᴇᴀᴍʟᴇꜱꜱ ʀᴇɴᴀᴍɪɴɢ ᴇxᴘᴇʀɪᴇɴᴄᴇ. ⚡️</b>
"""

    ABOUT_TXT = """<b>╭───────────⍟
├➽ ᴍy ɴᴀᴍᴇ : {}
├➽ Dᴇᴠᴇʟᴏᴩᴇʀ : <a href=https://t.me/Monkey_d_luufy>Lᴜꜰꜰʏ</a> 
├➽ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├➽ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├➽ Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>    
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>ʜᴏᴡ ᴛᴏ ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ</u></b>
  
<b>➽</b> /start ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ꜱᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ.
<b>➽</b> /del_thumb ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴏʟᴅ ᴛʜᴜᴍʙɴᴀɪʟ.
<b>➽</b> /view_thumb ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.\n
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>
<b>➽</b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>➽</b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>➽</b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}\n
✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>➽</b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].\n           
ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/MONKEY_D_LUUFY>𝗟𝗨𝗙𝗙𝗬</a>
"""

    # ⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @MONKEY_D_LUUFY🙏🥲
    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ Tᴏ Dᴇᴠᴇʟᴏᴩᴇʀ</b></u>\n
<b>» ᴏᴡɴᴇʀ : <a href=https://t.me/GeekLuffy>ʟᴜꜰꜰʏ</a>
» ɢɪᴛʜᴜʙ :  <a href=https://github.com/GeekLuffy/>ʟᴜꜰꜰʏ</a>
» ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href=https://t.me/Monkey_d_luufy>ᴇᴅɢᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ</a>
» ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Anime_Edge>ᴀɴɪᴍᴇ ᴇᴅɢᴇ</a>
» ᴍᴀɪɴ ɢʀᴏᴜᴘ : <a href=https://t.me/straw_hat_piratess>ꜱᴛʀᴀᴡʜᴀᴛ ᴘɪʀᴀᴛᴇꜱ</a></b>"""