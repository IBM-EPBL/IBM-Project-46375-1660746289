from gpiozero import Button, TrafficLights, Buzzer
from time import sleep
lights = TrafficLights(25, 8, 7)
while True:
    button.wait_for_press()
    lights.on()
    button.wait_for_release()
    lights.off()
buzzer = Buzzer(15)
while True:
    lights.blink()
    buzzer.beep()
    button.wait_for_press()
    lights.off()
    buzzer.off()
    button.wait_for_release()
while True:
    button.wait_for_press()
    lights.green.on()
    sleep(1)
    lights.amber.on()
    sleep(1)
    lights.red.on()
    sleep(1)
    lights.off()
