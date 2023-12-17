from all_emoji.emoji_aliases import list_of_smile_for_aliases
from positions.all_halva import *
from settings import BUTTON_HALVA_CAT
from utils import handlers_send, random_smile, handler_cat


'''HALVA'''
def halva(update, context):
    text_message = "Вот все наши сладости:"
    handler_cat(update, context, text_message, BUTTON_HALVA_CAT)


def halva_chocolate(update, context):
    image_path_1 = 'pictures/photos_halva/halva_choco.jpg'
    handlers_send(update, context, image_path_1, chocolate_halva)


def halva_strawberry(update, context):
    image_path_1 = 'pictures/photos_halva/halva_straw.jpg'
    handlers_send(update, context, image_path_1, strawberry_halva)


def halva_currant(update, context):
    image_path_1 = 'pictures/photos_halva/halva_black.jpg'
    handlers_send(update, context, image_path_1, currant_halva)


def halva_mango(update, context):
    image_path_1 = 'pictures/photos_halva/halva_mango.jpg'
    handlers_send(update, context, image_path_1, mango_halva)


def halva_garnet(update, context):
    image_path_1 = 'pictures/photos_halva/halva_garnet.jpg'
    handlers_send(update, context, image_path_1, garnet_halva)


def halva_zebra_choko(update, context):
    image_path_1 = 'pictures/photos_halva/halva_zebra_choko.jpg'
    handlers_send(update, context, image_path_1, zebra_choko_halva)


def halva_creamy(update, context):
    image_path_1 = 'pictures/photos_halva/halva_creamy.jpg'
    handlers_send(update, context, image_path_1, creamy_halva)


def halva_blueberries(update, context):
    image_path_1 = 'pictures/photos_halva/halva_blueberries.jpg'
    handlers_send(update, context, image_path_1, blueberries_halva)


def halva_rahat(update, context):
    image_path_1 = 'pictures/photos_halva/halva_rahat.jpg'
    handlers_send(update, context, image_path_1, rahat)
