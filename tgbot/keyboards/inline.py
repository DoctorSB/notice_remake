from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tgbot.misc.json_work import json_read, output_all, task_output


accept_button = [[InlineKeyboardButton(text="Принять", callback_data="accept")],
                 [InlineKeyboardButton(text="Отклонить", callback_data="cancel")]]

task_keyboard = InlineKeyboardMarkup(inline_keyboard=accept_button)


def task_preview_keyboard(json_file):
    data = json_read(json_file)
    keyboard = []
    for key in data:
        keyboard.append([InlineKeyboardButton(text=key, callback_data=key)])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

