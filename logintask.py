from loguru import logger
from apscheduler.schedulers.blocking import BlockingScheduler
from pathlib import Path
import os


def login_task():
    logger.info("login")
    log_shell_path = Path.cwd() / "BeihangLogin" / "login.sh"
    os.system("sh {}".format(str(log_shell_path)))


if __name__ == "__main__":
    logger.add("/log/logintask.log")
    login_task()
    sched = BlockingScheduler()
    sched.add_job(login_task, 'interval', hours=1 ,misfire_grace_time=10)
    sched.start()