from revthon import *
from revthon import reviq
from telethon import events
import asyncio

smedia = False


@reviq.on(admin_cmd(pattern="تفعيل الذاتية"))
async def start_datea(event):
    global smedia
    smedia = True
    await event.edit("- تم بنجاح تفعيل حفظ الميديا الذاتية من الان")

@reviq.on(admin_cmd(pattern="تعطيل الذاتية"))
async def stop_datea(event):
    global smedia
    smedia = False
    await event.edit("- تم بنجاح تعطيل حفظ الميديا الذاتية من الان")

@reviq.on(events.NewMessage(func=lambda e: e.is_private and (e.photo or e.video) and e.media_unread))
async def handler(event):
    global smedia
    if smedia:
        sender = await event.get_sender()
        username = sender.username
        user_id = sender.id

        result = await event.download_media()
        caption = (f"ميديا ذاتية التدمير وصلت لك !\n: المرسل @{username}\nالايدي : {user_id}")
        await reviq.send_file("me", result, caption=caption)
    pass  
