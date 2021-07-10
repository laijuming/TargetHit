from game_const import GAME_BEGIN, GAME_END


class GameState:
    def __init__(self):
        self.players = {}
        self.current_target = None
        self.players_life = {}
        self.game_status = GAME_BEGIN
        self.game_end_msg = None

    def add_player(self, player):
        self.players[player.id] = player
        self.players_life[player.id] = 1

    def add_target(self, target, pos_x, pos_y):
        self.current_target = (target, pos_x, pos_y)

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

    def remove_target(self):
        self.current_target = None

    def player_die(self,player_id):
        self.players_life[player_id] -= 1

    def check_game_status(self):
        winner = None
        loser = None
        for player_id, _ in self.players.items():
            if self.players_life[player_id] == 0:
                loser = player_id
            if self.players_life[player_id] > 0:
                winner = player_id
        if winner and not loser:
            return True
        elif not winner:
            self.game_end_msg = "Both die"
            self.game_status = GAME_END
            return False
        else:
            self.game_end_msg = "Winner is" + self.players[winner].name
            self.game_status = GAME_END
            return False




