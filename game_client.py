import json
from ws4py.client.threadedclient import WebSocketClient

from game_const import MSG_GAME_HOST_ACK, MSG_GAME_JOIN_ACK, MSG_GAME_UPDATE
from game_message import GameHostMsg, GamePlayerReadyMsg, GameJoinMsg, GameJoinAckMsg, GameHostAckMsg, \
    GameStatesUpdateMsg, DirectionUpdateMsg


class GameClient(WebSocketClient):
    """

    """
    def __init__(self, server_host):
        super().__init__(server_host)
        self._game_config = None
        self._game_session_id = None
        self._game_board_ui = None
        self._player = None
        self._game_initialized = False
        self._game_state = None

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
        decoded_msg = json.loads(str(message))
        if decoded_msg['msg_type'] == MSG_GAME_HOST_ACK:
            self._game_session_id = GameHostAckMsg.deserialize(decoded_msg['payload'])
            self._game_initialized = True
            self.send(GamePlayerReadyMsg.serialize(self._game_session_id, self._player.id))
        if decoded_msg['msg_type'] == MSG_GAME_JOIN_ACK:
            session_id, game_config = GameJoinAckMsg.deserialize(decoded_msg['payload'])
            self._game_session_id = session_id
            self._game_config = game_config
            self._game_initialized = True
            self.send(GamePlayerReadyMsg.serialize(self._game_session_id, self._player.id))
        if decoded_msg['msg_type'] == MSG_GAME_UPDATE:
            game_state_snapshot = GameStatesUpdateMsg.deserialize(decoded_msg['payload'])
            self._game_state = game_state_snapshot

    def change_direction(self,direction):
        print("gameclient change_direciton",direction)
        self.send(DirectionUpdateMsg.serialize(self._game_session_id,self._player.id,direction))

