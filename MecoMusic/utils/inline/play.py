import math
import random
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from MecoMusic import app
import config
from pyrogram.enums import ButtonStyle
from MecoMusic.utils.formatters import time_to_seconds

# 🎨 Dynamic Color Generator
def get_style_map():
    styles = [ButtonStyle.PRIMARY, ButtonStyle.SUCCESS, ButtonStyle.DANGER]
    random.shuffle(styles)
    # Row me buttons ke hisaab se color assign hoga (1, 2, 3, ya 5 buttons wali lines)
    return {1: styles[0], 2: styles[1], 3: styles[2], 5: styles[0]}


def track_markup(_, videoid, user_id, channel, fplay):
    s_map = get_style_map()
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}", style=s_map[2]
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}", style=s_map[2]
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "𖣐—————————"
    elif 10 < umm < 20:
        bar = "—𖣐————————"
    elif 20 <= umm < 30:
        bar = "—𖣐———————"
    elif 30 <= umm < 40:
        bar = "——𖣐——————"
    elif 40 <= umm < 50:
        bar = "———𖣐—————"
    elif 50 <= umm < 60:
        bar = "————𖣐————"
    elif 60 <= umm < 70:
        bar = "—————𖣐———"
    elif 70 <= umm < 80:
        bar = "——————𖣐——"
    elif 80 <= umm < 95:
        bar = "———————𖣐—"
    else:
        bar = "————————𖣐"

    s_map = get_style_map()  # ✅ FIXED INDENTATION
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
                style=s_map[5],
            )
        ],
        [
           # InlineKeyboardButton(text="", callback_data=f"ADMIN Resume|{chat_id}", icon_custom_emoji_id=5409222721869459068),
           # InlineKeyboardButton(text="", callback_data=f"ADMIN Pause|{chat_id}", icon_custom_emoji_id=5409042015415448331),
           # InlineKeyboardButton(text="", callback_data=f"ADMIN Stop|{chat_id}", icon_custom_emoji_id=5408832111773757273),
        ],
        [
            InlineKeyboardButton(text=_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true", style=s_map[5]),
        ],
        [
            InlineKeyboardButton(text="• ᴏᴡɴᴇʀ •", url="https://t.me/ll_DEVIL_SHIV_ll", style=s_map[5]),
            InlineKeyboardButton(text="• ɢʀᴏᴜᴘ •", url="https://t.me/betabot_support", style=s_map[5]),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def stream_markup(_, chat_id):
    s_map = get_style_map()
    buttons = [
        [
           # InlineKeyboardButton(text="", callback_data=f"ADMIN Resume|{chat_id}", icon_custom_emoji_id=5409222721869459068),
           # InlineKeyboardButton(text="", callback_data=f"ADMIN Pause|{chat_id}", icon_custom_emoji_id=5409042015415448331),
           # InlineKeyboardButton(text="", callback_data=f"ADMIN Stop|{chat_id}", icon_custom_emoji_id=5408832111773757273),
        ],
        [
            InlineKeyboardButton(text=_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true", style=s_map[5]),
        ],
        [
            InlineKeyboardButton(text="• ᴏᴡɴᴇʀ •", url="https://t.me/ll_DEVIL_SHIV_ll", style=s_map[5]),
            InlineKeyboardButton(text="• ɢʀᴏᴜᴘ •", url="https://t.me/betabot_support", style=s_map[5]),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    s_map = get_style_map()
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MecoPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}", style=s_map[2]
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MecoPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}", style=s_map[2]
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}", style=s_map[1]
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    s_map = get_style_map()
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}", style=s_map[1]
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}", style=s_map[1]
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    s_map = get_style_map()
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}", style=s_map[5]
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}", style=s_map[5]
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}", style=s_map[5]
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}", style=s_map[5]
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}", style=s_map[5]
            ),
        ],
    ]
    return buttons
