from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import yfinance as yf

updater = Updater("1340927566:AAHzy54vtOJcqB2OKO5Qgo5vHzLxvNYdkRY",
                  use_context=True)
debug = False
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Enter the company name")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /TCS - To get the TCS share price
    /WIPRO - To get the Wipro share price
    /TECHMAHINDRA - To get the Tech Mahindra share price
    /TITAN - To get the Titan share price""")
    
def unknown(update: Update, context: CallbackContext):
    company_name = str(update.message.text)[1:]
    if ' ' not in company_name:
        stock_info = yf.Ticker(company_name + '.NS').info
    else:
        stock_info = yf.Ticker(company_name).info
    # stock_info.keys() for other properties you can explore
    #print(stock_info.keys())
    market_price = stock_info['regularMarketPrice']
    #previous_close_price = stock_info['regularMarketPreviousClose']

    if debug == True:
        print('market price ', market_price)
        #print('previous close price ', previous_close_price)
    update.message.reply_text(
        "{}\nMarket Price - {}".format(str(company_name), str(market_price)))
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()
