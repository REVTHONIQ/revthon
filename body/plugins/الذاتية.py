from os import remove

from body import body


@body.ar_cmd(pattern="(سي|ذاتية)")
async def datea(event):
    await event.delete()
    scertpic = await event.get_reply_message()
    downloadjmthon = await scertpic.download_media()
    await body.send_file("me", downloadjmthon)
    remove(downloadjmthon)
