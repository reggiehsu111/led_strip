import time

# Running Pattern
def Run(led_strip):
	led_strip.pixels.fill((255, 0, 0))
	led_strip.pixels.show()
	time.sleep(1)

	# Comment this line out if you have RGBW/GRBW NeoPixels
	led_strip.pixels.fill((0, 255, 0))
	led_strip.pixels.show()
	time.sleep(1)

	# Comment this line out if you have RGBW/GRBW NeoPixels
	led_strip.pixels.fill((0, 0, 255))
	led_strip.pixels.show()
	time.sleep(1)
	led_strip.display_led()
	time.sleep(1)

def End(led_strip):
	led_strip.pixels.fill((0,0,0))
	led_strip.pixels.show()
