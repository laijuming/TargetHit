import json
from ws4py.client.threadedclient import WebSocketClient

from game_const import MSG_GAME_HOST_ACK, MSG_GAME_JOIN_ACK
from game_message import GameHostMsg, GamePlayerReadyMsg, GameJoinMsg, GameJoinAckMsg, GameHostAckMsg


class GameClient(WebSocketClient):
    def __init__(self, server_host):
        super().__init__(server_host)
        self._game_config = None
        self._game_session_id = None
        self._game_board_ui = None
        self._player = None
        self._game_initialized = False

    def host_game(self,_game_config, _player):
        self._game_config = _game_config
        self._player = _player
        host_msg = GameHostMsg.serialize(_game_config, _player)
        self.send(host_msg)
        print("host waiting for game join")

    def join_game(self,_player):
        self._player = _player
        join_msg = GameJoinMsg.serialize(_player)
        self.send(join_msg)
        print("join waiting for game match")

    def received_message(self, message):
        print(message)
        decoded_msg = json.loads(str(message))
        if decoded_msg['msg_type'] == MSG_GAME_HOST_ACK:
            self._game_session_id = GameHostAckMsg.deserialize(decoded_msg['payload'])
            self._game_initialized = True
            #self._game_board_ui = GameBoardUI(self._game_config)
            self.send(GamePlayerReadyMsg.serialize(self._game_session_id, self._player.id))
        if decoded_msg['msg_type'] == MSG_GAME_JOIN_ACK:
            session_id, game_config = GameJoinAckMsg.deserialize(decoded_msg['payload'])
            self._game_session_id = session_id
            self._game_config = game_config
            self._game_initialized = True
            #self._game_board_ui =GameBoardUI(self._game_config)
            self.send(GamePlayerReadyMsg.serialize(self._game_session_id, self._player.id))

