from pynput.keyboard import Key, Listener

class  key_detector():

	def __init__(self,w,t):
		self.w = w
		self.t = t
		self.w_delta = 0.2
		self.t_delta = 0.001
		self.key_listener= Listener(on_press=self.on_press)

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
		elif key == Key.tab:
			self._store_w = self.w
			print("store w")
		elif key == Key.shift:
			self.w = self._store_w
			print("recall")

	def start(self):
		self.key_listener.start()

	def stop(self):
		self.key_listener.stop()
