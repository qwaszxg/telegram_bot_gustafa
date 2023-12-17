from all_emoji.emoji_button_and_tea import (smile_germany,
                                            smile_india,
                                            smile_china,
                                            smile_russia,
                                            smile_uzb)
from all_emoji.emoji_aliases import down_arrow, smile_right_arrow
from settings import ILYA_TG, ILYA_VK, VK_GROUP


#NAME
def name_pozition(name):
    return f"<b>Название:</b>\n {name}"



#COUNTRY
GERMANY = f'<b>Страна:</b> Германия {smile_germany}'
INDIA = f'<b>Страна:</b> Индия {smile_india}'
CHINA = f'<b>Страна:</b> Китай {smile_china}'
RUSSIA = f'<b>Страна:</b> Россия {smile_russia}'
UZB = f'<b>Страна:</b> Узбекистан {smile_uzb}'


#COST
def present_cost(price_box, box_name):
    cost = (
        f"<b>Стоимость:</b> \n"
        f"Подарочный бокс {smile_right_arrow} {price_box} Рублей.\n"
        "\n"
        f"{down_arrow}Оформить заказ на:{down_arrow}\n"
        f"{box_name}\n"
    )
    return cost

def halva_cost(price_100g, price_1kg, halva_name):
    cost = (
        f"<b>Стоимость:</b> \n"
        f"100 гр {smile_right_arrow} {price_100g} Рублей.\n"
        f"1 кг {smile_right_arrow} {price_1kg} Рублей.\n"
        "\n"
        f"{down_arrow}Оформить заказ на:{down_arrow}\n"
        f"{halva_name}\n"
    )
    return cost

def tea_cost(price_100g, price_500g, tea_name):
    cost = (
        f"<b>Стоимость:</b> \n"
        f"100 гр {smile_right_arrow} {price_100g} Рублей.\n"
        f"500 гр {smile_right_arrow} {price_500g} Рублей.\n"
        "\n"
        f"{down_arrow}Оформить заказ на:{down_arrow}\n"
        f"{tea_name}\n"
    )
    return cost


#CONTACTS
CONTACTS_US = (
    f"Телеграмм: {ILYA_TG}\n"
    f"ВК: {ILYA_VK}\n"
    f"Группа ВК: {VK_GROUP}\n"
)
