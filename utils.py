# utility functions
from PIL import Image
import numpy as np

def load_image(infilename) :
	img = Image.open( infilename )
	img.load()
	return img

