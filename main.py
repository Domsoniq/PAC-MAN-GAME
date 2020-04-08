import pyglet

from ghost import Ghost
from mapp import Mapp
from pacman import Pacman

pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(
    pyglet.gl.GL_SRC_ALPHA,
    pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

window = pyglet.window.Window(640, 480)
fps = 60
p = Pacman()
m = Mapp("map.txt", p)


@window.event
def on_key_press(symbol, modifiers):
    p.key_pressed(symbol)

@window.event
def on_draw():
    window.clear()
    pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
    m.draw()
    p.draw()
    for g in m.ghosts:
        g.draw()

def update(dt):
    p.update(dt, m)
    for g in m.ghosts:
        g.update(dt, m)

pyglet.clock.schedule_interval(update, 1/fps)

m.set_position('P', p)
pyglet.app.run()