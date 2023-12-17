from all_emoji.emoji_aliases import smiling_face_sith_halo
from positions.all_teas import *
from settings import *
from utils import handlers_send, handler_cat


'''CATEGORY'''
def cat_tea(update, context):
    text_message = "Вот все категории чая:"
    handler_cat(update, context, text_message, BUTTON_CATEGORY)


def cat_green_tea(update, context):
    text_message = f"Вот все зелёные чаи. Можешь нажать на нужный чай и я расскажу тебе о нём более подробно {smiling_face_sith_halo}"
    handler_cat(update, context, text_message, BUTTON_CAT_GREEN_TEA)


def cat_fruit_tea(update, context):
    text_message = f"Вот все фруктовые чаи. Можешь нажать на нужный чай и я расскажу тебе о нём более подробно {smiling_face_sith_halo}"
    handler_cat(update, context, text_message, BUTTON_CAT_FRUIT_TEA)


def cat_ulun_tea(update, context):
    text_message = f"Вот все улуны. Можешь нажать на нужный чай и я расскажу тебе о нём более подробно {smiling_face_sith_halo}"
    handler_cat(update, context, text_message, BUTTON_CAT_ULUN_TEA)


def cat_grass_tea(update, context):
    text_message = f"Вот все травяные чаи. Можешь нажать на нужный чай и я расскажу тебе о нём более подробно {smiling_face_sith_halo}"
    handler_cat(update, context, text_message, BUTTON_CAT_GRASS_TEA)


def cat_black(update, context):
    text_message = f"Вот все черные чаи. Можешь нажать на нужный чай и я расскажу тебе о нём более подробно {smiling_face_sith_halo}"
    handler_cat(update, context, text_message, BUTTON_CAT_BLACK_TEA)


def cat_puer(update, context):
    text_message = f"Вот все пуэры. Можешь нажать на нужный чай и я расскажу тебе о нём более подробно {smiling_face_sith_halo}"
    handler_cat(update, context, text_message, BUTTON_CAT_PUER_TEA)


'''TEA POSITION'''
def cherries_tea(update, context):
    image_path_1 = 'pictures/photos_tea/cherries.jpg'
    handlers_send(update, context, image_path_1, tea_cherries)


def impudent_fruit_tea(update, context):
    image_path_1 = 'pictures/photos_tea/impudent_fruit.jpg'
    handlers_send(update, context, image_path_1, tea_impudent_fruit)


def glint_tea(update, context):
    image_path_1 = 'pictures/photos_tea/glint.jpg'
    handlers_send(update, context, image_path_1, tea_glint)


def mint_raspberry_tea(update, context):
    image_path_1 = 'pictures/photos_tea/mint_raspberry.jpg'
    handlers_send(update, context, image_path_1, tea_mint_raspberry)


def mao_fen_tea(update, context):
    image_path_1 = 'pictures/photos_tea/mao_fen.jpg'
    handlers_send(update, context, image_path_1, tea_mao_fen)


def uzbek_95_tea(update, context):
    image_path_1 = 'pictures/photos_tea/uzbek_95.jpg'
    handlers_send(update, context, image_path_1, tea_uzbek_95)


def da_hun_pao_tea(update, context):
    image_path_1 = 'pictures/photos_tea/da_hun_pao.jpg'
    handlers_send(update, context, image_path_1, tea_da_hun_pao)


def shen_ulun_tea(update, context):
    image_path_1 = 'pictures/photos_tea/shen_ulun.jpg'
    handlers_send(update, context, image_path_1, tea_shen_ulun)


def milk_ulun_tea(update, context):
    image_path_1 = 'pictures/photos_tea/milk_ulun.jpg'
    handlers_send(update, context, image_path_1, tea_milk_ulun)


def te_guan_in_tea(update, context):
    image_path_1 = 'pictures/photos_tea/te_guan_in.jpg'
    handlers_send(update, context, image_path_1, tea_te_guan_in)


def sunset_tea(update, context):
    image_path_1 = 'pictures/photos_tea/sunset.jpg'
    handlers_send(update, context, image_path_1, tea_sunset)


def sweet_ginger_tea(update, context):
    image_path_1 = 'pictures/photos_tea/sweet_ginger.jpg'
    handlers_send(update, context, image_path_1, tea_sweet_ginger)


def mint_raspberry_2_tea(update, context):
    image_path_1 = 'pictures/photos_tea/mint_raspberry_2.jpg'
    handlers_send(update, context, image_path_1, tea_mint_raspberry_2)


def healthy_sleep_tea(update, context):
    image_path_1 = 'pictures/photos_tea/healthy_sleep.jpg'
    handlers_send(update, context, image_path_1, tea_healthy_sleep)


def goji_tea(update, context):
    image_path_1 = 'pictures/photos_tea/goji.jpg'
    handlers_send(update, context, image_path_1, tea_goji)


def melisa_raspberry_tea(update, context):
    image_path_1 = 'pictures/photos_tea/melisa_raspberry.jpg'
    handlers_send(update, context, image_path_1, tea_melisa_raspberry)


def blackberry_tea(update, context):
    image_path_1 = 'pictures/photos_tea/blackberry.jpg'
    handlers_send(update, context, image_path_1, tea_blackberry)


def night_1001_tea(update, context):
    image_path_1 = 'pictures/photos_tea/night_1001.jpg'
    handlers_send(update, context, image_path_1, tea_night_1001)


def sencha_tea(update, context):
    image_path_1 = 'pictures/photos_tea/sencha.jpg'
    handlers_send(update, context, image_path_1, tea_sencha)


def erl_gray_tea(update, context):
    image_path_1 = 'pictures/photos_tea/erl_gray.jpg'
    handlers_send(update, context, image_path_1, tea_erl_gray)


def puer_home_tea(update, context):
    image_path_1 = 'pictures/photos_tea/puer_home.jpg'
    handlers_send(update, context, image_path_1, tea_puer_home)


def assam_fop_tea(update, context):
    image_path_1 = 'pictures/photos_tea/assam_fop.jpg'
    handlers_send(update, context, image_path_1, tea_assam_fop)
