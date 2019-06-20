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
    │                                # The following files are specific for rpi usage
    │
    ├── config.py                    # File to store global configurations
    ├── display.py                   # Main program to display the led patterns onto the leds strips
    ├── simpletest.py                # Simple testing program for led strip 
    │
    │                                # The following files are specific for emulating on PCs
    │
    ├── emulate.py                   # For emulating on PC, requires opencv
    │
    ├── utils.py                     # Helper functions including the display_equip class
    ├── led_fan.py                   # Class definition for led fan class
    └── transform_img.jpg            # Transformed image to be loaded
```

### Class Discriptions
  - The ```led_fan``` class takes a ```display_equip``` type object as an input
  - The ```emulate_fan``` class inherits from the ```led_fan``` class, with ```display_equip``` inheriting from an empty class
  
### Running the code
  - To run in emulation, set the ```global mode``` in ```config.py``` to ```mode = 'dev'```, then simply run
  ```
  python3 emulate.py
  ```
  Press ```q``` to exit the emulation program
  
  - To run in Rpi mode, set the ```global mode``` in ```config.py``` to ```mode = 'led'```, then simply run
  ```
  python3 display.py
  ```
  Press ```Ctrl-C``` to exit the emulation program
  
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
