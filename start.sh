#!/bin/bash

uvicorn vlc_router_main:fapi --reload --host 0.0.0.0 --port 8008

