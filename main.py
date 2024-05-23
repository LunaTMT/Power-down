from gpiozero import Button, PWMLED
from subprocess import check_call
from signal import pause
from time import sleep
from threading import Timer

flash_count = 0

def flash():
    global flash_count
    
    led.toggle()
    sleep(0.5)
    led.toggle()
    sleep(0.5)
    flash_count += 1

    if flash_count == 3:
        shutdown()

def reset_flash_count():
    global flash_count  
    flash_count = 0


def shutdown():
    for i in range(10, -1, -1):
        led.value = i / 10
        sleep(0.1)  

    print("shutdown")
    check_call(['sudo', 'poweroff'])

def repeater():
    flash()
    if not button.is_pressed:
        reset_flash_count()  
    else:
        Timer(1, repeater).start()


button = Button(2)
led = PWMLED(17)
button.when_pressed = repeater
pause()
    


