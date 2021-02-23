from dataclasses import dataclass

@dataclass
class Camera:
    id: int
    name: str
    url: str
    current_frame: bytes = None
