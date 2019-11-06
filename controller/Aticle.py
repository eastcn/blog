"""
@author: east
@date:
@function:
"""
import json
import datetime
import socket
import time
import traceback

from flask import Blueprint, request, make_response
from DAO.basic.article import ArticleSql
from Utils.getTitle import getTitle

article = Blueprint('article', url_prefix='/api/article', import_name=__name__)

db = ArticleSql()


@article.route('/getNameByKind', methods=['get'])
def get_article_id():
    kind = request.args.get('kind')
    data = db.select_by_kind(kind, 10)
    if data is not False:
        res_list = []
        if len(data) > 0:
            for item in data:
                article_dict = {
                    'name': item.title,
                    'id': item.id,
                    'time': item.create_time.strftime("%Y-%m-%d"),
                    'tags': json.loads(item.tag)
                }
                res_list.append(article_dict)
        return json.dumps(res_list)
    else:
        return 'error'


@article.route('/getPost', methods=['get'])
def get_article_text():
    res = {
        "code": 500,
        "post": "",
        "time": ""
    }
    try:
        article_id = request.args.get("id")
        data = db.select_by_id(article_id)
        if data:
            res['code'] = 200
            res['post'] = data.contend
            res['time'] = data.create_time.strftime("%Y-%m-%d")
    except Exception:
        traceback.print_exc()
    return json.dumps(res, ensure_ascii=False)


@article.route('/del')
def del_article():
    pass


@article.route('/uploadImage', methods=['post'])
def uploadImage():
    """
    上传图片
    :return:
    """
    result = {}
    try:
        f = request.files['image']
        file_name = f.filename.split('.')
        file_url = f'/static/{f.filename[0]}_{str(int(time.time()))}.{file_name[1]}'
        f.save(f'.{file_url}')
        result['url'] =  f'http://47.111.163.9:8089{file_url}'
        result['success'] = True
    except Exception:
        traceback.print_exc()
        result['success'] = False
        result['url'] = ''
    return json.dumps(result)


@article.route('/save', methods=['post'])
def saveArticle():
    result = {
        'code': 500
    }
    try:
        body = json.loads(request.data.decode('utf-8'))
        title = getTitle(body['data'])
        checkTitle =db.select_id_by_title(title)
        if checkTitle is True:
            result['code'] = 200
            article = {
                'id': body['id'],
                'title': title,
                'contend': body['data'],
                'tags': body['tags'],
                'kind': body['kind']
            }
            article_id = db.updateById(article)
            result['id'] = article_id
        if checkTitle is not True and checkTitle is not False:
            if checkTitle['id'] == body['id']:
                result['code'] = 200
                article = {
                    'id': body['id'],
                    'title': title,
                    'contend': body['data'],
                    'tags': body['tags'],
                    'kind': body['kind']
                }
                article_id = db.updateById(article)
                result['id'] = article_id
            else:
                result['code'] = 202  # 代表文章恢复
                result['id'] = checkTitle['id']
                result['contend'] = checkTitle['contend']
                result['updateTime'] = checkTitle['updateTime']
                if checkTitle['tags'] is not None:
                    result['tags'] = json.loads(checkTitle['tags'])
                if checkTitle['kind'] is not None:
                    result['kind'] = checkTitle['kind']
                else:
                    result['kind'] = None
    except Exception:
        traceback.print_exc()
    return json.dumps(result)


@article.route('/init', methods=['post'])
def initArticle():
    result = {
        'code': 500
    }
    try:
        body = json.loads(request.data.decode('utf-8'))
        title = getTitle(body['data'])
        article = {
            # 'id': body['id'],
            'title': title,
            'contend': body['data']
        }
        res = db.select_id_by_title(title)
        if res is True:
            article_id = db.insert(article)
            result['code'] = 200
            result['id'] = article_id
        elif res is not False and res is not True:
            print(res)
            if title == "不如来写篇文章吧":
                result['code'] = 200
            else:
                result['code'] = 201
            result['id'] = res['id']
            result['contend'] = res['contend']
        else:
            result['code'] = 202
    except Exception:
        traceback.print_exc()
    return json.dumps(result)
