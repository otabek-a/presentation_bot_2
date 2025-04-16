from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import re
from salom import data_help

a = data_help()

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(a)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_key = [['Pie chart', 'Bar chart'], ['Line graph']]
    make = ReplyKeyboardMarkup(reply_key, resize_keyboard=True)
    await update.message.reply_text(
        'Yo, bro! 😎 This bot helps you create diagrams. Type /help to get started! 🌟🚀',
        reply_markup=make
    )

async def pie_chart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'To create a pie chart 🍰, send a message after "pie/" (e.g., pie/name,value). Or just send "pie/values", bro 😜🎉.'
    )

async def bar_chart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'To create a bar chart 📊, send a message after "bar/" (e.g., bar/name,value). Or just send "bar/values", bro 😎🔥.'
    )

async def line_chart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
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

async def check_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    try:
        chart_type, data = text.split('/')
        parts = re.split(r'[,.]', data)
        if chart_type in ['pie', 'bar', 'line']:
            generate_chart(parts, chart_type)
            with open("chart.png", "rb") as photo:
                await update.message.reply_photo(photo)
    except Exception as e:
        await update.message.reply_text(f"Xatolik: {e}")

app = ApplicationBuilder().token('YOUR_BOT_TOKEN_HERE').build()

app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex('^Pie chart$'), pie_chart))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex('^Bar chart$'), bar_chart))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex('^Line graph$'), line_chart))
app.add_handler(MessageHandler(filters.TEXT, check_data))

if __name__ == '__main__':
    app.run_polling()
