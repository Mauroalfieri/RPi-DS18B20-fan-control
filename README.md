# Raspberry Pi DS18B20 fan control by Python
Control a fan by DS18B20 temperature sensor and Python

## BOM 
List of components for RPi DS18B20 fan control

*  RPi ( Model 1 A,A+,B,B+ or Model 2 B or Model 3 B )
*  DS18B20 temperature sensor
*  Fan model 40mm 12v 600mAh
*  1Kohm resistor
*  220 ohm resistor
*  BC337 transistor
*  1n4148 diode
*  12v DC power
 
## Electronic schema
How to connect the components to RPi

![N|Solid](https://github.com/Mauroalfieri/RPi-DS18B20-fan-control/blob/master/images/RPi%20fan%20control%20python%20schema.jpg?raw=true)

## Usage
Add to /boot/config.txt the line:

```
dtoverlay=w1-gpio
```
Reboot.

Load the module for DS18B20

```
modprobe w1-gpio
modprobe w1-therm
```

Check if in the path /sys/bus/w1/devices/ is present a new devices "28-....."

Add to root crontab the line:

```
@reboot /path_fan_control/launcher.sh > /path_fan_control/launcher.log 2>&1
