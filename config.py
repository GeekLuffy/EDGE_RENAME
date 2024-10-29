import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", 7414019)
    API_HASH  = os.environ.get("API_HASH", "d463ed3d695f5cd4164029405ad8388e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Zoro")
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/0624f0e874718a066a3f6.mp4")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1350488685 1893650891').split()]
    FORCE_SUB_1 = os.environ.get("FORCE_SUB_1", "EdgeBotSupport")
    FORCE_SUB_2 = os.environ.get("FORCE_SUB_2", "EdgeBots")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001863937035))
    DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", "-1002131803512"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """
<b>ʜᴇʏ {}!✨

🫧 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ!
ᴡʜɪᴄʜ ᴄᴀɴ ᴍᴀɴᴜᴀʟʟʏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ғɪʟᴇs ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴀʟsᴏ ᴄᴀɴ sᴇᴛ ᴘʀᴇғɪx ᴀɴᴅ sᴜғғɪx ᴏɴ ʏᴏᴜʀ ғɪʟᴇs.⚡️

✨ ᴛʜɪs ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ <a href=https://github.com/GeekLuffy/>ʟᴜꜰꜰʏ</a>
──────────────────
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴏᴡ ᴛᴏ ᴜsᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.</b>
"""

    DONATE_TXT = """<b>
👋 ʜᴇʏ ᴛʜᴇʀᴇ {},

Jᴜsᴛ ᴡᴀɴᴛᴇᴅ ᴛᴏ ᴅʀᴏᴘ ᴀ ǫᴜɪᴄᴋ ᴛʜᴀɴᴋs ʏᴏᴜʀ ᴡᴀʏ! Iɴ ᴏᴜʀ ᴛɪɴʏ ᴄᴏʀɴᴇʀ ᴏғ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ʙᴏᴛs, ʜᴀᴠɪɴɢ ʏᴏᴜʀ sᴜᴘᴘᴏʀᴛ ғᴇᴇʟs ʟɪᴋᴇ ɢᴇᴛᴛɪɴɢ ᴀ ᴡᴀʀᴍ ʜᴜɢ.

Nᴏ ɴᴇᴇᴅ ᴛᴏ sᴛʀᴇss ᴀʙᴏᴜᴛ ᴅᴏɴᴀᴛɪᴏɴs – ʏᴏᴜʀ ʟɪᴛᴛʟᴇ sᴜᴘᴘᴏʀᴛ ᴀɴᴅ ᴄʟɪᴄᴋs ᴍᴇᴀɴ ᴛʜᴇ ᴡᴏʀʟᴅ ᴛᴏ ᴜs.

Bɪɢ ᴛʜᴀɴᴋs ғᴏʀ ʙᴇɪɴɢ ᴛʜᴇ sᴜᴘᴘᴏʀᴛ sᴜᴘᴇʀsᴛᴀʀ ɪɴ ᴏᴜʀ sᴍᴀʟʟ, ʙᴜᴛ ᴀᴡᴇsᴏᴍᴇ, sᴘᴀᴄᴇ!🌟</b>"""

    HELP_TXT = """<b>ᴇᴅɢᴇ ʀᴇɴᴀᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs🫧
 
ᴇᴅɢᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ ɪꜱ ᴀ ᴠᴇʀʏ ʜᴀɴᴅʏ ᴀɴᴅ ʜᴇʟᴘғᴜʟ ʙᴏᴛ  ᴛʜᴀᴛ ʜᴇʟᴘꜱ ʏᴏᴜ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ ᴇꜰꜰᴏʀᴛʟᴇꜱꜱʟʏ.

<u>ɪᴍᴘᴏʀᴛᴀɴᴛ ғᴇᴀᴛᴜʀᴇs:</u>
➲ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴʏ ғɪʟᴇs.
➲ ᴄᴀɴ ᴍᴀɴᴀɢᴇ ᴍᴇᴛᴀᴅᴀᴛᴀ.
➲ ᴜᴘʟᴏᴀᴅ ɪɴ ᴅᴇsɪʀᴇ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
➲ ᴄᴀɴ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴘʀᴇғɪx & sᴜғғɪx.
➲ ʀᴇɴᴀᴍᴇ ғɪʟᴇs ᴠᴇʀʏ ǫᴜɪᴄᴋʟʏ.
</b>  
"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @GeekLuffy🙏🥲
    ABOUT_TXT = """<b>
» ᴅᴇᴠᴇʟᴏᴩᴇʀ : <a href=https://t.me/GeekLuffy>ʟᴜꜰꜰʏ</a>
» ɢɪᴛʜᴜʙ :  <a href=https://github.com/GeekLuffy/>ʟᴜꜰꜰʏ</a>
» ʟɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a>
» ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>ᴘʏᴛʜᴏɴ</a>
» ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href=https://t.me/Monkey_d_luufy>ᴇᴅɢᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ</a>
» ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Anime_Edge>ᴀɴɪᴍᴇ ᴇᴅɢᴇ</a>
» ᴍᴀɪɴ ɢʀᴏᴜᴘ : <a href=https://t.me/straw_hat_piratess>ꜱᴛʀᴀᴡʜᴀᴛ ᴘɪʀᴀᴛᴇꜱ</a></b>"""

    META_TXT = """
**ᴍᴀɴᴀɢɪɴɢ ᴍᴇᴛᴀᴅᴀᴛᴀ ғᴏʀ ʏᴏᴜʀ ᴠɪᴅᴇᴏs ᴀɴᴅ ғɪʟᴇs**

**ᴠᴀʀɪᴏᴜꜱ ᴍᴇᴛᴀᴅᴀᴛᴀ:**

- **ᴛɪᴛʟᴇ**: Descriptive title of the media.
- **ᴀᴜᴛʜᴏʀ**: The creator or owner of the media.
- **ᴀʀᴛɪꜱᴛ**: The artist associated with the media.
- **ᴀᴜᴅɪᴏ**: Title or description of audio content.
- **ꜱᴜʙᴛɪᴛʟᴇ**: Title of subtitle content.
- **ᴠɪᴅᴇᴏ**: Title or description of video content.

**ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴛᴜʀɴ ᴏɴ ᴏғғ ᴍᴇᴛᴀᴅᴀᴛᴀ:**
➜ /metadata: Turn on or off metadata.

**ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ꜱᴇᴛ ᴍᴇᴛᴀᴅᴀᴛᴀ:**

➜ /settitle: Set a custom title of media.
➜ /setauthor: Set the author.
➜ /setartist: Set the artist.
➜ /setaudio: Set audio title.
➜ /setsubtitle: Set subtitle title.
➜ /setvideo: Set video title.

**ᴇxᴀᴍᴘʟᴇ:** /settitle Your Title Here

**ᴜꜱᴇ ᴛʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ᴛᴏ ᴇɴʀɪᴄʜ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ᴡɪᴛʜ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ᴍᴇᴛᴀᴅᴀᴛᴀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ!**
"""
