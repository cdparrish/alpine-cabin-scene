import ctypes
import os
from pyglet.gl import *
from pyglet.window import key
from pywavefront import visualization, Wavefront
from camera import FirstPersonCamera

window = pyglet.window.Window(width=2560, height=1440, caption='Cabin in the Woods', resizable=True)
window.set_exclusive_mouse(True)
window.maximize()
camera = FirstPersonCamera(window)
keys = key.KeyStateHandler()
window.push_handlers(keys)

root_path = os.path.dirname(__file__)
chair = Wavefront(os.path.join(root_path, 'models/chair.obj'))
table = Wavefront(os.path.join(root_path, 'models/table.obj'))
tree = Wavefront(os.path.join(root_path, 'models/tree.obj'))
shroom = Wavefront(os.path.join(root_path, 'models/shroom.obj'))
grass = Wavefront(os.path.join(root_path, 'models/grass.obj'))
mountain = Wavefront(os.path.join(root_path, 'models/mountain.obj'))
flagpole = Wavefront(os.path.join(root_path, 'models/flagpole.obj'))
roof = Wavefront(os.path.join(root_path, 'models/roof.obj'))
siding = Wavefront(os.path.join(root_path, 'models/siding.obj'))
windows = Wavefront(os.path.join(root_path, 'models/windows.obj'))
door = Wavefront(os.path.join(root_path, 'models/door.obj'))
stump = Wavefront(os.path.join(root_path, 'models/stump.obj'))

rotation = 0.0
lightfv = ctypes.c_float * 4
ticker = 0
ticker1 = 0
cameraOn = True


@window.event
def on_resize(width, height):
    viewport_width, viewport_height = window.get_framebuffer_size()
    glViewport(0, 0, viewport_width, viewport_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45., float(width) / height, 1., 500.)
    glMatrixMode(GL_MODELVIEW)
    return True


@window.event
def on_draw():
    window.clear()
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.196078, 0.6, 0.8, 0.0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightfv(-1.0, 1.0, 1.0, 0.0))

    cameras()
    draw_objs()
    if keys[key._4]:
        treefalls()
    if keys[key._5]:
        flagraise()

    return pyglet.event.EVENT_HANDLED


def cameras():
    global cameraOn
    if keys[key._1]:
        cameraOn = False
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(1, 5.0, 10.0, 1, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif keys[key._2]:
        cameraOn = False
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(1, 30, 10, 1, 0.0, 0.0, 0.0, 1.0, 0.0)
    elif keys[key._3]:
        cameraOn = False
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(20, 30, 10, 1, 0.0, 0.0, 0.0, 1.0, 0.0)
    else:
        cameraOn = True
        camera.draw()


def treefalls():
    global ticker
    if ticker == 0:
        treefalls1 = Wavefront(os.path.join(root_path, 'models/treefalls1.obj'))
        visualization.draw(treefalls1)
    elif ticker < 30:
        treefalls2 = Wavefront(os.path.join(root_path, 'models/treefalls2.obj'))
        visualization.draw(treefalls2)
    elif ticker < 60:
        treefalls3 = Wavefront(os.path.join(root_path, 'models/treefalls3.obj'))
        visualization.draw(treefalls3)
    elif ticker < 90:
        treefalls4 = Wavefront(os.path.join(root_path, 'models/treefalls4.obj'))
        visualization.draw(treefalls4)
    elif ticker < 120:
        treefalls5 = Wavefront(os.path.join(root_path, 'models/treefalls5.obj'))
        visualization.draw(treefalls5)
    elif ticker < 150:
        treefalls6 = Wavefront(os.path.join(root_path, 'models/treefalls6.obj'))
        visualization.draw(treefalls6)
    elif ticker < 180:
        treefalls7 = Wavefront(os.path.join(root_path, 'models/treefalls7.obj'))
        visualization.draw(treefalls7)


def flagraise():
    global ticker1
    if ticker1 == 0:
        flagraise1 = Wavefront(os.path.join(root_path, 'models/flag1.obj'))
        visualization.draw(flagraise1)
    elif ticker1 < 10:
        flagraise2 = Wavefront(os.path.join(root_path, 'models/flag2.obj'))
        visualization.draw(flagraise2)
    elif ticker1 < 20:
        flagraise3 = Wavefront(os.path.join(root_path, 'models/flag3.obj'))
        visualization.draw(flagraise3)
    elif ticker1 < 30:
        flagraise4 = Wavefront(os.path.join(root_path, 'models/flag4.obj'))
        visualization.draw(flagraise4)
    elif ticker1 < 40:
        flagraise5 = Wavefront(os.path.join(root_path, 'models/flag5.obj'))
        visualization.draw(flagraise5)
    elif ticker1 < 50:
        flagraise6 = Wavefront(os.path.join(root_path, 'models/flag6.obj'))
        visualization.draw(flagraise6)
    elif ticker1 < 60:
        flagraise7 = Wavefront(os.path.join(root_path, 'models/flag7.obj'))
        visualization.draw(flagraise7)
    elif ticker1 < 60:
        flagraise8 = Wavefront(os.path.join(root_path, 'models/flag8.obj'))
        visualization.draw(flagraise8)
    elif ticker1 < 80:
        flagraise9 = Wavefront(os.path.join(root_path, 'models/flag9.obj'))
        visualization.draw(flagraise9)
    elif ticker1 < 90:
        flagraise10 = Wavefront(os.path.join(root_path, 'models/flag10.obj'))
        visualization.draw(flagraise10)
    elif ticker1 < 100:
        flagraise11 = Wavefront(os.path.join(root_path, 'models/flag11.obj'))
        visualization.draw(flagraise11)
    elif ticker1 < 120:
        flagraise12 = Wavefront(os.path.join(root_path, 'models/flag12.obj'))
        visualization.draw(flagraise12)
    elif ticker1 < 140:
        flagraise13 = Wavefront(os.path.join(root_path, 'models/flag13.obj'))
        visualization.draw(flagraise13)
    elif ticker1 < 160:
        flagraise14 = Wavefront(os.path.join(root_path, 'models/flag14.obj'))
        visualization.draw(flagraise14)
    elif ticker1 < 180:
        flagraise15 = Wavefront(os.path.join(root_path, 'models/flag15.obj'))
        visualization.draw(flagraise15)
    elif ticker1 < 200:
        flagraise16 = Wavefront(os.path.join(root_path, 'models/flag16.obj'))
        visualization.draw(flagraise16)
    elif ticker1 < 220:
        flagraise17 = Wavefront(os.path.join(root_path, 'models/flag17.obj'))
        visualization.draw(flagraise17)


def draw_objs():
    visualization.draw(chair)
    visualization.draw(table)
    visualization.draw(grass)
    visualization.draw(shroom)
    visualization.draw(mountain)
    visualization.draw(flagpole)
    visualization.draw(tree)
    visualization.draw(roof)
    visualization.draw(windows)
    visualization.draw(siding)
    visualization.draw(door)
    visualization.draw(stump)


def on_update(dt):
    if cameraOn:
        camera.update(dt)
    global rotation
    global ticker
    global ticker1
    ticker += 1
    ticker1 += 1
    if ticker == 210:
        ticker = 0
    if ticker1 == 240:
        ticker1 = 0
    rotation += 45 * dt
    if rotation > 720.0:
        rotation = 0.0


if __name__ == '__main__':
    pyglet.clock.schedule(on_update)
    pyglet.app.run()
