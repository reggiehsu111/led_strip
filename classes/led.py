import numpy as np
from PIL import Image
import time
import board
import neopixel
from classes.Parents import *


# class for led fan, inherit from Parent_fan
class led_fan(Parent_fan):

	def __init__(self,rot_image=None,angle=0,disp_equip=None,strips=5,strip_leds=12):
		super().__init__(rot_image=rot_image,angle=angle,disp_equip=disp_equip,strips=strips,strip_leds=strip_leds)
		self.rot_image = self.rot_image.resize((2*self.strip_leds,2*self.strip_leds),resample=Image.LANCZOS)
		self.resize_image = self.rot_image.resize((self.strip_leds,self.image_height), resample=Image.LANCZOS)
		self.resize_image = np.array(self.resize_image)

	# main function to display the rotated image to the led strips
	def display_led(self,w,t):
		self.w = w
		self.t = t
		self.update_angle((self.angle+self.w*self.t)%360)
		# discretize angle
		self.set_zero_row()
		# index on rot_image where the strip should display
		strip_index = np.array([int(x*self.strip_dist+self.zero_row) for x in range(self.strips)])
		strip_index = strip_index%self.image_height

		# print("strip_index: ",strip_index)

		# select the rows to be displayed and reshape it to (60,3) 2d array
		selected_rows = self.resize_image[strip_index]
		output_pix = selected_rows.reshape((selected_rows.shape[0]*selected_rows.shape[1],3))
		self.display_pix(output_pix)


	# display pixels given pixel array
	def display_pix(self,output_pix):
		for x in range(output_pix.shape[0]):
			self.pixels[x] = output_pix[x]
		self.pixels.show()


# led mode, inherit from Parent_equip and neopixel
class led_equip(Parent_equip,neopixel.NeoPixel):
	def __init__(self,pixel_pin=board.D18, ORDER=neopixel.GRB,strips=5, strip_leds=12):
		# pixel_pin :	Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
		# 				NeoPixels must be connected to D10, D12, D18 or D21 to work.
		# ORDER     :	The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green 
		#				reversed! 
		# 				For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
		num_pixels = strips*strip_leds
		Parent_equip.__init__(self, strips=strips, strip_leds=strip_leds)
		neopixel.NeoPixel.__init__(self, pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
