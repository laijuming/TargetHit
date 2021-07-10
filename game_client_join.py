import pygame
from ws4py.client.threadedclient import WebSocketClient

from game_board_ui import GameBoardUI
from game_config import GameConfig
from game_const import MAP_IMAGE, DIRECT_UP, MAP_WITHOBJECT_BKG, RED, PINK
from game_message import GameHostMsg, GameJoinMsg
from player import Player

from game_client import GameClient

if __name__ == '__main__':
    pygame.init()
    game_client = GameClient("ws://localhost:9007/")
    game_client.connect()
    player2 = Player('Nan', 54321, True, PINK, 40, DIRECT_UP, 800, 400)
    game_client.join_game(player2)
    game_board_ui = None
    while True:
        if not game_board_ui:
            if game_client._game_initialized:
                game_board_ui = GameBoardUI(game_client._game_config)

        if game_board_ui:
            game_board_ui.on_draw(None)

        pygame.time.delay(100)
