import shutil
import subprocess

from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

from config import Config
from plugins.antinsfw import check_anti_nsfw
from helper.utils import progress_for_pyrogram, convert, humanbytes
from helper.database import db

from asyncio import sleep
from PIL import Image
import os, time


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    # if await check_anti_nsfw(filename, message):
    #     return

    if file.file_size > 2000 * 1024 * 1024:
        return await message.reply_text("Sorry Bro This Bot Doesn't Support Uploading Files Bigger Than 2GB")

    try:
        await message.reply_text(
            text=f"**Please Enter New Filename...**\n\n**Old File Name** :- `{filename}`",
            reply_to_message_id=message.id,
            reply_markup=ForceReply(True)
        )
        await sleep(30)
    except FloodWait as e:
        await sleep(e.value)
        await message.reply_text(
            text=f"**Please Enter New Filename**\n\n**Old File Name** :- `{filename}`",
            reply_to_message_id=message.id,
            reply_markup=ForceReply(True)
        )
    except:
        pass


@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    reply_message = message.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
        new_name = message.text
        await message.delete()
        msg = await client.get_messages(message.chat.id, reply_message.id)
        file = msg.reply_to_message
        media = getattr(file, file.media.value)
        # if await check_anti_nsfw(new_name, message):
        #     return
        if not "." in new_name:
            if "." in media.file_name:
                extn = media.file_name.rsplit('.', 1)[-1]
            else:
                extn = "mkv"
            new_name = new_name + "." + extn
        await reply_message.delete()

        button = [[InlineKeyboardButton("📁 Document", callback_data="upload_document")]]
        if file.media in [MessageMediaType.VIDEO, MessageMediaType.DOCUMENT]:
            button.append([InlineKeyboardButton("🎥 Video", callback_data="upload_video")])
        elif file.media == MessageMediaType.AUDIO:
            button.append([InlineKeyboardButton("🎵 Audio", callback_data="upload_audio")])
        await message.reply(
            text=f"**Select The Output File Type**\n\n**File Name :-** `{new_name}`",
            reply_to_message_id=file.id,
            reply_markup=InlineKeyboardMarkup(button)
        )


