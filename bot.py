from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    updater = Updater("507556841:AAEXI4hE5P_B0efrOcUBFS9kUkAredoRkEA")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()

def talk_to_me(bot, update):
    user_text = update.message.text 
    logging.info(user_text)
    update.message.reply_text(user_text)

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

main()