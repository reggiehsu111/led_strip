from pynput.keyboard import Key, Listener
# class for detecting key strokes
class  key_detector():

	def __init__(self,w_offset,t):
		self.w_offset = w_offset
		self.t = t
		self.interval = 0.00
		# delta for changing w and t
		self.w_offset_delta = 1
		self.t_delta = 0.001
		self.interval_delta = 0.001
		self.key_listener= Listener(on_press=self.on_press)
		self.calibrate = True

	def on_press(self,key):
		if key == Key.up:
			self.interval += self.interval_delta
			print("\ninterval: ", self.interval)
		elif key == Key.down:
			if self.interval >0:
				self.interval -= self.interval_delta
			print("\ninterval: ", self.interval)
		elif key == Key.right:
			self.w_offset += self.w_offset_delta
			print("\nw_offset: ", self.w_offset )
		elif key == Key.left:
			self.w_offset -= self.w_offset_delta
			print("\nw_offset: ", self.w_offset )
		elif key == Key.shift:
			self.calibrate = not self.calibrate
			print("toggle calibrate")

	def start(self):
		self.key_listener.start()

	def stop(self):
		self.key_listener.stop()
		print("key_listener stopped")
