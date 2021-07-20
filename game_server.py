import asyncio
import json
import traceback

from ws4py.async_websocket import WebSocket
from ws4py.server.tulipserver import WebSocketProtocol

from game_const import MSG_HOST, MSG_JOIN, MSG_PLAYER_READY, GAME_RUNNING, MSG_DIRECTION_UPDATE, GAME_END
from game_manager import GameManager
from game_message import GameHostMsg, GameJoinMsg, GameHostAckMsg, GamePlayerReadyMsg, DirectionUpdateMsg
from player import Player

loop = asyncio.get_event_loop()

# global game manager on server
game_manager = GameManager()


class RemotePlayer(Player):
    """
    Inheritance from Player - to attach websocket to client
    """

    def __init__(self, _player, _ws):
        super().__init__(_player.name, _player.id, _player.is_host, _player.color, _player.speed,
                         _player.init_direction,
                         _player.init_x, _player.init_y)
        self.ws = _ws


@asyncio.coroutine
def server_update():
    # periodically send game state update message to clients async
    while True:
        yield from asyncio.sleep(0.01)
        for id, session in game_manager._game_session.items():
            # if session._game_state.game_status == GAME_RUNNING or session._game_state.game_status == GAME_END:
            while session._session_async_queue:
                conn, msg = session._session_async_queue.pop()
                conn.send(msg)


class GameSocket(WebSocket):
    """
    Game server message handler
    """
    def received_message(self, msg):
        try:
            decoded_msg = json.loads(str(msg))
            msg_type = decoded_msg["msg_type"]
            if msg_type == MSG_HOST:
                game_config, host = GameHostMsg.deserialize(decoded_msg["payload"])
                session_id = game_manager.create_game_session(game_config, RemotePlayer(host, self))
                self.send(GameHostAckMsg.serialize(session_id))

            elif msg_type == MSG_JOIN:
                player = GameJoinMsg.deserialize(decoded_msg["payload"])
                game_manager.match_game(RemotePlayer(player, self))

            elif msg_type == MSG_PLAYER_READY:
                session_id, player_id = GamePlayerReadyMsg.deserialize(decoded_msg["payload"])
                game_session = game_manager.get_game_session(session_id)
                game_session.player_ready(player_id)

            elif msg_type == MSG_DIRECTION_UPDATE:
                session_id, player_id, direction = DirectionUpdateMsg.deserialize(decoded_msg["payload"])
                game_session = game_manager.get_game_session(session_id)
                game_session.on_player_move(player_id, direction)


        except Exception as exp:
            print(str(exp))
            traceback.print_exc()


def start_server():
    proto_factory = lambda: WebSocketProtocol(GameSocket)
    return loop.create_server(proto_factory, '', 9007)


if __name__ == '__main__':
    server = loop.run_until_complete(start_server())
    print("server is up")
    asyncio.async(server_update())
    loop.run_forever()
