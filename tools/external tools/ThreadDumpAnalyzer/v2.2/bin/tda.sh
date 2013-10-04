#!/bin/sh
# Unix shell script for starting tda. If you have big log files
# you might need to adjzst Xmx setting.

cd ..; java -Xmx256m -jar ./tda.jar 
