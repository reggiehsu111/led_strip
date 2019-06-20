import numpy as np
from PIL import Image
from utils import *
# class for led fan

class led_fan:
	def __init__(self,rot_image=None,angle=0,disp_equip=None,strips=5,strip_leds=12):
		self.rot_image = rot_image
		self.image_height = self.rot_image.size[0]
		self.image_width = self.rot_image.size[1]
		self.angle = angle
		self.zero_row = 0
		self.strip_dist = self.image_height/(self.strips)

		# display_equip specific params
		self.pixels =disp_equip
		self.strips = self.pixels.strips
		self.strip_leds = self.pixels.strip_leds
		
		


	def resize_width(self):
		self.resize_image = self.rot_image.resize((self.strip_leds,self.image_height),
			resample=Image.LANCZOS)

	# update angle
	def update_angle(self,angle):
		self.angle = angle

	# set the zero row of the led strip
	def set_zero_row(self):
		self.zero_row = int(self.angle*self.image_height/360)
		return self.zero_row

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
		display_pix()


if __name__ == '__main__':
	input_image_path = 'transform_img.jpg'

	img = load_image(input_image_path)
	Fan = led_fan(rot_image = img)
	Fan.resize_width()
	Fan.display_led()
