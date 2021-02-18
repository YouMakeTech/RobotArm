import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')
servo = board.get_pin('d:9:s')

servo.write(0.0)
time.sleep(1)
servo.write(90.0)
time.sleep(1)
servo.write(180.0)
time.sleep(1)
servo.write(90.0)
time.sleep(1)

board.exit()
