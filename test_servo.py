import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.OUT)
pwm=GPIO.PWM(10, 50)
pwm.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(10, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(10, False)
    pwm.ChangeDutyCycle(0)
    
SetAngle(100)
sleep(2)
SetAngle(0)
sleep(2)
pwm.stop()
GPIO.cleanup()