import logging
import subprocess
import requests
import socket
import urllib3.util.connection as urllib3_cn

def allowed_gai_family():
    return socket.AF_INET

urllib3_cn.allowed_gai_family = allowed_gai_family

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

TOKEN = "7698714388:AAHnqvmbWfHsB-qtLUf6Nn76VgLHTIL5hfU"
    
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Load admin IDs from file
def load_admin_ids(file_path):
    try:
        with open(file_path, 'r') as file:
            admin_ids = [int(line.strip()) for line in file if line.strip().isdigit()]
        return admin_ids
    except Exception as e:
        logger.error(f"𝙴𝚛𝚛𝚘𝚛 𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚊𝚍𝚖𝚒𝚗 𝙸𝙳𝚜: {e}")
        return []

# Daftar ID admin yang diizinkan
ADMIN_IDS = load_admin_ids('lite.txt')

# States for conversation
REGISTER, REGISTER_NAME, REGISTER_EXP, EXTEND, EXTEND_DAYS, DELETE = range(6)

def count_registered_ips():
    try:
        response = requests.get('https://raw.githubusercontent.com/vermiliion/x-only/main/ip')
        response.raise_for_status()
        ip_list = response.text.splitlines()
        return len(ip_list)
    except requests.RequestException as e:
        logger.error(f"𝙴𝚛𝚛𝚘𝚛 𝚠𝚑𝚒𝚕𝚎 𝚏𝚎𝚝𝚌𝚑𝚒𝚗𝚐 𝙸𝙿 𝚕𝚒𝚜𝚝: {e}")
        return 0

