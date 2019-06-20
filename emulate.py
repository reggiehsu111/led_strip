import cv2
import numpy as np
import time
from led_fan import led_fan


# def display_rot_img(image):
# 	while(1):
class fan(led_fan):
	def __init__(self,w,t,width=5,rot_image=None, angle=0, strips=5):
		super().__init__(rot_image,angle,strips)
		self.t = t
		self.w = w
		self.rotate(w,t,width)

	# method for self rotation give angular velocity w
	def rotate(self,w,t,width):
		while(True):
			time.sleep(t)
			self.update_angle((self.angle+w*t)%360)
			self.display(width)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				breakq
		cv2.destroyAllWindows()

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
		cartesian_img = cv2.linearPolar(temp_img, (self.rot_image.shape[1]/2, self.rot_image.shape[0]/2),value, cv2.WARP_INVERSE_MAP).astype(np.uint8)
		cv2.imshow("cart_image",cartesian_img)
		# index to display


source = cv2.imread('./snoopy.jpeg')
img = source.astype(np.float32)
def transform_img(img):
	w,h = img.shape[0],img.shape[1]
	new_half = int(max(w,h)/2)
	temp_img = np.zeros((2*new_half,2*new_half,3))
	temp_img[new_half-int(w/2):new_half+int(w/2),new_half-int(h/2):new_half+int(h/2),:] = img
	return temp_img
img = transform_img(img)

# value 
value = np.sqrt(((img.shape[0]/2.0)**2.0)+((img.shape[1]/2.0)**2.0))
# value1 = img.shape[0]/2
polar_image = cv2.linearPolar(img,(img.shape[0]/2, img.shape[1]/2), value, cv2.WARP_FILL_OUTLIERS)
# print("polar shape: ", polar_image.shape)
cv2.imwrite("transform_img.jpg",polar_image)
cartisian_image = cv2.linearPolar(polar_image, (img.shape[1]/2, img.shape[0]/2),value, cv2.WARP_INVERSE_MAP)

polar_image = polar_image.astype(np.uint8)
cartisian_image = cartisian_image.astype(np.uint8)
# print("shape of polar image: ",polar_image.shape)
# cv2.imshow("Polar Image", polar_image)
# cv2.imshow("Cartisian Image", cartisian_image)
Fan = fan(1000000,0.0001,width=40,rot_image = polar_image)

cv2.waitKey(0)
cv2.destroyAllWindows()