import getopt
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
	

def printHeapDetails(server_name):
	domainRuntime()
	cd('/')
	cd('ServerRuntimes/'+server_name+'/JVMRuntime/'+server_name)
	hf = float(get('HeapFreeCurrent'))/1024
	hs = float(get('HeapSizeCurrent'))/1024
	hf = hf/1024
	hs = hs/1024
	heapfreepercent = get('HeapFreePercent')	
	print bcolors.OKGREEN + '\t\tHeap Free Current : ' + `hf` + ' MB' + bcolors.ENDC 
	print bcolors.OKGREEN + '\t\tHeap Size Current : ' + `hs` + ' MB' + bcolors.ENDC
	print bcolors.OKGREEN + '\t\tHeap Free Percent : ' + str(heapfreepercent) + bcolors.ENDC

def garbagecollect(server_name):
	domainRuntime()
        cd('/')
        cd('ServerRuntimes/'+server_name+'/JVMRuntime/'+server_name)
	cmo.runGC()
	
def serverState(server_name):
	print bcolors.WARNING + '==============================================' + bcolors.ENDC
	state(server_name)
	print bcolors.WARNING + '==============================================' + bcolors.ENDC

def connecttoadmin(user,password,adminurl):
	print bcolors.WARNING + '==============================================' + bcolors.ENDC
        connect(user, password, adminurl)
        print bcolors.WARNING + '==============================================' + bcolors.ENDC


def usage():
        print sys.argv[0]+" -u username -p password -n namenode t3://adminurl:port/"
try     :
        opts,args = getopt.getopt(sys.argv[1:],"u:p:n:")
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
	connecttoadmin(user,password,args[0])
	serverState(Servername)	
	#redirect WLST native output to /dev/null
	redirect("/dev/null",'false')	
	
except:
        usage()
        sys.exit(2)


print bcolors.WARNING + '==============================================' + bcolors.ENDC
print bcolors.OKGREEN + Servername  + bcolors.ENDC
print bcolors.OKGREEN + '\t- Status Beforer GC' + bcolors.ENDC
printHeapDetails(Servername)
print '\n '
print bcolors.OKGREEN + '\t- PERFORM GC' + bcolors.ENDC
garbagecollect(Servername)
print '\n '
print bcolors.OKGREEN + '\t- Status After GC' + bcolors.ENDC
printHeapDetails(Servername)
print bcolors.WARNING + '==============================================\n\n' + bcolors.ENDC






disconnect()
exit()
