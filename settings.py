import os

from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater
from dotenv import load_dotenv

from all_emoji.emoji_button_and_tea import *
from all_emoji.emoji_aliases import (smile_seedling,
                                     smile_green_book,
                                     smile_blue_book,
                                     smile_love_letter,
                                     smile_left_arrow,
                                     smile_right_arrow,
                                     smile_gift)



load_dotenv()

'''admins'''
PHONE_ILYA = os.getenv('PHONE_ILYA')
ILYA_VK = os.getenv('ILYA_VK')
ILYA_TG = os.getenv('ILYA_TG')
ILYA_ID = os.getenv('ILYA_ID')
VK_GROUP = os.getenv('GROUP_VK')

PHONE_ANDREY = os.getenv('PHONE_ANDREY')
ANDREY_VK = os.getenv('ANDREY_VK')
ANDREY_TG = os.getenv('ANDREY_TG')
ANDREY_ID = os.getenv('ANDREY_ID')

TOKEN = os.getenv('TOKEN')
updater = Updater(token=TOKEN, use_context=True)


'''BUTTON NAME'''
# teas
BUTTON_GREEN = f'{smile_herb} Зелёные {smile_herb}'
BUTTON_FRUIT = f'{smile_cherries} Фруктовые {smile_kiwi_fruit}'
BUTTON_ULUN = f'{smile_leaf_fluttering_in_wind} Улуны {smile_leaf_fluttering_in_wind}'
BUTTON_GRASS = f'{smile_seedling} Травяные {smile_seedling}'
BUTTON_BLACK = f'{smile_leaf_fluttering_in_wind} Черные {smile_herb}'
BUTTON_PUER = f'{smile_crown} Пуэры {smile_crown}'

# general buttons
BUTON_CAT = f'{smile_tea}Категории{shortcake}'
BUTTON_BACK_IN_MENU = f'{smile_right_arrow} Вернуться в меню {smile_left_arrow}'
BUTTON_ABOUT = f'{smile_green_book}О нас{smile_blue_book}'
BUTTON_CONTACT_US= f'{smile_love_letter}Связь с нами{smile_love_letter}'

# sweet button
BUTTON_HALVA = f'{shortcake} Сладости к чаю {shortcake}'

# presents button
BUTTON_PRESENTS = f'{smile_gift} Подарочные наборы {smile_gift}'

# button after command \start
BUTTON_HI = ReplyKeyboardMarkup([[BUTON_CAT],
                                 [BUTTON_ABOUT],
                                 [BUTTON_CONTACT_US]],
                                 resize_keyboard=True)

# button after BUTTON_CAT
BUTTON_CATEGORY = ReplyKeyboardMarkup([[BUTTON_GREEN, BUTTON_FRUIT],
                                      [BUTTON_ULUN, BUTTON_GRASS],
                                      [BUTTON_BLACK, BUTTON_PUER],
                                      [BUTTON_HALVA],
                                      [BUTTON_PRESENTS],
                                      [BUTTON_BACK_IN_MENU]], resize_keyboard=True)

# presents
MIDDLE_PRESENT = f"{smile_gift} Средний подарочный набор {smile_gift}"
SMALL_PRESENTS = f"{smile_gift} Маленький подарочный набор {smile_gift}"
SWEET_TUBLE = f"{smile_gift} Сладкий стол {smile_gift}"

BUTTON_PRESENTS_CAT = ReplyKeyboardMarkup([[MIDDLE_PRESENT],
                                           [SMALL_PRESENTS],
                                           [SWEET_TUBLE],
                                           [BUTTON_BACK_IN_MENU, BUTON_CAT]],
                                           resize_keyboard=True)


# halva
CHOCOLATE_HALVA = f'{smile_choco} Халва Шоколад {smile_choco}'
STRAWBERRY_HALVA = f'{smile_strawberry} Халва Клубника {smile_strawberry}'
CURRANT_HALVA = f'{candy} Халва Смородина {candy}'
MANGO_HALVA = f'{smile_mango} Халва Манго {smile_mango}'
GARNET_HALVA = f'{smile_granade}Халва Гранат{smile_granade}'
ZEBRA_CHOKO_HALVA = f'{smile_chocolate} Двойной шоколад {smile_ice_cream}'
CREAMY_HALVA = f'{smile_ice_cream} Халва Сливочная {smile_ice_cream}'
BLUEBERRIES_HALVA = f'{smile_blueberry} Халва Черника {smile_blueberry}'
RAHAT = f'{smile_peanut} Рахат Микс {smile_chestnut}'

