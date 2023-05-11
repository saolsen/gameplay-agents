import random
from gameplay import Match
from connect4 import Connect4Action as Action

def connect4_random_agent(match: Match) -> Action:
    # Pick a random open column
    open_columns = [i for i in range(7) if match.state.board[i][5] == " "]
    column = random.choice(open_columns)

    return Action(column=column)
