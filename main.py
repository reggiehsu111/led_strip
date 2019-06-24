# file to display rotated image on led strips
import argparse
import time
from PIL import Image
from utils import *


input_image_path = 'transform_img.jpg' 
image = load_image(input_image_path)



if __name__ == '__main__':
	# Arguments for 
	args = argparse.ArgumentParser(description='Display Equipment')
	args.add_argument('-m', '--mode', default='dev', type=str,
					  help='Runtime Mode ( \'dev\' for emulation and \'led\' for led strip)')
	args.add_argument('-s','--strips', default=5, type=int,
					  help='Number of strips')
	args.add_argument('-sl','--strip_leds', default=12, type=int,
					  help='Number of leds on a strip')
	args = args.parse_args()

	# initialize equipment for dev mode
	if args.mode == 'dev':
		from classes.emulate import *
		pixels = emulate_equip(strips=args.strips,strip_leds=args.strip_leds)
		led_strips = emulate_fan(1000000,0.0001,width=40,rot_image = image,disp_equip=pixels)

	# initialize equipment for led mode
	if args.mode == 'led':
		from classes.led import *
		pixels = led_equip(strips=args.strips,strip_leds=args.strip_leds)
		led_strips = led_fan(rot_image=image, disp_equip=pixels)

	# Run Pattern
	try:
		print("Press Ctrl-C to leave.")
		while True:
			led_strips.Run()

	except KeyboardInterrupt:
		led_strips.End()
