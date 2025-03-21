from enum import Enum

class Game:
    def __init__(self, name: str, game_id: int):
        self.name: str = name
        self.game_id: int = game_id


class GameStartType(Enum):
    UNIXBIN = 1  # UNIX binary
    WINEXE = 2  # Windows executable file (i.e. an .exe file)
    SCRIPT = 3  # Normally either a .sh or .bat file
    HTML = 4