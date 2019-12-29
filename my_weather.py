'''
This script prints out the weather for the cities given as arguments.
Cities should be separated by ','. FE: Dublin,Rome,London
Optional: add a '-f' flag for Fahrenheit, '-c' flag for Celsius.
If needed, please change the value of the api key.
'''

from requests import get
import json
import requests
import sys

# Change api key value to yours if needed
api_key = 'bc30006e191a5efcc61d86b1db0153bd'

def weather_in(city):
    city_list = city[1].split(',')
    fahrenheit = city[-1] == '-f'

    for city in city_list:
        try:
            url = 'http://api.weatherstack.com/current?access_key={}&query={}'.format(api_key, city)
            json_data = (requests.get(url)).json()

            celsius = json_data['current']['temperature']
            temperature = (celsius*1.8)+32 if fahrenheit else celsius
            scale = 'Fahrenheit' if fahrenheit else 'Celsius'

            print('The weather in {} today is {} degrees {}'.format(city, temperature, scale))

        except KeyError as city_error:
            print('{} does not exist, maybe try Bigfoot or Bacon'.format(city))


def main(cities):
    weather_in(cities)

if __name__ == '__main__':
    main(sys.argv)
