import getopt

configFileProd='niv-WebLogicConfig.properties'
keyFileProd='niv-WebLogicKey.properties'
configFileSim='sim.config'
keyFileSim='sim.key'
urldict={}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def connecttoadmin(configFileProd,keyFileProd,adminurl):
        print bcolors.WARNING + '==============================================' + bcolors.ENDC
        connect(userConfigFile=configFileProd,userKeyFile=keyFileProd, url=adminurl)
        print bcolors.WARNING + '==============================================' + bcolors.ENDC

def getServerList():
	serverlist=adminHome.getMBeansByType('Server')
	print bcolors.WARNING + '==============================================' + bcolors.ENDC
	for svr in serverlist:
		urldict[svr.getName()]='t3://'+svr.getListenAddress()+':'+str(svr.getListenPort())
		print bcolors.OKGREEN + svr.getName() + ': ' + urldict[svr.getName()]  + bcolors.ENDC	
	print bcolors.WARNING + '==============================================' + bcolors.ENDC	
	disconnect()

def datasourceState():
	for svr,url in urldict.items():
		try:
 			connect(userConfigFile=configFileProd,userKeyFile=keyFileProd, url=url)
		        serverRuntime()
		        dsMBeans = cmo.getJDBCServiceRuntime().getJDBCDataSourceRuntimeMBeans()
		        for ds in dsMBeans:
		                print bcolors.WARNING + '==============================================' + bcolors.ENDC
		                print bcolors.OKGREEN + 'Name : \t '+ svr + ' => ' + ds.getName() + bcolors.ENDC
				if ds.getState() != "Running":
					print bcolors.FAIL + 'Stat : \t ' +ds.getState() + bcolors.ENDC
					try:
						print bcolors.WARNING  + '\ttrying to resume datasource...' + bcolors.ENDC
						ds.resume()
					except:
						dumpStack()
					print bcolors.WARNING  + 'Stat after resume : \t ' +ds.getState() + bcolors.ENDC
				else:
					print bcolors.OKGREEN + 'Stat : \t ' + ds.getState()  + bcolors.ENDC
				try:
					testpool=str(ds.testPool())
		                      	if 'None' != testpool:
						print bcolors.OKGREEN + 'Testing on demand :' + bcolors.ENDC 
					 	print bcolors.WARNING  + '\n' +  testpool + '\n'
					else:
						print bcolors.OKGREEN + 'Testing on demand : Test of ' + ds.getName() + ' on server ' + svr + ' was succesful' + bcolors.ENDC
			        except:
		                        dumpStack()
		                print bcolors.WARNING + '==============================================' + bcolors.ENDC
			#disconnect()
		except:
			try:
				connect(userConfigFile=configFileSim,userKeyFile=keyFileSim, url=url)
				serverRuntime()
				dsMBeans = cmo.getJDBCServiceRuntime().getJDBCDataSourceRuntimeMBeans()
				for ds in dsMBeans:
					print bcolors.WARNING + '==============================================' + bcolors.ENDC
					print bcolors.OKGREEN + 'Name : \t '+ svr + ' => ' +ds.getName() + bcolors.ENDC
					print bcolors.OKGREEN + 'Stat : \t ' +ds.getState() + bcolors.ENDC
					#print bcolors.OKGREEN + 'URL  : \t ' +ds.getURL() + bcolors.ENDC	
					try:
						print bcolors.WARNING  + ds.testPool()
					except:
						dumpStack()
					print bcolors.WARNING + '==============================================' + bcolors.ENDC
			except:
				dumpStack()
				print bcolors.FAIL + "Skipping " + svr + bcolors.ENDC
		continue





def getServerStatus():
	for svr,url in urldict.items():
		try:
        	  	print bcolors.WARNING + '==============================================' + bcolors.ENDC 
			connect(userConfigFile=configFileProd,userKeyFile=keyFileProd, url=url)
	                serverRuntime()
			print '**************************************************\n'
               		print '############  JDBC CONNECTION POOLS  #############'
                	print ' '
                	print 'Name\t\t\t\tMaxcapacity\tActiveCurrent\tActiveHighCount\tWaitSecondsHighCount\tWaitingCurrentCount\tState'
                	print ' '
                	for poolRT in poolrtlist:
                        	pname=poolRT.getName()
                        	pmaxcapacity=poolRT.getAttribute("MaxCapacity")
                        	paccc=poolRT.getAttribute("ActiveConnectionsCurrentCount")
                        	pachc=poolRT.getAttribute("ActiveConnectionsHighCount")
                        	pwshc=poolRT.getAttribute("WaitSecondsHighCount")
                        	pwfccc=poolRT.getAttribute("WaitingForConnectionCurrentCount")
                        	pstate=poolRT.getAttribute("State")
                        	print bcolors.WARNING , pname,'\n\t\t\t\t',pmaxcapacity,'\t\t',paccc,'\t\t',pachc,'\t\t', pwshc,'\t\t\t',pwfccc,'\t\t\t', bcolors.OKGREEN , pstate , bcolors.ENDC
                        	print ' '	
                	disconnect()
		except:
               		dumpStack()	
			print bcolors.FAIL + "Skipping " + svr + bcolors.ENDC
        	continue

def usage():
        print sys.argv[0]+" -n namenode t3://adminurl:port/"
try     :
        opts,args = getopt.getopt(sys.argv[1:],"")
except getopt.GetoptError       :
        #print help information and exit        :
        usage()
        sys.exit(2)
for o, a in opts :
        if o =="-u" :
                user = a
        if o =="-p" :
                password = a
        if o =="-n" :
                Servername = a
if len(args) != 1:
        usage()
        sys.exit(2)
try:
        connecttoadmin(configFileProd,keyFileProd,args[0])
        #redirect WLST native output to /dev/null
        redirect("/dev/null",'false')

except:
        usage()
        sys.exit(2)

getServerList()
datasourceState()
