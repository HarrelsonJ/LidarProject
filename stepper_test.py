from stepper_motor import STEPPER
import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)
led.value(1)

motor = STEPPER(17,16,18,19)
motor.enable(False)
for i in range(0, 10):
    motor.set_reverse(False)
    motor.turn_to_angle(90)
    utime.sleep_ms(500)
    motor.set_reverse(True)
    motor.turn_to_angle(90)
    utime.sleep(1)

led.value(0)