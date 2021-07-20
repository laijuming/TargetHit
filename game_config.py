class GameConfig:
    """
    Take user input configuration parameters:
    parameters:
    game_map - background map
    game_name - player name
    board_size - this is not used now. size is determined by background map size now
    init_speed - initial speed of player
    game_mode - host a game or join a game
    """
    def __init__(self, game_map, game_name, board_size, init_speed, game_mode):
        self._game_map = game_map
        self._game_name = game_name
        self._board_size = board_size
        self._init_speed = init_speed
        self._game_mode = game_mode

    @property
    def map(self):
        return self._game_map

    @property
    def name(self):
        return self._game_name

    @property
    def board_size(self):
        return self._board_size

    @property
    def init_speed(self):
        return self._init_speed

    @property
    def game_mode(self):
        return self._game_mode