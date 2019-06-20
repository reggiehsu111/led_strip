# file to display rotated image on led strips
from neopixel import *# Simple test for NeoPixels on Raspberry Pi
import time
from PIL import Image
from led_fan import led_fan
from utils import *
from config import *

input_image_path = 'transform_img.jpg' 

pixels = display_equip(mode = mode)


if __name__ == '__main__':
	image = load_image(input_image_path)
	led_strips = led_fan(rot_image=image, disp_equip=pixels)
	try:
		while True:
			# Comment this line out if you have RGBW/GRBW NeoPixels
			led_strips.pixels.fill((255, 0, 0))
			# Uncomment this line if you have RGBW/GRBW NeoPixels
			# pixels.fill((255, 0, 0, 0))
			led_strips.pixels.show()
			time.sleep(1)

			# Comment this line out if you have RGBW/GRBW NeoPixels
			led_strips.pixels.fill((0, 255, 0))
			# Uncomment this line if you have RGBW/GRBW NeoPixels
			# pixels.fill((0, 255, 0, 0))
			led_strips.pixels.show()
			time.sleep(1)

			# Comment this line out if you have RGBW/GRBW NeoPixels
			led_strips.pixels.fill((0, 0, 255))
			# Uncomment this line if you have RGBW/GRBW NeoPixels
			# pixels.fill((0, 0, 255, 0))
			led_strips.pixels.show()
			time.sleep(1)
			led_strips.resize_width()
			led_strips.display_led()
			time.sleep(1)
                        

	except KeyboardInterrupt:
		led_strips.pixels.fill((0,0,0))
		led_strips.pixels.show()
