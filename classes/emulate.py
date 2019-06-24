import cv2
import numpy as np
import time
from classes.Parents import *
from PIL import Image

# Fan class for emulation, inherit from Parent_fan
class emulate_fan(Parent_fan):
	def __init__(self,w,t,width=5,rot_image=None, angle=0, disp_equip=None, strips=5):
		super().__init__(rot_image,angle,disp_equip=disp_equip,strips=strips)
		self.rot_image = np.array(rot_image)
		self.t = t
		self.w = w
		self.width = width
		self.end_flag = True
		self.radius = np.sqrt(((self.rot_image.shape[0]/2.0)**2.0)+((self.rot_image.shape[1]/2.0)**2.0))

	def display(self,width):
		# discretize angle
		self.set_zero_row()
		# index on rot_image where the strip should display
		strip_index = [int(x*self.strip_dist+self.zero_row) for x in range(self.strips)]
		strip_index = [list(range(x,x+width)) for x in strip_index]
		flatten = []
		for sublist in strip_index:
			for item in sublist:
				flatten.append(item%self.image_height)
		# print("strip_index: ",strip_index)
		temp_img = np.zeros(self.rot_image.shape)
		temp_img[flatten] = self.rot_image[flatten]
		# print(temp_img.shape)
		cartesian_img = cv2.linearPolar(temp_img, (self.rot_image.shape[1]/2, self.rot_image.shape[0]/2),self.radius, cv2.WARP_INVERSE_MAP).astype(np.uint8)
		cv2.imshow("cart_image",cartesian_img)
		# index to display


# class for emulate mode, inherit from Parent_equip
class emulate_equip(Parent_equip):
	def __init__(self, strips = 5, strip_leds = 12):
		super().__init__(strips = strips, strip_leds = strip_leds)
		return


def transform_img(img):
	w,h = img.shape[0],img.shape[1]
	new_half = int(max(w,h)/2)
	temp_img = np.zeros((2*new_half,2*new_half,3))
	temp_img[new_half-int(w/2):new_half+int(w/2),new_half-int(h/2):new_half+int(h/2),:] = img
	return temp_img


if __name__ == '__main__':
	# load original image
	source = cv2.imread('snoopy.jpeg')
	img = source.astype(np.float32)
	img = transform_img(img)


	# Polarize image
	value = np.sqrt(((img.shape[0]/2.0)**2.0)+((img.shape[1]/2.0)**2.0))
	polar_image = cv2.linearPolar(img,(img.shape[0]/2, img.shape[1]/2), value, cv2.WARP_FILL_OUTLIERS)

	# Save transformed image
	cv2.imwrite("transform_img.jpg",polar_image)

	# Transform back to cartisian
	cartisian_image = cv2.linearPolar(polar_image, (img.shape[1]/2, img.shape[0]/2),value, cv2.WARP_INVERSE_MAP)

	# Transform datatype as uint8
	polar_image = polar_image.astype(np.uint8)
	cartisian_image = cartisian_image.astype(np.uint8)

	pixels = emulate_equip()
	polar_image = Image.fromarray(polar_image)
	Fan = emulate_fan(1000000,0.0001,width=40,rot_image = polar_image,disp_equip=pixels)

	try:
		Fan.Run()

	except KeyboardInterrupt:
		Fan.End()
