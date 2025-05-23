

from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import MessageHandler, CommandHandler, Filters
from telegram.ext import  ConversationHandler
from database import Database
import globals
ADMIN_ID = 7958883639
db = Database("D:\\bakent_engeeniring_4-modul\\Django\\kebab_admin_site\\db.sqlite3")
GET_FEEDBACK = 1


def feebback_entry(update, context):
    user = update.message.from_user
    db_user = db.get_user_by_chat_id(user.id)
    lang_id = db_user['lang_id']
    update.message.reply_text(
        text=globals.FIKR_BILDIRISH[lang_id],
        reply_markup=ReplyKeyboardRemove()
    )
    return GET_FEEDBACK

def geet_feedback(update, context):
    feedback_text = update.message.text
    user = update.message.from_user
    db_user = db.get_user_by_chat_id(user.id)
    lang_id = db_user['lang_id']
    buttons = [
        [KeyboardButton(text=globals.BTN_ORDER[lang_id])],
        [KeyboardButton(text=globals.BTN_MY_ORDERS[lang_id]), KeyboardButton(text=globals.BTN_ABOUT_US[lang_id])],
        [KeyboardButton(text=globals.BTN_COMMENTS[lang_id]), KeyboardButton(text=globals.BTN_SETTINGS[lang_id])]
    ]

    context.bot.send_message(chat_id=ADMIN_ID,
        text=f"📩 <b>Yangi fikr kelib tushdi:</b>\n\n"
        f"{feedback_text}\n\n"
        f"👤<b>Foydalanuvchi:</b> @{user.username or 'No username'} \n(phone_number: {db_user['phone_number']})",
        parse_mode='HTML')
    update.message.reply_text(
        text=globals.FIKR_QABUL_QILINDI[lang_id],
        reply_markup=ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    )
    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text("bekor qilindi")
    return ConversationHandler.END

conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text([globals.BTN_COMMENTS[1] , globals.BTN_COMMENTS[2]]), feebback_entry)],
        states={
            GET_FEEDBACK:[MessageHandler(Filters.text & ~Filters.command, geet_feedback)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
