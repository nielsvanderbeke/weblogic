#!/bin/bash
set -x
set
numargs=$#
if [ $numargs -lt 2 ]; then
  echo usage: $0 scripturl scriptargs
  exit 2
fi
scripturl="$1"
RD_SCRIPTS=/export/home/weblogic/pp/rundeck/projects/Test/scripts
TMP_SCRIPT=$(mktemp -p /var/tmp) 

/usr/sfw/bin/wget -O "$TMP_SCRIPT" "$scripturl"
/opt/oracle/fmw/fmw11gR1PS2/wlserver_10.3/common/bin/wlst.sh $TMP_SCRIPT ${@:2:$numargs}
