from loguru import logger
from apscheduler.schedulers.blocking import BlockingScheduler
from BeihangLogin.srun4k import *
import logging_loki
from loguru import logger
from config import *


logger.add(logging_loki.LokiHandler(**config["loki_config"]))
logger.add("/log/{}.log".format(config["loki_config"]["tags"]["application"]))


def login_task():
    logger.info("login")
    ret = do_login(config["gatewayUrl"], config["USERNAME"], config["PASSWORD"])
    if ret['success']:
        logger.info('login success!')
    else:
        logger.warning('login failed\n' + ret['reason'])


if __name__ == "__main__":
    logger.info("login bot init:config is {}".format(str(config)))
    login_task()
    sched = BlockingScheduler()
    sched.add_job(login_task, 'interval', hours=1 ,misfire_grace_time=10)
    sched.start()