import RPi.GPIO as GPIO
from time import sleep

def SetAngle(pin,angle):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    
    pwm=GPIO.PWM(pin, 50)
    pwm.start(0)
    duty = angle / 18 + 2
    
    GPIO.output(pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(pin, False)
    pwm.ChangeDutyCycle(0)
    
    pwm.stop()
    GPIO.cleanup()