from character import Character


class Ghost(Character):
    def __init__(self):
        super().__init__(18)
        self.speed = 100

    def update(self, dt, m):
        super().update(dt, m)


class GhostLeftRight(Ghost):
    def __init__(self):
        super().__init__()
        self.state = self.Direction.LEFT

    def update(self, dt, m):
        super().update(dt, m)
        if m.character_touches_wall(self):
            self.x -= self.dx
            self.y -= self.dy
            self.snap()

            if self.state == self.Direction.LEFT:
                self.state = self.Direction.RIGHT
            elif self.state == self.Direction.RIGHT:
                self.state = self.Direction.LEFT

class GhostUpDown(Ghost):
    def __init__(self):
        super().__init__()
        self.state = self.Direction.UP

    def update(self, dt, m):
        super().update(dt, m)
        if m.character_touches_wall(self):
            self.x -= self.dx
            self.y -= self.dy
            self.snap()

            if self.state == self.Direction.UP:
                self.state = self.Direction.DOWN
            elif self.state == self.Direction.DOWN:
                self.state = self.Direction.UP


class GhostAimBot(Ghost):
    def __init__(self):
        super().__init__()
        self.direction = None

    def update(self, dt, m):
        super().update(dt, m)
        if m.character_touches_wall(self):
            self.x -= self.dx
            self.y -= self.dy
            self.snap()

            self.state = self.get_direction_to_pacman(m.pacman)

    def get_direction_to_pacman(self, pacman):
        diff_x = self.x - pacman.x
        diff_y = self.y - pacman.y

        if abs(diff_x) > abs(diff_y):
            if self.x > pacman.x:
                return self.Direction.LEFT
            else:
                return self.Direction.RIGHT
        else:
            if self.y > pacman.y:
                return self.Direction.DOWN
            else:
                return self.Direction.UP


