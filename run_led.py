# Run time script for led mode
import time
from classes.key_detection import key_detector
from classes.infrared_listener import infrared_listener

# Class containing Run and End methods to run in led mode
# Containing an infrared_listener attribute to detect fan pass events
# Containing an key_detector attribute to detect key stroke events
class led_Runner():
	
	def __init__(self,w,t,w_offset):
		self.w = w
		self.t = t
		self.w_offset = w_offset
		self.l_d = infrared_listener(self.w, self.t)
		self.k_d = key_detector(self.w_offset, self.t)

	# Running Pattern
	def Run(self,led_strip):
		self.k_d.start()
		self.l_d.start(led_strip)
		

		while True:
			start = time.time()	
		#	led_strip.pixels.fill((255,255,255))
		#	led_strip.pixels.show()
			led_strip.display_led(self.l_d.w + self.k_d.w_offset ,self.k_d.t)
		#	time.sleep(self.k_d.interval)

			if self.k_d.calibrate:
				led_strip.pixels.fill((0,0,0))
				led_strip.pixels.show()
			past = time.time()-start
		#	print("past: ", past)
			try:
				time.sleep(self.k_d.t-past)
			except ValueError:
				print("ValueError")
				pass

	def End(self,led_strip):
		led_strip.pixels.fill((0,0,0))
		led_strip.pixels.show()
		self.l_d.stop()
		self.k_d.stop()
