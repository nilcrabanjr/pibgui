from pibgui.Window import *
from pibgui.App import *
from pibgui.Label import *
from pibgui.Image import *

test = window("TestWindow")
test_label = text_label("test_label", "pibbles!!!", "Arial", 18, 100, 100, "center", "center")
test_label2 = text_label("test_label2", "are so cool", "Arial", 24, 200, 200, "center", "center")
test_image = image("test_image", "gleeble.jpg", 300, 300)
test.add_to_render(test_label, test_label2, test_image)

test.draw_window()
start_app()
