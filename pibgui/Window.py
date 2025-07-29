import pyglet
from pibgui.Image import *
from pibgui.Label import *
from pibgui.Keyboard import *

class Window():
	def __init__(window, name):
		window.name = name
		window.window = pyglet.window.Window()
		window.labellist = []
		window.imagelist = []
		window.keyboard = Keyboard()

		# Draw handler
		@window.window.event
		def on_draw():
			window.window.clear()
			for label in window.labellist:
				label.draw_text_label()
			for image in window.imagelist:
				image.draw_image()

		# Keyboard handlers
		@window.window.event
		def on_key_press(symbol, modifiers):
			window.keyboard.on_key_press(symbol, modifiers)

		@window.window.event
		def on_key_release(symbol, modifiers):
			window.keyboard.on_key_release(symbol, modifiers)

	def __str__(window):
		return window.name

	def add_to_render(window, *items):
		for item in items:
			if isinstance(item, TextLabel):
				window.labellist.append(item)
			elif isinstance(item, Image):
				window.imagelist.append(item)
			else:
				print(f"Error: Unknown item type")
