"""
@author: east
@date:
@function:
"""
import json
import traceback

from flask import Blueprint,request
from DAO.sneakerlover.record import RecordDao

sneaker = Blueprint('sneaker', import_name=__name__, url_prefix='/v1/sneaker')

@sneaker.route('/rank', methods=['get'])
def rank():

    result ={
        'data':[],
        'code': 500
    }
    try:
        dao = RecordDao()
        res = dao.rank()
        result['code'] = 200
        for item in res:
            item_dict = {
                'name': item[0],
                'times': item[1],
                'detail': dao.select_detail_by_name(item[0])
            }
            result['data'].append(item_dict)
        return json.dumps(result,ensure_ascii=False)
    except Exception:
        traceback.print_exc()
        return json.dumps(result)