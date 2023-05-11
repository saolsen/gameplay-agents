import random
from collections import defaultdict
from gameplay import Match
from connect4 import Connect4Action as Action

# Example of how to keep state.
state = defaultdict(lambda: {"count": 0})


def connect4_errors_agent(match: Match) -> Action:
    # Agent that throws 500's every other request.
    count = state[str(match.id)]["count"]
    state[str(match.id)]["count"] += 1

    if state[str(match.id)]["count"] % 2 == 0:
        open_columns = [i for i in range(7) if match.state.board[i][5] == " "]
        column = random.choice(open_columns)

        return Action(column=column)
    else:
        raise Exception("500 error")
