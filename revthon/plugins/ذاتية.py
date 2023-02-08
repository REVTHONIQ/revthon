from revthon import *
from revthon import reviq
from ..sql_helper.globals import gvarstatus

@reviq.on(pattern="(جلب الصورة|جلب الصوره|ذاتيه|ذاتية|حفظ)")
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    DEVREVV = await event.get_reply_message()
    pic = await DEVREVV.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
- تـم حفظ الصـورة بنجـاح ✓ 
- غير مبري الذمه اذا استخدمت الامر للابتزاز
- CH: @Revthon
- Dev: @DEVREVV
  """,
    )
    await event.delete()
