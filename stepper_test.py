import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)
dir = machine.Pin(16, machine.Pin.OUT, machine.Pin.PULL_UP)
step = machine.Pin(17, machine.Pin.OUT, machine.Pin.PULL_UP)
sleep = machine.Pin(18, machine.Pin.OUT, machine.Pin.PULL_UP)
config = machine.Pin(19, machine.Pin.OUT, machine.Pin.PULL_UP)

led.value(1)

dir.value(0)
step.value(0)
sleep.value(0)
config.value(0)

# Turn on motor
sleep.value(1)

# Set config mode
config.value(1)

# Pulse stepper
for i in range(0,1000):
    step.value(1)
    utime.sleep_ms(2)
    step.value(0)

led.value(0)