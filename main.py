
from conver_handler import conv_handler
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

import methods
from database import Database
from register import check
from messages import message_handler
from inlines import inline_handler
import globals
ADMIN_ID = 6215451224
TOKEN = "7927966985:AAGtciAS_DIk_zNt6socPxNklC2qYPgt-Fo"

db = Database("D:\\bakent_engeeniring_4-modul\\Django\kebab_admin_site\\db.sqlite3")

def start_handler(update, context):
    check(update, context)

def info(update, context):
    update.message.reply_text(
        text="Bu bot orqali uydan chiqmasdan hamyonbop narxlarda fastfood mahsulotlarini buyurtma qilishingiz mumkin"
    )

def contact_handler(update, context):
    message = update.message.contact.phone_number
    user = update.message.from_user
    db.update_user_data(user.id, "phone_number",message)
    check(update,context)

# lesson-4 #############
def location_handler(update, context):
    db_user = db.get_user_by_chat_id(update.message.from_user.id)
    location = update.message.location
    payment_type = context.user_data.get("payment_type", None)
    db.create_order(db_user['id'], context.user_data.get("carts", {}), payment_type, location)

    if context.user_data.get("carts", {}):
        carts = context.user_data.get("carts")
        text = "\n"
        lang_code = globals.LANGUAGE_CODE[db_user['lang_id']]
        total_price = 0
        for cart, val in carts.items():
            product = db.get_product_for_cart(int(cart))
            text += f"{val} x {product[f'cat_name_{lang_code}']} {product[f'name_{lang_code}']}\n"
            total_price += product['price'] * val

        text += f"\n{globals.ALL[db_user['lang_id']]}: {total_price} {globals.SUM[db_user['lang_id']]}"

    context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"<b>Yangi buyurtma:</b>\n\n"
             f"👤 <b>Ism-familiya:</b> {db_user['first_name']} {db_user['last_name']}\n"
             f"📞 <b>Telefon raqam:</b> {db_user['phone_number']} \n\n"
             f"📥 <b>Buyurtma:</b> \n"
             f"{text}",
        parse_mode='HTML'
    )


    context.bot.send_location(
        chat_id=ADMIN_ID,
        latitude=float(location.latitude),
        longitude=float(location.longitude)
    )
    methods.send_main_menu(context, update.message.from_user.id, db_user['lang_id'])
########################

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(CommandHandler("info", info))

    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler))

    updater.bot.get_updates(offset=-1)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
