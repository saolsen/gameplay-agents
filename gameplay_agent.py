from fastapi import FastAPI
from gameplay import Match, Action
from connect4_random import connect4_random_agent
from connect4_copycat import connect4_copycat_agent
from connect4_errors import connect4_errors_agent

def build_app():
    app = FastAPI()

    @app.post("/connect4_random")
    async def connect4_random(match: Match) -> Action:
        assert match.state.game == "connect4"
        assert match.state.next_player is not None
        return connect4_random_agent(match)

    @app.post("/connect4_copycat")
    async def connect4_mcts(match: Match):
        assert match.state.game == "connect4"
        assert match.state.next_player is not None
        return connect4_copycat_agent(match)

    @app.post("/connect4_errors")
    async def connect4_mcts(match: Match):
        assert match.state.game == "connect4"
        assert match.state.next_player is not None
        return connect4_errors_agent(match)

    return app
