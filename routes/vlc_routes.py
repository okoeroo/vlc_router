from typing import Union
from fastapi import APIRouter
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse


#let's create router
vlc_router = APIRouter(
    prefix='/vlc',
    tags = ['VLC']
)

@vlc_router.get('/status')
def route_status():
    return "status"
