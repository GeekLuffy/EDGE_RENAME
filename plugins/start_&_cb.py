import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import db
from config import Config, Txt


@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("Hᴏᴡ ᴛᴏ Usᴇ", callback_data='help')
    ], [
        InlineKeyboardButton('Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/EdgeBots'),
        InlineKeyboardButton('Sᴜᴩᴩᴏʀᴛ', url='https://t.me/EdgeBotSupport')
    ], [
        InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('Dᴏɴᴀᴛᴇ', callback_data='donate')
    ]])
    if Config.START_PIC:
        await message.reply_video(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button,
                                 disable_web_page_preview=True)


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Hᴏᴡ ᴛᴏ Usᴇ", callback_data='help')
            ], [
                InlineKeyboardButton('Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/EdgeBots'),
                InlineKeyboardButton('Sᴜᴩᴩᴏʀᴛ', url='https://t.me/EdgeBotSupport')
            ], [
                InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('Dᴏɴᴀᴛᴇ', callback_data='donate')
            ]])
        )
    elif data == "donate":
        await query.message.edit_text(
            text=Txt.DONATE_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                # ⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("Cʟᴏꜱᴇ", callback_data="close"),
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")
            ]])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT.format(client.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("Captions", callback_data="caption"),
                    InlineKeyboardButton("Thumbnails", callback_data="thumbnail")],
                [
                    InlineKeyboardButton("Suffix & Prefix", callback_data="suffix_prefix")],
                [
                    InlineKeyboardButton("Cʟᴏꜱᴇ", callback_data="close"),
                    InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")
                ]])
        )
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                # ⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("Cʟᴏꜱᴇ", callback_data="close"),
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")
            ]])
        )

    elif data == "caption":
        await query.message.edit_text(
            text="""<b><u>ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ</u></b>
**ᴠᴀʀɪᴀʙʟᴇꜱ :**         
ꜱɪᴢᴇ: {ꜰɪʟᴇꜱɪᴢᴇ}
ᴅᴜʀᴀᴛɪᴏɴ: {duration}
ꜰɪʟᴇɴᴀᴍᴇ: {ꜰɪʟᴇɴᴀᴍᴇ}
**➜ /set_caption:** ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
**➜ /see_caption:** ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
**➜ /del_caption:** ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.

**ᴇxᴀᴍᴘʟᴇ: /setcaption** ꜰɪʟᴇ ɴᴀᴍᴇ: {ꜰɪʟᴇɴᴀᴍᴇ}
        """,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Hᴏᴍᴇ", callback_data="start"),
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="help")
            ]])
        )
    elif data == "thumbnail":
        await query.message.edit_text(
            text="""<b>ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ</b>

**➜ /start:** ꜱᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜱᴇᴛ ɪᴛ ᴀꜱ ᴀ ᴛʜᴜᴍʙɴᴀɪʟ..
**➜ /del_thumb:** ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴏʟᴅ ᴛʜᴜᴍʙɴᴀɪʟ.
**➜ /view_thumb:** ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

ɴᴏᴛᴇ: ɪꜰ ɴᴏ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ɪɴ ʙᴏᴛ ᴛʜᴇɴ, ɪᴛ ᴡɪʟʟ ᴜꜱᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ᴛʜᴇ ᴏʀɪɢɪɴɪᴀʟ ꜰɪʟᴇ ᴛᴏ ꜱᴇᴛ ɪɴ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ
        """,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Hᴏᴍᴇ", callback_data="start"),
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="help")
            ]])
        )

    elif data == "suffix_prefix":
        await query.message.edit_text(
            text="""<b>ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ꜱᴜғғɪx & ᴘʀᴇғɪx</b>
            
**➜ /set_prefix:** ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇғɪx.
**➜ /del_prefix:** ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇғɪx.
**➜ /see_prefix:** ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇғɪx.
            
**➜ /set_suffix:** ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ꜱᴜғғɪx.
**➜ /del_suffix:** ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ꜱᴜғғɪx.
**➜ /see_suffix:** ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ꜱᴜғғɪx.
            
ᴇxᴀᴍᴘʟᴇ: /set_prefix [AE] | /set_suffix [AnimeEdge]
            """,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Hᴏᴍᴇ", callback_data="start"),
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="help")
            ]])
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()
