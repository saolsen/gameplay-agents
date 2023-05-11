from base import BaseAction, BaseState
from typing import Literal

class Connect4Action(BaseAction):
    game: Literal["connect4"] = "connect4"
    column: int

class Connect4State(BaseState):
    game: Literal["connect4"] = "connect4"
    board: list[list[str]]