import pyglet
from pyglet.window import key

class Keyboard:
    def __init__(keyboard):
        keyboard.keys_down = set()
        keyboard.keymap = {chr(i): getattr(key, chr(i)) for i in range(65, 91)}  # A-Z

    def on_key_press(keyboard, symbol, modifiers):
        for char, code in keyboard.keymap.items():
            if symbol == code:
                keyboard.keys_down.add(char)

    def on_key_release(keyboard, symbol, modifiers):
        for char, code in keyboard.keymap.items():
            if symbol == code and char in keyboard.keys_down:
                keyboard.keys_down.remove(char)

    def is_pressed(keyboard, char):
        return char.upper() in keyboard.keys_down

