import sys

import pygame as pg

from game_board_ui import GameBoardUI
from game_const import DIRECT_UP, PINK, DIRECT_DOWN, DIRECT_LEFT, DIRECT_RIGHT
from player import Player
from game_client import GameClient
"""
Main client to join a game

Pre configure player 1 as Red, can be changed to user config
Connect to local server, if connect to remote server, change to public IP

"""
if __name__ == '__main__':
    pg.init()
    game_client = GameClient("ws://localhost:9007/")
    game_client.connect()
    player2 = Player('Nan', 54321, True, PINK, 40, DIRECT_UP, 800, 400)
    game_client.join_game(player2)
    game_board_ui = None
    while True:
        if not game_board_ui:
            if game_client._game_initialized:
                game_board_ui = GameBoardUI(game_client._game_config)

        if game_client._game_state:
            if not game_client._game_state.check_game_status():
                game_client.close_connection()
                sys.exit()

            for event in pg.event.get():
                if event.type in (pg.QUIT, pg.K_ESCAPE):
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

