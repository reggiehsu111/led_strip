from pynput.keyboard import Key, Listener
# class for detecting key strokes
class  key_detector():

	def __init__(self,w,t):
		self.w = w
		self.t = t
		self.interval = 0.00
		# delta for changing w and t
		self.w_delta = 1
		self.t_delta = 0.001
		self.interval_delta = 0.001
		self.key_listener= Listener(on_press=self.on_press)
		self.calibrate = True

	def on_press(self,key):
		if key == Key.up:
			self.w += self.w_delta
			print("\nw: ", self.w)
		elif key == Key.down:
			self.w -= self.w_delta
			print("\nw: ", self.w)
		elif key == Key.right:
			self.t += self.t_delta
			print("\nt: ", self.t )
		elif key == Key.left:
			self.t -= self.t_delta
			print("\nt: ", self.t )
		elif key == Key.shift:
			self.calibrate = not self.calibrate
			print("\ntoggle calibrate")
		elif key == Key.tab:
			self.w = 360/self.t
			print("\nset w: ",self.w)
		elif key == Key.page_up:
			self.interval += self.interval_delta
			print("\n interval: ",self.interval)
		elif key == Key.page_down:
			if self.interval > 0:
				self.interval -= self.interval_delta
			print("\n interval: ",self.interval)

	def start(self):
		self.key_listener.start()

	def stop(self):
		self.key_listener.stop()
		print("key_listener stopped")
