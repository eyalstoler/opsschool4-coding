#!/usr/bin/env python
import click
from requests import get
import json
import sys

@click.command()
@click.option('--token', '-token', required=True, help='your API token')
@click.option('--city', '-city', required=True, help='the cities separated by commas')
@click.option('--T', 'temp_scale', '-T', type=click.Choice(['Celsius', 'Fahrenheit']),
                default='Celsius', show_default='Celsius', help='temperature scale')

def weather(token, city, temp_scale):
    for city in city.split(','):
        temp_url = 'f' if temp_scale == 'Fahrenheit' else 'm'
        weather_response = get('http://api.weatherstack.com/current?access_key={}&query={}&units={}'.format(token,city,temp_url))
        city_json = json.loads(weather_response.text)
        try:
            city_temp = str(city_json['current']['temperature'])
            location = city_json['location']['name']
            click.echo('The weather in %s is %s degrees %s' % (location,city_temp,temp_scale))
        except (KeyError) as city_error:
            print('Error: {} does not exist. Please try real cities like Blabla, Bigfoot, or Chicken'.format(city))

if __name__ == '__main__':
    weather()
