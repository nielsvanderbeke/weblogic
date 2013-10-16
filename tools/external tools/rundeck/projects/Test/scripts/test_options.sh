#!/bin/sh
# Called with adminurl adminuser adminpass
RD_SCRIPTS=/export/home/weblogic/pp/rundeck/projects/Test/scripts
. /opt/oracle/fmw/fmw11gR1PS2/wlserver_10.3/server/bin/setWLSEnv.sh
java weblogic.Admin -adminurl $1 -userconfigfile $RD_SCRIPTS/acc-userconfig.properties -userkeyfile $RD_SCRIPTS/acc-userkey.properties LIST
