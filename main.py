import sys

import pygame as pg
from pygame import QUIT, K_SPACE

from game_board_ui import GameBoardUI
from game_config import GameConfig
from game_const import MAP_IMAGE, MAP_NOOBJECT_BKG, PINK, RED, DIRECT_UP, DIRECT_DOWN, DIRECT_LEFT, DIRECT_RIGHT, \
    MAP_WITHOBJECT_BKG
from game_state import GameState
from player import Player

if __name__ == '__main__':
    pg.init()
    '''
    background = pg.image.load('background.png')
    screen = pg.display.set_mode(background.get_size())
    background.convert()
    screen.blit(background, (0, 0))
    '''
    new_game_config = GameConfig(MAP_IMAGE[MAP_WITHOBJECT_BKG], "Target Hit !", (640, 480), 10, 0)
    new_game_board_ui = GameBoardUI(new_game_config)
    player1 = Player('Jenna', 12345, True, RED, new_game_config.init_speed, DIRECT_UP, 400, 400)
    new_game_state = GameState()
    new_game_state.add_player(player1)
    #new_game_board_ui.on_draw(new_game_state)
    #pg.time.delay(10000)
    while 1:
        for event in pg.event.get():
            if event.type in (pg.QUIT, pg.K_SPACE):
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    new_game_state.player_change_direction(player1.id, DIRECT_UP)
                elif event.key == pg.K_DOWN:
                    new_game_state.player_change_direction(player1.id, DIRECT_DOWN)
                elif event.key == pg.K_LEFT:
                    new_game_state.player_change_direction(player1.id, DIRECT_LEFT)
                elif event.key == pg.K_RIGHT:
                    new_game_state.player_change_direction(player1.id, DIRECT_RIGHT)
        new_game_state.player_move()
        new_game_board_ui.on_draw(new_game_state)
        pg.time.delay(100)

