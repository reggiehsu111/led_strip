from PIL import Image
import numpy as np
import json
from collections import OrderedDict


def read_json(fname):
	with fname.open('rt') as handle:
		return json.load(handle, object_hook=OrderedDict)

def write_json(content, fname):
	with fname.open('wt') as handle:
		json.dump(content, handle, indent=4, sort_keys=False)

def load_image(infilename) :
	img = Image.open( infilename )
	img.load()
	return img


