from machine import Pin
from homemade_lidar import LIDAR
import utime

degrees_per_step = 1.8 / 4# Degrees / step

class STEPPER:
    def __init__(self, step_pin, dir_pin, sleep_pin, config_pin):
        self.pulse = Pin(step_pin, Pin.OUT, Pin.PULL_UP)
        self.dir = Pin(dir_pin, Pin.OUT, Pin.PULL_UP)
        self.sleep = Pin(sleep_pin, Pin.OUT, Pin.PULL_UP)
        self.config = Pin(config_pin, Pin.OUT, Pin.PULL_UP)
        self.set_reverse(False)
        self.config.value(1)
        self.angle = 0.0
        return
    
    def enable(self, is_enable = True):
        self.sleep.value(1 if is_enable else 0)
    
    def set_reverse(self, is_reverse = True):
        self.dir.value(1 if is_reverse else 0)

    def is_reversed(self):
        return self.dir.value()
    
    def step(self, delay):
        self.pulse.value(1)
        utime.sleep_ms(delay // 2)
        self.pulse.value(0)
        utime.sleep_ms(delay // 2)
        self.angle = self.angle - degrees_per_step if self.dir.value() == 1 else self.angle + degrees_per_step
        self.angle += degrees_per_step
        return self.angle
    
    def turn_to_angle(self, angle):
        self.enable(True)
        num_steps = int(angle / degrees_per_step)
        # stepper_profile = self.generate_stepper_profile(num_steps, 10, 2, 3)
        stepper_profile = [2] * num_steps
        stepper_profile[0] = 10
        stepper_profile[num_steps - 1] = 10
        stepper_profile[1] = 6
        stepper_profile[num_steps - 2] = 6
        stepper_profile[2] = 4
        stepper_profile[num_steps - 3] = 4
        for i in range(0, num_steps):
            self.step(stepper_profile[i])
        self.enable(False)

    def turn_and_scan(self, angle, lidar:LIDAR): #lidar is type LIDAR
        #self.enable(True)
        num_steps = int(angle / degrees_per_step)
        # stepper_profile = self.generate_stepper_profile(num_steps, 10, 2, 3)
        stepper_profile = [2] * num_steps
        stepper_profile[0] = 10
        stepper_profile[num_steps - 1] = 10
        stepper_profile[1] = 6
        stepper_profile[num_steps - 2] = 6
        stepper_profile[2] = 4
        stepper_profile[num_steps - 3] = 4
        for i in range(0, num_steps):
            if i % 10 == 0:
                sample = lidar.read(self.angle)
                print("timestamp: {}\t{} {}\t{} {}\t{} {}\t{} {}\n".format(sample.time, sample.scans[0][0], sample.scans[0][1],
                                                                                        sample.scans[1][0], sample.scans[1][1],
                                                                                        sample.scans[2][0], sample.scans[2][1],
                                                                                        sample.scans[3][0], sample.scans[3][1]))
            self.step(stepper_profile[i])
        #self.enable(False)

    def generate_stepper_profile(self, num_steps, max, min, step_accel):
        stepper_profile = [min] * num_steps
        delay, index, sub_index = max, 0, 0
        while(True):
            stepper_profile[index] = delay
            stepper_profile[num_steps - 1 - index] = delay

            if delay <= min:
                break
            if(index == num_steps - 1 - index):
                break

            if(sub_index >= 2):
                if (delay - step_accel < min):
                    delay = min
                else:
                    delay = delay - step_accel
                sub_index = 0

            index += 1
            sub_index += 1
        output = ""
        for i in range(0, num_steps):
            output += str(stepper_profile[i]) + ", "
        print(output)
        return stepper_profile