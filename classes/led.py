import numpy as np
from PIL import Image
from Parents import *
import time
import board
import neopixel
from classes.Parents import *


# class for led fan, inherit from Parent_fan
class led_fan(Parent_fan):

	def __init__(self,rot_image=None,angle=0,disp_equip=None,strips=5,strip_leds=12):
		super().__init__(rot_image=rot_image,angle=angle,disp_equip=disp_equip,strips=strips,strip_leds=strip_leds)

	# main function to display the rotated image to the led strips
	def display_led(self):
		# discretize angle
		self.set_zero_row()
		# index on rot_image where the strip should display
		strip_index = np.array([int(x*self.strip_dist+self.zero_row) for x in range(self.strips)])
		strip_index = strip_index%self.image_height

		# print("strip_index: ",strip_index)

		# select the rows to be displayed and reshape it to (60,3) 2d array
		selected_rows = np.array(self.resize_image)[strip_index]
		output_pix = selected_rows.reshape((selected_rows.shape[0]*selected_rows.shape[1],3))
		self.display_pix(output_pix)

	# display pixels given pixel array
	# issue: Bottleneck here at iterating over all pixels. The leds on the strip will light up one by one, 
	# 		 but the optimal way is to replace the whole pixels array with output_pix, so the led strip can 
	# 		 light up all at once, but the implementation of Neopixel doesn't allow this to happen.
	# Please refer to https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/master/neopixel.py
	# at __setitem__ method
	def display_pix(self,output_pix):
		for x in range(output_pix.shape[0]):
			self.pixels[x] = output_pix[x]
			self.pixels.show()

	# Running Pattern
	def Run(self):
		self.pixels.fill((255, 0, 0))
		# Uncomment this line if you have RGBW/GRBW NeoPixels
		# pixels.fill((255, 0, 0, 0))
		self.pixels.show()
		time.sleep(1)

		# Comment this line out if you have RGBW/GRBW NeoPixels
		self.pixels.fill((0, 255, 0))
		# Uncomment this line if you have RGBW/GRBW NeoPixels
		# pixels.fill((0, 255, 0, 0))
		self.pixels.show()
		time.sleep(1)

		# Comment this line out if you have RGBW/GRBW NeoPixels
		self.pixels.fill((0, 0, 255))
		# Uncomment this line if you have RGBW/GRBW NeoPixels
		# pixels.fill((0, 0, 255, 0))
		self.pixels.show()
		time.sleep(1)
		self.display_led()
		
	# Closing the Run
	def End(self):
		self.pixels.fill((0,0,0))
		self.pixels.show()

# led mode, inherit from Parent_equip and neopixel
class led_equip(Parent_equip,neopixel.NeoPixel):
	def __init__(self,pixel_pin=board.D18, ORDER=neopixel.GRB,strips=5, strip_leds=12):
		# pixel_pin :	Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
		# 				NeoPixels must be connected to D10, D12, D18 or D21 to work.
		# ORDER     :	The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green 
		#				reversed! 
		# 				For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
	
		display_equip.__init__(strips=strips, strip_leds=strip_leds)
		neopixel.NeoPixel.__init__(pixel_pin, self.num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
