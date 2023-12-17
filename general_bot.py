from telegram.ext import CommandHandler

from handlers.handlers_halva import *
from handlers.handlers_menu import *
from handlers.handlers_tea import *
from handlers.handlers_presents import *
from settings import *
from utils import message_handler


def main():
    updater.dispatcher.add_handler(CommandHandler('start', say_hi))

    '''GENERAL BUTTONS'''
    message_handler(BUTTON_BACK_IN_MENU, back_to_menu)
    message_handler(BUTON_CAT, cat_tea)
    message_handler(BUTTON_ABOUT, about)
    message_handler(BUTTON_CONTACT_US, contact_us)

    '''PRESENTS'''
    message_handler(BUTTON_PRESENTS, present)
    message_handler(MIDDLE_PRESENT, middle_present)
    message_handler(SMALL_PRESENTS, small_present)
    message_handler(SWEET_TUBLE, sweet_tuble)

    '''HALVA'''
    message_handler(BUTTON_HALVA, halva)
    message_handler(CHOCOLATE_HALVA, halva_chocolate)
    message_handler(STRAWBERRY_HALVA, halva_strawberry)
    message_handler(CURRANT_HALVA, halva_currant)
    message_handler(MANGO_HALVA, halva_mango)

    message_handler(GARNET_HALVA, halva_garnet)
    message_handler(ZEBRA_CHOKO_HALVA, halva_zebra_choko)
    message_handler(CREAMY_HALVA, halva_creamy)
    message_handler(BLUEBERRIES_HALVA, halva_blueberries)
    message_handler(RAHAT, halva_rahat)

    '''FRUIT TEAS'''
    message_handler(BUTTON_FRUIT, cat_fruit_tea)
    message_handler(CHERRIES, cherries_tea)
    message_handler(GLINT, glint_tea)
    message_handler(IMPUDENT_FRUIT, impudent_fruit_tea)

    '''GREEN TEAS'''
    message_handler(BUTTON_GREEN, cat_green_tea)
    message_handler(MAO_FEN, mao_fen_tea)
    message_handler(MINT_RASPBERRY, mint_raspberry_tea)
    message_handler(UZBEK_95, uzbek_95_tea)
    message_handler(GOJI, goji_tea)
    message_handler(NIGHT_1001, night_1001_tea)
    message_handler(SENCHA, sencha_tea)

    '''ULUN TEAS'''
    message_handler(BUTTON_ULUN, cat_ulun_tea)
    message_handler(DA_HUN_PAO, da_hun_pao_tea)
    message_handler(SHEN_ULUN, shen_ulun_tea)
    message_handler(MILK_ULUN, milk_ulun_tea)
    message_handler(TE_GUAN_IN, te_guan_in_tea)

    '''GRASS TEA'''
    message_handler(BUTTON_GRASS, cat_grass_tea)
    message_handler(SUNSET, sunset_tea)
    message_handler(SWEET_GINGER, sweet_ginger_tea)
    message_handler(MINT_RASPBERRY_2, mint_raspberry_2_tea)
    message_handler(HEALTHY_SLEEP, healthy_sleep_tea)

    '''BLACK TEA'''
    message_handler(BUTTON_BLACK, cat_black)
    message_handler(MELISA_RASPBERRY, melisa_raspberry_tea)
    message_handler(BLACKBERRY, blackberry_tea)
    message_handler(ASSAM_FOP, assam_fop_tea)
    message_handler(ERL_GRAY, erl_gray_tea)
    #NIGHT_1001 in GREEN TEA

    '''PUER_TEA'''
    message_handler(BUTTON_PUER, cat_puer)
    message_handler(PUER_HOME, puer_home_tea)

    updater.start_polling(poll_interval=0.1)
    updater.idle()

if __name__ == "__main__":
    main()
