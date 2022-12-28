"""
This file represents all the routes to administer media
"""

from fastapi import APIRouter

#let's create router
media_router = APIRouter(
    prefix='/media',
    tags = ['media']
)

@media_router.get('/list')
def route_list():
    return "list"

@media_router.get('/add')
def route_list():
    return "list"

@media_router.get('/remove')
def route_list():
    return "list"