from telebot import types

from localization.lang import *


def generate_main_menu(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_1 = types.KeyboardButton(text=menu_milliy[lang])
    btn_2 = types.KeyboardButton(text=menu_qoqon[lang])
    btn_3 = types.KeyboardButton(text=menu_osio[lang])
    btn_4 = types.KeyboardButton(text=setting[lang])
    btn_5 = types.KeyboardButton(text=call[lang])
    keyboard.row(btn_1, btn_2, btn_3)
    keyboard.row(btn_4, btn_5)
    return keyboard



def generate_faculty(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_1 = types.KeyboardButton(text=faculty1[lang])
    btn_2 = types.KeyboardButton(text=faculty2[lang])
    btn_3 = types.KeyboardButton(text=faculty3[lang])
    keyboard.row(btn_1, btn_2, btn_3)
    return keyboard


def share_contact(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn = types.KeyboardButton(text=send_contact[lang], request_contact=True)
    keyboard.row(btn)
    return keyboard


def commit(lang):
    markup = types.InlineKeyboardMarkup(row_width=2)
    yes_button = types.InlineKeyboardButton(send[lang], callback_data="confirm")
    no_button = types.InlineKeyboardButton(cancel[lang], callback_data="cancel")
    markup.add(yes_button, no_button)
    return markup


def settings(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    language = types.KeyboardButton(text=select_language[lang])
    back = types.KeyboardButton(text=back_to[lang])

    keyboard.row(language)
    keyboard.row(back)
    return keyboard


def generate_connect(url1, url2, lang):
    keyboard = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text=more[lang], url=url1)
    btn_2 = types.InlineKeyboardButton(text=message_admin[lang], url=url2)
    back = types.InlineKeyboardButton(text=back_to[lang], callback_data="back")
    keyboard.row(btn_1, btn_2)
    keyboard.row(back)
    return keyboard


def select_lang(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    uz = types.KeyboardButton(text="🇺🇿Uz")
    ru = types.KeyboardButton(text="🇷🇺Ru")
    en = types.KeyboardButton(text="🇬🇧En")
    back = types.KeyboardButton(text=back_to[lang])

    keyboard.row(uz, ru, en)
    keyboard.row(back)
    return keyboard


def social(url1, url2, lang):
    keyboard = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text=app[lang], url=url1)
    btn_2 = types.InlineKeyboardButton(text=app_store[lang], url=url2)
    keyboard.row(btn_1, btn_2)
    return keyboard