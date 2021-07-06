DIRECT_UP = 0
DIRECT_DOWN = 1
DIRECT_LEFT = 2
DIRECT_RIGHT = 3
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
PINK_HEAD_UP_IMAGE = "./assets/player/player_pink_head_up.png"
PINK_HEAD_DOWN_IMAGE = "./assets/player/player_pink_head_down.png"
PINK_HEAD_LEFT_IMAGE = "./assets/player/player_pink_head_left.png"
PINK_HEAD_RIGHT_IMAGE = "./assets/player/player_pink_head_right.png"
PINK_BODY_UP_IMAGE = "./assets/player/player_pink_body_up.png"
PINK_BODY_DOWN_IMAGE = "./assets/player/player_pink_body_down.png"
PINK_BODY_LEFT_IMAGE = "./assets/player/player_pink_body_left.png"
PINK_BODY_RIGHT_IMAGE = "./assets/player/player_pink_body_right.png"
RED_HEAD_UP_IMAGE = "./assets/player/player_red_head_up.png"
RED_HEAD_DOWN_IMAGE = "./assets/player/player_red_head_down.png"
RED_HEAD_LEFT_IMAGE = "./assets/player/player_red_head_left.png"
RED_HEAD_RIGHT_IMAGE = "./assets/player/player_red_head_right.png"
RED_BODY_UP_IMAGE = "./assets/player/player_red_body_up.png"
RED_BODY_DOWN_IMAGE = "./assets/player/player_red_body_down.png"
RED_BODY_LEFT_IMAGE = "./assets/player/player_red_body_left.png"
RED_BODY_RIGHT_IMAGE = "./assets/player/player_red_body_right.png"

PLAYER_HEAD = 0
PLAYER_BODY = 1

PINK = 999
RED = 888

PLAYER_IMAGE = {(PLAYER_HEAD, DIRECT_UP, PINK): PINK_HEAD_UP_IMAGE,
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

TARGET_TYPE_GOAL = 0
TARGET_TYPE_GROWTH = 1
TARGET_TYPE_IDEA = 2
TARGET_TYPE_SUPPORT = 3

TARGET_IMAGE = {TARGET_TYPE_GOAL: "./assets/player/goal_goal.png",
                TARGET_TYPE_GROWTH: "./assets/player/goal_growth.png",
                TARGET_TYPE_IDEA: "./assets/player/goal_idea.png",
                TARGET_TYPE_SUPPORT: "./assets/player/goal_support.png"
                }

MAP_NOOBJECT_BKG = 0
MAP_WITHOBJECT_BKG = 1
MAP_IMAGE = {MAP_NOOBJECT_BKG: "./assets/map/target_noobject_bkg.png",
             MAP_WITHOBJECT_BKG: "./assets/map/target_bkg.png"
             }