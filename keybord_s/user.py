#by @K1p1k#
#Downloaded from TG @KiTools#
#Leave this inscription#

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.db import get_AllChennel, get_Allplayer
from misc.plugin.KinoPoiskFree import get_FilmsMe
from .ohter import ikb_close_oikb

#получения листа о подписках#
async def sub_list():
    data_chennel=await get_AllChennel()
    sub_list=InlineKeyboardMarkup(row_width=1)
    for i in data_chennel:
        sub_list.add(InlineKeyboardButton(text=i[1], url=i[2]))
    sub_list.add(InlineKeyboardButton(text='Одна из сыллок не работает❓', callback_data='link_no_work'))
    return sub_list

#кнопки для просмотра кино с бесплатным плеером#
async def kb_films(name_films):
    ikb=InlineKeyboardMarkup(row_width=1)
    for i in await get_Allplayer():
        if i[2]:
            try:
                url=await get_FilmsMe(name=name_films, web=i[0])
                ikb.row(InlineKeyboardButton(text=i[3], url=url))
            except:
                pass
    ikb.row(ikb_close_oikb)
    return ikb

#Автор: @K1p1k#
#Загружено с TG @KiTools#
#Оставь эту надпись#