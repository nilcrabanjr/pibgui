from pibgui.Window import *
from pibgui.App import *
from pibgui.Label import *
from pibgui.Image import *
from pibgui.Keyboard import *
import pyglet

test = Window("TestWindow")

test_label = TextLabel("test_label", "pibbles!!!", "Arial", 18, 100, 100, "center", "center")
test_label2 = TextLabel("test_label2", "are so cool", "Arial", 24, 200, 200, "center", "center")
test_image = Image("test_image", "gleeble.jpg", 300, 300)
test.add_to_render(test_label, test_label2, test_image)

def check_input(dt):
	if test.keyboard.is_pressed("A"):
		print("'A' key pressed")

pyglet.clock.schedule_interval(check_input, 1 / 12.0)

start_app()
