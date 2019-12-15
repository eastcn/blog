"""
@author: east
@date:
@function:
"""


def getTitle(body):
    if '\n' in body and '#' in body:
        title = body.split('\n')[0].split('#')[1]
    else:
        title = body.split('#')[1]
    return title.replace(' ', '')
