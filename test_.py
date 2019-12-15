"""
date:
author:
function:
"""
import json

from DAO.movie.movie import MovieInfoDao

if __name__ == '__main__':
    movie_dict = """{"id":1, "tag": "热门", "name": "爱尔兰人 The Irishman‎ (2019)", "url": "https://movie.douban.com/subject/6981153/", "cover": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568902055.webp", "rate": "9.1", "playable": false, "new": false, "source": 1, "actors": ["罗伯特·德尼罗", "阿尔·帕西诺", "乔·佩西", "安娜·帕奎因", "杰西·普莱蒙", "哈威·凯特尔", "斯蒂芬·格拉汉姆", "鲍比·坎纳瓦尔", "杰克·休斯顿", "阿莱卡萨·帕拉迪诺", "凯瑟琳·纳杜奇", "多米尼克·隆巴多兹", "雷·罗马诺", "塞巴斯蒂安·马尼斯科", "杰克·霍夫曼", "保罗·本-维克托", "斯蒂芬妮·库尔特祖巴", "莎伦·菲弗", "路易斯·坎瑟米", "茵迪亚·恩能加", "J.C.麦肯泽", "巴里·普赖默斯", "吉姆·诺顿", "盖里·巴萨拉巴", "玛格丽特·安妮·佛罗伦斯", "约翰·斯库蒂", "约翰·塞纳迭姆博", "大卫·阿隆·贝克", "桃乐丝·麦卡锡", "凯文·凯恩", "加里·帕斯托雷", "约瑟夫·罗素", "凯文·奥罗克", "娜塔莎·罗曼诺娃", "杰里米·卢克", "凯莉·P·威廉姆斯", "詹妮弗·马奇", "保罗·鲍格才", "蒂姆·内夫", "斯蒂芬·梅尔勒", "克雷格·文森特", "比利·史密斯", "布莱斯·科里根", "斯泰西·爱丽丝·科恩", "吉诺·卡法雷利", "拉里·罗曼诺", "罗伯特·富纳罗", "维罗妮卡·阿利奇诺", "克劳黛特·拉利", "詹姆斯·洛林兹", "阿什莉·诺斯", "肯·斯拉迪克", "帕特里克·加洛", "杰伊·斯特凡", "路西·加里娜"], "directors": ["马丁·斯科塞斯"], "region": "美国", "types": ["剧情", "传记", "犯罪"], "release_year": "2019", "duration": "210分钟"}"""
    j_dict = json.loads(movie_dict)
    print(j_dict)
    MovieInfoDao().insert_movie(j_dict)
