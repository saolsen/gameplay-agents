from pydantic import BaseModel
from typing import Literal

Game = Literal["connect4"]

class BaseAction(BaseModel):
    game: Game

class BaseState(BaseModel):
    game: Game
    over: bool = False
    winner: int | None = None
    next_player: int | None = None
