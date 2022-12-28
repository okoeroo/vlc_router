#/usr/bin/env python3

import requests
import time


host = '127.0.0.1'
port = 8008


def http_request(method: str, params: dict, command: str):
    url = f"http://{host}:{port}/vlc/{command}"

    r = requests.request(method, 
                            url, 
                            params=params)
    if r.status_code < 200 or r.status_code >= 300:
        # Forward the HTTP client error
        return None

    return r.json()

print(http_request('GET', None, "status"))
print(http_request('GET', None, "playlist"))

para = {}
para['file'] = "/Users/okoeroo/Movies/samples/tearsofsteel/tearsofsteel_4k.mov"
print(http_request('GET', para, "queue"))

print(http_request('GET', None, "playlist"))
print(http_request('GET', None, "emptyqueue"))

para = {}
para['file'] = "/Users/okoeroo/Movies/samples/tearsofsteel/tearsofsteel_4k.mov"
print(http_request('GET', para, "queue"))

print(http_request('GET', None, "play"))

time.sleep(10)

print(http_request('GET', None, "pause"))

time.sleep(10)

print(http_request('GET', None, "play"))

time.sleep(10)

print(http_request('GET', None, "stop"))