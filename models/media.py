from dataclasses import dataclass


@dataclass
class MovingData():
    friendly_name: str
    move_filepath: str

@dataclass
class Media():
    friendly_name: str
    media_filepath: str

