from enum import Enum

import pyglet


class Character:
    class Direction(Enum):
        UP = 1
        DOWN = 2
        LEFT = 3
        RIGHT = 4
        STOP = 5

    def __init__(self, tile_row):
        self.x = 0
        self.y = 0
        self.tilemap = pyglet.resource.image('pacmann.png')
        self.tilemap_grid = pyglet.image.ImageGrid(self.tilemap, 20, 20)
        self.image = self.tilemap_grid[tile_row, 0]
        # 1 - gora, 2 - dol/ 3 - lewo. 4 - prawo * 5 - brak ruchu
        self.state = self.Direction.STOP
        self.speed = 100


    def draw(self):
        pyglet.gl.glBlendFunc(
            pyglet.gl.GL_SRC_ALPHA,
            pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
        self.image.blit(self.x, self.y)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def snap(self):
        if self.state == 1:
            self.y = (self.y + 31) // 32
            self.y = self.y * 32
        if self.state == 2:
            self.y = self.y // 32
            self.y = self.y * 32
        if self.state == 3:
            self.x = self.x // 32
            self.x = self.x * 32
        if self.state == 4:
            self.x = (self.x + 31) // 32
            self.x = self.x * 32

    def update(self, dt, m):
        self.dx = 0
        self.dy = 0
        if self.state == self.Direction.UP:
            self.dy = self.speed * dt
        elif self.state == self.Direction.DOWN:
            self.dy = -self.speed * dt
        elif self.state == self.Direction.LEFT:
            self.dx = -self.speed * dt
        elif self.state == self.Direction.RIGHT:
            self.dx = self.speed * dt
        self.x += self.dx
        self.y += self.dy
