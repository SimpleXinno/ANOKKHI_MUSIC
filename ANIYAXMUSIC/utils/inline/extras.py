from pyrogram.types import InlineKeyboardMarkup
from config import SUPPORT_CHAT
from ANIYAXMUSIC.utils.inline.buttons import inline


def botplaylist_markup(_):
    return inline.ikm(
        [
            [
                inline._button(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                    category="primary",
                ),
                inline._button(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    category="danger",
                ),
            ],
        ]
    )


def close_markup(_):
    return inline.ikm(
        [
            [
                inline._button(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    category="danger",
                ),
            ]
        ]
    )


def supp_markup(_):
    return inline.ikm(
        [
            [
                inline._button(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                    category="primary",
                ),
            ]
        ]
    )
