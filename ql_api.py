import json
import time
from typing import Tuple, Any

import requests

ql_auth_path = '/ql/config/auth.json'
# ql_auth_path = r'D:\Docker\ql\config\auth.json'
ql_url = 'http://localhost:5600'


def __get_token() -> str or None:
    with open(ql_auth_path, 'r', encoding='utf-8') as f:
        j_data = json.load(f)
    return j_data.get('token')


def __get__headers() -> dict:
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8',
        'Authorization': 'Bearer ' + __get_token()
    }
    return headers


# 查询任务
def get_crons(search_value: str = None) -> Tuple[bool, Any]:
    params = {
        't': int(time.time() * 1000)
    }
    if search_value is not None:
        params['searchValue'] = search_value
    res = requests.get(ql_url + '/api/crons', headers=__get__headers(), params=params)
    j_data = res.json()
    if j_data['code'] == 200:
        return True, j_data['data']
    return False, None


# 查询最后一条日志
def get_crons_log(cron_id: int) -> Tuple[bool, Any]:
    params = {
        't': int(time.time() * 1000)
    }
    res = requests.get(ql_url + '/api/crons/{}/log'.format(cron_id), headers=__get__headers(), params=params)
    j_data = res.json()
    if j_data['code'] == 200:
        return True, j_data['data']
    return False, None

