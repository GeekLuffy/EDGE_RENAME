from pyrogram import Client, filters, enums
from helper.database import db


@Client.on_message(filters.private & filters.command(['set_prefix', 'setprefix']))
async def add_caption(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**Gɪᴠᴇ Tʜᴇ Pʀᴇғɪx Aʟsᴏ\n\nExᴀᴍᴘʟᴇ:- `/set_prefix [@EdgeBots]`**")
    prefix = message.text.split(" ", 1)[1]
    EdgeBot = await message.reply_text("Please Wait ...")
    await db.set_prefix(message.from_user.id, prefix)
    await EdgeBot.edit("**Pʀᴇғɪx Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ✨**")


@Client.on_message(filters.private & filters.command(['del_prefix', 'delprefix']))
async def delete_prefix(client, message):

    EdgeBots = await message.reply_text("Please Wait ...")
    prefix = await db.get_prefix(message.from_user.id)
    if not prefix:
        return await EdgeBots.edit("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Pʀᴇғɪx Tᴏ Dᴇʟᴇᴛᴇ❌**")
    await db.set_prefix(message.from_user.id, None)
    await EdgeBots.edit("**Pʀᴇғɪx Dᴇʟᴇᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ⚡️**")


@Client.on_message(filters.private & filters.command(['see_prefix', 'seeprefix']))
async def see_prefix(client, message):

    EdgeBots = await message.reply_text("Please Wait ...")
    prefix = await db.get_prefix(message.from_user.id)
    if prefix:
        await EdgeBots.edit(f"**Yᴏᴜʀ Pʀᴇғɪx :-**\n\n`{prefix}`")
    else:
        await EdgeBots.edit("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Pʀᴇғɪx Tᴏ Sᴇᴇ**")


# SUFFIX
@Client.on_message(filters.private & filters.command(['set_suffix', 'setsuffix']))
async def add_csuffix(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**Gɪᴠᴇ Tʜᴇ Sᴜғғɪx\n\nExᴀᴍᴘʟᴇ:- `/set_suffix @Madflix_Bots`**")
    suffix = message.text.split(" ", 1)[1]
    EdgeBots = await message.reply_text("Please Wait ...")
    await db.set_suffix(message.from_user.id, suffix)
    await EdgeBots.edit("**Sᴜғғɪx Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ✨**")


@Client.on_message(filters.private & filters.command(['del_suffix', 'delsuffix']))
async def delete_suffix(client, message):

    EdgeBots = await message.reply_text("Please Wait ...")
    suffix = await db.get_suffix(message.from_user.id)
    if not suffix:
        return await EdgeBots.edit("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Sᴜғғɪx Tᴏ Dᴇʟᴇᴛᴇ❌**")
    await db.set_suffix(message.from_user.id, None)
    await EdgeBots.edit("**Sᴜғғɪx Dᴇʟᴇᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ⚡️**")


@Client.on_message(filters.private & filters.command(['see_suffix', 'seesuffix']))
async def see_suffix(client, message):
    EdgeBots = await message.reply_text("Please Wait ...")
    suffix = await db.get_suffix(message.from_user.id)
    if suffix:
        await EdgeBots.edit(f"**Yᴏᴜʀ Sᴜғғɪx :-**\n\n`{suffix}`")
    else:
        await EdgeBots.edit("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Sᴜғғɪx Tᴏ Sᴇᴇ**")
