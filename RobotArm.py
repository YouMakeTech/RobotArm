import pyfirmata
import time

class RobotArm(object):
    theta0 = 90.0; 
    theta1 = 90.0;
    theta2 = 90.0;
    theta3 = 0.0;
 
    board = None
    servo0 = None
    servo1 = None
    servo2 = None
    servo3 = None
    servo4 = None


    def __init__(self):
        print("in __init__")
        self.board = pyfirmata.Arduino('/dev/ttyACM0')

        self.board.servo_config(3, angle = self.theta0)
        self.servo0 = self.board.get_pin('d:3:s')
        self.servo0.write(self.theta0)

        self.board.servo_config(5, angle = self.theta1)
        self.servo1 = self.board.get_pin('d:5:s')
        self.servo1.write(self.theta1)

        self.board.servo_config(6, angle = self.theta2)
        self.servo2 = self.board.get_pin('d:6:s')
        self.servo2.write(self.theta2)

        self.board.servo_config(9, angle = self.theta3)
        self.servo3 = self.board.get_pin('d:9:s')
        self.servo3.write(self.theta3)

        self.board.servo_config(10, angle = 90.0)
        self.servo4 = self.board.get_pin('d:10:s')
        self.servo4.write(90.0)

    def __del__(self):
        print("in __del__")
        self.goto(90, 90 ,90)
        self.closeHand()
        self.closeGate()
        self.board.exit()


    def set0(self, theta0_desired):
        theta0_desired = max(theta0_desired, 0.0)
        theta0_desired = min(theta0_desired, 180.0)
        while abs(self.theta0-theta0_desired)>0.1:
            if self.theta0 <= theta0_desired:
                self.theta0 = self.theta0 + 1.0
            elif self.theta0 > theta0_desired:
                self.theta0 = self.theta0 - 1.0

            self.servo0.write(self.theta0)
            time.sleep(0.015)
        print(str(self.theta0) + "," + str(self.theta1) + "," + str(self.theta2))

    def set1(self, theta1_desired):
        theta1_desired = max(theta1_desired, 0.0)
        theta1_desired = min(theta1_desired, 180.0)
        while abs(self.theta1-theta1_desired)>0.1:
            if self.theta1 <= theta1_desired:
                self.theta1 = self.theta1 + 1.0
            elif self.theta1 > theta1_desired:
                self.theta1 = self.theta1 - 1.0

            self.servo1.write(self.theta1)
            time.sleep(0.015)
        print(str(self.theta0) + "," + str(self.theta1) + "," + str(self.theta2))

        
    def set2(self, theta2_desired):
        theta2_desired = max(theta2_desired, 0.0)
        theta2_desired = min(theta2_desired, 180.0)
        while abs(self.theta2-theta2_desired)>0.1:
            if self.theta2 <= theta2_desired:
                self.theta2 = self.theta2 + 1.0
            elif self.theta2 > theta2_desired:
                self.theta2 = self.theta2 - 1.0

            self.servo2.write(self.theta2)
            time.sleep(0.015)
        print(str(self.theta0) + "," + str(self.theta1) + "," + str(self.theta2))

    def set3(self, theta3_desired):
        theta3_desired = max(theta3_desired, 0.0)
        theta3_desired = min(theta3_desired, 90.0)
        while abs(self.theta3-theta3_desired)>0.1:
            if self.theta3 <= theta3_desired:
                self.theta3 = self.theta3 + 1.0
            elif self.theta3 > theta3_desired:
                self.theta3 = self.theta3 - 1.0

            self.servo3.write(self.theta3)
            time.sleep(0.015)
            
    def goto(self, theta0_desired, theta1_desired, theta2_desired):
        self.set0(theta0_desired)
        self.set1(theta1_desired)
        self.set2(theta2_desired)

        print(str(self.theta0) + "," + str(self.theta1) + "," + str(self.theta2))
        time.sleep(0.2)

    def openHand(self):
        self.set3(30.0)
        
    def closeHand(self):
        self.set3(0)
                
    def openGate(self):
        self.servo4.write(0)
        time.sleep(0.500)
    
    def closeGate(self):
        self.servo4.write(90)
  
