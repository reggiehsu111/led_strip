# Run time script for led mode
import time
from classes.key_detection import key_detector
from classes.infrared_listener import infrared_listener
import numpy as np

# Class containing Run and End methods to run in led mode
# Containing an infrared_listener attribute to detect fan pass events
# Containing an key_detector attribute to detect key stroke events
class led_Runner():
	
	def __init__(self,w,t,w_offset):
		self.w = w
		self.t = t
		self.w_offset = w_offset
		# Uncomment this for led fan pass detection mode with infrared detector
		self.l_d = infrared_listener(self.w, self.t)

		self.k_d = key_detector(self.w, self.t)

	# Running Pattern
	def Run(self,led_strip):
		self.k_d.start()

		# Uncomment this for led fan pass detection mode with infrared detector
		self.l_d.start(led_strip)
		

		while True:
			start = time.time()	

			# Comment this for led fan pass detection mode with infrared detector
		#	outputpix = led_strip.display_led(self.k_d.w, self.k_d.t)
			
			# Uncomment this for led fan pass detection mode with infrared detector
			self.l_d.t.value = self.k_d.t
			outputpix = self.l_d.outputpix[0]

			led_strip.display_pix(outputpix)
			time.sleep(self.k_d.interval)
			led_strip.pixels.show()

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
		
		# Uncomment for self adjusting mode with key inputs
		self.l_d.stop()
		self.k_d.stop()
