#! /bin/sh

### BEGIN INIT INFO
# Provides:          pi-fan-pwm.carousel.py
# Required-Start:
# Required-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting pi-fan-pwm/carousel.py"
    pkill -f /usr/local/bin/pi-fan-pwm/carousel.py
    /usr/local/bin/pi-fan-pwm/carousel.py --spi-port 0 --spi-device 0 --display sh1106 --interface spi &
    ;;
  stop)
    echo "Stopping pi-fan-pwm.py"
    pkill -f /usr/local/bin/pi-fan-pwm/carousel.py
    ;;
  *)
    echo "Usage: /etc/init.d/pi-fan-pwm.carousel.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
