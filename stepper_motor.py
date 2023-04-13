from machine import Pin
import machine
import utime

degrees_per_step = 360 / 800 # Degrees / step

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
        utime.sleep_ms(delay)
        self.pulse.value(0)
        utime.sleep_ms(delay)
        self.angle += degrees_per_step
        return self.angle
    
    def turn_to_angle(self, angle):
        self.enable(True)
        num_steps = int(angle / degrees_per_step)
        stepper_profile = self.generate_stepper_profile(num_steps, 50, 2, 5, 2)
        for i in range(0, num_steps):
            self.step(stepper_profile[i])
        self.enable(False)

    def generate_stepper_profile(self, num_steps, max, min, max_step_accel, min_step_accel):
        stepper_profile = [min] * num_steps
        i, j = max, 0
        while(i > min):
            stepper_profile[j] = i
            stepper_profile[num_steps - 1 - j] = i
            i -= max_step_accel
        return stepper_profile


motor = STEPPER(17,16,18,19)
motor.enable(False)
for i in range(0, 10):
    motor.set_reverse(False)
    motor.turn_to_angle(90)
    utime.sleep_ms(500)
    motor.set_reverse(True)
    motor.turn_to_angle(90)
    utime.sleep(1)