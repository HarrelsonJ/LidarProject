from homemade_lidar import LIDAR
from stepper_motor import STEPPER
import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)
led.value(1)

print("Initalizing Motor")
motor = STEPPER(17,16,18,19)
print("Initalizing I2C")
i2c = machine.I2C(1, scl=machine.Pin(3), sda=machine.Pin(2))
print("Initalizing Sensors")
lidar = LIDAR(i2c, [6, 7, 8, 9])
motor.enable(True)
#f = open('output.txt', 'w')
#f.write("Timestamp\tAngle 0\t Value 0\tAngle 1\t Value 1\tAngle 2\t Value 2\tAngle 3\t Value 3\n")
print("Timestamp\tAngle 0\t Value 0\tAngle 1\t Value 1\tAngle 2\t Value 2\tAngle 3\t Value 3")
while(True):
    try:
        motor.set_reverse(False)
        motor.turn_and_scan(90, lidar)
        motor.set_reverse(True)
        motor.turn_and_scan(90, lidar)
    except KeyboardInterrupt:
        motor.enable(False)
        led.value(0)
        #f.close()
        print("Keyboard interupt detected. Stopping program")
        break