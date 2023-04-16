from vl53l1x import VL53L1X
from laser_scan import SCAN
import machine
import utime


class LIDAR:
    def __init__(self, i2c:machine.I2C, shut_pins:list[int], angle_offsets = [0, 90, 180, 270]) -> None:
        # Store the i2c bus
        self.i2c = i2c
        self.start_time = utime.time()
        self.shut_pins = []
        for shut_pin in shut_pins:
            self.shut_pins.append(machine.Pin(shut_pin, machine.Pin.OUT, machine.Pin.PULL_UP))

        self.sensors = []
        self.offsets = angle_offsets

        # Shutdown pins for vl53l1x active on low
        # Bring low to reset all boards

        print("Bring xshut pins low")
        for shut_pin in self.shut_pins:
            shut_pin.value(0)

        for index, shut_pin in enumerate(self.shut_pins):
            print("Enable and configure device " + str(index))
            shut_pin.value(1) # Bring the xshut pin high
            machine.lightsleep(100) # Wait for the board to boot
            self.sensors.append(VL53L1X(i2c))
            self.sensors[index].set_i2c_address(30 + index)


    def read(self, angle:float) -> SCAN:
        time = utime.time() - self.start_time
        data = []
        for index, sensor in enumerate(self.sensors):
            data.append([(self.offsets[index] + angle) % 360, sensor.read()]) # Add in angle data from stepper
        return SCAN(time, *data)
