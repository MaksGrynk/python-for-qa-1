
import json
import xmltodict

import requests
from requests.auth import HTTPBasicAuth


DATA_ENDPOINT = 'https://python-for-qa.herokuapp.com/data'
LOGIN_ENDPOINT = 'https://python-for-qa.herokuapp.com/login'
AUTH = HTTPBasicAuth('admin', 'password')
FALSE_VALUES = ['false', '0']


def get_data(token, accept_type):
    response = requests.get(
        DATA_ENDPOINT, headers={'X-AUTH-TOKEN': token,
                                'Accept': accept_type})
    return response.content


def login():
    response = requests.get(LOGIN_ENDPOINT, auth=AUTH)
    if response.status_code == requests.codes.ok:
        return response.json()['token']
    return None


def str_to_bool(value):
    return value.lower() not in FALSE_VALUES


def diff(left, rigth):
    result = []

    if isinstance(left, list):
        if len(left) != len(rigth):
            return ['Length is not equal']
        for i in range(0, len(left)):
            result.extend(diff(left[i], rigth[i]))
    elif isinstance(left, dict):
        if set(left.keys()) != set(rigth.keys()):
            return ['Keys are not equal']
        for key in left.keys():
            result.extend(diff(left[key], rigth[key]))
    else:
        left_type = type(left)
        rigth = left_type(rigth) if left_type != bool else str_to_bool(rigth)
        if isinstance(left, str) or isinstance(left, unicode):
            left = left.replace('\r\n', '')
        return [(left, rigth)] if left != rigth else []

    return result


def main():
    token = login()

    json_data = json.loads(get_data(token, 'application/json'))
    xml_data = xmltodict.parse(get_data(token, 'application/xml'))
    xml_items = xml_data['items']['item']

    diffs = diff(json_data, xml_items)
    print(diffs)


if __name__ == '__main__':
    main()
