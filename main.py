from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,CallbackContext
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import re
from salom import data_help
token=os.getenv('TOKEN')
a = data_help()

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(a)

def start(update: Update, context: CallbackContext):
    reply_key = [['Pie chart', 'Bar chart'], ['Line graph']]
    make = ReplyKeyboardMarkup(reply_key, resize_keyboard=True)
    update.message.reply_text(
        'Yo, bro! 😎 This bot helps you create diagrams. Type /help to get started! 🌟🚀',
        reply_markup=make
    )

def pie_chart(update: Update, context: CallbackContext):
    update.message.reply_text(
        'To create a pie chart 🍰, send a message after "pie/" (e.g., pie/name,value). Or just send "pie/values", bro 😜🎉.'
    )

def bar_chart(update: Update, context: CallbackContext):
    update.message.reply_text(
        'To create a bar chart 📊, send a message after "bar/" (e.g., bar/name,value). Or just send "bar/values", bro 😎🔥.'
    )

def line_chart(update: Update, context: CallbackContext):
    update.message.reply_text(
        'To create a line graph 📈, send a message after "line/" (e.g., line/name,value). Or just send "line/values", bro 🚀👊.'
    )

def generate_chart(parts, chart_type):
    x = []
    y = []
    has_text = any(any(c.isalpha() for c in i) for i in parts)

    if has_text:
        for i in range(len(parts)):
            if i % 2 == 0:
                y.append(parts[i])
            else:
                x.append(int(parts[i]))
    else:
        x = [int(i) for i in parts]

    plt.figure()
    if chart_type == 'pie':
        if has_text:
            plt.pie(x, labels=y, shadow=True, autopct='%1.1f%%')
        else:
            plt.pie(x, shadow=True, autopct='%1.1f%%')
    elif chart_type == 'bar':
        if has_text:
            plt.bar(y, x)
        else:
            plt.bar(list(range(1, len(x) + 1)), x)
    elif chart_type == 'line':
        if has_text:
            plt.plot(y, x, marker='o', color='b', linestyle='-', label='Data Line 💥')
        else:
            plt.plot(list(range(1, len(x) + 1)), x, marker='o', color='g', linestyle='-', label='Data Line 💥')

    plt.savefig("chart.png")
    plt.close()

def check_data(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    try:
        chart_type, data = text.split('/')
        parts = re.split(r'[,.]', data)
        if chart_type in ['pie', 'bar', 'line']:
            generate_chart(parts, chart_type)
            with open("chart.png", "rb") as photo:
                update.message.reply_photo(photo)
    except Exception as e:
        update.message.reply_text(f"Xatolik: {e}")

def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(MessageHandler(Filters.text('Pie chart'), pie_chart))
    dp.add_handler(MessageHandler(Filters.text('Bar chart'), bar_chart))
    dp.add_handler(MessageHandler(Filters.text('Line graph'), line_chart))
    dp.add_handler(MessageHandler(Filters.text, check_data))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