# Fungsi untuk menampilkan menu awal dengan tombol
def start(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_id = user.id
    
    if user_id not in ADMIN_IDS:
        return ConversationHandler.END
        
    username = user.username if user.username else "𝚃𝚒𝚍𝚊𝚔 𝚊𝚍𝚊 𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎"
    total_ips = count_registered_ips()

    keyboard = [
        [InlineKeyboardButton("🥇 𝙳𝚊𝚏𝚝𝚊𝚛𝚔𝚊𝚗 𝙸𝙿", callback_data='register')],
        [InlineKeyboardButton("🥈 𝙿𝚎𝚛𝚙𝚊𝚗𝚓𝚊𝚗𝚐 𝙸𝙿", callback_data='extend')],
        [InlineKeyboardButton("🥉 𝙷𝚊𝚙𝚞𝚜 𝙸𝙿", callback_data='delete')],
        [InlineKeyboardButton("📋 𝙳𝚊𝚏𝚝𝚊𝚛 𝙸𝙿", callback_data='list_ips')] 
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        f"◇⟨💠 WIBU VPN STORE 💠⟩◇\n\n"
        f"Username: @{username}\nID: {user_id}\n"
        f"Total IP Terdaftar: {total_ips}\n\n"
        "Silahkan Pilih Opsi Menu:\n"
        "🏷️ 𝗗𝗮𝗳𝘁𝗮𝗿𝗸𝗮𝗻 𝗜𝗣 𝗯𝗮𝗿𝘂\n"
        "🏷️ 𝗣𝗲𝗿𝗽𝗮𝗻𝗷𝗮𝗻𝗴 𝗺𝗮𝘀𝗮 𝗯𝗲𝗿𝗹𝗮𝗸𝘂 𝗜𝗣\n"
        "🏷️ 𝗛𝗮𝗽𝘂𝘀 𝗜𝗣 𝘆𝗮𝗻𝗴 𝘁𝗲𝗿𝗱𝗮𝗳𝘁𝗮𝗿\n",
        reply_markup=reply_markup
    )
    return ConversationHandler.END

def button(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    if query.data == 'register':
        query.edit_message_text("🔄 𝙼𝚊𝚜𝚞𝚔𝚔𝚊𝚗 𝙸𝙿 𝚢𝚊𝚗𝚐 𝚒𝚗𝚐𝚒𝚗 𝚍𝚒𝚍𝚊𝚏𝚝𝚊𝚛𝚔𝚊𝚗:")
        return REGISTER
    elif query.data == 'extend':
        query.edit_message_text("🔄 𝙼𝚊𝚜𝚞𝚔𝚔𝚊𝚗 𝙸𝙿 𝚢𝚊𝚗𝚐 𝚒𝚗𝚐𝚒𝚗 𝚍𝚒𝚙𝚎𝚛𝚙𝚊𝚗𝚓𝚊𝚗𝚐:")
        return EXTEND
    elif query.data == 'delete':
        query.edit_message_text("❌ 𝙼𝚊𝚜𝚞𝚔𝚔𝚊𝚗 𝙸𝙿 𝚢𝚊𝚗𝚐 𝚒𝚗𝚐𝚒𝚗 𝚍𝚒𝚑𝚊𝚙𝚞𝚜:")
        return DELETE   
    elif query.data == 'list_ips':
        ip_list = load_registered_ips()
        context.user_data['list_data'] = ip_list
        context.user_data['page'] = 0
        send_ip_page(query.message.chat.id, context)
        return ConversationHandler.END
     
def register_ip(update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id
    if user_id not in ADMIN_IDS:
        update.message.reply_text("🚫 𝙰𝚗𝚍𝚊 𝚝𝚒𝚍𝚊𝚔 𝚖𝚎𝚖𝚒𝚕𝚒𝚔𝚒 𝚒𝚣𝚒𝚗 𝚞𝚗𝚝𝚞𝚔 𝚖𝚎𝚗𝚐𝚐𝚞𝚗𝚊𝚔𝚊𝚗 𝚙𝚎𝚛𝚒𝚗𝚝𝚊𝚑 𝚒𝚗𝚒.")
        return ConversationHandler.END

    context.user_data['ip'] = update.message.text
    update.message.reply_text("✍️ 𝙼𝚊𝚜𝚞𝚔𝚔𝚊𝚗 𝙽𝚊𝚖𝚊:")
    return REGISTER_NAME

def handle_register_name(update: Update, context: CallbackContext) -> int:
    context.user_data['name'] = update.message.text
    update.message.reply_text("📅 𝙼𝚊𝚜𝚞𝚔𝚔𝚊𝚗 𝙼𝚊𝚜𝚊 𝙱𝚎𝚛𝚕𝚊𝚔𝚞 (𝚑𝚊𝚛𝚒):")
    return REGISTER_EXP

def finalize_register(update: Update, context: CallbackContext) -> int:
    exp = update.message.text
    ip = context.user_data['ip']
    name = context.user_data['name']

    try:
        result = subprocess.run(
            ["/bin/bash", "literegis.sh", ip, name, exp],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            update.message.reply_text(
    f"✅ 𝙸𝙿 𝚋𝚎𝚛𝚑𝚊𝚜𝚒𝚕 𝚍𝚒𝚍𝚊𝚏𝚝𝚊𝚛𝚔𝚊𝚗!\n𝙾𝚞𝚝𝚙𝚞𝚝:\n{result.stdout}",
    parse_mode="HTML"
)
        else:
            update.message.reply_text(f"❌ 𝙴𝚛𝚛𝚘𝚛:\n{result.stderr}")
    except Exception as e:
        logger.error(f"𝙴𝚛𝚛𝚘𝚛  𝚠𝚑𝚒𝚕𝚎 𝚛𝚎𝚐𝚒𝚜𝚝𝚎𝚛𝚒𝚗𝚐 𝙸𝙿: {e}")
        update.message.reply_text(f"🚨 𝚃𝚎𝚛𝚓𝚊𝚍𝚒 𝚔𝚎𝚜𝚊𝚕𝚊𝚑𝚊𝚗: {e}")

    return ConversationHandler.END

def handle_extend_ip(update: Update, context: CallbackContext) -> int:
    context.user_data['ip'] = update.message.text
    update.message.reply_text("📅 𝙼𝚊𝚜𝚞𝚔𝚔𝚊𝚗 𝚃𝚊𝚖𝚋𝚊𝚑𝚊𝚗 𝙷𝚊𝚛𝚒:")
    return EXTEND_DAYS

def finalize_extend(update: Update, context: CallbackContext) -> int:
    extra_days = update.message.text
    ip = context.user_data['ip']

    try:
        result = subprocess.run(
            ["/bin/bash", "liteextend.sh", ip, extra_days],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            update.message.reply_text(f"✅ 𝙼𝚊𝚜𝚊 𝚋𝚎𝚛𝚕𝚊𝚔𝚞 𝙸𝙿 𝚋𝚎𝚛𝚑𝚊𝚜𝚒𝚕 𝚍𝚒𝚙𝚎𝚛𝚙𝚊𝚗𝚓𝚊𝚗𝚐!\n𝙾𝚞𝚝𝚙𝚞𝚝:\n{result.stdout}")
        else:
            update.message.reply_text(f"❌ Error:\n{result.stderr}")
    except Exception as e:
        logger.error(f"𝙴𝚛𝚛𝚘𝚛 𝚠𝚑𝚒𝚕𝚎 𝚎𝚡𝚝𝚎𝚗𝚍𝚒𝚗𝚐 𝙸𝙿: {e}")
        update.message.reply_text(f"🚨 𝚃𝚎𝚛𝚓𝚊𝚍𝚒 𝚔𝚎𝚜𝚊𝚕𝚊𝚑𝚊𝚗: {e}")

    return ConversationHandler.END

def handle_delete_ip(update: Update, context: CallbackContext) -> int:
    ip = update.message.text

    try:
        result = subprocess.run(
            ["/bin/bash", "litedelete.sh", ip],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            update.message.reply_text(f"✅ 𝙸𝙿 𝚋𝚎𝚛𝚑𝚊𝚜𝚒𝚕 𝚍𝚒𝚑𝚊𝚙𝚞𝚜!\n𝙾𝚞𝚝𝚙𝚞𝚝:\n{result.stdout}")
        else:
            update.message.reply_text(f"❌ 𝙴𝚛𝚛𝚘𝚛:\n{result.stderr}")
    except Exception as e:
        logger.error(f"Error while deleting IP: {e}")
        update.message.reply_text(f"🚨 𝚃𝚎𝚛𝚓𝚊𝚍𝚒 𝚔𝚎𝚜𝚊𝚕𝚊𝚑𝚊𝚗: {e}")

    return ConversationHandler.END

def pagination_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if 'list_data' not in context.user_data:
        return

    if query.data == 'next_page':
        context.user_data['page'] += 1
    elif query.data == 'prev_page':
        context.user_data['page'] -= 1

    query.message.delete()
    send_ip_page(query.message.chat.id, context)
    
def load_registered_ips():
    try:
        response = requests.get('https://raw.githubusercontent.com/vermiliion/x-only/main/ip')
        response.raise_for_status()
        lines = response.text.strip().splitlines()
        data = []
        for line in lines:
            if line.startswith("###"):
                parts = line.replace("### ", "").split()
                if len(parts) >= 3:
                    name = parts[0]
                    exp = parts[1]
                    ip = parts[2]
                elif len(parts) == 2:
                    name = parts[0]
                    exp = "lifetime"
                    ip = parts[1]
                else:
                    continue
                formatted = (
                    f"🏷️ *» Client:* {name}\n"
                    f"🏷️ *» IP:* `{ip}`\n"
                    f"🏷️ *» Exp:* `{exp}`"
                )
                data.append(formatted)
        return data
    except Exception as e:
        logger.error(f"Gagal memuat daftar IP: {e}")
        return []

def send_ip_page(chat_id, context: CallbackContext):
    data = context.user_data.get('list_data', [])
    page = context.user_data.get('page', 0)
    per_page = 5
    start = page * per_page
    end = start + per_page
    sliced = data[start:end]

    text = "\n\n".join(sliced)
    keyboard = []

    if start > 0:
        keyboard.append(InlineKeyboardButton("⬅️ Sebelumnya", callback_data='prev_page'))
    if end < len(data):
        keyboard.append(InlineKeyboardButton("➡️ Selanjutnya", callback_data='next_page'))

    reply_markup = InlineKeyboardMarkup([keyboard] if keyboard else [])

    context.bot.send_message(
        chat_id=chat_id,
        text=f"*📋 Daftar IP Terdaftar (Hal {page + 1})*\n\n{text}",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
    
def main() -> None:
	
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(button)],
        states={
            REGISTER: [MessageHandler(Filters.text & ~Filters.command, register_ip)],
            REGISTER_NAME: [MessageHandler(Filters.text & ~Filters.command, handle_register_name)],
            REGISTER_EXP: [MessageHandler(Filters.text & ~Filters.command, finalize_register)],
            EXTEND: [MessageHandler(Filters.text & ~Filters.command, handle_extend_ip)],
            EXTEND_DAYS: [MessageHandler(Filters.text & ~Filters.command, finalize_extend)],
            DELETE: [MessageHandler(Filters.text & ~Filters.command, handle_delete_ip)],
        },
        fallbacks=[]
    )

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("menu", start))
    dispatcher.add_handler(CallbackQueryHandler(pagination_handler, pattern='^(next_page|prev_page)$'))
    dispatcher.add_handler(conversation_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
