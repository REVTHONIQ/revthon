import asyncio
import contextlib
import os
import sys
from asyncio.exceptions import CancelledError

import heroku3
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from revthon import HEROKU_APP, UPSTREAM_REPO_URL, reviq

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)

cmdhd = Config.COMMAND_HAND_LER
ENV = bool(os.environ.get("ENV", False))
LOGS = logging.getLogger(__name__)

HEROKU_APP_NAME = Config.HEROKU_APP_NAME or None
HEROKU_API_KEY = Config.HEROKU_API_KEY or None
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"

UPSTREAM_REPO_BRANCH = Config.UPSTREAM_REPO_BRANCH

REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "master"
NO_HEROKU_APP_CFGD = "no heroku application found, but a key given? 😕 "
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
RESTARTING_APP = "re-starting heroku application"
IS_SELECTED_DIFFERENT_BRANCH = (
    "looks like a custom branch {branch_name} "
    "is being used:\n"
    "in this case, Updater is unable to identify the branch to be updated."
    "please check out to an official branch, and re-start the updater."
)


# -- Constants End -- #

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

requirements_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "requirements.txt"
)


async def gen_chlog(repo, diff):
    d_form = "%d/%m/%y"
    return "".join(
        f"  • {c.summary} ({c.committed_datetime.strftime(d_form)}) <{c.author}>\n"
        for c in repo.iter_commits(diff)
    )


async def print_changelogs(event, ac_br, changelog):
    changelog_str = (
        f"**• توفر تحديث جديد للفـرت [{ac_br}]:\n\nالتغييرات:**\n`{changelog}`"
    )
    if len(changelog_str) > 4096:
        await event.edit("**• التغييرات كثيرة جدا لذلك تم وضعها في ملف**")
        with open("output.txt", "w+") as file:
            file.write(changelog_str)
        await event.client.send_file(
            event.chat_id,
            "output.txt",
            reply_to=event.id,
        )
        os.remove("output.txt")
    else:
        await event.client.send_message(
            event.chat_id,
            changelog_str,
            reply_to=event.id,
        )
    return True


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def update_bot(event, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await update_requirements()
    revthon = await event.edit("**• تم بنجاح التحديث جار اعادة التشغيل الان**")
    await event.client.reload(revthon)


async def deploy(event):
    if HEROKU_API_KEY is None:
        return await event.edit("**• يرجى وضع فار HEROKU_API_KEY للتحديث**")
    heroku = heroku3.from_key(HEROKU_API_KEY)
    heroku_applications = heroku.apps()
    if HEROKU_APP_NAME is None:
        await event.edit(
            "**• يرجى وضع فار HEROKU_APP_NAME**" " لتتمكن من تحديث السورس "
        )
    heroku_app = next(
        (app for app in heroku_applications if app.name == HEROKU_APP_NAME),
        None,
    )
    if heroku_app is None:
            await event.edit(f"**• خطأ في التعرف على تطبيق هيروكو**")
            await event.edit(
        "**• جار اعادة تشغيل الدينو الان يرجى الانتظار من 2-5 دقائق**"
        )
    if HEROKU_APP is not None:
        HEROKU_APP.restart()


@reviq.ar_cmd(pattern="تحديث(| الان)?$")
async def upstream(event):
    await event.edit("**• جار الان التحديث أنتظر قليلا**")
    await deploy(event)



@reviq.ar_cmd(
    pattern="تحديث التنصيب$",
)
async def upstream(event):
    await event.edit("**• جار الان التحديث أنتظر قليلا**")
    await deploy(event)
