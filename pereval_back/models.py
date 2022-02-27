from datetime import datetime
from typing import Optional, List, Dict
from pydantic import BaseModel
# from uuid import UUID, uuid4


class User(BaseModel):
    id: str #Optional[UUID] = uuid4()
    email: str  
    phone: str      
    fam: str
    name: str
    otc: Optional[str]


class Coords(BaseModel):
    latitude: Optional[float] #??? "45.3842",
    longitude: Optional[float] #??? "7.1525",
    height: int #??? "1200"


class Level(BaseModel):
    winter: Optional[str] #"", // текстовое поле "Категория трудности"
    summer: Optional[str] 
    autumn: Optional[str] 
    spring: Optional[str] 


class Data(BaseModel):
    #data: dict
    id: int
    beautyTitle: str
    title: str
    other_titles: str
    connect: str #что соединяет  
    add_time: datetime
    user: User #допустимы поля id, email, phone, fam, name, otc
    coords: Coords # = {latitude: float #??? "45.3842",
            # longitude: float #??? "7.1525",
            # height: int #??? "1200"
            # }
    type: str = "pass" #константа для всех запросов приложения 
    level: Level #{"winter": "", // текстовое поле "Категория трудности"
    # "summer": "1А",
    # "autumn": "1А",
    # "spring": ""},
    images: List[Dict[str, str]]
