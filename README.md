# pi-fan-pwm

Scripts used to run a PWM fan according to Raspberry CPU temperature.

Tested with Noctua NF-A4x10 5V PWM and Raspberry Pi 4.

## Installation

1. Clone down this repo to your Raspberry Pi
2. Connect fan +5V/GND to the Raspberry, fan will run at max speed
3. Connect fan PWM pin to GPIO 18
4. Run and tweak duty cycles plus temperature thresholds in `pi-fan-pwm.py`
4. Use `stress-ng --cpu 4` plus `watch tools/temp.sh` to monitor your CPU temperature
5. Run `script/install`

That's it!
