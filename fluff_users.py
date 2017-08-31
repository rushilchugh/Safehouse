__author__ = 'Rushil'

if __name__ == '__main__':

    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Safehouse.settings')

    import django
    django.setup()

    print("Environment Setup Successfully")


import random
import requests

from readalert.models import People
import datetime

def get_random_ip():
    return '{0}.{1}.{2}.{3}'.format(random.randint(10, 255), random.randint(10, 255), random.randint(10, 255),
                                    random.randint(10, 255))

for _ in range(1, 100):

    curr_ip = get_random_ip()
    url = 'http://freegeoip.net/json/{0}'.format(curr_ip)

    r = requests.get(url)
    print(curr_ip, r.content, url)
    resp = r.json()

    perp = People.objects.create(ip_address = resp['ip'], latitude = resp['latitude'], longitude = resp['longitude'], timezone = resp['time_zone'], metro_code = resp['metro_code'], region_code = resp['region_code'], region_name = resp['region_name'], country_code = resp['country_code'], zip_code = resp['zip_code'], country_name = resp['country_name'], city = resp['city'], date_time = datetime.datetime.now(), is_safehouse = random.choice([0, 0, 0, 0, 1]))

    print('Created - ', People.objects.get(ip_address = curr_ip))
