# Led Strip Spinner
Led strip spinner using Raspberry pi and Python3 code. The final project could be installed on a bicycle wheel.

## Getting Started
Download zip file or git clone this repository with the following command
```
git clone https://github.com/reggiehsu111/led_strip.git
```

### Package requirements
The emulation.py and transform_img.py files are intended to run on PCs, it is not required to install opencv on the Raspberry Pi

#### Package requirements for Raspberry Pi
  - rpi_ws281x
  - Adafruit CircuitPython NeoPixel:
  - Pillow
  - board
  - numpy
  
##### Installing for Raspberry Pi
  ```
    pip3 install rpi_ws281x adafruit-circuitpython-neopixel Pillow board numpy
  ```
    
#### Package requirements for PC
  - opencv
  - numpy
  
##### Installing for PC
  ```
  pip3 install opencv-python numpy
  ```
  
## Running the Tests
### Project structure
The following files are specific for 
```
.
    │
    ├── main.py			     # Main program to display patterns, ```dev``` mode for emulation and ```led``` mode for runtime
    ├── simpletest.py                # Simple testing program for led strip
    │
    ├── /classes                     # Classes defined
    │	 ├── __init__.py	     
    │	 ├── Parents.py		     # Base classes ```Parent_fan``` and ```Parent_equip``` defined for inheritance
    │	 ├── emulate.py		     # Class inherited from base class for emulation mode
    │	 └── led.py		     # Class inherited from base class for runtime led mode
    │
    ├── utils.py                     # Helper functions
    └── transform_img.jpg            # Transformed image to be loaded
```

### Class Discriptions
  - The ```led_fan``` class takes a ```led_equip``` type object as an input
  - The ```emulate_fan``` class takes an ```emulate_equip``` type object as an input
  
### Running the code
  - To run in emulation (develop mode), simply run in sudo mode
  ```
  sudo python3 main.py -m dev
  ```
  
  - To run in Rpi runtime mode, simply run in sudo mode
  ```
  sudo python3 main.py -m led
  ```
  Press ```Ctrl-C``` to exit the emulation program
  
  
  - To configure the number of strips and the number of leds per strip, add the options ```-s``` and ```-sl```
  ```
  sudo python3 main.py -m dev -s 5 -sl 12
  ```
## Current issue
  - Current issue in ```led_fan.py```:
    In method display_pix(self,output_pix):
  ```
    # issue: Bottleneck here at iterating over all pixels. The leds on the strip will light up one by one, 
	#   	  but the optimal way is to replace the whole pixels array with output_pix, so the led strip can 
	# 	  light up all at once, but the implementation of Neopixel doesn't allow this to happen.
	# Please refer to https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/master/neopixel.py
	# at __setitem__ method
  ```
