from typing import Union

from ANIYAXMUSIC import app
from ANIYAXMUSIC.utils.inline.buttons import inline


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        inline._button(
            text=_["CLOSE_BUTTON"],
            callback_data="close",
            category="danger",
        )
    ]

    second = [
        inline._button(
            text=_["BACK_PAGE"],
            callback_data="mbot_cb",
            category="primary",
        ),
        inline._button(
            text=_["BACK_BUTTON"],
            callback_data="settingsback_helper",
            category="primary",
        ),
        inline._button(
            text=_["NEXT_PAGE"],
            callback_data="mbot_cb",
            category="success",
        ),
    ]

    mark = second if START else first

    return inline.ikm(
        [
            [
                inline._button(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1",
                    category="primary",
                ),
                inline._button(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                    category="primary",
                ),
                inline._button(
                    text=_["H_B_3"],
                    callback_data="help_callback hb3",
                    category="primary",
                ),
            ],
            [
                inline._button(
                    text=_["H_B_4"],
                    callback_data="help_callback hb4",
                    category="primary",
                ),
                inline._button(
                    text=_["H_B_5"],
                    callback_data="help_callback hb5",
                    category="primary",
                ),
                inline._button(
                    text=_["H_B_6"],
                    callback_data="help_callback hb6",
                    category="primary",
                ),
            ],
            [
                inline._button(
                    text=_["H_B_7"],
                    callback_data="help_callback hb7",
                    category="primary",
                ),
                inline._button(
                    text=_["H_B_8"],
                    callback_data="help_callback hb8",
                    category="primary",
                ),
                inline._button(
                    text=_["H_B_9"],
                    callback_data="help_callback hb9",
                    category="primary",
                ),
            ],
            [
                inline._button(
                    text=_["H_B_10"],
                    callback_data="help_callback hb10",
                    category="primary",
                ),
                inline._button(
                    text=_["H_B_11"],
                    callback_data="help_callback hb11",
                    category="primary",
                ),
                inline._button(
                    text=_["H_B_12"],
                    callback_data="help_callback hb12",
                    category="primary",
                ),
            ],
            [
                inline._button(
                    text=_["H_B_13"],
                    callback_data="help_callback hb13",
                    category="primary",
                ),
                inline._button(
                    text=_["H_B_14"],
                    callback_data="help_callback hb14",
                    category="primary",
                ),
                inline._button(
                    text=_["H_B_15"],
                    callback_data="help_callback hb15",
                    category="primary",
                ),
            ],
            mark,
        ]
    )


def help_back_markup(_):
    return inline.ikm(
        [
            [
                inline._button(
                    text=_["BACK_BUTTON"],
                    callback_data="settings_back_helper",
                    category="primary",
                )
            ]
        ]
    )


def private_help_panel(_):
    return inline.ikm(
        [
            [
                inline._button(
                    text=_["S_B_4"],
                    url=f"https://t.me/{app.username}?start=help",
                    category="success",
                )
            ]
        ]
    )
