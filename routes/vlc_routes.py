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


def vlc_http_request(method: str, params: dict, resource_file: str):
    config = vlc_router_main.fapi.config

    url = f"http://{config['VLC']['host']}:{config['VLC']['port']}/requests/{resource_file}"

    r = requests.request(method, 
                            url, 
                            params=params, 
                            auth=('', config['VLC']['http_password']))
    if r.status_code < 200 or r.status_code >= 300:
        # Forward the HTTP client error
        raise HTTPException(status_code=r.status_code, detail=r.text)

    return r.json()


@vlc_router.get('/status')
def route_status():
    return vlc_http_request('GET', None, "status.json")


@vlc_router.get('/playlist')
def route_playlist(videoid: int = 0):
    return vlc_http_request('GET', None, "playlist.json")


@vlc_router.get('/queue')
def route_status(file: str):
    para = {}
    para['command'] = "in_enqueue"
    para['input'] = file
    return vlc_http_request('GET', para, "status.json")


@vlc_router.get('/emptyqueue')
def route_status():
    para = {}
    para['command'] = "pl_empty"
    return vlc_http_request('GET', para, "status.json")


@vlc_router.get('/play')
def route_play():
    para = {}
    para['command'] = "pl_play"
    return vlc_http_request('GET', para, "status.json")


@vlc_router.get('/play_queue')
def route_play(videoid: int = 0):
    para = {}
    para['command'] = "pl_play"
    para['id'] = videoid
    return vlc_http_request('GET', para, "status.json")


@vlc_router.get('/pause')
def route_play():
#def route_play(videoid: int = 0):
    para = {}
    para['command'] = "pl_pause"
#    para['id'] = videoid
    return vlc_http_request('GET', para, "status.json")


@vlc_router.get('/stop')
def route_play():
#def route_play(videoid: int = 0):
    para = {}
    para['command'] = "pl_stop"
#    para['id'] = videoid
    return vlc_http_request('GET', para, "status.json")




# curl -u :vlcrouter "http://127.0.0.1:9090/requests/status.json?command=in_play&input=/Users/okoeroo/Movies/samples/tearsofsteel/tears_of_steel_720p.mov

# curl -u :testtest "http://127.0.0.1:8080/requests/status.json?command=pl_start"
# curl -u :testtest "http://127.0.0.1:8080/requests/status.json?command=pl_stop"
# curl -u :testtest "http://127.0.0.1:8080/requests/status.json?command=in_play&input=/Users/okoeroo/Movies/samples/tearsofsteel/tearsofsteel_4k.mov"

# curl -u :vlcrouter "http://127.0.0.1:9009/requests/status.json?command=in_play&input=/Users/okoeroo/Movies/samples/tearsofsteel/tears_of_steel_720p.mov&output=#std{access=udp, mux=ts, dst=127.0.0.1:1234}"