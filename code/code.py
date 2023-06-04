import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio
import analogio
import pwmio

# Set polling rate (seconds)
polling_rate = 0.01

# Enable / Disable serial console print
debug = True

# Init onboard LED
onboard_led = digitalio.DigitalInOut(board.LED)
onboard_led.direction = digitalio.Direction.OUTPUT
onboard_led.value = True

# Init switchs Ctrl
pin_sw_ctrl = digitalio.DigitalInOut(board.GP20)
pin_sw_ctrl.direction = digitalio.Direction.INPUT
pin_sw_ctrl.pull = digitalio.Pull.UP
# Init switchs Shift
pin_sw_shift = digitalio.DigitalInOut(board.GP21)
pin_sw_shift.direction = digitalio.Direction.INPUT
pin_sw_shift.pull = digitalio.Pull.UP
# Init switchs Alt
pin_sw_alt = digitalio.DigitalInOut(board.GP22)
pin_sw_alt.direction = digitalio.Direction.INPUT
pin_sw_alt.pull = digitalio.Pull.UP


# GPIO pin configuration
button_pins = [
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11
]
# Create DigitalInOut objets for each GPIO button_pins
buttons = []
for pin in button_pins:
    pin_obj = digitalio.DigitalInOut(pin)
    pin_obj.direction = digitalio.Direction.INPUT
    pin_obj.pull = digitalio.Pull.UP
    buttons.append(pin_obj)


# Init button_pins state memory
button_pins_state = [False] * len(button_pins)


# Create a Keyboard objet for sending commands to computer
keyboard = Keyboard(usb_hid.devices)


# Translate Keycode to text
def keycode_to_text(keycode):
    if keycode == Keycode.F13:
        return 'F13'
    elif keycode == Keycode.F14:
        return 'F14'
    elif keycode == Keycode.F15:
        return 'F15'
    elif keycode == Keycode.F16:
        return 'F16'
    elif keycode == Keycode.F17:
        return 'F17'
    elif keycode == Keycode.F18:
        return 'F18'
    elif keycode == Keycode.F19:
        return 'F19'
    elif keycode == Keycode.F20:
        return 'F20'
    elif keycode == Keycode.F21:
        return 'F21'
    elif keycode == Keycode.F22:
        return 'F22'
    elif keycode == Keycode.F23:
        return 'F23'
    elif keycode == Keycode.F24:
        return 'F24'


def send_macro(ctrl, alt, shift, virtualkey):
    keys_arr = []
    str_keys_arr = []
    if ctrl:  # Ctrl ON
        keys_arr.append(Keycode.CONTROL)
        if debug:
            str_keys_arr.append('CONTROL')
    if alt:  # ALT ON
        keys_arr.append(Keycode.ALT)
        if debug:
            str_keys_arr.append('ALT')
    if shift:  # Shift ON
        keys_arr.append(Keycode.SHIFT)
        if debug:
            str_keys_arr.append('SHIFT')
    keys_arr.append(virtualkey)
    if debug:
        str_keys_arr.append(keycode_to_text(virtualkey))
        print('Send '+'+'.join(str_keys_arr))
    keyboard.send(*keys_arr)


if debug:
    print("Ready !!! Wating for key press...")
onboard_led.value = False
for i in range(20):
    onboard_led.value = True
    time.sleep(0.03)
    onboard_led.value = False
    time.sleep(0.02)
# for end
onboard_led.value = False
for i in range(3):
    time.sleep(0.1)
    onboard_led.value = True
    time.sleep(0.2)
    onboard_led.value = False
# for end


