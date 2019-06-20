from PIL import Image
import numpy as np
from neopixel import *
import board

# wrapper class for output equipments
class display_equip(neopixel.NeoPixel if mode == 'led' else None):
	def __init__(self, mode='led', num_pixels=60, ORDER = neopixel.GRB, pixel_pin = board.D18, strips=5, strip_leds=12):
		# num_pixels:	The number of NeoPixels
		# pixel_pin :	Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
		# 				NeoPixels must be connected to D10, D12, D18 or D21 to work.
		# ORDER     :	The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green 
		#				reversed! 
		# 				For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
		# 'led' mode:	pixels
		# 'dev' mode:	numpy array
		self.mode = mode
		if self.mode == 'led':
			super().__init__(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
			self.num_pixels = num_pixels
			self.ORDER = ORDER
			self.strips = strips
			self.strip_leds = strip_leds


def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    return img

def wheel(pos):
	# Input a value 0 to 255 to get a color value.
	# The colours are a transition r - g - b - back to r.
	if pos < 0 or pos > 255:
		r = g = b = 0
	elif pos < 85:
		r = int(pos * 3)
		g = int(255 - pos*3)
		b = 0
	elif pos < 170:
		pos -= 85
		r = int(255 - pos*3)
		g = 0
		b = int(pos*3)
	else:
		pos -= 170
		r = 0
		g = int(pos*3)
		b = int(255 - pos*3)
	return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
	for j in range(255):
		for i in range(num_pixels):
			pixel_index = (i * 256 // num_pixels) + j
			pixels[i] = wheel(pixel_index & 255)
		pixels.show()
		time.sleep(wait)