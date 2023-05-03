import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio

# GPIO pin configuration
pins = [
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,

    board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17,
    board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26,

    board.GP27, board.GP28
]

# Create DigitalInOut objets for each GPIO pins
pin_objs = []
for pin in pins:
    pin_obj = digitalio.DigitalInOut(pin)
    pin_obj.direction = digitalio.Direction.INPUT
    pin_obj.pull = digitalio.Pull.UP
    pin_objs.append(pin_obj)

# Initialise pins state memory
pins_state = [False] * len(pins)

# Create a Keyboard objet for sending commands to computer
keyboard = Keyboard(usb_hid.devices)

print("Ready !!! Wating for key press...")

while True:
    for i in range(len(pins)):
        # Invert for pull-up resistor
        current_state = not pin_objs[i].value
        if current_state != pins_state[i]:  # The pin changed state
            pins_state[i] = current_state  # Keep in memory the new pin state
            if current_state:  # The pin is currently enabled (switch pushed)
                if pins[i] == board.GP0:
                    print("Press F13")
                    keyboard.press(Keycode.F13)
                elif pins[i] == board.GP1:
                    print("Press F14")
                    keyboard.press(Keycode.F14)
                # Add other keys here
            else:  # The pin is currently disabled (switch released)
                if pins[i] == board.GP0:
                    print("Release F13")
                    keyboard.release(Keycode.F13)
                elif pins[i] == board.GP1:
                    print("Release F14")
                    keyboard.release(Keycode.F14)
                # Add other keys here
            #  if end
        #  if end
    #  for end
    time.sleep(0.01)  # Ajust polling rate
#  while end