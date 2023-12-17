from all_emoji.emoji_button_and_tea import smile_tea, shortcake
from all_emoji.emoji_aliases import list_of_smile_for_aliases
from script_phrase import text_for_about, text_contact_us
from settings import *
from utils import random_smile, handlers_send, handler_cat


def say_hi(update, context):
    text_message = f"Привет! Я твой чайный бот! Я помогу тебе выбрать чай {smile_tea} и сладости {shortcake} к нему!"
    handler_cat(update, context, text_message, BUTTON_HI)


def back_to_menu(update, context):
    id = update.message.from_user.id
    context.bot.send_message(id,
                             text=f'Основное меню',
                             reply_markup=BUTTON_HI)


def about(update, context):
    image_path_1 = 'pictures/another_photo/about.jpg'
    handlers_send(update, context, image_path_1, text_for_about)


def contact_us(update, context):
    image_path_1 = 'pictures/another_photo/about.jpg'
    handlers_send(update, context, image_path_1, text_contact_us)
