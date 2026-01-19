import json
import time as t
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import sqlite3

TOKEN = "8429069048:AAE6P_Oce1Sees58esq-FS6Y6jxGc9-BmfM"
PUSHUPS, SQUATS, ABDOMINAL = range(3)

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    pushups INTEGER,
    squats INTEGER,
    abdominal INTEGER
)
""")
conn.commit()

def save_user(user_id):
    cursor.execute(
        "INSERT OR REPLACE INTO users (user_id) VALUES (?)",
        (user_id,)
    )
    conn.commit()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот работает.")
    save_user(update.effective_user.id)

async def launch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    await update.message.reply_text(f"Твой user_id={uid}")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("launch", launch))

app.run_polling()

def main():
    try:
        pushups = int(input('Введите число отжиманий: '))
        squats = int(input('Введите число приседаний: '))
        abdominal = int(input('Введите число пресса: '))
    except Exception as e:
        print(f'Ошибка: {e}')
        pushups = int(input('Введите число отжиманий: '))
        squats = int(input('Введите число приседаний: '))
        abdominal = int(input('Введите число пресса: '))

    try:
        with open("exersices.json", "r", encoding="utf-8") as f:
            total_pushups, total_squats, total_abdominal = json.load(f)
    except json.JSONDecodeError:
        total_squats = []
        total_pushups = []
        total_abdominal = []
    print('Opened')

    total_squats.append(squats)
    total_pushups.append(pushups)
    total_abdominal.append(abdominal)
    print('added')

    while True:
        t.sleep(3)
        try:
            pushups = int(input('Введите число отжиманий: '))
            squats = int(input('Введите число приседаний: '))
            abdominal = int(input('Введите число пресса: '))
        except Exception as e:
            print(f'Ошибка: {e}')
            pushups = int(input('Введите число отжиманий: '))
            squats = int(input('Введите число приседаний: '))
            abdominal = int(input('Введите число пресса: '))

        total_squats.append(squats)
        total_pushups.append(pushups)
        total_abdominal.append(abdominal)

        sum_pushups = sum(total_pushups)
        sum_squats = sum(total_squats)
        sum_abdominal = sum(total_abdominal)


        print('Всего:')
        print(f'Отжиманий: {sum_pushups}')
        print(f'Приседаний: {sum_squats}')
        print(f'Пресса: {sum_abdominal}')


        with open("exersices.json", "w", encoding="utf-8") as f:
            json.dump([total_pushups, total_squats, total_abdominal], f)

# if __name__ == "__main__":
#     main()


