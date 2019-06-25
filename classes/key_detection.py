from pynput.keyboard import Key, Listener

class  key_detector():

	def __init__(self,w,t):
		self.w = w
		self.t = t
		self.key_listener= Listener(on_press=self.on_press)

	def on_press(self,key):
		if key == Key.up:
			self.w += 5
			print("\nself.w: ", self.w)
		elif key == Key.down:
			self.w -= 5
			print("\nself.w: ", self.w)

	def start(self):
		self.key_listener.start()

	def stop(self):
		self.key_listener.stop()
