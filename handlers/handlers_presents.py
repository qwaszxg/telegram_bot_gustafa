from utils import handlers_send_presents, handler_cat
from positions.all_presents import present_middle, present_small, tuble_sweet
from settings import BUTTON_PRESENTS_CAT


def present(update, context):
    text_message = "Вот все наши подарки:"
    handler_cat(update, context, text_message, BUTTON_PRESENTS_CAT)


def middle_present(update, context):
    image_path_1 = 'pictures/photo_presents/middle_present_1.jpg'
    image_path_2 = 'pictures/photo_presents/middle_present_2.jpg'
    description_product = present_middle
    handlers_send_presents(update, context, image_path_1, image_path_2, description_product)

def small_present(update, context):
    image_path_1 = 'pictures/photo_presents/small_present_1.jpg'
    image_path_2 = 'pictures/photo_presents/small_present_2.jpg'
    description_product = present_small
    handlers_send_presents(update, context, image_path_1, image_path_2, description_product)


def sweet_tuble(update, context):
    image_path_1 = 'pictures/photo_presents/sweet_tuble_1.jpg'
    image_path_2 = 'pictures/photo_presents/sweet_tuble_2.jpg'
    description_product = tuble_sweet
    handlers_send_presents(update, context, image_path_1, image_path_2, description_product)

