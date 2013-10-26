import getopt

configFileProd='niv-WebLogicConfig.properties'
keyFileProd='niv-WebLogicKey.properties'
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
	#print bcolors.WARNING + '==============================================' + bcolors.ENDC
	for svr in serverlist:
		urldict[svr.getName()]='t3://'+svr.getListenAddress()+':'+str(svr.getListenPort())
		#print bcolors.OKGREEN + svr.getName() + ': ' + urldict[svr.getName()]  + bcolors.ENDC	
	#print bcolors.WARNING + '==============================================' + bcolors.ENDC	
	disconnect()

def getServerStatus():
	for svr,url in urldict.items():
		try:
        	  	print bcolors.WARNING + '==============================================' + bcolors.ENDC 
			connect(userConfigFile=configFileProd,userKeyFile=keyFileProd, url=url)
	                serverRuntime()
			print bcolors.OKBLUE + svr + bcolors.ENDC
			print bcolors.OKGREEN + '\tServer State          ' , get("State") + bcolors.ENDC
			print bcolors.OKGREEN + '\tServer ListenAddress  ' , get("ListenAddress") + bcolors.ENDC
			print bcolors.OKGREEN , '\tServer ListenPort     ' , get("ListenPort") , bcolors.ENDC
			print bcolors.OKGREEN , '\tServer Health State   ' , get("HealthState") , bcolors.ENDC
                	disconnect()
		except:
               		dumpStack()	
			print bcolors.FAIL + "Skipping " + svr + bcolors.ENDC
        	continue

def usage():
        print sys.argv[0]+" -n namenode t3://adminurl:port/"
try     :
        opts,args = getopt.getopt(sys.argv[1:],"n:")
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
getServerStatus()
