from PIL import Image

class Parent_fan():
	def __init__(self,rot_image=None,angle=0,disp_equip=None,strips=5,strip_leds=12):
	
		# display_equip specific params
		self.pixels = disp_equip
		self.strips = self.pixels.strips
		self.strip_leds = self.pixels.strip_leds
		self.rot_image = rot_image
		self.image_height = self.rot_image.size[0]
		self.image_width = self.rot_image.size[1]
		self.angle = angle
		self.zero_row = 0
		self.strip_dist = self.image_height/(self.strips)


	def resize_width(self):
		self.resize_image = self.rot_image.resize((self.strip_leds,self.image_height),
			resample=Image.LANCZOS)

	# update angle
	def update_angle(self,angle):
		self.angle = angle

	# set the zeroth row of the led strip
	def set_zero_row(self):
		self.zero_row = int(self.angle*self.image_height/360)
		return self.zero_row


# wrapper class for output equipments
class Parent_equip():
	# mode, num_pixels, ORDER, pixel_pin are imported from config.py
	def __init__(self, strips=5, strip_leds=12):
		# num_pixels:	The number of NeoPixels
		# strips    :	Number of strips
		# strip_leds:	Number of leds in a strip
		self.strips = strips
		self.strip_leds = strip_leds
		self.num_pixels = self.strips * self.strip_leds



	
