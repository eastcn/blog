"""
date: 2019.12.15
author: east
function: 定时任务调度
"""
from config import CONFIG
from Utils.log import log
from Movie.Service.movieJob import spider_job
from apscheduler.schedulers.blocking import BlockingScheduler


class JobServer:
    def __init__(self):
        self.schedule = BlockingScheduler()

    def add_movie_job(self):
        self.schedule.add_job(spider_job, 'cron', hour=CONFIG.SPIDER_HOUR, minute=CONFIG.SPIDER_MINUTE)

    def job_start(self):
        self.add_movie_job()
        log.info("movie 爬虫启动")
        self.schedule.start()


if __name__ == '__main__':
    JobServer().job_start()
