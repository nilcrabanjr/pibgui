import pyglet
from pibgui.Image import *
from pibgui.Label import *

class window():
	def __init__(window, name):
		window.name = name
		window.window = pyglet.window.Window()
		window.labellist = []
		window.imagelist = []

	def __str__(window):
		return

	def add_to_render(window, *items):
		for item in items:
			if isinstance(item, text_label):
				window.labellist.append(item)
			elif isinstance(item, image):
				window.imagelist.append(item)
			else:
				print(f"Warning: Unknown item type '{type(item)}' not added.")

	def draw_window(window):
		@window.window.event
		def on_draw():
			window.window.clear()
			for label in window.labellist:
				label.draw_text_label()
			for image in window.imagelist:
				image.draw_image()

