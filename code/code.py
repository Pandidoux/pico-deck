import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio

# Init onboard LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

# Init switchs Ctrl
pin_sw1 = digitalio.DigitalInOut(board.GP28)
pin_sw1.direction = digitalio.Direction.INPUT
pin_sw1.pull = digitalio.Pull.UP
# Init switchs Shift
pin_sw2 = digitalio.DigitalInOut(board.GP27)
pin_sw2.direction = digitalio.Direction.INPUT
pin_sw2.pull = digitalio.Pull.UP


# GPIO pin configuration
pins = [
    # Serie 1
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    # Serie 2
    # board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17,
    # board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26,
]

# Create DigitalInOut objets for each GPIO pins
pin_objs = []
for pin in pins:
    pin_obj = digitalio.DigitalInOut(pin)
    pin_obj.direction = digitalio.Direction.INPUT
    pin_obj.pull = digitalio.Pull.UP
    pin_objs.append(pin_obj)


# Init pins state memory
pins_state = [False] * len(pins)

# Create a Keyboard objet for sending commands to computer
keyboard = Keyboard(usb_hid.devices)

print("Ready !!! Wating for key press...")
led.value = False
for i in range(3):
    led.value = True
    time.sleep(0.2)
    led.value = False
    time.sleep(0.1)
# for end

