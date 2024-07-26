from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Ava import Jarvis as pbot
from Ava.modules.resources.fonts import Fonts

@pbot.on_message(filters.command(["font", "fonts"]))
async def style_buttons(c, m, cb=False):
    text = m.text.split(' ',1)[1]
    buttons = [
        [
            InlineKeyboardButton("𝚃𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛", callback_data="style+typewriter"),
            InlineKeyboardButton("𝕆𝕦𝕥𝕝𝕚𝕟𝕖", callback_data="style+outline"),
            InlineKeyboardButton("𝐒𝐞𝐫𝐢𝐟", callback_data="style+serif"),
        ],
        # Additional buttons...
        [InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close_reply"), InlineKeyboardButton("ɴᴇxᴛ ➻", callback_data="nxt")],
    ]
    if not cb:
        await m.reply_text(f"`{text}`", reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))

@pbot.on_callback_query(filters.regex("^nxt"))
async def nxt(c, m):
    buttons = [
        [
            InlineKeyboardButton("🇸 🇵 🇪 🇨 🇮 🇦 🇱 ", callback_data="style+special"),
            InlineKeyboardButton("🅂🅀🅄🄰🅁🄴🅂", callback_data="style+squares"),
            InlineKeyboardButton("🆂︎🆀︎🆄︎🅰︎🆁︎🅴︎🆂︎", callback_data="style+squares_bold"),
        ],
        # Additional buttons...
        [InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close_reply"), InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="nxt+0")],
    ]
    await m.answer()
    await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))

@pbot.on_callback_query(filters.regex("^style"))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split('+')
    font_map = {
        "typewriter": Fonts.typewriter,
        "outline": Fonts.outline,
        "serif": Fonts.serief,
        "bold_cool": Fonts.bold_cool,
        "cool": Fonts.cool,
        "small_cap": Fonts.smallcap,
        "script": Fonts.script,
        "script_bolt": Fonts.bold_script,
        "tiny": Fonts.tiny,
        "comic": Fonts.comic,
        "sans": Fonts.san,
        "slant_sans": Fonts.slant_san,
        "slant": Fonts.slant,
        "sim": Fonts.sim,
        "circles": Fonts.circles,
        "circle_dark": Fonts.dark_circle,
        "gothic": Fonts.gothic,
        "gothic_bolt": Fonts.bold_gothic,
        "cloud": Fonts.cloud,
        "happy": Fonts.happy,
        "sad": Fonts.sad,
        "special": Fonts.special,
        "squares": Fonts.square,
        "squares_bold": Fonts.dark_square,
        "andalucia": Fonts.andalucia,
        "manga": Fonts.manga,
        "stinky": Fonts.stinky,
        "bubbles": Fonts.bubbles,
        "underline": Fonts.underline,
        "ladybug": Fonts.ladybug,
        "rays": Fonts.rays,
        "birds": Fonts.birds,
        "slash": Fonts.slash,
        "stop": Fonts.stop,
        "skyline": Fonts.skyline,
        "arrows": Fonts.arrows,
        "qvnes": Fonts.rvnes,
        "strike": Fonts.strike,
        "frozen": Fonts.frozen,
    }

    cls = font_map.get(style)
    if cls:
        original_text = m.message.reply_to_message.text.split(' ', 1)[1]
        new_text = cls(original_text)
        try:
            await m.message.edit_text(new_text, reply_markup=m.message.reply_markup)
        except:
            pass

__mod_name__ = "Fᴏɴᴛ"
