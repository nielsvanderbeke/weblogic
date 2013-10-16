#!/bin/bash
set -x
set

expandScript() {
	if [ -z "$1" ]                           # Is parameter #1 zero length?
		then
			echo "-Parameter #1 is zero length.-"  # Or no parameter passed.
		else
     cat <<_HERE_ >$1
import getopt

def usage():
        print sys.argv[0]+" userconfigfile userkeyfile  t3://adminurl:port"
try     :
        opts,args = getopt.getopt(sys.argv[1:],"u:p:d:")
except getopt.GetoptError       :
        #print help information and exit        :
        usage()
        sys.exit(2)
if len(sys.argv) != 4:
        usage()
        sys.exit(2)
try:
        connect(userConfigFile=sys.argv[1],userKeyFile=sys.argv[2],url=sys.argv[3])
except:
        usage()
        sys.exit(2)
#easeSyntax()

cd('Deployments')


lijst_datasource = []
lijst_datasouces_raw = ls()
lijst_datasouces_raw_split = lijst_datasouces_raw.split("\ndr--   ")
for datasource in lijst_datasouces_raw_split:
        if datasource != '':
                datasource = datasource.strip()
                if datasource.find("datasource") > 0:
                        cd(datasource)
                        type = cmo.getType()
                        if type == 'JDBCConnectionPool':
                                lijst_datasource.append(datasource)
                        cd('..')
print lijst_datasource
type = cmo.getType()
#goto = 'JDBCSystemResources/' + datasource + '/JDBCResource/' + datasource + '/JDBCDriverParams/' + datasource
#cd(goto)
#ls()

for datasource in lijst_datasource:
        cd(datasource)
        datasource_url = get('URL')
        datasource_Properties = get('Properties')
        datasource_InitialCapacity = get('InitialCapacity')
        datasource_MaxCapacity = get('MaxCapacity')
        datasource_DriverName = get('DriverName')
        datasource_TestConnectionsOnReserve = get('TestConnectionsOnReserve')
        datasource_Password = get('Password')

        print '=============================================='
        print datasource
        print '\tURL : ' + datasource_url
        print '\tDriverName : ' + datasource_DriverName
        print '\tProperties : ' + str(datasource_Properties)
        print '\tpasswoord : ' + datasource_Password
        print '\tInitalCapacity : ' + str(datasource_InitialCapacity)
        print '\tMaxCapacity : ' + str(datasource_MaxCapacity)
        print '\tTestConnectionsOnReserve : ' +str(datasource_TestConnectionsOnReserve)
        print '==============================================\n\n'
        cd('..')
_HERE_
		fi
}


numargs=$#
if [ $numargs -lt 1 ]; then
  echo usage: $0 scriptargs
  exit 2
fi
TMP_SCRIPT=$(mktemp -t embedded.XXXXX)
expandScript $TMP_SCRIPT
/opt/oracle/fmw/fmw11gR1PS2/wlserver_10.3/common/bin/wlst.sh $TMP_SCRIPT ${@:1:$numargs}
RET=$?
if [ $RET -eq 0 ]; then
  /bin/rm $TMP_SCRIPT # clean up
  exit $RET
fi
exit $RET