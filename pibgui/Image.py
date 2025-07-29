import pyglet

class image():
	def __init__(image, name, source, x, y):
		image.name = name
		image.source = source
		image.image = pyglet.resource.image(image.source)
		image.x = x 
		image.y = y 

	def draw_image(image):
		image.image.blit(image.x, image.y)