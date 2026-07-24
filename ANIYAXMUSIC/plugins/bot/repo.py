from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ANIYAXMUSIC import app
from config import BOT_USERNAME
from ANIYAXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
❥ ωєℓ¢σмє тσ  ˵𓄼˳𝜜𝒏𝒐𝒌𝒉𝒊 𝒙 𝜧𝒖𝒔𝒊𝒄 ༉‧₊˚.

❥ ʀᴇᴘᴏ ᴄʜᴀᴀʜɪʏe ᴛᴏ ʙᴏᴛ ᴋᴏ 

❥ 3 ɢᴄ ᴍᴀɪ ᴀᴅᴅ ᴋᴀʀ ᴋᴇ 

❥ ᴀᴅᴍɪɴ ʙᴀɴᴏ ᴀᴜʀ sᴄʀᴇᴇɴsʜᴏᴛ 
     
❥ ᴏᴡɴᴇʀ @II_SB_SIMPLE_II ᴋᴏ ᴅᴏ ғɪʀ ʀᴇᴘᴏ ᴍɪʟ sᴀᴋᴛɪ ʜᴀɪ 

"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("♡ α∂∂ иσω ♡", url=f"https://t.me/Anokhi_MusicBot?startgroup=true")
        ],
        [
          InlineKeyboardButton("ѕυρρσɾƚ", url="https://t.me/heartstealer_x"),
          InlineKeyboardButton(" ❍ƴꫀ─̽𝐌 ɪ ͢ͷ 𝛆᪵🤍", url="https://t.me/II_SB_SIMPLE"),
          ],
               [
                InlineKeyboardButton("ᴏᴛʜᴇʀ ʙᴏᴛs", url=f"https://t.me/ABOUT_NIGHT_SQUAD"),
],
[
InlineKeyboardButton("ᴄʜᴇᴄᴋ", url=f"https://t.me/misskittymusicbot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/90ef1bc444de679d65209-335d94a31975f4eda6.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
