"""
@author: east
@date:
@function:
"""


class CONFIG:
    """数据库相关"""
    ENV = "LOCAL"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:EASTlove7!@47.111.163.9:3306/blog"
    SQLALCHEMY_DATABASE_URI_SNEAKER = "mysql+pymysql://root:EASTlove7!@47.111.163.9:3306/sneakerlover"

    """豆瓣爬虫相关"""
    HEADER = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
    TAG = ['喜剧', "热门"]
    DOUBAN_USERNAME = "123123"
    DOUBAN_PASSWORD = "123123"
    SPIDER_HOUR = "0"  # 爬取时的小时
    SPIDER_MINUTE = "15"  # 爬取时的分钟

    """代理相关"""
    PROXY_USER_ID = "d1464633124a4338a040b921230264d5"
    PROXY_ORDER_NO = "YZ20198295024v8ZKOX"
