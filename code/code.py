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
pin_sw_ctrl = digitalio.DigitalInOut(board.GP28)
pin_sw_ctrl.direction = digitalio.Direction.INPUT
pin_sw_ctrl.pull = digitalio.Pull.UP
# Init switchs Shift
pin_sw_shift = digitalio.DigitalInOut(board.GP27)
pin_sw_shift.direction = digitalio.Direction.INPUT
pin_sw_shift.pull = digitalio.Pull.UP
# Init switchs Alt
pin_sw_alt = digitalio.DigitalInOut(board.GP26)
pin_sw_alt.direction = digitalio.Direction.INPUT
pin_sw_alt.pull = digitalio.Pull.UP


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
    pin_sw_ctrl_on = not pin_sw_ctrl.value
    pin_sw_shift_on = not pin_sw_shift.value
    pin_sw_alt_on = not pin_sw_alt.value

    for i in range(len(pins)):
        # Invert for pull-up resistor
        current_state = not pin_objs[i].value
        if current_state != pins_state[i]:  # The pin changed state
            led.value = True
            pins_state[i] = current_state  # Keep in memory the new pin state

            if current_state:  # The pin is currently enabled (switch pushed)

                if pins[i] == board.GP0:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.press(Keycode.F13)
                        print("Press F13")
                    else:
                        keys_arr = []
                        str_keys_arr = []
                        if pin_sw_ctrl_on:  # Ctrl ON
                            keys_arr.append(Keycode.CONTROL)
                            str_keys_arr.append('Ctrl')
                        if pin_sw_alt_on:  # ALT ON
                            keys_arr.append(Keycode.ALT)
                            str_keys_arr.append('Alt')
                        if pin_sw_shift_on:  # Shift ON
                            keys_arr.append(Keycode.SHIFT)
                            str_keys_arr.append('Shift')
                        str_keys_arr.append('F13')
                        print('Send '+'+'.join(str_keys_arr))
                        keyboard.send(*keys_arr)

                elif pins[i] == board.GP1:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.press(Keycode.F14)
                        print("Press F14")
                    else:
                        keys_arr = []
                        str_keys_arr = []
                        if pin_sw_ctrl_on:  # Ctrl ON
                            keys_arr.append(Keycode.CONTROL)
                            str_keys_arr.append('Ctrl')
                        if pin_sw_alt_on:  # ALT ON
                            keys_arr.append(Keycode.ALT)
                            str_keys_arr.append('Alt')
                        if pin_sw_shift_on:  # Shift ON
                            keys_arr.append(Keycode.SHIFT)
                            str_keys_arr.append('Shift')
                        str_keys_arr.append('F14')
                        print('Send '+'+'.join(str_keys_arr))
                        keyboard.send(*keys_arr)

                elif pins[i] == board.GP2:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.press(Keycode.F15)
                        print("Press F15")
                    else:
                        keys_arr = []
                        str_keys_arr = []
                        if pin_sw_ctrl_on:  # Ctrl ON
                            keys_arr.append(Keycode.CONTROL)
                            str_keys_arr.append('Ctrl')
                        if pin_sw_alt_on:  # ALT ON
                            keys_arr.append(Keycode.ALT)
                            str_keys_arr.append('Alt')
                        if pin_sw_shift_on:  # Shift ON
                            keys_arr.append(Keycode.SHIFT)
                            str_keys_arr.append('Shift')
                        str_keys_arr.append('F15')
                        print('Send '+'+'.join(str_keys_arr))
                        keyboard.send(*keys_arr)

                elif pins[i] == board.GP3:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.press(Keycode.F16)
                        print("Press F16")
                    else:
                        keys_arr = []
                        str_keys_arr = []
                        if pin_sw_ctrl_on:  # Ctrl ON
                            keys_arr.append(Keycode.CONTROL)
                            str_keys_arr.append('Ctrl')
                        if pin_sw_alt_on:  # ALT ON
                            keys_arr.append(Keycode.ALT)
                            str_keys_arr.append('Alt')
                        if pin_sw_shift_on:  # Shift ON
                            keys_arr.append(Keycode.SHIFT)
                            str_keys_arr.append('Shift')
                        str_keys_arr.append('F16')
                        print('Send '+'+'.join(str_keys_arr))
                        keyboard.send(*keys_arr)

                elif pins[i] == board.GP4:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.press(Keycode.F17)
                        print("Press F17")
                    else:
                        keys_arr = []
                        str_keys_arr = []
                        if pin_sw_ctrl_on:  # Ctrl ON
                            keys_arr.append(Keycode.CONTROL)
                            str_keys_arr.append('Ctrl')
                        if pin_sw_alt_on:  # ALT ON
                            keys_arr.append(Keycode.ALT)
                            str_keys_arr.append('Alt')
                        if pin_sw_shift_on:  # Shift ON
                            keys_arr.append(Keycode.SHIFT)
                            str_keys_arr.append('Shift')
                        str_keys_arr.append('F17')
                        print('Send '+'+'.join(str_keys_arr))
                        keyboard.send(*keys_arr)

                elif pins[i] == board.GP5:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.press(Keycode.F18)
                        print("Press F18")
                    else:
                        keys_arr = []
                        str_keys_arr = []
                        if pin_sw_ctrl_on:  # Ctrl ON
                            keys_arr.append(Keycode.CONTROL)
                            str_keys_arr.append('Ctrl')
                        if pin_sw_alt_on:  # ALT ON
                            keys_arr.append(Keycode.ALT)
                            str_keys_arr.append('Alt')
                        if pin_sw_shift_on:  # Shift ON
                            keys_arr.append(Keycode.SHIFT)
                            str_keys_arr.append('Shift')
                        str_keys_arr.append('F18')
                        print('Send '+'+'.join(str_keys_arr))
                        keyboard.send(*keys_arr)

                elif pins[i] == board.GP6:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.press(Keycode.F19)
                        print("Press F19")
                    else:
                        keys_arr = []
                        str_keys_arr = []
                        if pin_sw_ctrl_on:  # Ctrl ON
                            keys_arr.append(Keycode.CONTROL)
                            str_keys_arr.append('Ctrl')
                        if pin_sw_alt_on:  # ALT ON
                            keys_arr.append(Keycode.ALT)
                            str_keys_arr.append('Alt')
                        if pin_sw_shift_on:  # Shift ON
                            keys_arr.append(Keycode.SHIFT)
                            str_keys_arr.append('Shift')
                        str_keys_arr.append('F19')
                        print('Send '+'+'.join(str_keys_arr))
                        keyboard.send(*keys_arr)

                elif pins[i] == board.GP7:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.press(Keycode.F20)
                        print("Press F20")
                    else:
                        keys_arr = []
                        str_keys_arr = []
                        if pin_sw_ctrl_on:  # Ctrl ON
                            keys_arr.append(Keycode.CONTROL)
                            str_keys_arr.append('Ctrl')
                        if pin_sw_alt_on:  # ALT ON
                            keys_arr.append(Keycode.ALT)
                            str_keys_arr.append('Alt')
                        if pin_sw_shift_on:  # Shift ON
                            keys_arr.append(Keycode.SHIFT)
                            str_keys_arr.append('Shift')
                        str_keys_arr.append('F20')
                        print('Send '+'+'.join(str_keys_arr))
                        keyboard.send(*keys_arr)

                elif pins[i] == board.GP8:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.press(Keycode.F21)
                        print("Press F21")
                    else:
                        keys_arr = []
                        str_keys_arr = []
                        if pin_sw_ctrl_on:  # Ctrl ON
                            keys_arr.append(Keycode.CONTROL)
                            str_keys_arr.append('Ctrl')
                        if pin_sw_alt_on:  # ALT ON
                            keys_arr.append(Keycode.ALT)
                            str_keys_arr.append('Alt')
                        if pin_sw_shift_on:  # Shift ON
                            keys_arr.append(Keycode.SHIFT)
                            str_keys_arr.append('Shift')
                        str_keys_arr.append('F21')
                        print('Send '+'+'.join(str_keys_arr))
                        keyboard.send(*keys_arr)

                elif pins[i] == board.GP9:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.press(Keycode.F22)
                        print("Press F22")
                    else:
                        keys_arr = []
                        str_keys_arr = []
                        if pin_sw_ctrl_on:  # Ctrl ON
                            keys_arr.append(Keycode.CONTROL)
                            str_keys_arr.append('Ctrl')
                        if pin_sw_alt_on:  # ALT ON
                            keys_arr.append(Keycode.ALT)
                            str_keys_arr.append('Alt')
                        if pin_sw_shift_on:  # Shift ON
                            keys_arr.append(Keycode.SHIFT)
                            str_keys_arr.append('Shift')
                        str_keys_arr.append('F22')
                        print('Send '+'+'.join(str_keys_arr))
                        keyboard.send(*keys_arr)

                elif pins[i] == board.GP10:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.press(Keycode.F23)
                        print("Press F23")
                    else:
                        keys_arr = []
                        str_keys_arr = []
                        if pin_sw_ctrl_on:  # Ctrl ON
                            keys_arr.append(Keycode.CONTROL)
                            str_keys_arr.append('Ctrl')
                        if pin_sw_alt_on:  # ALT ON
                            keys_arr.append(Keycode.ALT)
                            str_keys_arr.append('Alt')
                        if pin_sw_shift_on:  # Shift ON
                            keys_arr.append(Keycode.SHIFT)
                            str_keys_arr.append('Shift')
                        str_keys_arr.append('F23')
                        print('Send '+'+'.join(str_keys_arr))
                        keyboard.send(*keys_arr)

                elif pins[i] == board.GP11:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.press(Keycode.F24)
                        print("Press F24")
                    else:
                        keys_arr = []
                        str_keys_arr = []
                        if pin_sw_ctrl_on:  # Ctrl ON
                            keys_arr.append(Keycode.CONTROL)
                            str_keys_arr.append('Ctrl')
                        if pin_sw_alt_on:  # ALT ON
                            keys_arr.append(Keycode.ALT)
                            str_keys_arr.append('Alt')
                        if pin_sw_shift_on:  # Shift ON
                            keys_arr.append(Keycode.SHIFT)
                            str_keys_arr.append('Shift')
                        str_keys_arr.append('F24')
                        print('Send '+'+'.join(str_keys_arr))
                        keyboard.send(*keys_arr)
                # Add other keys here

            else:  # The pin is currently disabled (switch released)

                if pins[i] == board.GP0:

                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.release(Keycode.F13)
                        print("Release F13")
                    # else:
                    #     keys_arr = []
                    #     str_keys_arr = ['Release ']
                    #     if pin_sw_ctrl_on:  # Ctrl ON
                    #         keys_arr.append(Keycode.CONTROL)
                    #         str_keys_arr.append('Ctrl')
                    #     if pin_sw_alt_on:  # ALT ON
                    #         keys_arr.append(Keycode.ALT)
                    #         str_keys_arr.append('Alt')
                    #     if pin_sw_shift_on:  # Shift ON
                    #         keys_arr.append(Keycode.SHIFT)
                    #         str_keys_arr.append('Shift')
                    #     str_keys_arr.append('F13')
                    #     print('+'.join(str_keys_arr))
                    #     keyboard.release(*keys_arr)
                    #     # keyboard.release_all()

                elif pins[i] == board.GP1:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.release(Keycode.F14)
                        print("Release F14")
                    # else:
                    #     keys_arr = []
                    #     str_keys_arr = ['Release ']
                    #     if pin_sw_ctrl_on:  # Ctrl ON
                    #         keys_arr.append(Keycode.CONTROL)
                    #         str_keys_arr.append('Ctrl')
                    #     if pin_sw_alt_on:  # ALT ON
                    #         keys_arr.append(Keycode.ALT)
                    #         str_keys_arr.append('Alt')
                    #     if pin_sw_shift_on:  # Shift ON
                    #         keys_arr.append(Keycode.SHIFT)
                    #         str_keys_arr.append('Shift')
                    #     str_keys_arr.append('F14')
                    #     print('+'.join(str_keys_arr))
                    #     keyboard.release(*keys_arr)
                    #     # keyboard.release_all()

                elif pins[i] == board.GP2:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.release(Keycode.F15)
                        print("Release F15")
                    # else:
                    #     keys_arr = []
                    #     str_keys_arr = ['Release ']
                    #     if pin_sw_ctrl_on:  # Ctrl ON
                    #         keys_arr.append(Keycode.CONTROL)
                    #         str_keys_arr.append('Ctrl')
                    #     if pin_sw_alt_on:  # ALT ON
                    #         keys_arr.append(Keycode.ALT)
                    #         str_keys_arr.append('Alt')
                    #     if pin_sw_shift_on:  # Shift ON
                    #         keys_arr.append(Keycode.SHIFT)
                    #         str_keys_arr.append('Shift')
                    #     str_keys_arr.append('F15')
                    #     print('+'.join(str_keys_arr))
                    #     keyboard.release(*keys_arr)
                    #     # keyboard.release_all()

                elif pins[i] == board.GP3:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.release(Keycode.F16)
                        print("Release F16")
                    # else:
                    #     keys_arr = []
                    #     str_keys_arr = ['Release ']
                    #     if pin_sw_ctrl_on:  # Ctrl ON
                    #         keys_arr.append(Keycode.CONTROL)
                    #         str_keys_arr.append('Ctrl')
                    #     if pin_sw_alt_on:  # ALT ON
                    #         keys_arr.append(Keycode.ALT)
                    #         str_keys_arr.append('Alt')
                    #     if pin_sw_shift_on:  # Shift ON
                    #         keys_arr.append(Keycode.SHIFT)
                    #         str_keys_arr.append('Shift')
                    #     str_keys_arr.append('F16')
                    #     print('+'.join(str_keys_arr))
                    #     keyboard.release(*keys_arr)
                    #     # keyboard.release_all()

                elif pins[i] == board.GP4:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.release(Keycode.F17)
                        print("Release F17")
                    # else:
                    #     keys_arr = []
                    #     str_keys_arr = ['Release ']
                    #     if pin_sw_ctrl_on:  # Ctrl ON
                    #         keys_arr.append(Keycode.CONTROL)
                    #         str_keys_arr.append('Ctrl')
                    #     if pin_sw_alt_on:  # ALT ON
                    #         keys_arr.append(Keycode.ALT)
                    #         str_keys_arr.append('Alt')
                    #     if pin_sw_shift_on:  # Shift ON
                    #         keys_arr.append(Keycode.SHIFT)
                    #         str_keys_arr.append('Shift')
                    #     str_keys_arr.append('F17')
                    #     print('+'.join(str_keys_arr))
                    #     keyboard.release(*keys_arr)
                    #     # keyboard.release_all()

                elif pins[i] == board.GP5:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.release(Keycode.F18)
                        print("Release F18")
                    # else:
                    #     keys_arr = []
                    #     str_keys_arr = ['Release ']
                    #     if pin_sw_ctrl_on:  # Ctrl ON
                    #         keys_arr.append(Keycode.CONTROL)
                    #         str_keys_arr.append('Ctrl')
                    #     if pin_sw_alt_on:  # ALT ON
                    #         keys_arr.append(Keycode.ALT)
                    #         str_keys_arr.append('Alt')
                    #     if pin_sw_shift_on:  # Shift ON
                    #         keys_arr.append(Keycode.SHIFT)
                    #         str_keys_arr.append('Shift')
                    #     str_keys_arr.append('F18')
                    #     print('+'.join(str_keys_arr))
                    #     keyboard.release(*keys_arr)
                    #     # keyboard.release_all()

                elif pins[i] == board.GP6:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.release(Keycode.F19)
                        print("Release F19")
                    # else:
                    #     keys_arr = []
                    #     str_keys_arr = ['Release ']
                    #     if pin_sw_ctrl_on:  # Ctrl ON
                    #         keys_arr.append(Keycode.CONTROL)
                    #         str_keys_arr.append('Ctrl')
                    #     if pin_sw_alt_on:  # ALT ON
                    #         keys_arr.append(Keycode.ALT)
                    #         str_keys_arr.append('Alt')
                    #     if pin_sw_shift_on:  # Shift ON
                    #         keys_arr.append(Keycode.SHIFT)
                    #         str_keys_arr.append('Shift')
                    #     str_keys_arr.append('F19')
                    #     print('+'.join(str_keys_arr))
                    #     keyboard.release(*keys_arr)
                    #     # keyboard.release_all()

                elif pins[i] == board.GP7:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.release(Keycode.F20)
                        print("Release F20")
                    # else:
                    #     keys_arr = []
                    #     str_keys_arr = ['Release ']
                    #     if pin_sw_ctrl_on:  # Ctrl ON
                    #         keys_arr.append(Keycode.CONTROL)
                    #         str_keys_arr.append('Ctrl')
                    #     if pin_sw_alt_on:  # ALT ON
                    #         keys_arr.append(Keycode.ALT)
                    #         str_keys_arr.append('Alt')
                    #     if pin_sw_shift_on:  # Shift ON
                    #         keys_arr.append(Keycode.SHIFT)
                    #         str_keys_arr.append('Shift')
                    #     str_keys_arr.append('F20')
                    #     print('+'.join(str_keys_arr))
                    #     keyboard.release(*keys_arr)
                    #     # keyboard.release_all()

                elif pins[i] == board.GP8:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.release(Keycode.F21)
                        print("Release F21")
                    # else:
                    #     keys_arr = []
                    #     str_keys_arr = ['Release ']
                    #     if pin_sw_ctrl_on:  # Ctrl ON
                    #         keys_arr.append(Keycode.CONTROL)
                    #         str_keys_arr.append('Ctrl')
                    #     if pin_sw_alt_on:  # ALT ON
                    #         keys_arr.append(Keycode.ALT)
                    #         str_keys_arr.append('Alt')
                    #     if pin_sw_shift_on:  # Shift ON
                    #         keys_arr.append(Keycode.SHIFT)
                    #         str_keys_arr.append('Shift')
                    #     str_keys_arr.append('F21')
                    #     print('+'.join(str_keys_arr))
                    #     keyboard.release(*keys_arr)
                    #     # keyboard.release_all()

                elif pins[i] == board.GP9:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.release(Keycode.F22)
                        print("Release F22")
                    # else:
                    #     keys_arr = []
                    #     str_keys_arr = ['Release ']
                    #     if pin_sw_ctrl_on:  # Ctrl ON
                    #         keys_arr.append(Keycode.CONTROL)
                    #         str_keys_arr.append('Ctrl')
                    #     if pin_sw_alt_on:  # ALT ON
                    #         keys_arr.append(Keycode.ALT)
                    #         str_keys_arr.append('Alt')
                    #     if pin_sw_shift_on:  # Shift ON
                    #         keys_arr.append(Keycode.SHIFT)
                    #         str_keys_arr.append('Shift')
                    #     str_keys_arr.append('F22')
                    #     print('+'.join(str_keys_arr))
                    #     keyboard.release(*keys_arr)
                    #     # keyboard.release_all()

                elif pins[i] == board.GP10:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.release(Keycode.F23)
                        print("Release F23")
                    # else:
                    #     keys_arr = []
                    #     str_keys_arr = ['Release ']
                    #     if pin_sw_ctrl_on:  # Ctrl ON
                    #         keys_arr.append(Keycode.CONTROL)
                    #         str_keys_arr.append('Ctrl')
                    #     if pin_sw_alt_on:  # ALT ON
                    #         keys_arr.append(Keycode.ALT)
                    #         str_keys_arr.append('Alt')
                    #     if pin_sw_shift_on:  # Shift ON
                    #         keys_arr.append(Keycode.SHIFT)
                    #         str_keys_arr.append('Shift')
                    #     str_keys_arr.append('F23')
                    #     print('+'.join(str_keys_arr))
                    #     keyboard.release(*keys_arr)
                    #     # keyboard.release_all()

                elif pins[i] == board.GP11:
                    if not (pin_sw_ctrl_on or pin_sw_shift_on or pin_sw_alt_on):
                        keyboard.release(Keycode.F24)
                        print("Release F24")
                    # else:
                    #     keys_arr = []
                    #     str_keys_arr = ['Release ']
                    #     if pin_sw_ctrl_on:  # Ctrl ON
                    #         keys_arr.append(Keycode.CONTROL)
                    #         str_keys_arr.append('Ctrl')
                    #     if pin_sw_alt_on:  # ALT ON
                    #         keys_arr.append(Keycode.ALT)
                    #         str_keys_arr.append('Alt')
                    #     if pin_sw_shift_on:  # Shift ON
                    #         keys_arr.append(Keycode.SHIFT)
                    #         str_keys_arr.append('Shift')
                    #     str_keys_arr.append('F24')
                    #     print('+'.join(str_keys_arr))
                    #     keyboard.release(*keys_arr)
                    #     # keyboard.release_all()

                # Add other keys here
            #  if end

        #  if end
    #  for end
    time.sleep(0.01)  # Ajust polling rate

    if led.value:  # Onboard LED OFF
        led.value = False
    #  if end

#  while end