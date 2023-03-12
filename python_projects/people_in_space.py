#!/usr/bin/python3

import requests

response = requests.get('http://api.open-notify.org/astros.json')

json = response.json()

print("The People in Space are:")

for person in json['people']:

        print(person['name'])
