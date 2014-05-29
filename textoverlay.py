import sys, math
from wand.image import Image
from wand.display import display
from wand.drawing import Drawing
from wand.color import Color
from wand.font import Font

if len(sys.argv) > 3:
	with Drawing() as draw:
		try:
			with Image(filename=sys.argv[1]) as image:
					draw.font = 'LibreBaskerville-Bold.ttf'
					draw.stroke_color = Color('#fff')
					draw.stroke_width = 2
					draw.text_alignment = 'center'
					draw.text_antialias = 'True'

					draw.font_size = (image.width / len(sys.argv[2])) / 0.8
					draw.text(image.width / 2, int(math.floor(image.height / 6)), sys.argv[2].upper())		# don't ask me about these values, they were just trial and error and this is what seemed to work out the best.
					draw.font_size = (image.width / len(sys.argv[3])) / 0.8
					draw.text(image.width / 2, int(math.floor(image.height / 1.1)), sys.argv[3].upper())
					draw(image)
					image.save(filename="output.png")
		except IOError:
			print "Invalid file! Usage: \'textoverlay.py filename \"top text\" \"bottom text\"\'"
else:
	print "Not enough arguments! Usage: \'textoverlay.py filename \"top text\" \"bottom text\"\'"
