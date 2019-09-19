
"""Module for the TSD Auth API."""

import json
import requests

from client_config import ENV

def get_jwt_basic_auth(env, pnum, api_key):
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(api_key)}
    url = '{0}/{1}/auth/basic/token'.format(ENV[env], pnum)
    try:
        resp = requests.post(url, headers=headers)
    except Exception:
        return None
    if resp.status_code in [200, 201]:
        token = json.loads(resp.text)['token']
        return token
    else:
        return None


def get_jwt_tsd_auth(env, pnum, api_key, user_name, password,
                     otp, token_type):
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(api_key)}
    data = {'user_name': user_name, 'password': password, 'otp': otp}
    url = '{0}/{1}/auth/tsd/token?type={2}' % (ENV[env], pnum, token_type)
    try:
        resp = requests.post(url, data=json.dumps(data), headers=headers)
    except Exception:
        return None
    if resp.status_code in [200, 201]:
        token = json.loads(resp.text)['token']
        return token
    else:
        return None
