"""
@author: east
@date:
@function:
"""
import json
import datetime
import time
import traceback

from flask import Blueprint, request, make_response
from DAO.basic.article import ArticleSql
from Utils.getTitle import getTitle

article = Blueprint('article', url_prefix='/article', import_name=__name__)


@article.route('/getNameByKind', methods=['get'])
def get_article_id():
    kind = request.args.get('kind')
    data = ArticleSql().select_by_kind(kind, 10)
    if data is not False:
        res_list = []
        if len(data) > 0:
            for item in data:
                article_dict = {
                    'name': item[1],
                    'id': item[0],
                    'time': item[6].strftime("%Y-%m-%d"),
                    'tags': json.loads(item[3])
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
        data = ArticleSql().select_by_id(article_id)
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
    result = {}
    try:
        f = request.files['image']
        file_name = f.filename.split('.')
        file_url = f'/static/{f.filename[0]}_{str(int(time.time()))}.{file_name[1]}'
        f.save(f'.{file_url}')
        result['url'] = './api' + file_url
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
        result['code'] = 200
        article = {
            'id': body['id'],
            'title': title,
            'contend': body['data']
        }
        article_id = ArticleSql().updateById(article)
        result['id'] = article_id
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
        res = ArticleSql().select_id_by_title(title)
        if res is True:
            article_id = ArticleSql().insert(article)
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
