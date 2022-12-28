from typing import Union
from fastapi import APIRouter
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

import vlc_router_main

import requests


#let's create router
vlc_router = APIRouter(
    prefix='/vlc',
    tags = ['VLC']
)

@vlc_router.get('/status')
def route_status():
    config = vlc_router_main.fapi.config

    url = f"http://127.0.0.1:9009/requests/status.json"
    r = requests.get(url, auth=('', config['VLC']['vlc_http_password']))

    print(r.text)

    return r.text


# curl -u :testtest "http://127.0.0.1:8080/requests/status.json?command=pl_start"
# curl -u :testtest "http://127.0.0.1:8080/requests/status.json?command=pl_stop"
# curl -u :testtest "http://127.0.0.1:8080/requests/status.json?command=in_play&input=/Users/okoeroo/Movies/samples/tearsofsteel/tearsofsteel_4k.mov"

# curl -u :vlcrouter "http://127.0.0.1:9009/requests/status.json?command=in_play&input=/Users/okoeroo/Movies/samples/tearsofsteel/tears_of_steel_720p.mov&output=#std{access=udp, mux=ts, dst=127.0.0.1:1234}"