# Led Strip Spinner
Led strip spinner using Raspberry pi and Python3 code. The final project could be installed on a bicycle wheel.

## Getting Started
Download zip file or git clone this repository with the following command
```
git clone https://github.com/reggiehsu111/led_strip.git
```

### Hardware requirements
  - raspberry pi 3
  - ws281x led strips
  #### Step 1
   Concatenate the led strips' digital inputs and stablize the strips into a fan shape. 
  #### Step 2
   Place it on a motor or a wheel, and place an infrared emitter on one of the fan blades. 
  #### Step 3
   Place an infrared sensor near the fan, so that the sensor can detect the emitter.

### Package requirements
The ```dev``` mode is intended to run on PCs, which requires ```opencv``` preinstalled. 
The ```led``` mode is intended to run on Raspberry Pis, which requires ```board``` and ```Adafruit CircuitPython NeoPixel``` preinstalled. It is not required to install opencv on the Raspberry Pi.

#### Package requirements for Raspberry Pi
  - rpi_ws281x
  - Adafruit CircuitPython NeoPixel
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
    ├── main.py                      # Main program to display patterns, ```dev``` mode for emulation and ```led``` mode for runtime
    ├── run_emulate.py               # Containing class emulate_RUnner, run time script for dev mode
    ├── run_led.py                   # Containing class led_RUnner, run time script for led mode
    ├── transform.py                 # Transform images and run emulation
    ├── utils.py                     # Helper functions
    │
    ├── /classes                     # Classes defined
    │  ├── __init__.py         
    │  ├── key_detection.py          # Class key_detector for detecting key strokes
    │  ├── infrared_listener.py      # Class infrared_listener for detecting fan pass using infrared sensor
    │  ├── Parents.py                # Base classes ```Parent_fan``` and ```Parent_equip``` defined for inheritance
    │  ├── emulate.py                # Class inherited from base class for emulation mode
    │  └── led.py                    # Class inherited from base class for runtime led mode
    │
    ├── /images                      # Folder containing images
    │
    ├── README.md
    └── .gitignore
```

### Class Discriptions
  - The ```Parent_fan``` and ```Parent_equip``` classes are the base classes for led and emulation mode
  - The ```led_fan``` class takes a ```led_equip``` type object as an input
  - The ```emulate_fan``` class takes an ```emulate_equip``` type object as an input
  - The ```key_detector``` class is a thread detects key strokes while running in led mode
  - The ```infrared_listener``` class spawns 2 processes to listen for a led fan passing through
  
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

  - To specify the image to output, add the options ```-i```
  ```
  sudo python3 main.py -m led -i image.jpg
  ``` 

  - To specify the angular velocity, the refresh time, and the offset for angular velocity, add the options ```-w```, ```-t```, and ```-wo``` respectively
  ```
  sudo python3 main.py -m led -w 1000 -t 0.05 -wo 10
  ```


## Current Issues
  - Image transformation can only be run on PC. Need a Raspberry Pi version of the ```cv2.linearPolar``` function using only ```PIL``` and ```numpy``` packages


