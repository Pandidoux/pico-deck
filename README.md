# Pico Deck

## Introduction

Use a Raspberry pi Pico to make your own usb macro keyboard.

Use CircuitPython and adafruit's libraries.

## Feature
- Full anti-ghosting
- Use F13 to F24 virtual keyboard keys
- Up to 12 physical buttons

### Todo
- Two physical switches (on/off) to switch between 4 profils (F#, Ctrl+F#, Shift+F#, Ctrl+Shift+F#)

## Install on your Pico

- Clone or download this repostory.
#### Flash CircuitPython `firmware`
- On your Pico, press BOOTSEL button while plugin to your computer via USB
- Drag and drop the [latest CircuitPython](https://circuitpython.org/downloads) firmware file (.uf2) on your pico storage, it will reboot.
#### Install `code`
- Plug your Pico to your computer (do not press BOOTSEL)
- Drag and drop the new `code.py` on your Pico.
- Drag and drop the library folder `lib` on your Pico.
