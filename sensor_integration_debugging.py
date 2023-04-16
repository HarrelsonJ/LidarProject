from vl53l1x import VL53L1X
import machine
import utime

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
xshut = machine.Pin(2, machine.Pin.OUT)

xshut.value(0)

machine.lightsleep(500)

xshut.value(1)

machine.lightsleep(500)

sensor = VL53L1X(i2c)

print("Default Address " + str(sensor.read_i2c_address()))
sensor.set_i2c_address(15)
print("New Address " + str(sensor.read_i2c_address()))

print(str(sensor.read()))