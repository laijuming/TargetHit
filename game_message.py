import json

from game_config import GameConfig
from game_const import MSG_HOST, MSG_JOIN, MSG_GAME_HOST_ACK, MSG_GAME_JOIN_ACK, MSG_PLAYER_READY
from player import Player


class GameHostMsg:
    @staticmethod
    def serialize(_game_config, _host):
        msg = {"msg_type": MSG_HOST,
               "payload": {"map": _game_config._game_map,
                           "name": _game_config._game_name,
                           "board_size": _game_config._board_size,
                           "speed": _game_config._init_speed,
                           "game_mode": _game_config._game_mode,
                           "player_name": _host.name,
                           "player_id": _host.id,
                           "player_is_host": _host.is_host,
                           "player_color": _host.color,
                           "player_speed": _host.speed,
                           "player_init_direction": _host.init_direction,
                           "player_init_x": _host.init_x,
                           "player_init_y": _host.init_y}
               }
        return json.dumps(msg)

    @staticmethod
    def deserialize(decoded_payload):
        return GameConfig(decoded_payload["map"], decoded_payload["name"], decoded_payload["board_size"], \
                          decoded_payload["speed"], decoded_payload["game_mode"]), \
               Player(decoded_payload["player_name"], decoded_payload["player_id"], decoded_payload["player_is_host"],
                      decoded_payload["player_color"], decoded_payload["player_speed"],
                      decoded_payload["player_init_direction"], decoded_payload["player_init_x"],
                      decoded_payload["player_init_y"])


class GameJoinMsg:
    @staticmethod
    def serialize(_player):
        msg = {"msg_type": MSG_JOIN,
               "payload": {"player_id": _player.id,
                           "player_name": _player.name,
                           "player_color": _player.color,
                           "player_speed": _player.speed,
                           "player_is_host": _player.is_host,
                           "player_init_direction": _player.init_direction,
                           "player_init_x": _player.init_x,
                           "player_init_y": _player.init_y
                           }
               }
        return json.dumps(msg)

    @staticmethod
    def deserialize(decoded_payload):
        return Player(decoded_payload["player_name"], decoded_payload["player_id"], decoded_payload["player_is_host"],
                      decoded_payload["player_color"], decoded_payload["player_speed"],
                      decoded_payload["player_init_direction"], decoded_payload["player_init_x"],
                      decoded_payload["player_init_y"])


class GamePlayerReadyMsg:
    @staticmethod
    def serialize(_session_id, _player_id):
        msg = {"msg_type": MSG_PLAYER_READY,
               "payload": {"session_id": _session_id,
                           "player_id": _player_id
                           }
               }
        print("GamePlayerReadyMsg",str(msg))
        return json.dumps(msg)

    @staticmethod
    def deserialize(decoded_payload):
        return decoded_payload["session_id"], decoded_payload["player_id"]


class GameHostAckMsg:
    @staticmethod
    def serialize(_session_id):
        msg = {"msg_type": MSG_GAME_HOST_ACK,
               "payload": {"session_id": _session_id
                           }
               }
        return json.dumps(msg)

    @staticmethod
    def deserialize(decoded_payload):
        return decoded_payload["session_id"]


class GameJoinAckMsg:
    @staticmethod
    def serialize(_session_id, _game_config):
        msg = {"msg_type": MSG_GAME_JOIN_ACK,
               "payload": {"session_id": _session_id,
                           "game_map": _game_config._game_map,
                           "game_name": _game_config._game_name,
                           "board_size": _game_config._board_size,
                           "init_speed": _game_config._init_speed,
                           "game_mode": _game_config._game_mode
                           }
               }
        return json.dumps(msg)

    @staticmethod
    def deserialize(decoded_payload):
        return decoded_payload["session_id"], \
               GameConfig(decoded_payload["game_map"],
                          decoded_payload["game_name"],
                          decoded_payload["board_size"],
                          decoded_payload["init_speed"],
                          decoded_payload["game_mode"])
