import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio

# Configuration des broches
pins = [
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,

    board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17,
    board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26,

    board.GP27, board.GP28
]

# Création des objets DigitalInOut pour chaque broche
pins_state = {}
for pin in pins:
    pin_obj = digitalio.DigitalInOut(pin)
    pin_obj.direction = digitalio.Direction.INPUT
    pin_obj.pull = digitalio.Pull.UP
    pins_state[pin] = False

# Création de l'objet Keyboard pour l'envoi des commandes
keyboard = Keyboard(usb_hid.devices)

print("Prêt !!! En attente de l'appui sur une touche...")

while True:
    for pin, state in pins_state.items():
        current_state = not pin.value  # Inversion pour la pull-up resistor
        if current_state != state:  # Le pin a changé d'état
            pins_state[pin] = current_state  # Garde en mémoire le nouvel état du pin
            if current_state:  # Le pin est actuellement activé
                if pin == board.GP0:
                    print("Touche F13 enfoncée")
                    keyboard.press(Keycode.F13)
                elif pin == board.GP1:
                    print("Touche F14 enfoncée")
                    keyboard.press(Keycode.F14)
                # Ajouter d'autres touches ici
            else:  # Le pin est actuellement désactivé
                if pin == board.GP0:
                    print("Touche F13 relâchée")
                    keyboard.release(Keycode.F13)
                elif pin == board.GP1:
                    print("Touche F14 relâchée")
                    keyboard.release(Keycode.F14)
                # Ajouter d'autres touches ici
    time.sleep(0.01)
