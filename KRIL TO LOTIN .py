# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:43:51 2025

@author: Eldorbek
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "7920268003:AAHJnIbUo0ntXfIQiCdVjxYlsGVVKeghaNM"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# Xabarlarni faylga yozish funksiyasi
def save_message_to_file(user_id, username, message):
    try:
        with open("messages.txt", "a", encoding="utf-8") as file:
            file.write(f"Foydalanuvchi ID: {user_id} | Foydalanuvchi nomi: @{username} | Xabar: {message}\n")
        print("Xabar faylga muvaffaqiyatli yozildi!")  # Debug uchun
    except Exception as e:
        print(f"Faylga yozishda xatolik: {e}")  # Xatolikni konsolga chiqarish

# Start komandasi
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id  # Foydalanuvchi ID sini olish
    first_name = message.from_user.first_name  # Foydalanuvchi ismini olish
    username = message.from_user.username  # Foydalanuvchi nomini olish (agar mavjud bo'lsa)

    # Foydalanuvchi nomi yoki ismi bilan xabar tayyorlash
    if username:
        javob = f"Assalomu aleykum, {first_name}! Xush kelibsiz!"
    else:
        javob = f"Assalomu aleykum, @{username}! Xush kelibsiz!"

    javob += "\nMatn kiriting: "
    bot.reply_to(message, javob)

# Foydalanuvchi xabarlarini qayta ishlash
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    user_id = message.from_user.id  # Foydalanuvchi ID sini olish
    username = message.from_user.username  # Foydalanuvchi nomini olish

    # Konsolga foydalanuvchi ma'lumotlari va xabarini chiqarish
    print(f"Foydalanuvchi ID: {user_id} | Foydalanuvchi nomi: @{username} | Xabar: {msg}")

    # Xabarni faylga saqlash
    save_message_to_file(user_id, username, msg)

    # Matnni lotin yoki kirill alifbosiga o'girish
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)

    # Foydalanuvchiga javob qaytarish
    bot.reply_to(message, javob)

# Botni ishga tushirish
bot.polling()