"""
date: 
author: east
function: 打印日志和保存日志
"""
import logging
from logging.handlers import TimedRotatingFileHandler


class Logger:
    def __init__(self):
        self.logger = logging.getLogger("blog")
        self.default_level = logging.INFO
        logger_main_level, logger_file_level, logger_console_level = "DEBUG", "DEBUG", "INFO"
        self.logger.setLevel(logger_main_level)
        format_ = logging.Formatter('[%(asctime)s] %(filename)s line:%(lineno)d [%(levelname)s]%(message)s')
        file_log_job = TimedRotatingFileHandler(filename="./Log/log/blog_", when="D", interval=1, backupCount=7,
                                                encoding="utf-8")
        file_log_job.suffix = "%Y-%m-%d.log"
        file_log_job.setLevel(logger_file_level)
        file_log_job.setFormatter(format_)

        console_log_job = logging.StreamHandler()
        console_log_job.setLevel(logger_console_level)
        console_log_job.setFormatter(format_)

        if self.logger.hasHandlers() is False:
            self.logger.addHandler(file_log_job)
            self.logger.addHandler(console_log_job)

    def log(self):
        return self.logger
