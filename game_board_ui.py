import pygame as pg

from game_const import PLAYER_HEAD, PINK, PLAYER_BODY, DIRECT_DOWN, RED, DIRECT_LEFT, \
    DIRECT_RIGHT, DIRECT_UP, TARGET_TYPE_GOAL, TARGET_TYPE_GROWTH, TARGET_TYPE_IDEA, TARGET_TYPE_SUPPORT, GAME_END


class GameBoardUI:
    def __init__(self, _game_config):
        self._map = pg.image.load(_game_config._game_map)
        self._window = pg.display.set_mode(self._map.get_size())
        pg.display.set_caption(_game_config._game_name)
        self._map.convert()
        
        PINK_HEAD_UP_IMAGE = pg.image.load("./assets/player/player_pink_head_up.png")
        PINK_HEAD_UP_IMAGE.convert()
        PINK_HEAD_DOWN_IMAGE = pg.image.load("./assets/player/player_pink_head_down.png")
        PINK_HEAD_DOWN_IMAGE.convert()
        PINK_HEAD_LEFT_IMAGE = pg.image.load("./assets/player/player_pink_head_left.png")
        PINK_HEAD_LEFT_IMAGE.convert()
        PINK_HEAD_RIGHT_IMAGE = pg.image.load("./assets/player/player_pink_head_right.png")
        PINK_HEAD_RIGHT_IMAGE.convert()
        PINK_BODY_UP_IMAGE = pg.image.load("./assets/player/player_pink_body_up.png")
        PINK_BODY_UP_IMAGE.convert()
        PINK_BODY_DOWN_IMAGE = pg.image.load("./assets/player/player_pink_body_down.png")
        PINK_BODY_DOWN_IMAGE.convert()
        PINK_BODY_LEFT_IMAGE = pg.image.load("./assets/player/player_pink_body_left.png")
        PINK_BODY_LEFT_IMAGE.convert()
        PINK_BODY_RIGHT_IMAGE = pg.image.load("./assets/player/player_pink_body_right.png")
        PINK_BODY_RIGHT_IMAGE.convert()
        RED_HEAD_UP_IMAGE = pg.image.load("./assets/player/player_red_head_up.png")
        RED_HEAD_UP_IMAGE.convert()
        RED_HEAD_DOWN_IMAGE = pg.image.load("./assets/player/player_red_head_down.png")
        RED_HEAD_DOWN_IMAGE.convert()
        RED_HEAD_LEFT_IMAGE = pg.image.load("./assets/player/player_red_head_left.png")
        RED_HEAD_LEFT_IMAGE.convert()
        RED_HEAD_RIGHT_IMAGE = pg.image.load("./assets/player/player_red_head_right.png")
        RED_HEAD_RIGHT_IMAGE.convert()
        RED_BODY_UP_IMAGE = pg.image.load("./assets/player/player_red_body_up.png")
        RED_BODY_UP_IMAGE.convert()
        RED_BODY_DOWN_IMAGE = pg.image.load("./assets/player/player_red_body_down.png")
        RED_BODY_DOWN_IMAGE.convert()
        RED_BODY_LEFT_IMAGE = pg.image.load("./assets/player/player_red_body_left.png")
        RED_BODY_LEFT_IMAGE.convert()
        RED_BODY_RIGHT_IMAGE = pg.image.load("./assets/player/player_red_body_right.png")
        RED_BODY_RIGHT_IMAGE.convert()

        #display_msg = pg.font.SysFont('Comic Sans MS', 50) #cause slowness
        #self.game_end_surface = display_msg.render("Game end", True, (255, 255, 255))

        self.player_image = {(PLAYER_HEAD, DIRECT_UP, PINK): PINK_HEAD_UP_IMAGE,
                    (PLAYER_HEAD, DIRECT_DOWN, PINK): PINK_HEAD_DOWN_IMAGE,
                    (PLAYER_HEAD, DIRECT_LEFT, PINK): PINK_HEAD_LEFT_IMAGE,
                    (PLAYER_HEAD, DIRECT_RIGHT, PINK): PINK_HEAD_RIGHT_IMAGE,
                    (PLAYER_HEAD, DIRECT_UP, RED): RED_HEAD_UP_IMAGE,
                    (PLAYER_HEAD, DIRECT_DOWN, RED): RED_HEAD_DOWN_IMAGE,
                    (PLAYER_HEAD, DIRECT_LEFT, RED): RED_HEAD_LEFT_IMAGE,
                    (PLAYER_HEAD, DIRECT_RIGHT, RED): RED_HEAD_RIGHT_IMAGE,
                    (PLAYER_BODY, DIRECT_UP, PINK): PINK_BODY_UP_IMAGE,
                    (PLAYER_BODY, DIRECT_DOWN, PINK): PINK_BODY_DOWN_IMAGE,
                    (PLAYER_BODY, DIRECT_LEFT, PINK): PINK_BODY_LEFT_IMAGE,
                    (PLAYER_BODY, DIRECT_RIGHT, PINK): PINK_BODY_RIGHT_IMAGE,
                    (PLAYER_BODY, DIRECT_UP, RED): RED_BODY_UP_IMAGE,
                    (PLAYER_BODY, DIRECT_DOWN, RED): RED_BODY_DOWN_IMAGE,
                    (PLAYER_BODY, DIRECT_LEFT, RED): RED_BODY_LEFT_IMAGE,
                    (PLAYER_BODY, DIRECT_RIGHT, RED): RED_BODY_RIGHT_IMAGE,
                    }

        GOAL_IMAGE = pg.image.load("./assets/player/goal_goal.png")
        GOAL_IMAGE.convert()
        GROWTH_IMAGE = pg.image.load("./assets/player/goal_growth.png")
        GROWTH_IMAGE.convert()
        IDEA_IMAGE = pg.image.load("./assets/player/goal_idea.png")
        IDEA_IMAGE.convert()
        SUPPORT_IMAGE = pg.image.load("./assets/player/goal_support.png")
        SUPPORT_IMAGE.convert()

        self.target_image = {TARGET_TYPE_GOAL: GOAL_IMAGE,
                    TARGET_TYPE_GROWTH: GROWTH_IMAGE,
                    TARGET_TYPE_IDEA: IDEA_IMAGE,
                    TARGET_TYPE_SUPPORT: SUPPORT_IMAGE
                    }

    def on_draw(self, game_state):
        self._window.blit(self._map, (0, 0))
        if game_state is not None:
            for bt, direct, color, x, y,_ in game_state.get_players_state():
                # pos = image.get_rect().move(x, y)
                # print("BoardUI x, y",x,y)
                self._window.blit(self.player_image[(bt, direct, color)], (x, y))
            target = game_state.get_target_state()
            if target:
                self._window.blit(self.target_image[target[0]], (target[1], target[2]))
            if game_state.game_status == GAME_END:
                pass
                #self._window.blit(self.game_end_surface,(100,100))
        pg.display.flip()
        # pg.display.update()
