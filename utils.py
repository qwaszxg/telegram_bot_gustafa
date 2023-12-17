from random import choice

from telegram.ext import MessageHandler, Filters
from telegram import ParseMode, InputMediaPhoto

from all_emoji.emoji_aliases import list_of_smile_for_aliases
from settings import updater


def random_smile(list_of_smile):
    smile = choice(list_of_smile)
    return smile


def message_handler(text_reactions, tea_cat):
    return updater.dispatcher.add_handler(MessageHandler(Filters.text(text_reactions), tea_cat))


def handlers_send(update, context, photo, tea):
    image_path_1 = photo
    user_id = update.message.from_user.id
    with open(image_path_1, 'rb') as photo:
        context.bot.send_photo(user_id,
                               photo=photo,
                               caption=tea,
                               parse_mode=ParseMode.HTML)


def handler_cat(update, context, text_message, markup):
    user_name = update.message.from_user.first_name
    id = update.message.from_user.id
    smile = random_smile(list_of_smile_for_aliases)
    context.bot.send_message(id, text=f'{smile} {user_name}, {text_message}', reply_markup=markup)



def handlers_send_presents(update, context, photo_1, photo_2, tea):
    image_path_1 = photo_1
    image_path_2 = photo_2
    user_id = update.message.from_user.id
    with open(image_path_1, 'rb') as photo1, open(image_path_2, 'rb') as photo2:
        caption = f'<b>{tea}</b>'
        context.bot.send_media_group(user_id, [
            InputMediaPhoto(media=photo1),
            InputMediaPhoto(media=photo2)
        ], reply_markup=None, timeout=None)
        context.bot.send_message(user_id, text=caption, parse_mode=ParseMode.HTML)
