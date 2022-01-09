speed = 0.7 #Set ROBOT Speed
import time
def moveforward(x):

    from gpiozero import Robot
    from time import sleep

    robot = Robot(left=(4,18), right=(23,17))
    for i in range(x):
        robot.forward(speed)
        sleep(1)

def movebackward(x):

    from gpiozero import Robot
    from time import sleep

    robot = Robot(left=(4,18), right=(23,17))
    for i in range(x):
        robot.backward(speed)
        sleep(1)

def moveleftward(x):

    from gpiozero import Robot
    from time import sleep

    robot = Robot(left=(4,18), right=(23,17))

    for i in range(x):
        robot.left(1)
        sleep(1)

def moverightward(x):

    from gpiozero import Robot
    from time import sleep

    robot = Robot(left=(4,18), right=(23,17))
    for i in range(x):
        robot.right(1)
        sleep(1)

def scan():
    moveleftward(4)
    moverightward(4)
    moverightward(4)
    moveleftward(3)

def nudgeno():
    from gpiozero import Robot
    from time import sleep
    robot = Robot(left=(4,18), right=(23,17))
    robot.left(1)
    sleep(0.2)
    robot.right(1)
    sleep(0.3)
  
def nudgeyes():
    from gpiozero import Robot
    from time import sleep
    robot = Robot(left=(4,18), right=(23,17))
    robot.forward(0.5)
    sleep(0.2)
    robot.backward(0.5)
    sleep(0.3)    

#nudgeno()
#nudgeyes()
#moveforward(2)
