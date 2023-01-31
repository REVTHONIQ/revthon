from bodython import *
from bodython import bodyiq
from ..sql_helper.globals import gvarstatus

@bodyiq.on(admin_cmd(pattern="(جلب الصورة|جلب الصوره|ذاتيه|ذاتية|حفظ)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    JF_61 = await event.get_reply_message()
    pic = await JF_61.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
- تـم حفظ الصـورة بنجـاح ✓ 
- غير مبري الذمه اذا استخدمت الامر للابتزاز
- CH: @bodython
- Dev: @JF_61
  """,
    )
    await event.delete()
