#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import signal
import sys

# Used for tests before install
def signal_handler(sig, frame):
        tFile.close()
        fFile.close()
        GPIO.cleanup()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
fan = GPIO.PWM(18, 25000) #I also tried frequecies of 2 and 2000
fan.start(100)

while True:
        tFile = open('/sys/class/thermal/thermal_zone0/temp')
        temp = float(tFile.read())
        tFile.close()
        tempC = temp/1000
        fFile = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq')
        freq = long(fFile.read()) / 1000
        fFile.close()

        # Depending on heatsinks:
        # 3.182: FAN at 100% for CPU at 60C
        # 4.118: FAN at 100% for CPU at 55C
        # Tweak here minimal dc (PWM Duty Cycle), temp threshold and ratio
        dc = 30 + max(0, int((tempC - 38) * 4.118))
        dc = min(dc, 100)

        # Uncomment for tests before install
        #print str(tempC) + "C " + str(dc) + "% " + str(freq) + "kHz"

        fan.ChangeDutyCycle(dc)
        time.sleep(1)
