import pygame as pg


class GameBoardUI:
    def __init__(self, _game_config):
        self._map = pg.image.load(_game_config._game_map)
        self._window = pg.display.set_mode(self._map.get_size())
        pg.display.set_caption(_game_config._game_name)
        self._map.convert()

    def on_draw(self, game_state):
        self._window.blit(self._map, (0, 0))
        for image, x, y in game_state.get_players_state():
             #pos = image.get_rect().move(x, y)
             print("BoardUI x, y",x,y)
             self._window.blit(image, (x,y))
        target = game_state.get_target_state()
        if target:
            self._window.blit(target[0],(target[1],target[2]))
        pg.display.flip()
        #pg.display.update()

