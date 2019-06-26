# Script to transform image to polar coordinate
# Only run from PCs
import argparse
import cv2
import numpy as np
from classes.emulate import *

# Cut image to square
def square_img(img):
	w,h = img.shape[0],img.shape[1]
	new_half = int(max(w,h)/2)
	temp_img = np.zeros((2*new_half,2*new_half,3))
	temp_img[new_half-int(w/2):new_half+int(w/2),new_half-int(h/2):new_half+int(h/2),:] = img[:2*int(w/2),:2*int(h/2)]
	return temp_img

def cart2polar(image_path, output_path):

	# read image from image_path and cut image to square
	source = cv2.imread(image_path)
	img = source.astype(np.float32)
	img = square_img(img)

	# Polarize image
	radius = np.sqrt(((img.shape[0]/2.0)**2.0)+((img.shape[1]/2.0)**2.0))
	polar_image = cv2.linearPolar(img,(img.shape[0]/2, img.shape[1]/2), radius, cv2.WARP_FILL_OUTLIERS)

	# write image
	cv2.imwrite(output_path, polar_image)
	
	return img, polar_image

if __name__ == '__main__':
	from run_emulate import *
	
	# Arguments
	args = argparse.ArgumentParser(description="Image input and output")
	args.add_argument('-i','--input', default='1.jpg', type=str, help='Input image path to transformed')
	args.add_argument('-o','--output', default='transform_1.jpg', type=str, help='Transformed image path to output')
	args = args.parse_args()

	original_img, polar_image = cart2polar('images/'+args.input, 'images/'+args.output)
	print("type of polar_image: ", type(polar_image))
	radius = np.sqrt(((original_img.shape[0]/2.0)**2.0)+((original_img.shape[1]/2.0)**2.0))

	# Transform back to cartisian
	cartisian_image = cv2.linearPolar(polar_image, (original_img.shape[1]/2, original_img.shape[0]/2),radius, cv2.WARP_INVERSE_MAP)

	# Transform datatype as uint8
	polar_image = polar_image.astype(np.uint8)
	cartisian_image = cartisian_image.astype(np.uint8)

	pixels = emulate_equip()
	polar_image = Image.fromarray(polar_image)
	Fan = emulate_fan(1000000,0.0001,width=40,rot_image = polar_image,disp_equip=pixels)
	Runner = emulate_Runner()
	try:
		Runner.Run(Fan)

	except KeyboardInterrupt:
		Runner.End(Fan)
