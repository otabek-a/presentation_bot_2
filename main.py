from telegram.ext import CallbackContext, Filters, MessageHandler, Updater, CommandHandler
from telegram import ReplyKeyboardMarkup
import os
import matplotlib
matplotlib.use('Agg')  # Important: Disable GUI
import matplotlib.pyplot as plt
import re
from salom import data_help
a=data_help()
def help(update,contet):
    update.message.reply_text(
     a
    )
def start(update, context):
    reply_key = [
        ['Pie chart', 'Bar chart'],
        ['Line graph'],
    ]
    make = ReplyKeyboardMarkup(reply_key)
    update.message.reply_text(
        'Yo, bro! 😎 This bot helps you create diagrams. Type  to get started! 🌟🚀 '
        '/help',
        reply_markup=make
    )

def pie_chart(update, context):
    update.message.reply_text(
        'To create a pie chart 🍰, send a message after "pie/" (for example: pie/name,value). Or just send "pie/values", bro 😜🎉.'
    )

def bar_chart(update, context):
    update.message.reply_text(
        'To create a bar chart 📊, send a message after "bar/" (for example: bar/name,value). Or just send "bar/values", bro 😎🔥.'
    )

def line_chart(update, context):
    update.message.reply_text(
        'To create a line graph 📈, send a message after "line/" (for example: line/name,value). Or just send "line/values", bro 🚀👊.'
    )

def data_pie(update, context, part):
    x = []
    y = []
    alifbe = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    count = False
    for i in part:
        for n in i:
            if n in alifbe:
                count = True
    if count:
        for i in range(len(part)):
            if i % 2 == 0:
                y.append(part[i])
            else:
                x.append(int(part[i]))

        plt.pie(x, labels=y, shadow=True, autopct='%1.1f%%')
    else:
        for i in part:
            x.append(int(i))
        plt.pie(x, shadow=True, autopct='%1.1f%%')

    plt.savefig("chart.png")
    plt.close()
    with open("chart.png", "rb") as photo:
        update.message.reply_photo(photo)

def data_bar(update, context, part):
    x = []
    y = []
    alifbe = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    count = False
    for i in part:
        for n in i:
            if n in alifbe:
                count = True
    if count:
        for i in range(len(part)):
            if i % 2 == 0:
                y.append(part[i])
            else:
                x.append(int(part[i]))

        plt.bar(y, x)
    else:
        for i in part:
            y.append(int(i))
        plt.bar(list(range(1, len(y) + 1)), y)

    plt.savefig("chart.png")
    plt.close()
    with open("chart.png", "rb") as photo:
        update.message.reply_photo(photo)

def data_line(update, context, part):
    x = []
    y = []
    alifbe = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    count = False
    for i in part:
        for n in i:
            if n in alifbe:
                count = True
    if count:
        for i in range(len(part)):
            if i % 2 == 0:
                y.append(part[i])
            else:
                x.append(int(part[i]))

        plt.plot(y, x, marker='o', color='b', linestyle='-', label='Data Line 💥')

    else:
        for i in part:
            y.append(int(i))
        plt.plot(list(range(1, len(y) + 1)), y, marker='o', color='g', linestyle='-', label='Data Line 💥')

    plt.savefig("chart.png")
    plt.close()
    with open("chart.png", "rb") as photo:
        update.message.reply_photo(photo)

def check_data(update, context):
    text = update.message.text.lower()
    text = update.message.text.split('/')
    diagram = text[0]
    parts = re.split(r'[,.]', text[1])
    if diagram == 'pie':
        data_pie(update, context, parts)
    elif diagram == 'bar':
        data_bar(update, context, parts)
    elif diagram == 'line':
        data_line(update, context, parts)

updater = Updater(token='7807102037:AAEko05lnFrTVmX8LAgpMXOiGV_y4f2hbrg')

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(Filters.text('Pie chart'), pie_chart))
dispatcher.add_handler(MessageHandler(Filters.text('Bar chart'), bar_chart))
dispatcher.add_handler(MessageHandler(Filters.text('Line graph'), line_chart))
dispatcher.add_handler(MessageHandler(Filters.text, check_data))

updater.start_polling()
updater.idle()
