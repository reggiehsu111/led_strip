# Run time script for emulate mode
import time
import cv2

class emulate_Runner():

	def __init__(self):
		pass
	def Run(self,led_strip):
		while(led_strip.end_flag):
			w = led_strip.w
			t = led_strip.t
			width = led_strip.width
			time.sleep(t)
			led_strip.update_angle((led_strip.angle+w*t)%360)
			led_strip.display(width)
			cv2.waitKey(1)
		cv2.waitKey(0)
		cv2.destroyAllWindows()


	def End(self,led_strip):
		led_strip.end_flag = False
