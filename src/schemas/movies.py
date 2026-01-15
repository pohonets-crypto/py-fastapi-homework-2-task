import datetime

from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional

class MovieDetailSchema(BaseModel):
    id: int
    name: str
    date: datetime.date
    score: float
    genre: str
    overview: str
    crew: str
    orig_title: str
    status: str
    orig_lang: str
    budget: float
    revenue: float
    country: str
    model_config = ConfigDict(from_attributes=True)


class MovieListResponseSchema(BaseModel):
    movies: List[MovieDetailSchema]
    prev_page: Optional[str]
    next_page: Optional[str]
    total_pages: int
    total_items: int


class MovieListItemSchema(BaseModel):
    id: int
    name: str
    date: str
    score: float
    overview: str


class MovieCreate(BaseModel):
    name: str
    date: datetime.date
    score: float
    overview: Optional[str]
    status: str
    budget: float
    revenue: float
    country: str
    genres: List[str] = []
    actors: List[str] = []
    languages: List[str] = []


class MovieUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    date: Optional[datetime.date]
    score: Optional[float] = Field(None, ge=0, le=100)
    overview: Optional[str]
    status: Optional[str]
    budget: Optional[float] = Field(None, ge=0)
    revenue: Optional[float] = Field(None, ge=0)


class CountryResponse(BaseModel):
    id: int
    code: str
    name: Optional[str]


class GenreResponse(BaseModel):
    id: int
    name: str


class ActorResponse(BaseModel):
    id: int
    name: str


class LanguageResponse(BaseModel):
    id: int
    name: str
