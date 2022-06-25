#!/bin/bash
sudo -E sh -c 'echo 0 > /sys/class/backlight/rpi_backlight/bl_power'

#We don't need it on this project, but you can also define a power off:
#sudo -E sh -c 'echo 1 > /sys/class/backlight/rpi_backlight/bl_power'
