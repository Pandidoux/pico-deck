import storage
import board, digitalio

# If not pressed, the key will be at +V (due to the pull-up).
# https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial#circuitpy-mass-storage-device-3096583-4
button_firmware = digitalio.DigitalInOut(board.GP0)
button_firmware.direction = digitalio.Direction.INPUT
button_firmware.pull = digitalio.Pull.UP

# Disable devices only if button is not pressed.
if button_firmware.value:
    print(f"boot: button not pressed, disabling drive")
    storage.disable_usb_drive()