while True:

    # Update Ctrl and Shift swiches (Invert for pull-up resistor)
    pin_sw1_enabled = not pin_sw1.value
    pin_sw2_enabled = not pin_sw2.value

    for i in range(len(pins)):
        # Invert for pull-up resistor
        current_state = not pin_objs[i].value
        if current_state != pins_state[i]:  # The pin changed state
            led.value = True
            pins_state[i] = current_state  # Keep in memory the new pin state

            if current_state:  # The pin is currently enabled (switch pushed)

                if pins[i] == board.GP0:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.press(Keycode.F13)
                        print("Press F13")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.send(Keycode.CONTROL, Keycode.F13)
                        print("Press Ctrl+F13")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.send(Keycode.SHIFT, Keycode.F13)
                        print("Press Shift+F13")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F13)
                        print("Press Ctrl+Shift+F13")

                elif pins[i] == board.GP1:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.press(Keycode.F14)
                        print("Press F14")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.send(Keycode.CONTROL, Keycode.F14)
                        print("Press Ctrl+F14")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.send(Keycode.SHIFT, Keycode.F14)
                        print("Press Shift+F14")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F14)
                        print("Press Ctrl+Shift+F14")

                elif pins[i] == board.GP2:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.press(Keycode.F15)
                        print("Press F15")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.send(Keycode.CONTROL, Keycode.F15)
                        print("Press Ctrl+F15")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.send(Keycode.SHIFT, Keycode.F15)
                        print("Press Shift+F15")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F15)
                        print("Press Ctrl+Shift+F15")

                elif pins[i] == board.GP3:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.press(Keycode.F16)
                        print("Press F16")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.send(Keycode.CONTROL, Keycode.F16)
                        print("Press Ctrl+F16")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.send(Keycode.SHIFT, Keycode.F16)
                        print("Press Shift+F16")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F16)
                        print("Press Ctrl+Shift+F16")

                elif pins[i] == board.GP4:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.press(Keycode.F17)
                        print("Press F17")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.send(Keycode.CONTROL, Keycode.F17)
                        print("Press Ctrl+F17")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.send(Keycode.SHIFT, Keycode.F17)
                        print("Press Shift+F17")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F17)
                        print("Press Ctrl+Shift+F17")

                elif pins[i] == board.GP5:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.press(Keycode.F18)
                        print("Press F18")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.send(Keycode.CONTROL, Keycode.F18)
                        print("Press Ctrl+F18")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.send(Keycode.SHIFT, Keycode.F18)
                        print("Press Shift+F18")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F18)
                        print("Press Ctrl+Shift+F18")

                elif pins[i] == board.GP6:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.press(Keycode.F19)
                        print("Press F19")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.send(Keycode.CONTROL, Keycode.F19)
                        print("Press Ctrl+F19")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.send(Keycode.SHIFT, Keycode.F19)
                        print("Press Shift+F19")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F19)
                        print("Press Ctrl+Shift+F19")

                elif pins[i] == board.GP7:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.press(Keycode.F20)
                        print("Press F20")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.send(Keycode.CONTROL, Keycode.F20)
                        print("Press Ctrl+F20")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.send(Keycode.SHIFT, Keycode.F20)
                        print("Press Shift+F20")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F20)
                        print("Press Ctrl+Shift+F20")

                elif pins[i] == board.GP8:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.press(Keycode.F21)
                        print("Press F21")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.send(Keycode.CONTROL, Keycode.F21)
                        print("Press Ctrl+F21")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.send(Keycode.SHIFT, Keycode.F21)
                        print("Press Shift+F21")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F21)
                        print("Press Ctrl+Shift+F21")

                elif pins[i] == board.GP9:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.press(Keycode.F22)
                        print("Press F22")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.send(Keycode.CONTROL, Keycode.F22)
                        print("Press Ctrl+F22")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.send(Keycode.SHIFT, Keycode.F22)
                        print("Press Shift+F22")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F22)
                        print("Press Ctrl+Shift+F22")

                elif pins[i] == board.GP10:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.press(Keycode.F23)
                        print("Press F23")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.send(Keycode.CONTROL, Keycode.F23)
                        print("Press Ctrl+F23")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.send(Keycode.SHIFT, Keycode.F23)
                        print("Press Shift+F23")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F23)
                        print("Press Ctrl+Shift+F23")

                elif pins[i] == board.GP11:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.press(Keycode.F24)
                        print("Press F24")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.send(Keycode.CONTROL, Keycode.F24)
                        print("Press Ctrl+F24")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.send(Keycode.SHIFT, Keycode.F24)
                        print("Press Shift+F24")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.F24)
                        print("Press Ctrl+Shift+F24")
                # Add other keys here

            else:  # The pin is currently disabled (switch released)

                if pins[i] == board.GP0:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.release(Keycode.F13)
                        print("Release F13")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.release_all()
                        print("Release all Ctrl+F13")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.release_all()
                        print("Release all Shift+F13")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.release_all()
                        print("Release all Ctrl+Shift+F13")

                elif pins[i] == board.GP1:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.release(Keycode.F14)
                        print("Release F14")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.release_all()
                        print("Release all Ctrl+F14")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.release_all()
                        print("Release all Shift+F14")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.release_all()
                        print("Release all Ctrl+Shift+F14")

                elif pins[i] == board.GP2:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.release(Keycode.F15)
                        print("Release F15")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.release_all()
                        print("Release all Ctrl+F15")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.release_all()
                        print("Release all Shift+F15")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.release_all()
                        print("Release all Ctrl+Shift+F15")

                elif pins[i] == board.GP3:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.release(Keycode.F16)
                        print("Release F16")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.release_all()
                        print("Release all Ctrl+F16")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.release_all()
                        print("Release all Shift+F16")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.release_all()
                        print("Release all Ctrl+Shift+F16")

                elif pins[i] == board.GP4:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.release(Keycode.F17)
                        print("Release F17")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.release_all()
                        print("Release all Ctrl+F17")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.release_all()
                        print("Release all Shift+F17")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.release_all()
                        print("Release all Ctrl+Shift+F17")

                elif pins[i] == board.GP5:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.release(Keycode.F18)
                        print("Release F18")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.release_all()
                        print("Release all Ctrl+F18")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.release_all()
                        print("Release all Shift+F18")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.release_all()
                        print("Release all Ctrl+Shift+F18")

                elif pins[i] == board.GP6:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.release(Keycode.F19)
                        print("Release F19")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.release_all()
                        print("Release all Ctrl+F19")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.release_all()
                        print("Release all Shift+F19")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.release_all()
                        print("Release all Ctrl+Shift+F19")

                elif pins[i] == board.GP7:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.release(Keycode.F20)
                        print("Release F20")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.release_all()
                        print("Release all Ctrl+F20")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.release_all()
                        print("Release all Shift+F20")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.release_all()
                        print("Release all Ctrl+Shift+F20")

                elif pins[i] == board.GP8:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.release(Keycode.F21)
                        print("Release F21")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.release_all()
                        print("Release all Ctrl+F21")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.release_all()
                        print("Release all Shift+F21")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.release_all()
                        print("Release all Ctrl+Shift+F21")

                elif pins[i] == board.GP9:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.release(Keycode.F22)
                        print("Release F22")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.release_all()
                        print("Release all Ctrl+F22")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.release_all()
                        print("Release all Shift+F22")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.release_all()
                        print("Release all Ctrl+Shift+F22")

                elif pins[i] == board.GP10:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.release(Keycode.F23)
                        print("Release F23")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.release_all()
                        print("Release all Ctrl+F23")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.release_all()
                        print("Release all Shift+F23")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.release_all()
                        print("Release all Ctrl+Shift+F23")

                elif pins[i] == board.GP11:
                    if not pin_sw1_enabled and not pin_sw2_enabled:  # All switch OFF
                        keyboard.release(Keycode.F24)
                        print("Release F24")
                    elif pin_sw1_enabled and not pin_sw2_enabled:  # Ctrl ON
                        keyboard.release_all()
                        print("Release all Ctrl+F24")
                    elif not pin_sw1_enabled and pin_sw2_enabled:  # Shift ON
                        keyboard.release_all()
                        print("Release all Shift+F24")
                    elif pin_sw1_enabled and pin_sw2_enabled:  # Ctrl and Shift ON
                        keyboard.release_all()
                        print("Release all Ctrl+Shift+F24")

                # Add other keys here
            #  if end

        #  if end
    #  for end
    time.sleep(0.01)  # Ajust polling rate

    if led.value:  # Onboard LED OFF
        led.value = False
    #  if end

#  while end