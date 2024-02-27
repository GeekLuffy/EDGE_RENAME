from pyrogram import Client, filters, enums
from helper.database import db


@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_caption(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**Gɪᴠᴇ Tʜᴇ Pʀᴇғɪx Aʟsᴏ\n\nExample:- `/set_prefix [@EdgeBots]`**")
    prefix = message.text.split(" ", 1)[1]
    madflixbotz = await message.reply_text("Please Wait ...")
    await db.set_prefix(message.from_user.id, prefix)
    await madflixbotz.edit("**Pʀᴇғɪx Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ✨**")


@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):

    madflixbotz = await message.reply_text("Please Wait ...")
    prefix = await db.get_prefix(message.from_user.id)
    if not prefix:
        return await madflixbotz.edit("**You Don't Have Any Prefix ❌**")
    await db.set_prefix(message.from_user.id, None)
    await madflixbotz.edit("**Prefix Deleted Successfully 🗑️**")


@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_caption(client, message):

    madflixbotz = await message.reply_text("Please Wait ...")
    prefix = await db.get_prefix(message.from_user.id)
    if prefix:
        await madflixbotz.edit(f"**Your Prefix :-**\n\n`{prefix}`")
    else:
        await madflixbotz.edit("**You Don't Have Any Prefix ❌**")


# SUFFIX
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_csuffix(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Give The Suffix__\n\nExample:- `/set_suffix @Madflix_Bots`**")
    suffix = message.text.split(" ", 1)[1]
    madflixbotz = await message.reply_text("Please Wait ...")
    await db.set_suffix(message.from_user.id, suffix)
    await madflixbotz.edit("**Suffix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):

    madflixbotz = await message.reply_text("Please Wait ...")
    suffix = await db.get_suffix(message.from_user.id)
    if not suffix:
        return await madflixbotz.edit("**You Don't Have Any Suffix ❌**")
    await db.set_suffix(message.from_user.id, None)
    await madflixbotz.edit("**Suffix Deleted Successfully ✅**")


@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_suffix(client, message):

    madflixbotz = await message.reply_text("Please Wait ...")
    suffix = await db.get_suffix(message.from_user.id)
    if suffix:
        await madflixbotz.edit(f"**Your Suffix :-**\n\n`{suffix}`")
    else:
        await madflixbotz.edit("**You Don't Have Any Suffix ❌**")
