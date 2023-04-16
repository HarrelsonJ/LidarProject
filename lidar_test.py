from homemade_lidar import LIDAR
import machine

i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16))

lidar = LIDAR(i2c, [], [])