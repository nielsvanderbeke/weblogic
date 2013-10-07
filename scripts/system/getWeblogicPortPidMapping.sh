#!/bin/ksh 
 
pids=$(/usr/bin/ps -ef -o pid=)
 
if [ $# -eq 0 ]; then 
   read wlport?"Enter port you would like to know Java Process Id for: " 
else 
   wlport=$1 
fi 
 
for f in $pids 
do 
   /usr/proc/bin/pfiles $f 2>/dev/null | /usr/xpg4/bin/grep -q "port: $wlport$" 
   if [ $? -eq 0 ]; then 
        echo "===============***=============***==============="
        echo "ListenPort: $wlport is being used by Java PID:\c" 
        ps -ef -o pid -o args | egrep -v "grep|pfiles" | grep $f 
        exit 0 # if you suspect more Weblogic instances with same listen port remove this
   fi 
done