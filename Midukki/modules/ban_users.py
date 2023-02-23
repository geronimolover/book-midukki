from pyrogram import Client, filters
from Midukki.midukki import Midukki_RoboT
from Midukki.functions.extract_user import extract_user
from Midukki.functions.extract_time import extract_time
from Midukki.functions.handlers import Ban

@Midukki_RoboT.on_message(Ban.a)
async def ban_user(_, message):
    user_id, user_first_name, _ = extract_user(message)

    try:
        await message.chat.ban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Another nuisance ..! "
                f"{user_first_name}"
                " is banned!."
            )
        else:
            await message.reply_text(
                "Another nuisance..! "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>"
                " is banned."
            )

@Client.on_message(Ban.b)
async def un_ban_user(_, message):
    user_id, user_first_name, _ = extract_user(message)

    try:
        await message.chat.unban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Hmm... ok. Now "
                f"{user_first_name}  "
                " can join the group."
            )
        else:
            await message.reply_text(
                "Hmm... ok. Now  "
                f"<a href='tg://user?id={user_id}'>"
                f"{user_first_name}"
                "</a>  "
                " can join the group."
            )

@Midukki_RoboT.on_message(Ban.c)
async def temp_ban_user(_, message):
    if not len(message.command) > 1:
        return

    user_id, user_first_name, _ = extract_user(message)

    until_date_val = extract_time(message.command[1])
    if until_date_val is None:
        await message.reply_text(
            (
                "Invalid time formate "
                "expected m, h, or d, getting: {}"
            ).format(message.command[1][-1])
        )
        return

    try:
        await message.chat.ban_member(user_id=user_id, until_date=until_date_val)
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "Yet another one..! "
                f"{user_first_name}"
                f" banned for {message.command[1]}!"
            )
        else:
            await message.reply_text(
                "Yet another oneനു..! "
                f"<a href='tg://user?id={user_id}'>"
                "***"
                "</a>"
                f" banned for {message.command[1]}!"
            )
