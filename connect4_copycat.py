import random
from gameplay import Match
from connect4 import Connect4Action as Action

def connect4_copycat_agent(match: Match) -> Action:
    last_turn = match.turns[-1]
    if last_turn.action is None:
        # new game, pick the middle
        return Action(column=3)

    column = last_turn.action.column
    print("they picked column", column, "last turn")

    # If the column is still open copy the last move.
    if match.state.board[column][5] == " ":
        print("I picked column", column, "too")
        return Action(column=column)

    # Otherwise pick a random open column.
    open_columns = [i for i in range(7) if match.state.board[i][5] == " "]
    column = random.choice(open_columns)

    return Action(column=column)
