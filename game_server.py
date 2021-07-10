import asyncio
import json
import traceback

from ws4py.async_websocket import WebSocket
from ws4py.server.tulipserver import WebSocketProtocol

from game_const import MSG_HOST, MSG_JOIN, MSG_GAME_HOST_ACK, MSG_PLAYER_READY
from game_manager import GameManager
from game_message import GameHostMsg, GameJoinMsg, GameHostAckMsg, GamePlayerReadyMsg
from player import Player

loop = asyncio.get_event_loop()

game_manager = GameManager()


class RemotePlayer(Player):
    def __init__(self, _player, _ws):
        super().__init__(_player.name, _player.id, _player.is_host, _player.color, _player.speed,
                         _player.init_direction,
                         _player.init_x, _player.init_y)
        self.ws = _ws


class GameSocket(WebSocket):
    def received_message(self, msg):
        try:
            # print(message)
            print("enter server")
            print(msg)
            decoded_msg = json.loads(str(msg))
            msg_type = decoded_msg["msg_type"]
            #print(msg_type)
            if msg_type == MSG_HOST:
                print("enter host")
                game_config, host = GameHostMsg.deserialize(decoded_msg["payload"])
                session_id = game_manager.create_game_session(game_config, RemotePlayer(host,self))
                print("game hosted session_id, player_name", session_id, host.name)
                self.send(GameHostAckMsg.serialize(session_id))

            elif msg_type == MSG_JOIN:
                player = GameJoinMsg.deserialize(decoded_msg["payload"])
                game_manager.match_game(RemotePlayer(player, self))

            elif msg_type == MSG_PLAYER_READY:
                session_id, player_id = GamePlayerReadyMsg.deserialize(decoded_msg["payload"])
                print("PLAYER READY session id", session_id)
                game_session = game_manager.get_game_session(session_id)
                game_session.player_ready(player_id)

        except Exception as exp:
            print(str(exp))
            traceback.print_exc()


def start_server():
    proto_factory = lambda: WebSocketProtocol(GameSocket)
    return loop.create_server(proto_factory, '', 9007)


if __name__ == '__main__':
    server = loop.run_until_complete(start_server())
    loop.run_forever()
