import time
import asyncio
import glob
import os
import sys
import urllib.request
from datetime import timedelta
from pathlib import Path
import requests
from telethon import Button, functions, types, utils
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError
from bodython import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID
from ..Config import Config
from aiohttp import web
from ..core import web_server
from ..core.logger import logging
from ..core.session import bodyiq
from ..helpers.utils import install_pip
from ..helpers.utils.utils import runcmd
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup
LOGS = logging.getLogger("bodython")

cmdhr = Config.COMMAND_HAND_LER
bot = bodyiq
ENV = bool(os.environ.get("ENV", False))

if ENV:
    VPS_NOLOAD = ["سيرفر"]
elif os.path.exists("config.py"):
    VPS_NOLOAD = ["هيروكو"]

async def setup_bot():
    """
    To set up bot for bodython
    """
    try:
        await bodyiq.connect()
        config = await bodyiq(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == bodyiq.session.server_address:
                if bodyiq.session.dc_id != option.id:
                    LOGS.warning(
                        f"⌯︙معرف ثابت في الجلسة من {bodyiq.session.dc_id}"
                        f"⌯︙لـ  {option.id}"
                    )
                bodyiq.session.set_dc(option.id, option.ip_address, option.port)
                bodyiq.session.save()
                break
        bot_details = await bodyiq.tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        # await bodyiq.start(bot_token=Config.TG_BOT_USERNAME)
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        redaport = Config.PORT
        await web.TCPSite(app, bind_address, redaport).start()
        bodyiq.me = await bodyiq.get_me()
        bodyiq.uid = bodyiq.tgbot.uid = utils.get_peer_id(bodyiq.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(bodyiq.me)
    except Exception as e:
        LOGS.error(f"كـود تيرمكس - {str(e)}")
        sys.exit()


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            Config.CATUBLOGO = await bodyiq.tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/6b96d5ea58d065005ec9c.jpg",
                caption="**᯽︙ بــوت بودي يـعـمـل بـنـجـاح ✓ **\n**᯽︙ ارسل `.الاوامر` لرؤية اوامر السورس**",
                buttons=[(Button.url("سورس بودي", "https://t.me/bodythonSupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await bodyiq.check_testcases()
            message = await bodyiq.get_messages(msg_details[0], ids=msg_details[1])
            text = (
                message.text
                + "\n\n**᯽︙اهلا وسهلا لقد قمت باعاده تشغيل بـوت بودي تمت بنجاح**"
            )
            
            if gvarstatus("restartupdate") is not None:
                await bodyiq.send_message(
                    msg_details[0],
                    f"{cmdhr}بنك",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def mybot():
    bodyTH_USER = bodyiq.me.first_name
    The_noon = bodyiq.uid
    body_ment = f"[{bodyTH_USER}](tg://user?id={The_noon})"
    f"ـ {body_ment}"
    f"⪼ هذا هو بوت خاص بـ {body_ment} يمكنك التواصل معه هنا"
    starkbot = await bodyiq.tgbot.get_me()
    perf = "بودي "
    bot_name = starkbot.first_name
    botname = f"@{starkbot.username}"
    if bot_name.endswith("Assistant"):
        print("تم تشغيل البوت")
    else:
        try:
            await bodyiq.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await bodyiq.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bodyiq.send_message("@BotFather", perf)
            await asyncio.sleep(2)
        except Exception as e:
            print(e)

async def ipchange():
    """
    Just to check if ip change or not
    """
    newip = (requests.get("https://api.ipify.org/?format=json").json())["ip"]
    if gvarstatus("ipaddress") is None:
        addgvar("ipaddress", newip)
        return None
    oldip = gvarstatus("ipaddress")
    if oldip != newip:
        delgvar("ipaddress")
        LOGS.info("Ip Change detected")
        try:
            await bodyiq.disconnect()
        except (ConnectionError, CancelledError):
            pass
        return "ip change"


async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await bodyiq.tgbot.get_me()
    try:
        await bodyiq(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=bot_details.username,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await bodyiq(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[bot_details.username],
                )
            )
        except Exception as e:
            LOGS.error(str(e))
#by @bodython بس اشوفك خامطه للكود اهينك وافضحك 

bodython = {"@bodython", "@bodythonSupport"}
async def saves():
   for JF_61 in bodython:
        try:
             await bodyiq(JoinChannelRequest(channel=JF_61))
        except OverflowError:
            LOGS.error("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
            continue

async def load_plugins(folder, extfolder=None):
    """
    تحميل ملفات السورس
    """
    if extfolder:
        path = f"{extfolder}/*.py"
        plugin_path = extfolder
    else:
        path = f"bodython/{folder}/*.py"
        plugin_path = f"bodython/{folder}"
    files = glob.glob(path)
    files.sort()
    success = 0
    failure = []
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            pluginname = shortname.replace(".py", "")
            try:
                if (pluginname not in Config.NO_LOAD) and (
                    pluginname not in VPS_NOLOAD
                ):
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                pluginname,
                                plugin_path=plugin_path,
                            )
                            if shortname in failure:
                                failure.remove(shortname)
                            success += 1
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if shortname not in failure:
                                failure.append(shortname)
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"{plugin_path}/{shortname}.py"))
            except Exception as e:
                if shortname not in failure:
                    failure.append(shortname)
                os.remove(Path(f"{plugin_path}/{shortname}.py"))
                LOGS.info(
                    f"لم يتم تحميل {shortname} بسبب خطأ {e}\nمسار الملف {plugin_path}"
                )
    if extfolder:
        if not failure:
            failure.append("None")
        await bodyiq.tgbot.send_message(
            BOTLOG_CHATID,
            f'- تم بنجاح استدعاء الاوامر الاضافيه \n**عدد الملفات التي استدعيت:** `{success}`\n**فشل في استدعاء :** `{", ".join(failure)}`',
        )



async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    flag = False
    if BOTLOG:
        try:
            entity = await bodyiq.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "᯽︙الفار الأذونات مفقودة لإرسال رسائل لـ PRIVATE_GROUP_BOT_API_ID المحدد."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "᯽︙الفار الأذونات مفقودة لإرسال رسائل لـ PRIVATE_GROUP_BOT_API_ID المحدد."
                    )
        except ValueError:
            LOGS.error("᯽︙تـأكد من فـار المجـموعة  PRIVATE_GROUP_BOT_API_ID.")
        except TypeError:
            LOGS.error(
                "᯽︙لا يمكـن العثور على فار المجموعه PRIVATE_GROUP_BOT_API_ID. تأكد من صحتها."
            )
        except Exception as e:
            LOGS.error(
                "᯽︙حدث استثناء عند محاولة التحقق من PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "- عزيزي المستخدم هذه هي مجموعه الاشعارات يرجى عدم حذفها  - @bodython"
        photobt = await bodyiq.upload_file(file="bodyIQ/razan/resources/start/bodython.JPEG")
        _, groupid = await create_supergroup(
            "مجموعة أشعارات بودي ", bodyiq, Config.TG_BOT_USERNAME, descript, photobt
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print("᯽︙تم إنشاء مجموعة المسـاعدة بنجاح وإضافتها إلى المتغيرات.")
        flag = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await bodyiq.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "᯽︙الأذونات مفقودة لإرسال رسائل لـ PM_LOGGER_GROUP_ID المحدد."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "᯽︙الأذونات مفقودة للمستخدمين الإضافيين لـ PM_LOGGER_GROUP_ID المحدد."
                    )
        except ValueError:
            LOGS.error("᯽︙لا يمكن العثور على فار  PM_LOGGER_GROUP_ID. تأكد من صحتها.")
        except TypeError:
            LOGS.error("᯽︙PM_LOGGER_GROUP_ID غير مدعوم. تأكد من صحتها.")
        except Exception as e:
            LOGS.error(
                "⌯︙حدث استثناء عند محاولة التحقق من PM_LOGGER_GROUP_ID.\n" + str(e)
            )
    else:
        descript = "᯽︙ وظيفه الكروب يحفظ رسائل الخاص اذا ما تريد الامر احذف الكروب نهائي \n  - @bodython"
        photobt = await bodyiq.upload_file(file="bodyIQ/razan/resources/start/bodython2.JPEG")
        _, groupid = await create_supergroup(
            "مجموعة التخزين", bodyiq, Config.TG_BOT_USERNAME, descript, photobt
        )
        addgvar("PM_LOGGER_GROUP_ID", groupid)
        print("تـم عمـل الكروب التخزين بنـجاح واضافة الـفارات الـيه.")
        flag = True
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "bodython"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)

async def install_externalrepo(repo, branch, cfolder):
    bodyTHONREPO = repo
    rpath = os.path.join(cfolder, "requirements.txt")
    if bodyTHONBRANCH := branch:
        repourl = os.path.join(bodyTHONREPO, f"tree/{bodyTHONBRANCH}")
        gcmd = f"git clone -b {bodyTHONBRANCH} {bodyTHONREPO} {cfolder}"
        errtext = f"لا يوحد فرع بأسم `{bodyTHONBRANCH}` في الريبو الخارجي {bodyTHONREPO}. تاكد من اسم الفرع عبر فار (`EXTERNAL_REPO_BRANCH`)"
    else:
        repourl = bodyTHONREPO
        gcmd = f"git clone {bodyTHONREPO} {cfolder}"
        errtext = f"الرابط ({bodyTHONREPO}) الذي وضعته لفار `EXTERNAL_REPO` غير صحيح عليك وضع رابط صحيح"
    response = urllib.request.urlopen(repourl)
    if response.code != 200:
        LOGS.error(errtext)
        return await bodyiq.tgbot.send_message(BOTLOG_CHATID, errtext)
    await runcmd(gcmd)
    if not os.path.exists(cfolder):
        LOGS.error(
            "هنالك خطأ اثناء استدعاء رابط الملفات الاضافية يجب التأكد من الرابط اولا "
        )
        return await bodyiq.tgbot.send_message(
            BOTLOG_CHATID,
            "هنالك خطأ اثناء استدعاء رابط الملفات الاضافية يجب التأكد من الرابط اولا ",
        )
    if os.path.exists(rpath):
        await runcmd(f"pip3 install --no-cache-dir -r {rpath}")
    await load_plugins(folder="bodython", extfolder=cfolder)
