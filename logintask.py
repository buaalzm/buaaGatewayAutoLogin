from loguru import logger
from apscheduler.schedulers.blocking import BlockingScheduler
from BeihangLogin.srun4k import *
from config import *


def login_task():
    logger.info("login")
    ret = do_login(gatewayUrl, USERNAME, PASSWORD)
    if ret['success']:
        logger.info('成功！')
    else:
        logger.warning('失败！\n' + ret['reason'])


if __name__ == "__main__":
    logger.add("/log/logintask.log")
    login_task()
    sched = BlockingScheduler()
    sched.add_job(login_task, 'interval', hours=1 ,misfire_grace_time=10)
    sched.start()