from pyrogram.types import InlineKeyboardMarkup
from config import SUPPORT_CHAT
from ANIYAXMUSIC.utils.inline.start import api_btn  # Assuming api_btn is here


def botplaylist_markup(_):
    buttons = [
        [
            api_btn(text=_["S_B_9"], url=SUPPORT_CHAT, style="primary"),
            api_btn(text=_["CLOSE_BUTTON"], callback_data="close", style="danger"),
        ],
    ]
    return buttons


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                api_btn(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style="danger"
                ),
            ]
        ]
    )
    return upl


def supp_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                api_btn(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                    style="primary"
                ),
            ]
        ]
    )
    return upl