
import requests


COOKIES_ENDPOINT = 'http://httpbin.org/cookies/set/sessioncookie/123456789'
GET_ENDPOINT = 'http://httpbin.org/get'


def main():
    session = requests.Session()
    session.headers.update({'x-test': 'true'})

    response = session.get(COOKIES_ENDPOINT)
    # cookies saved for future requests
    print(response.text)  # "X-Test": "true"

    response = session.get(GET_ENDPOINT)
    # cookies sent automatically
    print(response.request._cookies.values())  # ['123456789']
    print(response.text)  # "X-Test": "true"


if __name__ == '__main__':
    main()
