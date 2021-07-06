import pygame

from game_const import TARGET_IMAGE


class GameState:
    def __init__(self):
        self.players = {}
        self.current_target = None

    def add_player(self, player):
        self.players[player.id] = player

    def add_target(self, target, pos_x, pos_y):
        self.current_target = (pygame.image.load(TARGET_IMAGE[target]), pos_x, pos_y)

    def get_players_state(self):
        for _, each in self.players.items():
            for part in each.get_player_state():
                yield part

    def get_target_state(self):
        return self.current_target

    def player_change_direction(self, id, direction):
        if id in self.players:
            self.players[id].change_head_direction(direction)

    def player_move(self):
        for _, each in self.players.items():
            each.move()
