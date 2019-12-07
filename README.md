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

## Adding luma.oled display scripts

Add a 128x64 OLED display to the Pi SPI port and install luma. See https://github.com/rm-hull/luma.oled

Once the repo cloned, run its carousel.py script (example with the SH1106 driver):
python ./luma/carousel.py --spi-port 0 --spi-device 0  --display sh1106 --interface spi

pi-fan-pwm.py updates /run/pi-fan-pwm.dc with the fan duty cycle. Data is read and displayed by cpu_state widget.

luma/carousel.py was adapted from https://github.com/rm-hull/luma.examples carousel.py script.
