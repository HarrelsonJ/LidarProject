from vl53l1x import VL53L1X
import machine

pin0 = machine.Pin(0, machine.Pin.OUT, machine.Pin.PULL_UP)
pin1 = machine.Pin(1, machine.Pin.OUT, machine.Pin.PULL_UP)
pin2 = machine.Pin(2, machine.Pin.OUT, machine.Pin.PULL_UP)
pin3 = machine.Pin(3, machine.Pin.OUT, machine.Pin.PULL_UP)

# Shutdown pins for vl53l1x active on low
# Bring low to reset all boards

print("Bring xshut pins low")
pin0.value(0)
pin1.value(0)
pin2.value(0)
pin3.value(0)

# Configure the i2c bus
print("Configure the i2c bus")
i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16))

# Enable first device
print("Enable and configure device 0")
pin0.value(1)
machine.lightsleep(10) # Wait for the board to boot
sensor0 = VL53L1X(i2c)

print("Change I2C address for device 0")
sensor0.set_i2c_address(30)


# Enable second device
print("Enable and configure device 1")
pin1.value(1)
machine.lightsleep(10) # Wait for the board to boot
sensor1 = VL53L1X(i2c)

print("Change I2C address for device 1")
sensor1.set_i2c_address(31)

# Enable third device
print("Enable and configure device 2")
pin2.value(1)
machine.lightsleep(10) # Wait for the board to boot
sensor2 = VL53L1X(i2c)

print("Change I2C address for device 2")
sensor2.set_i2c_address(32)


# Enable fourth device
print("Enable and configure device 3")
pin3.value(1)
machine.lightsleep(10) # Wait for the board to boot
sensor3 = VL53L1X(i2c)

print("Change I2C address for device 3")
sensor3.set_i2c_address(33)

print("Begin Loop")
while(True):
    print("Sensor0: " + str(sensor0.read()) + "\n")
    print("Sensor1: " + str(sensor1.read()) + "\n")
    print("Sensor2: " + str(sensor2.read()) + "\n")
    print("Sensor3: " + str(sensor3.read()) + "\n")
    machine.lightsleep(2000)

