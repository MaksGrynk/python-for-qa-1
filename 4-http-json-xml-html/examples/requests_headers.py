
import requests


ENDPOINT = 'https://httpbin.org/post'


def main():
    headers = {'X-TOKEN': 'token123456'}
    response = requests.post(ENDPOINT, headers=headers)
    print(response.text)

if __name__ == '__main__':
    main()
