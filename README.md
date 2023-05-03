# Pico Deck

## Introduction

Use a Raspberry pi Pico to make your own usb macro keyboard.

Use CircuitPython and adafruit's libraries.

## Feature
- Anti-ghosting
- Use F13 to F24 virtual keyboard keys
- Up to 12 physical buttons
- Two physical switches (on/off) to toggle 4 profils

### Informations
#### About profils
- F# : Instruction press send when the button is press and release when the button is release (implement anti-ghosting)
- Ctrl+F# : Instruction press+release send when the buton is press. When button is release send release all keys
- Shift+F# : Instruction press+release send when the buton is press. When button is release send release all keys
- Ctrl+Shift+F# : Instruction press+release send when the buton is press. When button is release send release all keys

## Install on your Pico

- Clone or download this repostory.
#### Flash CircuitPython `firmware`
- On your Pico, press BOOTSEL button while plugin to your computer via USB
- Drag and drop the [latest CircuitPython](https://circuitpython.org/downloads) firmware file (.uf2) on your pico storage, it will reboot.
#### Install `code`
- Plug your Pico to your computer (do not press BOOTSEL)
- Drag and drop the new `code.py` on your Pico.
- Drag and drop the library folder `lib` on your Pico.

## Wiring
- GP0 --- `F13` Push button --- GND
- GP1 --- `F14` Push button --- GND
- GP2 --- `F15` Push button --- GND
- GP3 --- `F16` Push button --- GND
- GP4 --- `F17` Push button --- GND
- GP5 --- `F18` Push button --- GND
- GP6 --- `F19` Push button --- GND
- GP7 --- `F20` Push button --- GND
- GP8 --- `F21` Push button --- GND
- GP9 --- `F22` Push button --- GND
- GP10 --- `F23` Push button --- GND
- GP11 --- `F24` Push button --- GND
- GP28 --- `Ctrl` Switch --- GND
- GP27 --- `Shift` Switch --- GND