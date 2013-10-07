FileName: wlsPid.sh
# This script will Fetches PID of WebLogic Server instances
# =========================================================
 clear
 echo "PID associated with WebLogic instances"
 echo  "====================================="
 /usr/ucb/ps -awwx | grep "weblogic.Name" | grep -v "grep weblogic.Name" | nawk 'BEGIN {} ;
{
NUM = match($0, "weblogic.Name=") ;
START_POS  = RSTART+RLENGTH ;
START_STR = substr($0, START_POS) ;  
FINISH = match(START_STR, " ") ;
FINISH_POS = START_POS+RSTART+RLENGTH ;  
FINISH_STR = substr($0, START_POS, FINISH_POS) ;
NUM = split(FINISH_STR,FINISH_ARRAY) ;
printf ("%s\t%s\n",FINISH_ARRAY[1], $1) ;
}
END {}'