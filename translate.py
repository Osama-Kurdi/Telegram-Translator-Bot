import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from googletrans import Translator
import os

PORT = int(os.environ.get('PORT', 9000))

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)
token = "1930106303:AAF0Yx3DkqgBZwriH8xA_-Z-tGbr9gbOXWQ"


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Welcome {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True))
    update.message.reply_text("Thanks for using our bot.\nIf you have any problems you can always use the /help command.\nIf you still have the same problem or you want to suggest new ideas you can find contact section at /about.")
    update.message.reply_text("You can start by sending any text.")

 
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    # TODO
    update.message.reply_text('Send the word in any language and it will be automatically translated to English.\nEnglish will be translated only to Arabic.')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    text = update.message.text
    translator = Translator()
    scr = translator.detect(text).lang
    dest = 'en'
    if scr == 'en':
        dest = 'ar'
    translated = translator.translate(text, scr=scr, dest=dest)
    update.message.reply_text(translated.text)


def about(update, context):
    update.message.reply_text("✅ About bot:\nThis bot will translate from any language to English.\nEnglish will be translated only to Arabic.\n\n✅ About developer:\nContact me at: @OKurdi or osama4kurdi@gmail.com")
    #update.message.reply_text("Translating from English will be only to Arabic.")


def main() -> None:
    """Start the bot."""
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("about", about))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=token)
    updater.bot.setWebhook('https://translatorbot0.herokuapp.com/' + token)
    #updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
