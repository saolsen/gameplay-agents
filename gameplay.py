from pydantic import BaseModel, Field
from typing import Literal, Annotated
from connect4 import Connect4Action, Connect4State

class User(BaseModel):
    kind: Literal["user"] = "user"
    username: str

class Agent(BaseModel):
    kind: Literal["agent"] = "agent"
    username: str
    agentname: str

Player = Annotated[User|Agent, Field(discrminator="kind")]

Action = Connect4Action
State = Connect4State
class Turn(BaseModel):
    number: int
    player: int | None
    action: Action | None
    next_player: int | None

class Match(BaseModel):
    id: int
    players: list[Player]
    turns: list[Turn]
    state: State
