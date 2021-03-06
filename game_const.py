"""
This file stores all constants
"""
#player direction
DIRECT_UP = 0
DIRECT_DOWN = 1
DIRECT_LEFT = 2
DIRECT_RIGHT = 3

# to distinguish head and body of the player
PLAYER_HEAD = 0
PLAYER_BODY = 1

#player color
PINK = 999
RED = 888

#goal type
TARGET_TYPE_GOAL = 0
TARGET_TYPE_GROWTH = 1
TARGET_TYPE_IDEA = 2
TARGET_TYPE_SUPPORT = 3

#background
MAP_NOOBJECT_BKG = 0
MAP_WITHOBJECT_BKG = 1
MAP_IMAGE = {MAP_NOOBJECT_BKG: "./assets/map/target_noobject_bkg.png",
             MAP_WITHOBJECT_BKG: "./assets/map/target_bkg.png"
             }

#window size -  now matching background map
WINDOW_WIDTH, WINDOW_HEIGHT = 1500, 1500
GRID_SIZE = 50
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

#message type
MSG_HOST = 0
MSG_JOIN = 1
MSG_GAME_START = 2
MSG_GAME_UPDATE = 3
MSG_GAME_END = 4
MSG_GAME_HOST_ACK = 5
MSG_GAME_JOIN_ACK = 6 #payload is session_id
MSG_PLAYER_READY = 8
MSG_MATCH_NOT_FOUND = 9
MSG_DIRECTION_UPDATE = 10

#session status
SESSION_CREATED = 0
SESSION_MATCHED = 1

#game status
GAME_BEGIN = 1
GAME_END = 0
GAME_RUNNING = 2

#player status
PLAYER_JOIN = 0
PLAYER_READY = 1
