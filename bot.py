import logging
import commands
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import jokes
import suggestions
import memes
from telegram import InputMediaPhoto,ParseMode
import youtube
import os
import wiki
import images
import random
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
# bot - context.bot
# chat_id = update.message.chat.id
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hi! Use /help to learn my commands')


def help(update, context):
    update.message.reply_text(commands.helpMsg)

def joke(update, context):
    joke = jokes.getJoke()
    update.message.reply_text(joke)


def echo(update, context):
    update.message.reply_text(update.message.text)

def about(update, context):
    update.message.reply_text(commands.aboutMsg)

def suggest(update, context):
    m=suggestions.registerSuggestion(update.message.text)
    update.message.reply_text(m)

def meme(update,context):
    category = ""
    content = update.message.text
    content = content.split(" ")

    if len(content)>1:
        category=content[1]
    else:
        category="regular"
    update.message.reply_text("Finding a meme for you...")
    url = memes.getMemeUrl(category)
    context.bot.send_photo(chat_id=update.message.chat_id,photo=url)

def image(update,context):
    msg = update.message.text
    msg = msg.replace("/image","")
    msg = msg.strip()
    if len(msg)<1:
        update.message.reply_text("Search term can't be blank...duh!") 
    else:
        allUrls = images.getPhoto(msg)
        url = random.choice(allUrls)
        link = url[0]
        print("LINK!!!!!!!",link)
        try:
            context.bot.send_photo(chat_id=update.message.chat_id,photo=link,caption=f"Photograph by: <a href='{url[2]}'>{url[1]}</a>\nPhotos from <a href='https://www.pexels.com'>Pexels</a>",parse_mode=ParseMode.HTML)
        except:
            name=images.download(link)
            context.bot.send_photo(chat_id=update.message.chat_id,photo=open(name,'rb'),caption=f"Photograph by: <a href='{url[2]}'>{url[1]}</a>\nPhotos from <a href='https://www.pexels.com'>Pexels</a>",parse_mode=ParseMode.HTML)
            os.remove(name)
def youtubeVid(update,context):
    searchTerm=update.message.text.replace("/youtube","")
    url=youtube.getVideo(searchTerm)
    update.message.reply_text(url)

def info(update,context):
    msg = update.message.text
    msg = msg.replace("/wiki","")
    msg = msg.strip()
    if len(msg)<1:
        update.message.reply_text("Search term can't be blank...duh!")
    else:
        resp = wiki.getInfo(msg)
        update.message.reply_text(resp)    
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning(update, context.error)
    update.message.reply_text("Something's wrong....I can feel it. \n\nContact developer pls")    


def main():
    
    updater = Updater(os.environ['bot_id'], use_context=True)
 
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("joke", joke))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("suggestion", suggest))
    dp.add_handler(CommandHandler("meme", meme))
    dp.add_handler(CommandHandler("youtube", youtubeVid))
    dp.add_handler(CommandHandler("wiki", info))
    dp.add_handler(CommandHandler("image", image))
    


    # dp.add_handler(MessageHandler(Filters.text, echo)) 

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()