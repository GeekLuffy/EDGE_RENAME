from pyrogram import Client, enums, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import Config
from helper.database import db


async def not_subscribed(_, client, message):
    await db.add_user(client, message)
    if not Config.FORCE_SUB_1 and Config.FORCE_SUB_2:
        return False
    try:
        user1 = await client.get_chat_member(Config.FORCE_SUB_1, message.from_user.id)
        user2 = await client.get_chat_member(Config.FORCE_SUB_2, message.from_user.id)
        if user1.status == enums.ChatMemberStatus.BANNED and user2.status == enums.ChatMemberStatus.BANNED:
            return True
        else:
            return False
    except UserNotParticipant:
        pass
    return True


@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    user_firstname = message.from_user.first_name

    buttons = [
        [
            InlineKeyboardButton(text="⚡️ Join Channel 1 ⚡️", url=f"https://t.me/{Config.FORCE_SUB_1}"),
            InlineKeyboardButton(text="⚡️ Join Channel 2 ⚡️", url=f"https://t.me/{Config.FORCE_SUB_2}")
        ],
        [
            InlineKeyboardButton(text="Verify Membership", callback_data="check_joined")
        ]
    ]

    text = f"""**Hold on, {user_firstname}! You're missing out on some serious action.
To unleash my full power and access all the premium features, you've got to join both of our electrifying update channels below:**"""

    try:
        user_channel_1 = await client.get_chat_member(Config.FORCE_SUB_1, message.from_user.id)
        user_channel_2 = await client.get_chat_member(Config.FORCE_SUB_2, message.from_user.id)

        if (user_channel_1.status == enums.ChatMemberStatus.BANNED) and (
                user_channel_2.status == enums.ChatMemberStatus.BANNED):
            return await client.send_message(message.from_user.id, text="Sorry, You're Banned to Use Me")
    except UserNotParticipant:
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))

    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("check_joined"))
async def check_joined_callback(client, query):
    user = query.from_user

    try:
        user_channel_1 = await client.get_chat_member(Config.FORCE_SUB_1, user.id)
        user_channel_2 = await client.get_chat_member(Config.FORCE_SUB_2, user.id)
    except UserNotParticipant:
        await query.answer("You must join both channels to access my premium features.",show_alert=True)
        return
    if user_channel_1.status == enums.ChatMemberStatus.MEMBER and user_channel_2.status == enums.ChatMemberStatus.MEMBER:
        await query.answer("You have joined both Channels! Now you can freely use me", show_alert=True)
    else:
        await query.answer("You must join both channels to access my premium features.", show_alert=True)
