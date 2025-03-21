import webbrowser
from lib.game_handler import GameStartType

def start_html(url: str) -> None:
    webbrowser.open_new(url)


def start_game_directly(game_id: int, game_start_type: GameStartType):
    pass