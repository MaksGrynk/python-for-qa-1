
import requests


ENDPOINT = 'https://maps.googleapis.com/maps/api/geocode/json'
KEY = 'AIzaSyAKQ5TpmQrvEP4lbLND34Pg3o3BQLvuQHM'


def main():
    params = {'key': KEY,
              'address': 'Market Square, Lviv',
              'components': 'country:UA'}

    response = requests.get(ENDPOINT, params=params)
    print(response.text)


if __name__ == '__main__':
    main()
