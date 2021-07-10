import datetime
import json

from game_const import SESSION_CREATED, SESSION_MATCHED, MSG_MATCH_NOT_FOUND
from game_message import GameJoinAckMsg
from game_session import GameSession


class GameManager:
    def __init__(self):
        self._game_session = {}

    def create_game_session(self, _game_config, _host):
        session_id = _host.name + datetime.datetime.now().strftime("%H:%M:%S")
        new_game_session = GameSession(_game_config, SESSION_CREATED)
        new_game_session.add_player(_host)
        self._game_session[session_id] = new_game_session
        return session_id

    def match_game(self, _player):
        for session_id in self._game_session:
            if self._game_session[session_id].session_status == SESSION_CREATED:
                self._game_session[session_id].session_status == SESSION_MATCHED
                self._game_session[session_id].add_player(_player)
                _player.ws.send(GameJoinAckMsg.serialize(session_id, self._game_session[session_id]._game_config
                                                         ))
                return
        _player.ws.send(json.dumps({'msg_type':MSG_MATCH_NOT_FOUND}))

    def end_game(self, _session_id):
        pass

    def get_game_session(self, _session_id):
        return self._game_session[_session_id]
