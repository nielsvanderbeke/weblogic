#!/bin/sh
PATH=$PATH:/opt/smals/bin
#wls_nodes='Odysseus_BE_1 Odysseus_BE_2'
wls_nodes="$*"
for node in $wls_nodes; do
  echo $node
  if [ -f "/bea/user_projects/domains/odysseusdomain/servers/$node/data/nodemanager/$node.pid" ]
  then
    filename=/var/tmp/$node-`date +%Y%m%d%H%M%S`.jfr
    pid=`cat /bea/user_projects/domains/odysseusdomain//servers/$node/data/nodemanager/$node.pid`
    echo $pid
    cd /bea/user_projects/tools
    sudo -u weblogic ./WLoperation jrcmd $pid dump_flightrecording recording=0 copy_to_file=$filename
  fi
done
