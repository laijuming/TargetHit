from game_const import PLAYER_JOIN, PLAYER_READY
from game_master import GameMaster
from game_state import GameState


class GameSession:
    def __init__(self, _game_config, _session_status):
        self._game_config = _game_config
        self._game_state = GameState()
        self._game_master = GameMaster(self._game_state)
        self._session_status = _session_status
        self._player_status = {}

    @property
    def session_status(self):
        return self._session_status

    @session_status.setter
    def session_status(self, _session_status):
        self._session_status = _session_status

    def add_player(self, _player):
        self._game_state.add_player(_player)
        self._player_status[_player.id] = PLAYER_JOIN

    def game_start(self):
        print("session game start")
        pass

    def game_end(self):
        pass

    def game_init(self):
        pass

    def on_player_move(self, play_move_msg):
        pass

    def on_game_update(self):
        pass

    def player_join(self, player, player_pos):
        pass

    def player_ready(self, player_id):
        self._player_status[player_id] = PLAYER_READY
        is_game_start = True
        print("in player_ready",self._player_status)
        if len(self._player_status) > 1:
            print("length", len(self._player_status))
            for player_id, player_status in self._player_status.items():
                print("player_status",player_status)
                if player_status == PLAYER_JOIN:
                    is_game_start = False
        else:
            is_game_start = False

        if is_game_start:
            print("game starting")
            self.game_start()

    def get_game_status(self):
        pass
