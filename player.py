from game_const import DIRECT_UP, DIRECT_DOWN, DIRECT_LEFT, DIRECT_RIGHT, PLAYER_HEAD, GRID_SIZE, PLAYER_BODY, \
    WINDOW_WIDTH, WINDOW_HEIGHT


class PlayerBody:
    """Link list to move body following head"""

    def __init__(self, body_type, direction, pos_x, pos_y, color):
        self.body_type = body_type
        self.direction = direction
        self.next = None
        self.color = color
        self.x = pos_x
        self.y = pos_y

    def update_direction(self, direction):
        next_direction = self.direction

        if self.direction in [DIRECT_UP, DIRECT_DOWN] and direction in [DIRECT_LEFT, DIRECT_RIGHT]:
            next_direction = direction
        elif self.direction in [DIRECT_LEFT, DIRECT_RIGHT] and direction in [DIRECT_UP, DIRECT_DOWN]:
            next_direction = direction

        if next_direction is not self.direction:
            self.direction = direction


class Player:
    """Player's head control and actions"""

    def __init__(self, name, id, is_host, color, init_speed, init_direction, init_x, init_y):
        self.name = name
        self.id = id
        self.is_host = is_host
        self.color = color
        self.speed = init_speed
        self.init_direction = init_direction
        self.init_x = init_x
        self.init_y = init_y
        self.player_target = PlayerBody(PLAYER_HEAD, init_direction, init_x, init_y, color)
        self.tail = self.player_target

    def move(self):
        p = self.tail

        while p.next:
            p.update_direction(p.next.direction)
            p.x = p.next.x
            p.y = p.next.y
            # print("px py",p.x,p.y)
            p = p.next

        if self.player_target.direction == DIRECT_UP:
            self.player_target.y -= self.speed
        elif self.player_target.direction == DIRECT_DOWN:
            self.player_target.y += self.speed
        elif self.player_target.direction == DIRECT_LEFT:
            self.player_target.x -= self.speed
        elif self.player_target.direction == DIRECT_RIGHT:
            self.player_target.x += self.speed

        self.player_target.x = self.player_target.x % WINDOW_WIDTH if self.player_target.x >= 0 \
            else self.player_target.x + WINDOW_WIDTH
        self.player_target.y = self.player_target.y % WINDOW_HEIGHT if self.player_target.y >= 0 \
            else self.player_target.y + WINDOW_HEIGHT

    def get_player_state(self):
        p = self.tail
        while p:
            # print("body_type,x,y", p.body_type, p.x, p.y)
            yield p.body_type, p.direction, p.color, p.x, p.y, self.id
            p = p.next

    def change_head_direction(self, direction):
        self.player_target.update_direction(direction)

    def grow(self):
        new_x = self.tail.x
        new_y = self.tail.y
        if self.tail.direction == DIRECT_UP:
            new_y += self.speed
        elif self.tail.direction == DIRECT_DOWN:
            new_y -= self.speed
        elif self.tail.direction == DIRECT_LEFT:
            new_x += self.speed
        elif self.tail.direction == DIRECT_RIGHT:
            new_x -= self.speed

        # print("newx,newy", new_x, new_y)
        new_body = PlayerBody(PLAYER_BODY, self.tail.direction, new_x, new_y, self.tail.color)
        new_body.next = self.tail
        self.tail = new_body
