from PIL import Image
from utils import load_image
import numpy as np
import csv

input_image_path = 'transform_img.jpg' 
image = load_image(input_image_path)
image = np.array(image)
image = image.flatten()

print("image dtype:", image.dtype)

with open('output.csv','a') as f:
	writer = csv.writer(f)
	writer.writerow(image)

with open('output.csv','r') as f:
	imagereader = csv.reader(f)
	for row in imagereader:
		data = np.array(row)
data = data.reshape(800,800)
data = data.view(np.uint8)
print(data[0])
print("data type: ", type(data))
print("data shape: ", data.shape)
print("data dtype: ", data.dtype)

reloaded_img = Image.fromarray(data)
reloaded_img.show()


