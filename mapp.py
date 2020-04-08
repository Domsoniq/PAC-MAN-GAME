import pyglet

from ghost import Ghost, GhostUpDown, GhostLeftRight, GhostAimBot


class Mapp:
    def __init__(self, filename, pacman):
        self.pacman = pacman
        self.data = []
        self.ghosts = []
        with open(filename) as f:
            for line in f:
                self.data.append(line)
        self.wall = pyglet.resource.image('W.png')

        ghost_y = 0
        for line in self.data:
            ghost_x = 0
            for spot in line:
                if spot == '1':
                    g =GhostLeftRight()
                    g.set_position(ghost_x, ghost_y)
                    self.ghosts.append(g)
                elif spot == '2':
                    g = GhostUpDown()
                    g.set_position(ghost_x, ghost_y)
                    self.ghosts.append(g)
                elif spot == '3':
                    g = GhostAimBot()
                    g.set_position(ghost_x, ghost_y)
                    g.state = g.get_direction_to_pacman(self.pacman)
                    self.ghosts.append(g)
                ghost_x += 32
            ghost_y += 32

    def draw(self):
        wall_y = 0
        for line in self.data:
            wall_x = 0
            for spot in line:
                if spot == '#':
                    self.wall.blit(wall_x, wall_y)
                wall_x += 32
            wall_y += 32

    def set_position(self, character, p):
        for line_number, line in enumerate(self.data):
            for column_number, spot in enumerate(line):
                if spot == character:
                    x = column_number * 32
                    y = line_number * 32
                    p.set_position(x, y)

    def is_position_on_the_wall(self, xx, yy):
        nk = int(xx // 32)
        nl = int(yy // 32)
        line = self.data[nl]
        spot = line[nk]
        return spot == "#"

    def character_touches_wall(self, p):
        w1 = self.is_position_on_the_wall(p.x, p.y)
        w2 = self.is_position_on_the_wall(p.x + 32 - 1, p.y)
        w3 = self.is_position_on_the_wall(p.x + 32 - 1, p.y + 32 - 1)
        w4 = self.is_position_on_the_wall(p.x, p.y + 32 - 1)
        return w1 or w2 or w3 or w4

