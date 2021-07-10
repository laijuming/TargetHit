import pygame

from game_board_ui import GameBoardUI
from game_config import GameConfig
from game_const import MAP_IMAGE, DIRECT_UP, MAP_WITHOBJECT_BKG, RED
from player import Player

from game_client import GameClient

if __name__ == '__main__':
    pygame.init()
    game_client = GameClient("ws://localhost:9007/")
    game_client.connect()
    new_game_config = GameConfig(MAP_IMAGE[MAP_WITHOBJECT_BKG], "Target Hit !", (640, 480), 40, 0)
    player1 = Player('Jenna', 12345, True, RED, new_game_config.init_speed, DIRECT_UP, 400, 400)
    game_client.host_game(new_game_config,player1)
    game_board_ui = None
    while True:
        if not game_client._game_initialized:
            game_board_ui = GameBoardUI(game_client._game_config)

        if game_board_ui: game_board_ui.on_draw(None)

        pygame.time.delay(100)


