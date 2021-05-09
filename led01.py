from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    print("on")
    led.on()
    sleep(2)
    print("off")
    led.off()
    sleep(2)
