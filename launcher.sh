#!/bin/bash
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /root/fanControl
PID=$(ps -ef |grep fan_control.py |grep -v grep |grep sudo |awk '{print $2}');
if [ "$PID" == "" ]; then 
   sudo python fan_control.py &
   echo $! > ./fan_control.pid
else
   echo "fan_control is running"
fi

exit 0
