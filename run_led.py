import time
from classes.key_detection import key_detector
from classes.infrared_listener import infrared_listener


class led_Runner():
	
	def __init__(self,w,t):
		self.w = w
		self.t = t
		self.l_d = infrared_listener(self.w, self.t)
		self.k_d = key_detector(self.w, self.t)

	# Running Pattern
	def Run(self,led_strip):
		# led_strip.pixels.fill((255, 0, 0))
		# led_strip.pixels.show()
		# time.sleep(1)
		# led_strip.pixels.fill((0, 255, 0))
		# led_strip.pixels.show()
		# time.sleep(1)
		# led_strip.pixels.fill((0, 0, 255))
		# led_strip.pixels.show()
		# time.sleep(1)
		
		self.l_d .start()
		self.k_d.start()

		while True:
			start = time.time()	
		#	led_strip.pixels.fill((255,255,255))
		#	led_strip.pixels.show()
			led_strip.display_led(self.l_d.w,self.k_d.t)

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
