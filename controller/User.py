"""
@author: east
@date:
@function:
"""
import json

from flask import Blueprint
from DAO.basic.user import UserMethod

USER = Blueprint('USER', import_name=__name__, url_prefix='/user')


@USER.route('/getUserInfo', methods=['get'])
def getUserInfo():
    data = UserMethod().selectUserInfo()
    user_info = {}
    if data is not False:
        user_info['name'] = data[0][1]
        user_info['headImage'] = data[0][-2]
        user_info['words'] = data[0][2]
        user_info['headWord'] = data[0][-1]
    return json.dumps(user_info, ensure_ascii=False)
