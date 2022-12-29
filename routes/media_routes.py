from fastapi import APIRouter
from models.media import Media, MovingData
import vlc_router_main


media_router = APIRouter(
    prefix='/media',
    tags = ['media']
)


@media_router.get('/list')
def route_list():
    session = vlc_router_main.fapi.Session_generator()
    medias = [m for m in session.query(Media).order_by(Media.id)]
    return medias


@media_router.get('/add')
def route_add(friendly: str, filepath: str):
    session = vlc_router_main.fapi.Session_generator()
    m = Media(friendly_name=friendly, filepath=filepath)    
    session.add(m)
    session.commit()
    return str(m)


@media_router.get('/remove')
def route_remove():
    return "list"