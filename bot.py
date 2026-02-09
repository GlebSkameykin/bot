from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests


TOKEN = "8215267561:AAEN1UmmOM2sttzVmzYxoXZor6fNp75JV1w"

CRYPTO_NAME_TO_TICKER = {
    "Bitcoin": "BTCUSDT",
    "Etherium": "ETHUSDT",
    "Doge": "DOGEUSDT"
}

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def welcome(message):
    markup = ReplyKeyboardMarkup(row_width=3)
    for crypto_name in CRYPTO_NAME_TO_TICKER.keys():
        item_button = KeyboardButton(crypto_name)
        markup.add(item_button)
    bot.send_message(message.chat.id, "Choose a coin", reply_markup=markup)
        
@bot.message_handler(func=lambda message: message.text in CRYPTO_NAME_TO_TICKER.keys())
def send_price(message):
    crypto_name = message.text
    ticker = CRYPTO_NAME_TO_TICKER[crypto_name]
    price = get_price_by_ticker(ticker=ticker)
    bot.send_message(message.chat.id, f"Price of {crypto_name} is {price} USDT")

def get_price_by_ticker(*, ticker: str) -> float:
    endpoint = "https://www.binance.com/api/v3/ticker/price"
    params = {
        'symbol': ticker,
    }
    responce = requests.get(endpoint, params=params)
    data = responce.json()
    price = round(float(data["price"]), 2)
    
    return price
    

bot.infinity_polling() 
