import time
from telebot import TeleBot
from keyboard import *
from localization.lang import *

token = "7053553473:AAFa-MWRvNWyjlHfns8ZFAYYYIqb7Y2bJqQ"

bot = TeleBot(token)

user_data = {}
user_langs = {}

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    bot.send_photo(chat_id, open("image/image.jpg", "rb"), caption=start_bot[lang], reply_markup=social("https://play.google.com/store/apps/details?id=uz.testim", "https://apps.apple.com/uz/app/protestim/id1666392601", lang))
    bot.send_message(chat_id, select_to[lang], reply_markup=generate_main_menu(lang))
    bot.register_next_step_handler(message, choose_catalog)


def choose_catalog(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    if message.text == call[lang]:
        bot.send_photo(chat_id, photo=open("image/img.jpg", "rb"), caption=catalog_lang[lang], reply_markup=generate_connect("https://protestim.olympiada.uz/", "t.me/Akbarikramov0606", lang))

    elif message.text == setting[lang]:
        bot.send_message(chat_id, "Quyidagilardan birini tanlang: ", reply_markup=settings(lang))
        bot.register_next_step_handler(message, languge)


    elif message.text == menu_milliy[lang]:
        universitet_name = menu_milliy[lang]
        return send_data(message, universitet_name)


    elif message.text == menu_qoqon[lang]:
        universitet_name = menu_qoqon[lang]
        return send_data(message, universitet_name)


    elif message.text == menu_osio[lang]:
        universitet_name = menu_osio[lang]
        return send_data(message, universitet_name)


@bot.callback_query_handler(func=lambda call: call.data == "back")
def back(call):
    return start(call.message)

def languge(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    if message.text == select_language[lang]:
        bot.send_message(chat_id, f"{select_language[lang]}:", reply_markup=select_lang(lang))
        bot.register_next_step_handler(message, lang_catalog)

    elif message.text == back_to[lang]:
        return start(message)

def lang_catalog(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    if message.text == "🇺🇿Uz":
        lang = "uz"
        bot.send_message(chat_id,
                         start_bot[lang],
                         reply_markup=generate_main_menu(lang))
        bot.register_next_step_handler(message, choose_catalog)


    elif message.text == "🇷🇺Ru":
        lang = "ru"
        bot.send_message(chat_id,
                         start_bot[lang],
                         reply_markup=generate_main_menu(lang))
        bot.register_next_step_handler(message, choose_catalog)


    elif message.text == "🇬🇧En":
        lang = "en"
        bot.send_message(chat_id,
                         start_bot[lang],
                         reply_markup=generate_main_menu(lang))
        bot.register_next_step_handler(message, choose_catalog)


    elif message.text == back_to[lang]:
        bot.send_message(chat_id, select_to[lang], reply_markup=settings(lang))
        bot.register_next_step_handler(message, languge)

    user_langs[chat_id] = lang




def send_data(message, universitet_name):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")
    bot.send_message(chat_id, fish[lang])
    bot.register_next_step_handler(message, send_screen, universitet_name)


def send_screen(message, universitet_name):
    chat_id = message.chat.id
    fio = message.text
    lang = user_langs.get(chat_id, "uz")

    bot.send_message(chat_id, screen[lang])
    bot.register_next_step_handler(message, send_contract, fio, universitet_name)


def send_contract(message, fio, universitet_name):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    if message.document:
        document = message.document.file_id
        bot.send_message(chat_id, document_to[lang])
        bot.register_next_step_handler(message, wait_for_second_file, document, fio, universitet_name, True)  # True для документа

    elif message.photo:
        photo = message.photo[-1].file_id
        bot.send_message(chat_id, document_to[lang])
        bot.register_next_step_handler(message, wait_for_second_file, photo, fio, universitet_name, False)  # False для фото

    else:
        bot.send_message(chat_id, error_photos[lang])
        return send_screen(message, universitet_name)


def wait_for_second_file(message, first_file_id, fio, universitet_name, is_document_first):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    if message.document:
        second_file_id = message.document.file_id
        bot.send_message(chat_id, contact_info[lang], reply_markup=share_contact(lang))
        bot.register_next_step_handler(message, commit_contact, first_file_id, second_file_id, fio, universitet_name, is_document_first, True)  # True для документа

    elif message.photo:
        second_file_id = message.photo[-1].file_id
        bot.send_message(chat_id, contact_info[lang], reply_markup=share_contact(lang))
        bot.register_next_step_handler(message, commit_contact, first_file_id, second_file_id, fio, universitet_name, is_document_first, False)

    else:
        bot.send_message(chat_id, error_photos[lang])
        return send_screen(message, universitet_name)


def commit_contact(message, first_file_id, second_file_id, fio, universitet_name, is_document_first, is_document_second):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, "uz")

    phone_number = message.contact.phone_number if message.contact else message.text

    # Обновление данных пользователя
    user_data[chat_id] = {
        'first_file_id': first_file_id,
        'second_file_id': second_file_id,
        'fio': fio,
        'universitet_name': universitet_name,
        'is_document_first': is_document_first,
        'is_document_second': is_document_second,
        'phone_number': phone_number
    }

    # После обновления данных, получить актуальные данные
    data = user_data.get(chat_id)

    caption_text = (
        f"<b>{name_univer[lang]}</b> {data['universitet_name']}\n"
        f"<b>{name_fio[lang]}</b> {data['fio']}\n"
        f"<b>{name_phone[lang]}</b> {data['phone_number']}\n"
    )

    bot.send_message(chat_id, check_data[lang])

    if is_document_first:
        bot.send_document(chat_id, first_file_id)
    else:
        bot.send_photo(chat_id, first_file_id)

    if is_document_second:
        bot.send_document(chat_id, second_file_id)
    else:
        bot.send_photo(chat_id, second_file_id)

    bot.send_message(chat_id, caption_text, parse_mode="HTML", reply_markup=commit(lang))


@bot.callback_query_handler(func=lambda call: call.data in ["confirm", "cancel"])
def commit_data(call):
    chat_id = call.message.chat.id
    lang = user_langs.get(chat_id, "uz")

    data = user_data.get(chat_id)
    tg_username = call.from_user.username
    channel_id = -1002171342653

    if call.data == "confirm":
        bot.send_message(chat_id, commit_message[lang])

        if data:
            caption_text = (
                f"<b>{name_univer[lang]}</b> {data['universitet_name']}\n"
                f"<b>{name_fio[lang]}</b> {data['fio']}\n"
                f"<b>{user_name[lang]}</b> @{tg_username}\n"
                f"<b>{name_phone[lang]}</b> {data['phone_number']}\n"
            )

            if data['is_document_first']:
                bot.send_document(channel_id, data['first_file_id'])
            else:
                bot.send_photo(channel_id, data['first_file_id'])

            if data['is_document_second']:
                bot.send_document(channel_id, data['second_file_id'])
            else:
                bot.send_photo(channel_id, data['second_file_id'])

            bot.send_message(channel_id, caption_text, parse_mode="HTML")

        time.sleep(5)
        return start(call.message)

    elif call.data == "cancel":
        bot.send_message(chat_id, cancel_message[lang])
        return start(call.message)

    user_data.pop(chat_id, None)


bot.polling(non_stop=True)


