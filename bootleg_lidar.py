from homemade_lidar import LIDAR
from stepper_motor import STEPPER
import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)
led.value(1)

motor = STEPPER(17,16,18,19)
i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16))
lidar = LIDAR(i2c, [0, 1, 2, 3])
motor.enable(False)
for i in range(0, 10):
    motor.set_reverse(False)
    motor.turn_and_scan(90, lidar)
    utime.sleep_ms(500)
    motor.set_reverse(True)
    motor.turn_and_scan(90, lidar)
    utime.sleep(1)

motor.enable(False)
led.value(0)