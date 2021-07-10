import sys
from random import random, randint

from game_const import GRID_WIDTH, GRID_SIZE, GRID_HEIGHT, PLAYER_HEAD, PLAYER_BODY


class GameMaster:
    """
    Server -
    GameMaster is to control the game events
    such as random targets
    """
    def __init__(self, game_state):
        self._game_state = game_state

    def random_event(self):
        if not self._game_state.current_target:
            if random() <= 0.1:
                position = (randint(0, GRID_WIDTH - 1) * GRID_SIZE, randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
                target_type = randint(0, 3) # total of 4 types of goals
                self._game_state.add_target(target_type,position[0], position[1])

    def game_update(self):
        self._game_state.player_move()
        for player_id, player in self._game_state.players.items():
            if self._game_state.current_target:
                if self.doOverlap((player.player_target.x, player.player_target.y),
                                  (player.player_target.x+GRID_SIZE,player.player_target.y+GRID_SIZE),
                                  (self._game_state.current_target[1],self._game_state.current_target[2]),
                                  (self._game_state.current_target[1] +GRID_SIZE,self._game_state.current_target[2]+\
                                                                                 GRID_SIZE)):
                    player.grow()
                    self._game_state.remove_target()
            for body_type, direction, color, x, y, id in self._game_state.get_players_state():
                if player_id == id:
                    continue
                if self.doOverlap((player.player_target.x, player.player_target.y),
                                  (player.player_target.x+GRID_SIZE,player.player_target.y+GRID_SIZE),
                                  (x,y),
                                  (x+GRID_SIZE, y+GRID_SIZE)):
                    if body_type == PLAYER_BODY:
                        print("player",player.name,"die")
                        self._game_state.player_die(player_id)
                        #sys.exit()
                    elif body_type == PLAYER_HEAD:
                        print("both die")
                        #sys.exit()
                        self._game_state.player_die(id)
                        self._game_state.player_die(player_id)

    def doOverlap(self, l1, r1, l2, r2):
        # To check if either rectangle is actually a line
        # For example  :  l1 ={-1,0}  r1={1,1}  l2={0,-1}  r2={0,1}
        if (l1[0] == r1[0] or l1[1] == r1[1] or l2[0] == r2[0] or l2[1] == r2[1]):
            # the line cannot have positive overlap
            return False
        # If one rectangle is on left side of other
        if (l1[0] >= r2[0] or l2[0] >= r1[0]):
            return False
        # If one rectangle is above other
        if (l1[1] >= r2[1] or l2[1] >= r1[1]):
            return False

        return True


