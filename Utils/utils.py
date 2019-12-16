"""
date:
author:
function:
"""
import json

import requests

from config import CONFIG


def true_or_false(word):
    """
    把true or false 转化为0或1
    """
    res = 1
    if word is True:
        res = 0
    return res


def get_ip_proxy(count):
    """
    获取讯代理的长效ip
    """
    print("获取ip代理")
    spider_id = CONFIG.PROXY_USER_ID
    order_no = CONFIG.PROXY_ORDER_NO
    url = f"http://api.xdaili.cn/xdaili-api/greatRecharge/getGreateIp?{spider_id}&ordernoo={order_no}&returnType=2&count={count}"
    result = json.loads(requests.get(url).text)
    print(f"获取到的代理结果为：{result}")
    if result['ERRORCODE'] == "0":
        ip_list = result['RESULT']
        return ip_list
    else:
        return []
