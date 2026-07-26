from pyrogram import Client, filters
from pyrogram.types import Message
import os
import math

from ANIYAXMUSIC import app

MAX_SIZE = 5 * 1024 * 1024 * 1024  # 5 GiB


def parse_size(size_str):
    size_str = size_str.strip().lower()

    if size_str.endswith("mb"):
        return int(float(size_str[:-2]) * 1024 * 1024)

    elif size_str.endswith("gb"):
        size = int(float(size_str[:-2]) * 1024 * 1024 * 1024)
        if size > MAX_SIZE:
            raise ValueError("Maximum allowed split size is 5GB.")
        return size

    else:
        raise ValueError("Use MB or GB. Example: /split 10mb")


@app.on_message(filters.command("split") & filters.reply)
async def split_file(client: Client, message: Message):
    replied = message.reply_to_message

    if not replied or not replied.document:
        return await message.reply_text(
            "Reply to a TXT file.\nExample:\n`/split 10mb`"
        )

    try:
        size = parse_size(message.command[1])
    except:
        return await message.reply_text(
            "Usage:\n"
            "`/split 10mb`\n"
            "`/split 500mb`\n"
            "`/split 2gb`\n"
            "Maximum: 5GB"
        )

    file_path = await client.download_media(replied.document)

    if not file_path:
        return await message.reply("Download failed.")

    total_size = os.path.getsize(file_path)
    total_parts = math.ceil(total_size / size)

    base_name = os.path.splitext(replied.document.file_name)[0]

    try:
        with open(file_path, "rb") as f:

            for part in range(total_parts):
                part_file = f"{base_name}_part{part+1}.txt"

                with open(part_file, "wb") as out:
                    out.write(f.read(size))

                await client.send_document(
                    message.chat.id,
                    part_file,
                    caption=f"Part {part+1}/{total_parts}"
                )

                os.remove(part_file)

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)