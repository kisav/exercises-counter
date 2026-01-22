import json
import time as t
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    JobQueue,
    filters,
)
import sqlite3

TOKEN = "8429069048:AAE6P_Oce1Sees58esq-FS6Y6jxGc9-BmfM"
ASK_EXERCISES = range(1)

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    pushups INTEGER,
    squats INTEGER,
    abdominal INTEGER
)
""")
conn.commit()

def save_data(user_id, pushups, squats, abdominal):
    cursor.execute(
        "INSERT INTO users (user_id, pushups, squats, abdominal) VALUES (?, ?, ?, ?)",
        (user_id, pushups, squats, abdominal)
    )
    conn.commit()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот работает.")

async def ask_exercise(context):
    chat_id = context.job.chat_id

    context.application.chat_data[chat_id]["awaiting"] = True

    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text="Напиши кол-во сделанных упражнений через пробел."
    )

async def save_exercise(update, context):
    cd = context.chat_data

    if not cd.get("awaiting"):
        return

    cd["awaiting"] = False

    user_id = update.effective_user.id
    exercises = update.message.text.split(' ')

    pushups = exercises[0]
    squats = exercises[1]
    abdominal = exercises[2]

    save_data(user_id, pushups, squats, abdominal)

    cursor.execute(
        "SELECT pushups, squats, abdominal FROM users WHERE user_id = ?",
        (user_id,)
    )
    rows = cursor.fetchall()

    total_pushups = sum(r[0] for r in rows)
    total_squats = sum(r[1] for r in rows)
    total_abdominal = sum(r[2] for r in rows)

    await update.message.reply_text(f"Сумма всех отжиманий: {total_pushups} \n Сумма всех приседаний: {total_squats} \n Сумма всех упражнений на пресс: {total_abdominal}")
    return ConversationHandler.END

async def launch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id


    context.job_queue.run_repeating(
        ask_exercise,
        interval=10,
        first=0,
        chat_id=chat_id,
        name=str(chat_id),
    )

    await update.message.reply_text("Я буду задавать тебе вопрос раз в 10 секунд.")


async def stop(update, context):
    user_id = update.effective_user.id
    job_name = str(user_id)

    jobs = context.job_queue.get_jobs_by_name(job_name)

    if not jobs:
        await update.message.reply_text("Нет активных задач.")
        return

    for job in jobs:
        job.schedule_removal()

    await update.message.reply_text("Задача остановлена.")

async def reset(update, context):
    user_id = update.effective_user.id

    cursor.execute(
        "DELETE FROM users WHERE user_id = ?",
        (user_id,)  # user_id — конкретное значение
    )

    await update.message.reply_text("Все записи удалены.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stop", stop))
app.add_handler(CommandHandler("launch", launch))
app.add_handler(CommandHandler("reset", reset))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, save_exercise)
)


app.run_polling()


