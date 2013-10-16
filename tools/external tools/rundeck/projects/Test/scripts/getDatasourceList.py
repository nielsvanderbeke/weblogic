import getopt

def usage():
        print sys.argv[0]+" -u username -p password -d datasourcename t3://adminurl:port/"
try     :
        opts,args = getopt.getopt(sys.argv[1:],"u:p:d:")
except getopt.GetoptError       :
        #print help information and exit        :
        usage()
        sys.exit(2)
for o, a in opts :
        if o =="-u" :
                user = a
        if o =="-p" :
                password = a
        if o =="-d" :
                datasource = a
if len(args) != 1:
        usage()
        sys.exit(2)
try:
        connect(user, password,args[0])
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