BUTTON_HALVA_CAT = ReplyKeyboardMarkup([[CHOCOLATE_HALVA],
                                        [MANGO_HALVA],
                                        [CURRANT_HALVA],
                                        [STRAWBERRY_HALVA],
                                        [GARNET_HALVA],
                                        [ZEBRA_CHOKO_HALVA],
                                        [CREAMY_HALVA],
                                        [BLUEBERRIES_HALVA],
                                        [RAHAT],
                                        [BUTTON_BACK_IN_MENU, BUTON_CAT]],
                                        resize_keyboard=True)


# green tea
MINT_RASPBERRY = f'{smile_rose} Мятная малина {smile_seedling}'
MAO_FEN = f'{smile_herb} Мао Фен с жасмином {smile_herb}'
UZBEK_95 = f'{smile_leaf_fluttering_in_wind} Узбекский № 95 {smile_leaf_fluttering_in_wind}'
GOJI = f'{smile_seedling} Годжи Облепиха {smile_leaf_fluttering_in_wind}'
NIGHT_1001 = f'{smile_leaf_fluttering_in_wind} 1001 ночь {smile_leaf_fluttering_in_wind}'
SENCHA = f'{smile_herb} Сенча {smile_herb}'

BUTTON_CAT_GREEN_TEA = ReplyKeyboardMarkup([[MINT_RASPBERRY],
                                            [MAO_FEN],
                                            [UZBEK_95],
                                            [GOJI],
                                            [NIGHT_1001],
                                            [SENCHA],
                                            [BUTTON_BACK_IN_MENU, BUTON_CAT]],
                                            resize_keyboard=True)


# fruit tea
IMPUDENT_FRUIT = f'{smile_grapes} Наглый фрукт {smile_apple}'
CHERRIES = f'{smile_cherries} Вишенка {smile_cherries}'
GLINT = f'{smile_green_apple} Глинтвейн {smile_tangerine}'

BUTTON_CAT_FRUIT_TEA = ReplyKeyboardMarkup([[IMPUDENT_FRUIT],
                                            [CHERRIES],
                                            [GLINT],
                                            [BUTTON_BACK_IN_MENU, BUTON_CAT]],
                                            resize_keyboard=True)


# ulun tea
DA_HUN_PAO = f'{smile_peach} Да Хун Пао {smile_leaf_fluttering_in_wind}'
SHEN_ULUN = f'{smile_leaf_fluttering_in_wind} Женьшень улун {smile_leaf_fluttering_in_wind}'
MILK_ULUN = f'{smile_herb} Молочный улун {smile_herb}'
TE_GUAN_IN = f'{smile_seedling} Те Гуань Инь {smile_seedling}'

BUTTON_CAT_ULUN_TEA = ReplyKeyboardMarkup([[DA_HUN_PAO],
                                           [SHEN_ULUN],
                                           [MILK_ULUN],
                                           [TE_GUAN_IN],
                                           [BUTTON_BACK_IN_MENU, BUTON_CAT]],
                                           resize_keyboard=True)


# grass tea
SUNSET = f'{smile_sunset} Закат {smile_seedling}'
SWEET_GINGER = f'{smile_lemon} Сладкий имбирь {smile_leaf_fluttering_in_wind}'
MINT_RASPBERRY_2 = f'{smile_hibiscus} Малина-мята {smile_sunflower}'
HEALTHY_SLEEP = f'{smile_leaf_fluttering_in_wind} Здоровый сон {smile_green_apple}'

BUTTON_CAT_GRASS_TEA = ReplyKeyboardMarkup([[SUNSET],
                                            [SWEET_GINGER],
                                            [MINT_RASPBERRY_2],
                                            [HEALTHY_SLEEP],
                                            [BUTTON_BACK_IN_MENU, BUTON_CAT]],
                                            resize_keyboard=True)


# black tea
MELISA_RASPBERRY = f'{smile_hibiscus} Мелисса малина {smile_lemon}'
BLACKBERRY = f'{smile_hibiscus} Ежевичная поляна {smile_leaf_fluttering_in_wind}'
#NIGHT_1001 in GREEN TEA TOO
ASSAM_FOP = f'{smile_herb} Ассам FOP {smile_herb}'
ERL_GRAY = f'{smile_leaf_fluttering_in_wind} Эрл Грей {smile_leaf_fluttering_in_wind}'

BUTTON_CAT_BLACK_TEA = ReplyKeyboardMarkup([[MELISA_RASPBERRY],
                                            [NIGHT_1001],
                                            [ASSAM_FOP],
                                            [ERL_GRAY],
                                            [BLACKBERRY],
                                            [BUTTON_BACK_IN_MENU, BUTON_CAT]],
                                            resize_keyboard=True)


# puer tea
PUER_HOME = f'{smile_castle} Пуэр дворцовый {smile_castle}'

BUTTON_CAT_PUER_TEA = ReplyKeyboardMarkup([[PUER_HOME],
                                           [BUTTON_BACK_IN_MENU, BUTON_CAT]],
                                           resize_keyboard=True)
