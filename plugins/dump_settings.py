from pyrogram import filters, Client, enums

from helper.database import db


@Client.on_message(filters.private & filters.command("setdump"))
async def set_dump_channel(client, message):
    user_id = message.from_user.id

    # Check command format
    if len(message.command) != 2:
        await message.reply_text(
            "**Usage:**\n"
            "/setdump channel_id\n\n"
            "**Example:**\n"
            "`/setdump -1001234567890`\n\n"
            "Make sure:\n"
            "1. Bot is admin in the channel\n"
            "2. Channel ID starts with -100\n"
            "3. You are the admin of the channel"
        )
        return

    try:
        channel_id = int(message.command[1])

        # Verify bot is admin in the channel
        try:
            bot_member = await client.get_chat_member(channel_id, (await client.get_me()).id)
            user_member = await client.get_chat_member(channel_id, user_id)

            if not bot_member.privileges.can_post_messages:
                await message.reply_text("I need to be an admin with post messages permission in the channel!")
                return

            if not user_member.status in [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]:
                await message.reply_text("You must be an admin of the channel to set it as dump channel!")
                return

        except Exception as e:
            await message.reply_text(
                "Failed to verify channel. Make sure:\n"
                "1. The channel ID is correct\n"
                "2. I am an admin in the channel\n"
                "3. You are an admin of the channel\n"
                f"Error: {str(e)}"
            )
            return

        await db.set_dump_channel(user_id, channel_id)
        await message.reply_text(
            "✅ Dump channel set successfully!\n\n"
            "Now all your renamed files will be automatically\n"
            "forwarded to this channel."
        )

    except ValueError:
        await message.reply_text("Please provide a valid channel ID")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

@Client.on_message(filters.private & filters.command("viewdump"))
async def view_dump_channel(client, message):
    user_id = message.from_user.id
    dump_channel = await db.get_dump_channel(user_id)

    if dump_channel:
        try:
            chat = await client.get_chat(dump_channel)
            await message.reply_text(
                f"**Your dump channel:**\n\n"
                f"**Channel ID:** `{dump_channel}`\n"
                f"**Channel Name:** {chat.title}\n\n"
                "All your renamed files are being forwarded to this channel."
            )
        except Exception as e:
            await message.reply_text(
                f"**Your dump channel ID:** `{dump_channel}`\n"
                f"(Unable to fetch channel details: {str(e)})"
            )
    else:
        await message.reply_text(
            "No dump channel set.\n"
            "Use /setdump to set one.\n\n"
            "**Note:** Setting a dump channel will automatically forward\n"
            "all your renamed files to that channel."
        )

@Client.on_message(filters.private & filters.command("removedump"))
async def remove_dump_channel(client, message):
    user_id = message.from_user.id

    if not await db.get_dump_channel(user_id):
        await message.reply_text("You haven't set any dump channel yet!")
        return

    await db.remove_dump_channel(user_id)
    await message.reply_text(
        "✅ Dump channel removed successfully!\n\n"
        "Your renamed files will no longer be forwarded\n"
        "to any channel automatically."
    )