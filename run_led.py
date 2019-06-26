import time
from classes.key_detection import key_detector

# Running Pattern
def Run(led_strip):
	# led_strip.pixels.fill((255, 0, 0))
	# led_strip.pixels.show()
	# time.sleep(1)
	# led_strip.pixels.fill((0, 255, 0))
	# led_strip.pixels.show()
	# time.sleep(1)
	# led_strip.pixels.fill((0, 0, 255))
	# led_strip.pixels.show()
	# time.sleep(1)
	w = 1074
	t = 0.398
	k_d = key_detector(w,t)
	k_d.start()

	while True:
		start = time.time()	
	#	led_strip.pixels.fill((255,255,255))
	#	led_strip.pixels.show()
		led_strip.display_led(k_d.w,k_d.t)
		if k_d.calibrate:
			led_strip.pixels.fill((0,0,0))
			led_strip.pixels.show()
		past = time.time()-start
	#	print("past: ", past)
		try:
			time.sleep(k_d.t-past)
		except ValueError:
			print("ValueError")
			pass

def End(led_strip):
	led_strip.pixels.fill((0,0,0))
	led_strip.pixels.show()
