global mode
mode = 'dev'

global num_pixels
num_pixels = 60

global ORDER
if mode == 'led':
	import neopixel
	ORDER = neopixel.GRB
else:
	ORDER = None

global pixel_pin
if mode == 'led':
	import board
	pixel_pin = board.D18
else:
	pixel_pin = None
