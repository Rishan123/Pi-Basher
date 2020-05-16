from gpiozero import Robot
from time import sleep

speed = 0.4
motors = Robot(right=(3,4),left=(2,14))

motors.forward(speed=speed)
sleep(1)
motors.left(speed=speed)
sleep(1)
motors.right(speed=speed)
sleep(1)
motors.backward(speed=speed)
sleep(1)
motors.stop()