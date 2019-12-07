#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.

import time, os, stat

from hotspot.common import title_text, right_text, tiny_font

def pwmDC():
    if os.path.isfile('/run/pi-fan-pwm.dc'):
        f = open('/run/pi-fan-pwm.dc', 'r')
        elapsed = time.time() - os.stat('/run/pi-fan-pwm.dc')[stat.ST_MTIME]
        if elapsed <= 3:
            dc = f.read() + "%"
        else:
            dc = "Err"

        f.close()

    try:
        if dc is None or not dc:
            dc = "Err"
    except NameError:
        dc = "Err"

    return dc

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
    draw.text((margin, 35), text="Freq:", font=tiny_font, fill="white")
    draw.text((margin, 45), text="Fan DC:", font=tiny_font, fill="white")

    right_text(draw, 20, width, margin, text="{0:0.1f}C".format(tempC))
    right_text(draw, 35, width, margin, text="{0}k".format(int(freqC)))
    right_text(draw, 45, width, margin, text="{0}".format(pwmDC()))
