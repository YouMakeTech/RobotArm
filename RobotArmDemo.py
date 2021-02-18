from RobotArm import *

robot = RobotArm()

while True:
    robot.goto(90,90,90)
    robot.openHand()

    robot.openGate()
    robot.closeGate()
  
    robot.goto(117,120,30)
    robot.goto(117,130,30)
    robot.goto(117,131,37)
    robot.goto(117,132,37)
    robot.closeHand()

    robot.goto(117,130,39)
    robot.goto(117,130,50)
    robot.goto(73,90,130)
    robot.goto(73,135,130)
    robot.openHand()
   