while True:

    # Update Ctrl and Shift swiches (Invert for pull-up resistor)
    is_ctrl_on = not pin_sw_ctrl.value
    is_shift_on = not pin_sw_shift.value
    is_alt_on = not pin_sw_alt.value

    for i in range(len(button_pins)):
        # Invert for pull-up resistor
        current_state = not buttons[i].value
        if current_state != button_pins_state[i]:  # The pin changed state
            onboard_led.value = True
            button_pins_state[i] = current_state  # Keep in memory the new pin state

            if current_state:  # The pin is currently enabled (switch pushed)

                if button_pins[i] == board.GP0:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.press(Keycode.F13)
                        if debug:
                            print("Press F13")
                    else:
                        send_macro(is_ctrl_on, is_alt_on, is_shift_on, Keycode.F13)

                elif button_pins[i] == board.GP1:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.press(Keycode.F14)
                        if debug:
                            print("Press F14")
                    else:
                        send_macro(is_ctrl_on, is_alt_on, is_shift_on, Keycode.F14)

                elif button_pins[i] == board.GP2:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.press(Keycode.F15)
                        if debug:
                            print("Press F15")
                    else:
                        send_macro(is_ctrl_on, is_alt_on, is_shift_on, Keycode.F15)

                elif button_pins[i] == board.GP3:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.press(Keycode.F16)
                        if debug:
                            print("Press F16")
                    else:
                        send_macro(is_ctrl_on, is_alt_on, is_shift_on, Keycode.F16)

                elif button_pins[i] == board.GP4:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.press(Keycode.F17)
                        if debug:
                            print("Press F17")
                    else:
                        send_macro(is_ctrl_on, is_alt_on, is_shift_on, Keycode.F17)

                elif button_pins[i] == board.GP5:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.press(Keycode.F18)
                        if debug:
                            print("Press F18")
                    else:
                        send_macro(is_ctrl_on, is_alt_on, is_shift_on, Keycode.F18)

                elif button_pins[i] == board.GP6:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.press(Keycode.F19)
                        if debug:
                            print("Press F19")
                    else:
                        send_macro(is_ctrl_on, is_alt_on, is_shift_on, Keycode.F19)

                elif button_pins[i] == board.GP7:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.press(Keycode.F20)
                        if debug:
                            print("Press F20")
                    else:
                        send_macro(is_ctrl_on, is_alt_on, is_shift_on, Keycode.F20)

                elif button_pins[i] == board.GP8:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.press(Keycode.F21)
                        if debug:
                            print("Press F21")
                    else:
                        send_macro(is_ctrl_on, is_alt_on, is_shift_on, Keycode.F21)

                elif button_pins[i] == board.GP9:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.press(Keycode.F22)
                        if debug:
                            print("Press F22")
                    else:
                        send_macro(is_ctrl_on, is_alt_on, is_shift_on, Keycode.F22)

                elif button_pins[i] == board.GP10:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.press(Keycode.F23)
                        if debug:
                            print("Press F23")
                    else:
                        send_macro(is_ctrl_on, is_alt_on, is_shift_on, Keycode.F23)

                elif button_pins[i] == board.GP11:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.press(Keycode.F24)
                        if debug:
                            print("Press F24")
                    else:
                        send_macro(is_ctrl_on, is_alt_on, is_shift_on, Keycode.F24)
                # Add other keys here

            else:  # The pin is currently disabled (switch released)

                if button_pins[i] == board.GP0:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.release(Keycode.F13)
                        if debug:
                            print("Release F13")

                elif button_pins[i] == board.GP1:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.release(Keycode.F14)
                        if debug:
                            print("Release F14")

                elif button_pins[i] == board.GP2:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.release(Keycode.F15)
                        if debug:
                            print("Release F15")

                elif button_pins[i] == board.GP3:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.release(Keycode.F16)
                        if debug:
                            print("Release F16")

                elif button_pins[i] == board.GP4:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.release(Keycode.F17)
                        if debug:
                            print("Release F17")

                elif button_pins[i] == board.GP5:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.release(Keycode.F18)
                        if debug:
                            print("Release F18")

                elif button_pins[i] == board.GP6:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.release(Keycode.F19)
                        if debug:
                            print("Release F19")

                elif button_pins[i] == board.GP7:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.release(Keycode.F20)
                        if debug:
                            print("Release F20")

                elif button_pins[i] == board.GP8:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.release(Keycode.F21)
                        if debug:
                            print("Release F21")

                elif button_pins[i] == board.GP9:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.release(Keycode.F22)
                        if debug:
                            print("Release F22")

                elif button_pins[i] == board.GP10:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.release(Keycode.F23)
                        if debug:
                            print("Release F23")

                elif button_pins[i] == board.GP11:
                    if not (is_ctrl_on or is_shift_on or is_alt_on):
                        keyboard.release(Keycode.F24)
                        if debug:
                            print("Release F24")
                # Add other keys here
            #  if end

        #  if end
    #  for end


    if onboard_led.value:  # Onboard LED OFF
        onboard_led.value = False
    #  if end


    time.sleep(polling_rate)  # Wait before next loop
#  while end