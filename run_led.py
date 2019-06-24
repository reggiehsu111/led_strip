import time
import keyboard

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
	w = 100
	t= 0.01
	led_strip.display_led(w,t)
	time.sleep(t)

def End(led_strip):
	led_strip.pixels.fill((0,0,0))
	led_strip.pixels.show()
