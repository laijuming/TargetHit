import asyncio
import time

from game_const import PLAYER_JOIN, PLAYER_READY, GAME_RUNNING
from game_master import GameMaster
from game_message import GameStatesUpdateMsg
from game_state import GameState
from threading import Thread


class GameSession:
    def __init__(self, _game_config, _session_status):
        self._game_config = _game_config
        self._game_state = GameState()
        self._game_master = GameMaster(self._game_state)
        self._session_status = _session_status
        self._player_status = {}
        self._game_runner = Thread(name='game_runner', target=self.run_game)
        self._game_runner.daemon = True

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
        self._game_state.game_status = GAME_RUNNING
        self._game_runner.start()

    def run_game(self):

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)


        while self._game_state.check_game_status():
            self._game_master.game_update()
            self._game_master.random_event()

            game_state_update = GameStatesUpdateMsg.serialize(self._game_state)

            for _, player in self._game_state.players.items():
                print("run_game",game_state_update)
                loop.run_until_complete(player.ws.send(game_state_update))

            time.sleep(0.1)


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
