from typing import Union
from ANIYAXMUSIC import app
from ANIYAXMUSIC.utils.inline.start import api_btn


def help_pannel(_, START: Union[bool, int] = None):
    first = [api_btn(text=_["CLOSE_BUTTON"], callback_data="close", style="danger")]
    second = [
        api_btn(text=_["BACK_PAGE"], callback_data="mbot_cb", style="primary"),
        api_btn(text=_["BACK_BUTTON"], callback_data="settingsback_helper", style="primary"),
        api_btn(text=_["NEXT_PAGE"], callback_data="mbot_cb", style="success"),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                api_btn(text=_["H_B_1"], callback_data="help_callback hb1", style="primary"),
                api_btn(text=_["H_B_2"], callback_data="help_callback hb2", style="primary"),
                api_btn(text=_["H_B_3"], callback_data="help_callback hb3", style="primary"),
            ],
            [
                api_btn(text=_["H_B_4"], callback_data="help_callback hb4", style="primary"),
                api_btn(text=_["H_B_5"], callback_data="help_callback hb5", style="primary"),
                api_btn(text=_["H_B_6"], callback_data="help_callback hb6", style="primary"),
            ],
            [
                api_btn(text=_["H_B_7"], callback_data="help_callback hb7", style="primary"),
                api_btn(text=_["H_B_8"], callback_data="help_callback hb8", style="primary"),
                api_btn(text=_["H_B_9"], callback_data="help_callback hb9", style="primary"),
            ],
            [
                api_btn(text=_["H_B_10"], callback_data="help_callback hb10", style="primary"),
                api_btn(text=_["H_B_11"], callback_data="help_callback hb11", style="primary"),
                api_btn(text=_["H_B_12"], callback_data="help_callback hb12", style="primary"),
            ],
            [
                api_btn(text=_["H_B_13"], callback_data="help_callback hb13", style="primary"),
                api_btn(text=_["H_B_14"], callback_data="help_callback hb14", style="primary"),
                api_btn(text=_["H_B_15"], callback_data="help_callback hb15", style="primary"),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                api_btn(text=_["BACK_BUTTON"], callback_data="settings_back_helper", style="primary"),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            api_btn(text=_["S_B_4"], url=f"https://t.me/{app.username}?start=help", style="success"),
        ],
    ]
    return buttons