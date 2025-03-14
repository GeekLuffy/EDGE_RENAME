from config import Config
import psutil
from helper.database import db
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
import os, sys, time, asyncio, logging, datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
 
# Import the psutil module for system-related information
import psutil

@Client.on_message(filters.command(["stats", "status"]) & filters.user(Config.ADMIN))
async def get_stats(bot, message):
    total_users = await db.total_users_count()
    uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - bot.uptime))
    start_t = time.time()
    st = await message.reply('`📊 Fetching Stats...`')
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000

    # CPU Information
    cpu_usage = psutil.cpu_percent()
    cpu_freq = psutil.cpu_freq()
    cpu_count = psutil.cpu_count()
    physical_cores = psutil.cpu_count(logical=False)
    
    # Memory Information
    memory_info = psutil.virtual_memory()
    memory_usage_gb = memory_info.used / (1024 ** 3)
    total_memory_gb = memory_info.total / (1024 ** 3)
    
    # Disk Information
    disk_info = psutil.disk_usage('/')
    disk_used_gb = (disk_info.total - disk_info.free) / (1024 ** 3)
    disk_total_gb = disk_info.total / (1024 ** 3)
    
    stats_text = f"""
╭─《 **BOT STATUS** 》
├ **Users:** `{total_users:,}`
├ **Uptime:** `{uptime}`
├ **Response:** `{time_taken_s:.1f} ms`
│
├─《 **CPU INFO** 》
├ **Usage:** `{cpu_usage:.1f}%`
├ **Cores:** `{physical_cores}`
├ **Threads:** `{cpu_count}`
├ **Frequency:** `{cpu_freq.current/1000:.1f} GHz`
├ **Max Freq:** `{cpu_freq.max/1000:.1f} GHz`
├ **Min Freq:** `{cpu_freq.min/1000:.1f} GHz`
│
├─《 **MEMORY INFO** 》
├ **Used:** `{memory_usage_gb:.1f}/{total_memory_gb:.1f} GB`
├ **Percentage:** `{memory_info.percent}%`
├ **Available:** `{(memory_info.available/1024/1024/1024):.1f} GB`
│
├─《 **STORAGE INFO** 》
├ **Used:** `{disk_used_gb:.1f}/{disk_total_gb:.1f} GB`
├ **Percentage:** `{disk_info.percent}%`
├ **Free Space:** `{(disk_info.free/1024/1024/1024):.1f} GB`
╰─《 **@EdgeBots** 》"""

    await st.edit(stats_text)



#Restart to cancell all process 
@Client.on_message(filters.private & filters.command("restart") & filters.user(Config.ADMIN))
async def restart_bot(b, m):
    await m.reply_text("🔄__Rᴇꜱᴛᴀʀᴛɪɴɢ.....__")
    os.execl(sys.executable, sys.executable, *sys.argv)


@Client.on_message(filters.command("broadcast") & filters.user(Config.ADMIN) & filters.reply)
async def broadcast_handler(bot: Client, m: Message):
    await bot.send_message(Config.LOG_CHANNEL, f"{m.from_user.mention} or {m.from_user.id} Iꜱ ꜱᴛᴀʀᴛᴇᴅ ᴛʜᴇ Bʀᴏᴀᴅᴄᴀꜱᴛ......")
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    sts_msg = await m.reply_text("Bʀᴏᴀᴅᴄᴀꜱᴛ Sᴛᴀʀᴛᴇᴅ..!") 
    done = 0
    failed = 0
    success = 0
    start_time = time.time()
    total_users = await db.total_users_count()
    async for user in all_users:
        sts = await send_msg(user['_id'], broadcast_msg)
        if sts == 200:
           success += 1
        else:
           failed += 1
        if sts == 400:
           await db.delete_user(user['_id'])
        done += 1
        if not done % 20:
           await sts_msg.edit(f"Bʀᴏᴀᴅᴄᴀꜱᴛ Iɴ Pʀᴏɢʀᴇꜱꜱ: \nTᴏᴛᴀʟ Uꜱᴇʀꜱ {total_users} \nCᴏᴍᴩʟᴇᴛᴇᴅ: {done} / {total_users}\nSᴜᴄᴄᴇꜱꜱ: {success}\nFᴀɪʟᴇᴅ: {failed}")
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await sts_msg.edit(f"Bʀᴏᴀᴅᴄᴀꜱᴛ Cᴏᴍᴩʟᴇᴛᴇᴅ: \nCᴏᴍᴩʟᴇᴛᴇᴅ Iɴ `{completed_in}s`.\n\nTᴏᴛᴀʟ Uꜱᴇʀꜱ {total_users}\nCᴏᴍᴩʟᴇᴛᴇᴅ: {done} / {total_users}\nSᴜᴄᴄᴇꜱꜱ: {success}\nFᴀɪʟᴇᴅ: {failed}")
           
async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=int(user_id))
        return 200
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        logger.info(f"{user_id} : Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ")
        return 400
    except UserIsBlocked:
        logger.info(f"{user_id} : Bʟᴏᴄᴋᴇᴅ Tʜᴇ Bᴏᴛ")
        return 400
    except PeerIdInvalid:
        logger.info(f"{user_id} : Uꜱᴇʀ Iᴅ Iɴᴠᴀʟɪᴅ")
        return 400
    except Exception as e:
        logger.error(f"{user_id} : {e}")
        return 500
 
