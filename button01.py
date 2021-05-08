from gpiozero import Button
from time import sleep

button = Button(27)

while True:
    if button.is_pressed:
        print("pressed")
    sleep(1)
        