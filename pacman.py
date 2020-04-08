import pyglet

from character import Character


class Pacman(Character):
    def __init__(self):
        super().__init__(19)

        self.pacman_frames = 2
        self.pacman_actual_frame = 0
        self.pacman_time_count = 0.0

        self.speed = 160

    def key_pressed(self, key):
        if key == pyglet.window.key.UP:
            self.state = self.Direction.UP
        if key == pyglet.window.key.DOWN:
            self.state = self.Direction.DOWN
        if key == pyglet.window.key.LEFT:
            self.state = self.Direction.LEFT
        if key == pyglet.window.key.RIGHT:
            self.state = self.Direction.RIGHT
        if key == pyglet.window.key.SPACE:
            self.state = self.Direction.STOP

    def update(self, dt, m):
        super().update(dt, m)

        if m.character_touches_wall(self):
            self.x -= self.dx
            self.y -= self.dy
            self.snap()
            self.state = 5

        self.pacman_time_count += dt
        if self.pacman_time_count > 0.3:
            self.pacman_actual_frame = (self.pacman_actual_frame + 1) % self.pacman_frames
            self.pacman_time_count = 0.0
        self.image = self.tilemap_grid[19, self.pacman_actual_frame]
