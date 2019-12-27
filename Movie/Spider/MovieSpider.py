"""
date: 2019.12.16
author: east
function: 爬取www.douban.com数据
爬取的规则如下：
从豆瓣首页拿到指定的tag下的电影，目前为喜剧和热门。由于其他tag中的按评价排序的数据没有时间限制，所以有两套筛选逻辑。
1。 热门
在对应的tag下，取近期热门和评价高的两组json,每组各50（下同）。
用此两组json比较，筛选出同时存在于这两组json中的数据，作为推荐列表，每天推荐一部。
2。 其他（如喜剧）
在对应的tag下，取近期热门的数据，筛选出评分高于7的电影。
"""
import json
import traceback
import requests
from config import CONFIG


class MovieSpider:
    def __init__(self):
        self.url = "https://movie.douban.com/j/search_subjects"
        self.category = CONFIG.TAG
        # self.cookie = DoubanLogin().login()
        self.header = CONFIG.HEADER

    def get_movies(self):
        """
        通过douban的接口获取到近期热度高的电影和评分高的电影
        return movies dict类型
        """
        all_movies = {}
        for tag in self.category:
            # todo 加入代理
            if tag == "热门":
                all_movies['热门'] = self.get_hot_movies()
            else:
                all_movies[tag] = self.get_tag_movies(tag)
        return all_movies

    def get_hot_movies(self):
        """
        获取热门的数据
        """
        try:
            url_rank = f"{self.url}?type=movie&tag=热门&sort=rank&watched=on&page_limit=50&page_start=0"
            url_recommend = f"{self.url}?type=movie&tag=热门&sort=recommend&watched=on&page_limit=50&page_start=0"
            res_rank = json.loads(
                requests.get(url=url_rank, headers=self.header, cookies=self.cookie, verify=False).text)
            print(json.dumps(res_rank, ensure_ascii=False))
            res_recommend = json.loads(
                requests.get(url=url_recommend, cookies=self.cookie, headers=self.header, verify=False).text)
            hot_movies = compare_two_list(res_rank['subjects'], res_recommend['subjects'])
            return hot_movies
        except Exception:
            print("获取热门的电影-error")
            traceback.print_exc()
            return []

    def get_tag_movies(self, tag):
        """
        获取到其他标签的电影
        """
        try:
            tag_movies = []
            url_tag = f"{self.url}??type=movie&tag={tag}&sort=recommend&watched=on&page_limit=50&page_start=0"
            res_tag = json.loads(requests.get(url_tag, headers=self.header, verify=False).text)
            for movie in res_tag['subjects']:
                if movie['rate'] >= '7.0':
                    tag_movies.append(movie)
            return tag_movies
        except Exception:
            print("获取其他标签电影error")
            traceback.print_exc()
            return []

    def get_movie_detail(self, movie_id):
        """
        获取电影详细介绍
        """
        try:
            detail_url = f"https://movie.douban.com/j/subject_abstract?subject_id={movie_id}"
            res_detail = json.loads(requests.get(detail_url, headers=self.header, verify=False).text)
            return res_detail
        except Exception:
            print("获取详情时报错error")
            traceback.print_exc()
            return "null"

    def get_cover(self, cover_url, movie):
        """
        获取电影的海报，并保存
        """
        print("获取电影cover")
        file_name = f"static/img/{movie}.webp"
        res = requests.get(cover_url, headers=self.header, verify=False)
        with open(file_name, "wb") as f:
            f.write(res.content)
            f.close()
        print(f"获取成功，地址为：{file_name}")
        return file_name


def get_source_from_btdx8():
    """
    获取movie source 从bt大熊网站
    """
    pass


def compare_two_list(l_1, l_2):
    """
    用于比较两个json中是否存在相同的电影名
    """
    final_id_list = []
    final_movie_list = []
    id_list_1 = [movie['id'] for movie in l_1]
    id_list_2 = [movie['id'] for movie in l_2]
    for id_1 in id_list_1:
        for id_2 in id_list_2:
            if id_1 == id_2:
                final_id_list.append(id_1)
    for movie in l_1:
        if movie['id'] in final_id_list:
            final_movie_list.append(movie)
    return final_movie_list


class DoubanLogin:
    def __init__(self):
        self.username = CONFIG.DOUBAN_USERNAME
        self.password = CONFIG.DOUBAN_PASSWORD

    def login(self):
        """
        登录豆瓣，获取cookie
        返回账号cookie信息，dick类型
        """
        login_url = "https://accounts.douban.com/j/mobile/login/basic"
        data = {
            "name": self.username,
            "password": self.password
        }
        res = requests.post(url=login_url, data=data, headers=CONFIG.HEADER, verify=False)
        cookie = requests.utils.dict_from_cookiejar(res.cookies)
        print(f"本次登录获取到的cookie：{cookie}")
        return cookie


if __name__ == '__main__':
    pass
