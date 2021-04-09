import collections
import math
import pyglet


class FirstPersonCamera(object):
    DEFAULT_MOVEMENT_SPEED = 10.0

    DEFAULT_MOUSE_SENSITIVITY = 0.25

    DEFAULT_KEY_MAP = {
        'forward': pyglet.window.key.W,
        'backward': pyglet.window.key.S,
        'left': pyglet.window.key.A,
        'right': pyglet.window.key.D,
        'up': pyglet.window.key.SPACE,
        'down': pyglet.window.key.LSHIFT
    }

    class InputHandler(object):
        def __init__(self):
            self.pressed = collections.defaultdict(bool)
            self.dx = 0
            self.dy = 0

        def on_key_press(self, symbol, modifiers):
            self.pressed[symbol] = True

        def on_key_release(self, symbol, modifiers):
            self.pressed[symbol] = False

        def on_mouse_motion(self, x, y, dx, dy):
            self.dx = dx
            self.dy = dy

    def __init__(self, window, position=(0, 0, 0), key_map=DEFAULT_KEY_MAP, movement_speed=DEFAULT_MOVEMENT_SPEED, mouse_sensitivity=DEFAULT_MOUSE_SENSITIVITY, y_inv=True):
        self.__position = list(position)
        self.__yaw = 0.0
        self.__pitch = 0.0
        self.__input_handler = FirstPersonCamera.InputHandler()

        window.push_handlers(self.__input_handler)

        self.y_inv = y_inv
        self.key_map = key_map
        self.movement_speed = movement_speed
        self.mouse_sensitivity = mouse_sensitivity

    def yaw(self, yaw):
        self.__yaw += yaw * self.mouse_sensitivity

    def pitch(self, pitch):
        self.__pitch += pitch * self.mouse_sensitivity * ((-1) if self.y_inv else 1)

    def move_forward(self, distance):
        self.__position[0] -= distance * math.sin(math.radians(self.__yaw))
        self.__position[2] += distance * math.cos(math.radians(self.__yaw))

    def move_backward(self, distance):
        self.__position[0] += distance * math.sin(math.radians(self.__yaw))
        self.__position[2] -= distance * math.cos(math.radians(self.__yaw))

    def move_left(self, distance):
        self.__position[0] -= distance * math.sin(math.radians(self.__yaw - 90))
        self.__position[2] += distance * math.cos(math.radians(self.__yaw - 90))

    def move_right(self, distance):
        self.__position[0] -= distance * math.sin(math.radians(self.__yaw + 90))
        self.__position[2] += distance * math.cos(math.radians(self.__yaw + 90))

    def move_up(self, distance):
        self.__position[1] -= distance

    def move_down(self, distance):
        self.__position[1] += distance

    def update(self, delta_time):
        self.yaw(self.__input_handler.dx)
        self.__input_handler.dx = 0

        self.pitch(self.__input_handler.dy)
        self.__input_handler.dy = 0

        if self.__input_handler.pressed[self.key_map['forward']]:
            self.move_forward(delta_time * self.movement_speed)

        if self.__input_handler.pressed[self.key_map['backward']]:
            self.move_backward(delta_time * self.movement_speed)

        if self.__input_handler.pressed[self.key_map['left']]:
            self.move_left(delta_time * self.movement_speed)

        if self.__input_handler.pressed[self.key_map['right']]:
            self.move_right(delta_time * self.movement_speed)

        if self.__input_handler.pressed[self.key_map['up']]:
            self.move_up(delta_time * self.movement_speed)

        if self.__input_handler.pressed[self.key_map['down']]:
            self.move_down(delta_time * self.movement_speed)

    def draw(self):
        pyglet.gl.glRotatef(self.__pitch, 1.0, 0.0, 0.0)
        pyglet.gl.glRotatef(self.__yaw, 0.0, 1.0, 0.0)
        pyglet.gl.glTranslatef(*self.__position)