from pynput.keyboard import Key,Controller
import time

keyboard = Controller()

while True:
    for i in range(10):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        time.sleep(0.1)
    time.sleep(2) 