import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from bodython import bodyiq
from ..helpers.utils import reply_id

# الي يخمط ويكول من كتابتي الا امه انيجه وقد اعذر من انذر
@bodyiq.on(admin_cmd(pattern="حالتي ?(.*)"))
async def _(event):
    await event.edit("**- يتم التاكد من حالتك اذا كنت محظور او لا**")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("** اولا الغي حظر @SpamBot وحاول مجددا**")
            return
        await event.edit(f"- {response.message.message}\n @bodython")


@bodyiq.on(admin_cmd(pattern="الاغنية ?(.*)"))
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("**▾∮ يجب الرد على الاغنيه اولا**")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("**▾∮ يتم التعرف على الاغنية انتظر**")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await event.edit(
                        "**▾∮ يجب ان يكون حجم الاغنيه من 5 الى 10 ثواني **."
                    )
                await event.edit("- انتظر قليلا")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("```Mohon buka blokir (@auddbot) dan coba lagi```")
                return
            namem = f"**الأغنية : **{result.text.splitlines()[0]}\
        \n\n**التفاصيـل : **{result.text.splitlines()[2]}"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id,
                [start_msg.id, send_audio.id, check.id, result.id, response.id],
            )
    except TimeoutError:
        return await event.edit("***حدث خطا ما حاول مجددا**")


@bodyiq.on(admin_cmd(pattern="ايميل وهمي(?: |$)(.*)"))
async def _(event):
    chat = "@TempMailBot"
    geez = await event.edit("**جاري انشاء بريد ...**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=220112646)
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            bodyiqmail = (response).reply_markup.rows[2].buttons[0].url
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit("**الغي حظر @TempMailBot  و حاول مجددا**")
            return
        await event.edit(
            f"الايميل الخاص هو `{response.message.message}`\n[ اضغط هنا لرؤية من رسائل الايميل الواردة]({bodyiqmail})"
        )
@bodyiq.on(admin_cmd(outgoing=True, pattern="غنيلي$"))
async def bodyvois(vois):
  rl = random.randint(3,267)
  url = f"https://t.me/DwDi1/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="᯽︙ BY : @bodyTHON 🎀",parse_mode="html")
  await vois.delete()

@bodyiq.on(admin_cmd(outgoing=True, pattern="شعر$"))
async def bodyvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/L1BBBL/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="᯽︙ BY : @bodyTHON 🎀",parse_mode="html")
  await vois.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="قران$"))
async def bodyvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/Quraanbody/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="᯽︙ BY : @bodyTHON 🤲🏻☪️",parse_mode="html")
  await vois.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="ثيم$"))
async def bodyThe(theme):
  rl = random.randint(2,510)
  url = f"https://t.me/GSSSD/{rl}"
  await theme.client.send_file(theme.chat_id,url,caption="᯽︙ THEME BY : @bodyTHON 🎊",parse_mode="html")
  await theme.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="لاتغلط$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/4"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="بجيت$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/5"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="نشاقة$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/3"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="احب الله$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/2"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="روح$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/6"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="انمي1$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/7"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="انمي2$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/9"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="انمي3$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/11"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="انمي4$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/12"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="انمي5$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/13"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="انمي6$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/14"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="انمي7$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/15"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="انمي8$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/16"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="انمي9$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/17"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="انمي10$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/18"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="زيج2$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/19"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="زيج$"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/20"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
@bodyiq.on(admin_cmd(outgoing=True, pattern="(شيله عبود|شيلة عبود)"))
async def bodymeme(memebody):
  body = await reply_id(memebody)
  url = f"https://t.me/MemeSoundbody/21"
  await memebody.client.send_file(memebody.chat_id,url,caption="",parse_mode="html",reply_to=body)
  await memebody.delete()
