from  multiprocessing import Process, Event
import time
import RPi.GPIO as GPIO
import time

class infrared_listener():
	def __init__(self,w,t):
		''' parameters '''
		self.w = w
		self.t = t
		self.window_len = 5.0
		self.PIN_list   = [ 17 ]
		self.PIN_window = [ 0 ] * len( self.PIN_list ) 
		self.threshold  = 0.7
		self.p1 = Process(name="fan_pass_listener", target=self.update_outputpix)
		self.p2 = Process(name="fan_pass_reader", target = self.main_process)
		# variable to store led_strip object after process starts
		self.led_strip = None
	
	# call when a fan pass event is raised		
	def update_outputpix(self):
		
		print("waiting for event")
		try:
			while True:
				self.led_strip.display_led(self.w,self.t)
		except KeyboardInterrupt:
			return

	def main_process(self):
		
		GPIO.setmode(GPIO.BCM)
		for index in range(len(self.PIN_list)):
			GPIO.setup(self.PIN_list[index], GPIO.IN)

		start = -1
		end   = -1
		try:
			while True:
				for PIN_idx in range( len( self.PIN_list ) ):
					if GPIO.input( self.PIN_list[ PIN_idx ] ) ^ 1:
						#print(1)
						if start == -1 and end == -1:
							start = time.time()
						elif start != -1:
							end = time.time()
							print( "w: ", 360 / ( end - start ) )
							self.w = 360 / (end-start)
							start = end
						time.sleep(0.02)
					else:
						pass
		except KeyboardInterrupt:
			return

	
	def start(self,led_strip):
		self.led_strip = led_strip
		self.p1.start()
		self.p2.start()
		print("Infrared listener start")
	
	def stop(self):
		self.p1.join()
		self.p2.join()
		print("Infrared listener stopped")

if __name__ == '__main__':
	il = infrared_listener(w = 3, t = 2)
	il.start_process()
