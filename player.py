import pygame

from game_const import DIRECT_UP, DIRECT_DOWN, DIRECT_LEFT, DIRECT_RIGHT, PLAYER_IMAGE, PLAYER_HEAD


class PlayerTarget:

    def __init__(self, body_type, direction, pos_x, pos_y, color):
        self.body_type = body_type
        self.direction = direction
        self.next = None
        self.color = color
        self.x = pos_x
        self.y = pos_y
        print(PLAYER_IMAGE[(self.body_type, self.direction, self.color)])
        self.image = pygame.image.load(PLAYER_IMAGE[(self.body_type, self.direction, self.color)])
        self.image.convert()


    def update_direction(self, direction):
        next_direction = self.direction

        if self.direction in [DIRECT_UP, DIRECT_DOWN] and direction in [DIRECT_LEFT, DIRECT_RIGHT]:
            next_direction = direction
        elif self.direction in [DIRECT_LEFT, DIRECT_RIGHT] and direction in [DIRECT_UP, DIRECT_DOWN]:
            next_direction = direction

        print('direction',direction)
        print('current direction',self.direction)
        print("next_direction",next_direction)
        if next_direction is not self.direction:
            self.direction = direction
            self.image = pygame.image.load(PLAYER_IMAGE[(self.body_type, self.direction, self.color)])


class Player:
    def __init__(self, name, id, is_host, color, init_speed, init_direction, init_x, init_y):

        self.name = name
        self.id = id
        self.is_host = is_host
        self.color = color
        self.speed = init_speed
        self.player_target = PlayerTarget(PLAYER_HEAD, init_direction, init_x, init_y, color)

    def move(self):

        if self.player_target.direction == DIRECT_UP:
            self.player_target.y -= self.speed
        elif self.player_target.direction == DIRECT_DOWN:
            self.player_target.y += self.speed
        elif self.player_target.direction == DIRECT_LEFT:
            self.player_target.x -= self.speed
        elif self.player_target.direction == DIRECT_RIGHT:
            self.player_target.x += self.speed

        print('x,y',self.player_target.x,self.player_target.y)
        p = self.player_target

        while p.next:
            p.next.update_direction(p.direction)
            p.next.x = p.x
            p.next.y = p.y
            p = p.next

    def get_player_state(self):
        p = self.player_target
        while p:
            yield p.image, p.x, p.y
            p = p.next

    def change_head_direction(self, direction):
        self.player_target.update_direction(direction)

    def eat(self):
        pass
