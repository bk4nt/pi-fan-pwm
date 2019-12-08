#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import signal
import sys

FAN_PWM    = 18    # PWM input pin
FAN_TACH   = 23    # Fan's tachometer output pin
FAN_PULSES = 2     # Noctua fans puts out two pluses per revolution
FAN_FREQ   = 100   # Shall be 25kHz. See README.md

def signal_handler(sig, frame):
        tFile.close()
        fan.ChangeDutyCycle(100) # Fan at full speed on exit
        GPIO.cleanup()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
fan = GPIO.PWM(FAN_PWM, FAN_FREQ)
fan.start(100) # Start at full fan speed

GPIO.setup(FAN_TACH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
t = time.time()
pulses = 0

# Count pulses on FAN_TACH pin
def fell(n):
    global t
    global pulses
    if time.time() - t > 0.005: # Eliminate any spurious pulses
        pulses += 1
        t = time.time()

GPIO.add_event_detect(FAN_TACH, GPIO.FALLING, fell)

dc = 0

while True:
        time.sleep(1)

        rpm = pulses * 60 / FAN_PULSES
        pulses = 0

        outFile = open('/run/pi-fan-pwm.out', 'w')
        outFile.write(str(dc) + " " + str(rpm))
        outFile.close

# Uncomment for tests before install
#       fFile = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq')
#       freq = long(fFile.read()) / 1000
#       fFile.close()
#       print str(tempC) + "C " + str(dc) + "% " + str(freq) + "kHz " + str(rpm) + "RPM"

        tFile = open('/sys/class/thermal/thermal_zone0/temp')
        temp = float(tFile.read())
        tFile.close()
        tempC = temp/1000

        # Depending on heatsinks:
        # 3.182: FAN at 100% for CPU at 60C
        # 4.118: FAN at 100% for CPU at 55C
        # Tweak here minimal dc (PWM Duty Cycle), temp threshold and ratio
        dc = 30 + max(0, int((tempC - 38) * 4.118))
        dc = min(dc, 100)
        fan.ChangeDutyCycle(dc)


