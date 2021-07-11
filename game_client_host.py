import sys

import pygame as pg

from game_board_ui import GameBoardUI
from game_config import GameConfig
from game_const import MAP_IMAGE, DIRECT_UP, MAP_WITHOBJECT_BKG, RED, DIRECT_DOWN, DIRECT_LEFT, DIRECT_RIGHT
from player import Player

from game_client import GameClient

if __name__ == '__main__':
    pg.init()
    game_client = GameClient("ws://localhost:9007/")
    game_client.connect()
    new_game_config = GameConfig(MAP_IMAGE[MAP_WITHOBJECT_BKG], "Target Hit !", (640, 480), 40, 0)
    player1 = Player('Jenna', 12345, True, RED, new_game_config.init_speed, DIRECT_UP, 400, 400)
    game_client.host_game(new_game_config,player1)
    game_board_ui = None
    while True:
        if not game_board_ui:
            if game_client._game_initialized:
                game_board_ui = GameBoardUI(game_client._game_config)

        if game_client._game_state:
            if not game_client._game_state.check_game_status():
                print("inside")
                game_client.close_connection()
                sys.exit()

            for event in pg.event.get():
                if event.type in (pg.QUIT, pg.K_SPACE):
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        game_client.change_direction(DIRECT_UP)
                    elif event.key == pg.K_DOWN:
                        game_client.change_direction(DIRECT_DOWN)
                    elif event.key == pg.K_LEFT:
                        game_client.change_direction(DIRECT_LEFT)
                    elif event.key == pg.K_RIGHT:
                        game_client.change_direction(DIRECT_RIGHT)

        if game_board_ui: game_board_ui.on_draw(game_client._game_state)

        pg.time.delay(80)


