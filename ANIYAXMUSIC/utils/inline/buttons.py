from pyrogram import enums, types


class Inline:
    def __init__(self):
        self.ikm = types.InlineKeyboardMarkup
        self.ikb = types.InlineKeyboardButton

        try:
            self.styles = {
                "default": enums.ButtonStyle.DEFAULT,
                "primary": enums.ButtonStyle.PRIMARY,
                "success": enums.ButtonStyle.SUCCESS,
                "danger": enums.ButtonStyle.DANGER,
            }
            self.has_styles = True
        except AttributeError:
            self.styles = {}
            self.has_styles = False

    def _button(self, text: str, category: str = "default", **kwargs):
        if self.has_styles:
            return self.ikb(
                text=text,
                style=self.styles.get(
                    category,
                    enums.ButtonStyle.DEFAULT,
                ),
                **kwargs,
            )

        return self.ikb(
            text=text,
            **kwargs,
        )


inline = Inline()
