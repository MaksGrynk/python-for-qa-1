
import requests


ENDPOINT = 'https://httpbin.org/post'


def main():
    data = {'field1': 'value1',
            'field2': 'value2'}
    response = requests.post(ENDPOINT, data)
    print(response.text)

if __name__ == '__main__':
    main()
