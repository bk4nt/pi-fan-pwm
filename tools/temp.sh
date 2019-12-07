#!/bin/bash
cpuTemp0=$(cat /sys/class/thermal/thermal_zone0/temp)
cpuTemp1=$(($cpuTemp0/1000))
cpuTemp2=$(($cpuTemp0%1000/100))

cpuSpeed0=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq)
cpuSpeed1=$((cpuSpeed0/1000))

pwmDC=$(cat /run/pi-fan-pwm.dc)
echo "CPU temp=${cpuTemp1}.${cpuTemp2}'C freq=${cpuSpeed1}kHz"
echo "Fan duty cycle=${pwmDC}"
