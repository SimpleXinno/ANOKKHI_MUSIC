# chk.py
# Educational sandbox report formatter
# No real card checking

import os
from pyrogram import filters


def make_report(status, gateway, amount, response):
    emoji = "✅" if status == "APPROVED" else "❌"

    return f"""
{emoji} {status}

💳 TEST CARD: **** **** **** 1234

🛒 Gᴀᴛᴇᴡᴀʏ: {gateway}
📝 Rᴇsᴘᴏɴsᴇ: {response}
💸 Pʀɪᴄᴇ: £{amount}

🧪 ENVIRONMENT: TEST MODE

💡 Educational Sandbox Result
"""


def register_chk(app):

    @app.on_message(filters.command("chk"))
    async def chk_command(client, message):

        if not message.reply_to_message or not message.reply_to_message.document:
            await message.reply(
                "❌ Please reply to a TXT test file with /chk"
            )
            return

        path = await message.reply_to_message.download()

        total = 0
        approved = 0
        declined = 0

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            lines = [
                x.strip()
                for x in f.readlines()
                if x.strip()
            ]

        for _ in lines:
            total += 1

            # Demo sandbox result only
            if total % 2 == 0:
                approved += 1
            else:
                declined += 1

        report = f"""
✅ Cʜᴇᴄᴋ Cᴏᴍᴘʟᴇᴛᴇ! ✅

📊 Rᴇsᴜʟᴛs:

┣ ✅ Approved: {approved}
┣ ❌ Declined: {declined}
┣ ⚠️ Errors: 0
┗ 📊 Total: {total}

🧪 TEST MODE ONLY
"""

        await message.reply(report)

        os.remove(path)