

import requests
from requests.auth import HTTPBasicAuth


ENDPOINT = 'https://httpbin.org/basic-auth/user/passwd'
USER = 'user'
PASSWORD = 'passwd'


def main():
    response = requests.get(ENDPOINT)
    print(response.status_code)  # 401

    response = requests.get(ENDPOINT, auth=HTTPBasicAuth(USER, PASSWORD))
    print(response.status_code)  # 200

if __name__ == '__main__':
    main()
