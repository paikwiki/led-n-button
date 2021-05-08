from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(27)
ledState = 0

while True:
    if button.is_pressed:
        if ledState == 0:
            ledState = 1
            led.on()
        else:
            ledState = 0
            led.off()
        sleep(0.8)
