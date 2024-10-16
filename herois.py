from pydantic import BaseModel
from typing import Optional

class Heros(BaseModel):
    id: Optional[int]
    nome: str
    poderes: str


herois = [
    Heros(id=1, nome='Surfista prateado', poderes='Controlar o tempo, e paralisar pessoas. '),
    Heros(id=2, nome='Capitão américa', poderes='Super força, e telepatia. '),
    Heros(id=3, nome='Viuva negra', poderes='ultrapassa paredes, e ficar invisível. '),
   
]