#/usr/bin/env python3

import os
import sys
import signal

# FastAPI
from fastapi import FastAPI
from routes.media_routes import media_router
from routes.vlc_routes import vlc_router

# Import functies
from funcs.config import read_config, check_config, get_vlc_cmdline
from funcs.process_handling import kill_proc, start_fresh_vlc

from funcs.database import setup_database_engine_into_session_generator


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
### Fire up the database
##########################################
Session_generator = setup_database_engine_into_session_generator(config)


##########################################
### Start VLC
##########################################
try:
    start_fresh_vlc(get_vlc_cmdline(config), config['VLC']['pid_filename'])
except FileNotFoundError as e:
    print(f"Error starting VLC: executable not found. cmdline: \"{get_vlc_cmdline(config)}\"")

    # Kill parent, being uvicorn here
    kill_proc(os.getppid(), signal.SIGTERM)
    sys.exit(1)

##########################################
### FastAPI Loading
##########################################
fapi = FastAPI()

## Adding routes
fapi.include_router(media_router)
fapi.include_router(vlc_router)

## Global passing
fapi.config = config
fapi.Session_generator = Session_generator
