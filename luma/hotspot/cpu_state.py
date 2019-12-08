#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.

import time, os, stat

from hotspot.common import title_text, right_text, tiny_font

def fanOut():
    if os.path.isfile('/run/pi-fan-pwm.out'):
        f = open('/run/pi-fan-pwm.out', 'r')
        elapsed = time.time() - os.stat('/run/pi-fan-pwm.out')[stat.ST_MTIME]
        if elapsed <= 3:
            out = f.read()
        else:
            out = "Err Err"

        f.close()

    try:
        if out is None or not out:
            out = "Err Err"
    except NameError:
        out = "Err Err"

    return out

def render(draw, width, height):
    tFile = open('/sys/class/thermal/thermal_zone0/temp')
    tempC = float(tFile.read()) / 1000
    tFile.close()

    fFile = open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq')
    freqC = long(fFile.read()) / 1000
    fFile.close()

    margin = 3
    title_text(draw, margin, width, "CPU status")
    draw.text((margin, 20), text="Temp:", font=tiny_font, fill="white")
    draw.text((margin, 30), text="Freq:", font=tiny_font, fill="white")
    draw.text((margin, 40), text="Fan:", font=tiny_font, fill="white")
    draw.text((margin, 50), text="RPM:", font=tiny_font, fill="white")

    right_text(draw, 20, width, margin, text="{0:0.1f}C".format(tempC))
    right_text(draw, 30, width, margin, text="{0}k".format(int(freqC)))
    fan = fanOut()
    fanDC,fanRPM = fan.split(" ")
    if "Err" not in fanDC:
        fanDC += "%"
    right_text(draw, 40, width, margin, fanDC)
    right_text(draw, 50, width, margin, fanRPM)
