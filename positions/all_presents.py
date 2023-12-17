from positions.positions_content import (RUSSIA,
                                         CONTACTS_US,
                                         name_pozition,
                                         halva_cost,
                                         present_cost)
from settings import MIDDLE_PRESENT, SMALL_PRESENTS, SWEET_TUBLE
from all_emoji.emoji_button_and_tea import *
from all_emoji.emoji_aliases import *
smile_agree = '\u2705'


exclamation_mark_1 = '\u2757'


present_middle = (
    f"{name_pozition(MIDDLE_PRESENT)}\n"
    "\n"
    f"{RUSSIA}\n"
    "\n"
    "<b>Состав набора:</b>\n"
    f"{smile_agree} Импортный фруктовый{smile_cherries} / травяной{smile_herb} чай 75г.\n"
    "\n"
    f"{smile_agree} Мёд-суфле{smile_honey_pot} 40г.\n"
    "\n"
    f"{smile_agree} Халва манго{smile_mango} / шоколад{smile_choco} / гранат{smile_granade} 100гр.\n"
    "\n"
    f"{smile_agree} Нежный молочный шоколад{smile_chocolate} baby fox {smile_fox_face} 1шт.\n"
    "\n"
    f"{smile_agree} Мини шоколадки Ritter sport{smile_chocolate} 3шт.\n"
    "\n"
    f"{smile_agree} Конфеты baby fox {smile_fox_face} 3шт.\n"
    "\n"
    f"{smile_agree} Нежные конфеты с манго {smile_mango} 3шт.\n"
    "\n"
    f"{exclamation_mark_1}ВАЖНО{exclamation_mark_1}\n"
    "Подарочный набор можно изменять в зависимости от запроса!\n"
    "\n"
    f"{present_cost(1050, MIDDLE_PRESENT)}"
    "\n"
    f"{CONTACTS_US}"
)

present_small = (
    f"{name_pozition(SMALL_PRESENTS)}\n"
    "\n"
    f"{RUSSIA}\n"
    "\n"
    "<b>Состав набора:</b>\n"
    f"{smile_agree} Импортный фруктовый{smile_cherries} / травяной{smile_herb} чай в упаковке (75г).\n"
    "\n"
    f"{smile_agree} Небольшой набор халвы и рахата (MIX)\n"
    "\n"
    "Вес бокса ---> 400 гр.\n"
    f"{present_cost(750, SMALL_PRESENTS)}"
    "\n"
    f"{CONTACTS_US}"
)

tuble_sweet = (
    f"{name_pozition(SWEET_TUBLE)}\n"
    "\n"
    f"{RUSSIA}\n"
    "\n"
    "<b>Состав набора:</b>\n"
    f"{smile_agree} Халва Шоколад\n"
    f"{smile_agree} Халва Манго\n"
    f"{smile_agree} Халва Клубника\n"
    f"{smile_agree} Халва Смородина\n"
    f"{smile_agree} Халва Сливочная\n"
    f"{smile_agree} Халва Черника\n"
    f"{smile_agree} Халва Гранат\n"
    f"{smile_agree} Халва Двойной Шоколад\n"
    f"{smile_agree} Рахат 4 вкуса\n"
    "\n"
    "Вес бокса ---> 800 гр. \n"
    "\n"
    f"{present_cost(1050, SWEET_TUBLE)}\n"
    "\n"
    f"{CONTACTS_US}"
)