@Client.on_callback_query(filters.regex("upload"))
async def doc(bot, update):
    user_id = update.from_user.id
    prefix = await db.get_prefix(update.message.chat.id)
    suffix = await db.get_suffix(update.message.chat.id)
    new_name = update.message.text
    new_filename_ = new_name.split(":-")[1]

    try:
        if prefix and suffix:
            shorted = new_filename_[:-4:]
            extension = new_filename_[-4::]
            new_filename = f"{prefix} {shorted} {suffix}{extension}"

        elif prefix:
            shorted = new_filename_[:-4:]
            extension = new_filename_[-4::]
            new_filename = f"{prefix} {shorted}{extension}"

        elif suffix:
            shorted = new_filename_[:-4:]
            extension = new_filename_[-4::]
            new_filename = f"{shorted} {suffix}{extension}"

        else:
            new_filename = new_filename_
    except:
        await update.message.edit(
            "⚠️ Something went wrong can't able to set Prefix or Suffix in the File ☹️ \n\n Contact in Support Group for Help -> @EdgeBotSupport")

    file_path = f"downloads/{new_filename}"
    file = update.message.reply_to_message

    ms = await update.message.edit("`Trying To Downloading`")
    try:
        path = await bot.download_media(message=file, file_name=file_path, progress=progress_for_pyrogram,
                                        progress_args=("`Download Started....`", ms, time.time()))
    except Exception as e:
        return await ms.edit(e)

    user_metadata_enabled = await db.get_metadata(user_id)
    if user_metadata_enabled == "On":

        # Generate a temporary file path
        temp_output_file = file_path.replace('.mkv', '_temp.mkv')

        ffmpeg_cmd = shutil.which('ffmpeg')

        title = await db.get_title(user_id)
        author = await db.get_author(user_id)
        artist = await db.get_artist(user_id)
        video = await db.get_video(user_id)
        audio = await db.get_audio(user_id)
        subtitle = await db.get_subtitle(user_id)

        # Add metadata using subprocess and ffmpeg command
        metadata_command = [
            'ffmpeg',
            '-i', file_path,
            '-metadata', f'title={title}',
            '-metadata', f'artist={artist}',
            '-metadata', f'author={author}',
            # '-metadata', 'comment=Join @Anime_Edge for more content',
            '-metadata', 'additional_key=additional_value',
            '-metadata:s:v', f'title={video}',
            '-metadata:s:a', f'title={audio}',
            '-metadata:s:s', f'title={subtitle}',
            '-map', '0',
            '-c', 'copy',
            '-loglevel', 'error',
            temp_output_file
        ]

        try:
            subprocess.run(metadata_command, check=True)
            # Rename the temporary file to the desired output file
            shutil.move(temp_output_file, file_path)

        except subprocess.CalledProcessError as e:
            # send the error to the user
            await ms.edit(f"Error adding metadata: {e}")
            print(f"Error adding metadata: {e}")

        finally:
            # Cleanup: Remove the temporary file if it exists
            if os.path.exists(temp_output_file):
                os.remove(temp_output_file)
    else:
        print("Metadata is disabled for this user.")

    duration = 0
    try:
        metadata = extractMetadata(createParser(file_path))
        if metadata.has("duration"):
            duration = metadata.get('duration').seconds
    except:
        pass
    ph_path = None
    user_id = int(update.message.chat.id)
    media = getattr(file, file.media.value)
    c_caption = await db.get_caption(update.message.chat.id)
    c_thumb = await db.get_thumbnail(update.message.chat.id)

    if c_caption:
        try:
            caption = c_caption.format(filename=new_filename, filesize=humanbytes(media.file_size),
                                       duration=convert(duration))
        except Exception as e:
            return await ms.edit(text=f"Your Caption Error Except Keyword Argument: ({e})")
        logcaption = f"**{new_filename}**\nUploaded by {update.from_user.mention()}"
    else:
        caption = f"**{new_filename}**"
        logcaption = f"**{new_filename}**\nUploaded by {update.from_user.mention()}"

    if (media.thumbs or c_thumb):
        if c_thumb:
            ph_path = await bot.download_media(c_thumb)
        else:
            ph_path = await bot.download_media(media.thumbs[0].file_id)
        Image.open(ph_path).convert("RGB").save(ph_path)
        img = Image.open(ph_path)
        img.resize((320, 320))
        img.save(ph_path, "JPEG")

    await ms.edit("Tʀyɪɴɢ Tᴏ Uᴩʟᴏᴀᴅɪɴɢ....")
    type = update.data.split("_")[1]
    try:
        if type == "document":
            await bot.send_document(
                update.message.chat.id,
                document=file_path,
                thumb=ph_path,
                caption=caption,
                progress=progress_for_pyrogram,
                progress_args=("Uᴩʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))
            await bot.send_document(
                Config.DUMP_CHANNEL,
                document=file_path,
                thumb=ph_path,
                caption=logcaption)
        elif type == "video":
            await bot.send_video(
                update.message.chat.id,
                video=file_path,
                caption=caption,
                thumb=ph_path,
                duration=duration,
                progress=progress_for_pyrogram,
                progress_args=("Uᴩʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))
            await bot.send_video(
                Config.DUMP_CHANNEL,
                video=file_path,
                thumb=ph_path,
                caption=logcaption)
        elif type == "audio":
            await bot.send_audio(
                update.message.chat.id,
                audio=file_path,
                caption=caption,
                thumb=ph_path,
                duration=duration,
                progress=progress_for_pyrogram,
                progress_args=("Uᴩʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))
            await bot.send_audio(
                Config.DUMP_CHANNEL,
                audio=file_path,
                thumb=ph_path,
                caption=logcaption)
    except Exception as e:
        os.remove(file_path)
        if ph_path:
            os.remove(ph_path)
        return await ms.edit(f" Eʀʀᴏʀ {e}")

    await ms.delete()
    os.remove(file_path)
    if ph_path: os.remove(ph_path)
