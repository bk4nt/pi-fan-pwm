#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.

from datetime import datetime
import psutil
from hotspot.common import title_text, right_text

def render(draw, width, height):
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    elapsed = datetime.now() - boot_time
    margin = 3
    title_text(draw, margin, width, "Uptime")
    right_text(draw, 20, width, margin, text="{0} s".format(int(elapsed.total_seconds())))

    if int(elapsed.total_seconds()) > 172800:
        days = str(int(elapsed.total_seconds())/86400) + " days"
    elif int(elapsed.total_seconds()) > 86400:
        days = "1 day"
    else:
        days = None

    if days:
        right_text(draw, 35, width, margin, days)
