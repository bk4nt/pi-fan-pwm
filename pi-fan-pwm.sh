#! /bin/sh

### BEGIN INIT INFO
# Provides:          pi-fan-pwm.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     1 2 3 4 5
# Default-Stop:      0 6
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting pi-fan-pwm.py"
    /usr/local/bin/pi-fan-pwm.py &
    ;;
  stop)
    echo "Stopping pi-fan-pwm.py"
    pkill -f /usr/local/bin/pi-fan-pwm.py
    ;;
  *)
    echo "Usage: /etc/init.d/pi-fan-pwm.sh {start|stop}"
    exit 1
    ;;
esac

exit 0
