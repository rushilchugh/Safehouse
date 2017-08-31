from django.shortcuts import render
import datetime
from .models import People
from ipware.ip import get_ip
import requests
import random
from math import sin, cos, sqrt, atan2, radians
import operator
import json
from .forms import UserForm
# Create your views here.

u_ip = '34.234.239.234'

def dist(lat1, long1, lat2, long2):

    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(long1)
    lat2 = radians(lat2)
    lon2 = radians(long2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


def home(request):

    ##Configuring Map##

    dist_dict = []

    user_lat_long = People.objects.all()[0]

    for j, i in enumerate(People.objects.all()):
        curr_dist = dist(user_lat_long.latitude, user_lat_long.longitude, i.latitude, i.longitude)
        dist_dict.append([str(curr_dist), float(i.latitude), float(i.longitude), j])

    sorted_dist_dict = sorted(dist_dict, key = operator.itemgetter(0))

    nearest_10 = sorted_dist_dict[1:11]
    nearest_10.insert(0, ["0", float(user_lat_long.latitude), float(user_lat_long.longitude)])

    print(nearest_10)

    context_dict = {
        "array": nearest_10,
        "cent_lat": user_lat_long.latitude,
        "cent_long": user_lat_long.longitude,
    }

    print(nearest_10)


    return render(request, 'readalert/reg.html', context_dict)

def index(request):
    ip_address_user = get_ip(request)
    print(ip_address_user)

    form = UserForm()

    url = 'http://freegeoip.net/json/{0}'.format(ip_address_user)
    r = requests.get(url)
    resp = r.json()

    print(resp)

    perp = People(ip_address = resp['ip'], latitude = resp['latitude'], longitude = resp['longitude'], timezone = resp['time_zone'], metro_code = resp['metro_code'], region_code = resp['region_code'], region_name = resp['region_name'], country_code = resp['country_code'], zip_code = resp['zip_code'], country_name = resp['country_name'], city = resp['city'], date_time = datetime.datetime.now(), is_safehouse = random.choice([0, 0, 0, 0, 1]))
    perp.save()

    mappings = open(r'C:\NOS\Coding_2\Safehouse\lookups\mappings.txt', 'a+')
    format_string = '''{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}|{10}\n'''.format(resp['ip'], resp['latitude'], resp['longitude'], resp['time_zone'], resp['metro_code'], resp['region_code'], resp['region_name'], resp['country_code'], resp['zip_code'], resp['country_name'], resp['city'])
    mappings.write(format_string)
    mappings.close()

    print(format_string)

    context_dict = {

    }

    return render(request, 'readalert/index.html', context_dict)


def register(request):

    context_dict = {
        'form': UserForm()
    }

    return render(request, 'readalert/register.html', context_dict)

def alert(request):

    dist_dict = {}

    ip_address_user = get_ip(request)

    user_lat_long = People.objects.get(ip_address = u_ip)

    for i in People.objects.all():
        curr_dist = dist(user_lat_long.latitude, user_lat_long.longitude, i.latitude, i.longitude)
        dist_dict[i] = curr_dist

    sorted_dist_dict = sorted(dist_dict.items(), key = operator.itemgetter(1))

    nearest_10 = sorted_dist_dict[1:11]

    context_dict = {
        'ip': user_lat_long.ip_address,
        'nearest_10': nearest_10
    }

    print(nearest_10)

    for i, j in nearest_10:
        print(i.ip_address, i.latitude, i.longitude, i.region_code, j, sep = '\t')

    return render(request, 'readalert/alert.html', context_dict)


def disp_map(request):

    dist_dict = {}

    ip_address_user = get_ip(request)

    user_lat_long = People.objects.get(ip_address = u_ip)

    for i in People.objects.all():
        curr_dist = dist(user_lat_long.latitude, user_lat_long.longitude, i.latitude, i.longitude)
        dist_dict[i] = curr_dist
#{a:b, c:d}
    sorted_dist_dict = sorted(dist_dict.items(), key = operator.itemgetter(1))

    nearest_10 = sorted_dist_dict[1:11]

    j_resp = []

    for i, j in nearest_10:
        j_resp.append({'title': i.ip_address, 'lat': str(i.latitude), 'lng': str(i.longitude), 'description': '{0} Kilometers Away'.format(j)})

    context_dict = {
        'json_resp': json.dumps(j_resp),
    }

    return render(request, 'readalert/map.html', context_dict)