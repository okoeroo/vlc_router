#/usr/bin/env python3

from fastapi import FastAPI
from funcs.config import read_config, check_config, get_vlc_cmdline

# Import routers
from routes.media_routes import media_router
from routes.vlc_routes import vlc_router
from funcs.process_handling import start_fresh_vlc

from httpx import AsyncClient


##########################################
### CONFIG
##########################################
config_file = "config.ini"
config = read_config(config_file)
try:
    check_config(config)
except Exception as e:
    print(f"Error: failure in {config_file} file. {e}")


##########################################
### Start VLC
##########################################
start_fresh_vlc(get_vlc_cmdline(config), config['VLC']['vlc_pid_filename'])


##########################################
### FastAPI Loading
##########################################
fapi = FastAPI()

## Adding routes
fapi.include_router(media_router)
fapi.include_router(vlc_router)

## Global passing
fapi.config = config

## Global async http client
client = AsyncClient()
fapi.client = client
