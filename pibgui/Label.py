import pyglet

class TextLabel():
	def __init__(text_label, name, text, font, fontsize, x, y, xanchor, yanchor):
		text_label.name = name
		text_label.text = text 
		text_label.font = font 
		text_label.fontsize = fontsize
		text_label.x = x
		text_label.y = y 
		text_label.xanchor = xanchor
		text_label.yanchor = yanchor
		text_label.label = pyglet.text.Label(text_label.text, font_name=text_label.font, 
			font_size=text_label.fontsize, x=text_label.x, y=text_label.y, 
			anchor_x=text_label.xanchor, anchor_y=text_label.yanchor)

	def draw_text_label(text_label):
		text_label.label.draw()