import getopt

configFileProd='/bea/user_projects/tools/carto/prd.config'
keyFileProd='/bea/user_projects/tools/carto/prd.key'
configFileAcc='/bea/user_projects/tools/carto/acc.config'
keyFileAcc='/bea/user_projects/tools/carto/acc.key'
configFileSim='/bea/user_projects/tools/carto/sim.config'
keyFileSim='/bea/user_projects/tools/carto/sim.key'
urldict={}

def connecttoadmin(configFile,keyFile,adminurl):
        print '=============================================='
	print 'connect to ' + adminurl
        connect(userConfigFile=configFile,userKeyFile=keyFile, url=adminurl)
        print '=============================================='

def getServerList():
        serverlist=adminHome.getMBeansByType('Server')
        print '=============================================='
        for svr in serverlist:
                urldict[svr.getName()]='t3://'+svr.getListenAddress()+':'+str(svr.getListenPort())
                print svr.getName() + ': ' + urldict[svr.getName()]
        print '=============================================='
        disconnect()

def getdatasourceInfo(configFile,keyFile):
        for svr,url in urldict.items():
                try:
                        connect(userConfigFile=configFile,userKeyFile=keyFile, url=url)
                        serverRuntime()
                        dsMBeans = cmo.getJDBCServiceRuntime().getJDBCDataSourceRuntimeMBeans()
                        for ds in dsMBeans:
#                               print '=============================================='
#                               print 'Name : \t '+ svr + ' => ' + ds.getName()
#                               print 'Stat before resume : \t ' +ds.getState()
#				print 'ActiveConnectionsAverageCount : \t ' + str(ds.getActiveConnectionsAverageCount())
#				print 'ActiveConnectionsCurrentCount : \t ' + str(ds.getActiveConnectionsCurrentCount())
#				print 'ActiveConnectionsHighCount : \t\t ' + str(ds.getActiveConnectionsHighCount())
#				print 'ConnectionDelayTime : \t\t\t ' + str(ds.getConnectionDelayTime())
#				print 'FailedReserveRequestCount : \t\t ' + str(ds.getFailedReserveRequestCount())
#				print 'FailuresToReconnectCount : \t\t ' + str(ds.getFailuresToReconnectCount())
#				print 'HighestNumAvailable : \t\t\t ' + str(ds.getHighestNumAvailable())
#				print 'HighestNumUnavailable : \t\t ' + str(ds.getHighestNumUnavailable())
#				print 'PrepStmtCacheAccessCount : \t\t ' + str(ds.getPrepStmtCacheAccessCount())
#				print 'PrepStmtCacheAddCount : \t\t ' + str(ds.getPrepStmtCacheAddCount())
#				print 'PrepStmtCacheCurrentSize : \t\t ' + str(ds.getPrepStmtCacheCurrentSize())
#				print 'PrepStmtCacheDeleteCount : \t\t ' + str(ds.getPrepStmtCacheDeleteCount())
#				print 'PrepStmtCacheHitCount : \t\t ' + str(ds.getPrepStmtCacheHitCount())
#				print 'PrepStmtCacheMissCount : \t\t ' + str(ds.getPrepStmtCacheMissCount())
#				print 'ReserveRequestCount : \t\t\t ' + str(ds.getReserveRequestCount())
#				print 'WaitSecondsHighCount : \t\t\t ' + str(ds.getWaitSecondsHighCount())
#				print 'WaitingForConnectionCurrentCount : \t ' + str(ds.getWaitingForConnectionCurrentCount())
#				print 'WaitingForConnectionFailureTotal : \t ' + str(ds.getWaitingForConnectionFailureTotal())
#				print 'WaitingForConnectionHighCount : \t ' + str(ds.getWaitingForConnectionHighCount())
#				print 'WaitingForConnectionSuccessTotal : \t ' + str(ds.getWaitingForConnectionSuccessTotal())
#				print 'WaitingForConnectionTotal : \t\t ' + str(ds.getWaitingForConnectionTotal())		
				if ds.getPrepStmtCacheAccessCount()!= 0:
					print '=============================================='
					print 'Name : \t '+ svr + ' => ' + ds.getName()
					print 'Stat before resume : \t ' +ds.getState()
	                                print 'PrepStmtCacheAccessCount : \t\t ' + str(ds.getPrepStmtCacheAccessCount())
					print 'PrepStmtCacheAddCount : \t\t ' + str(ds.getPrepStmtCacheAddCount())
					print 'PrepStmtCacheCurrentSize : \t\t ' + str(ds.getPrepStmtCacheCurrentSize())
					print 'PrepStmtCacheDeleteCount : \t\t ' + str(ds.getPrepStmtCacheDeleteCount())
					print 'PrepStmtCacheHitCount : \t\t ' + str(ds.getPrepStmtCacheHitCount())
					print 'PrepStmtCacheMissCount : \t\t ' + str(ds.getPrepStmtCacheMissCount())
					print ''
					hitratio=(float(ds.getPrepStmtCacheHitCount())/float(ds.getPrepStmtCacheAccessCount()))*100
					missratio=(float(ds.getPrepStmtCacheMissCount())/float(ds.getPrepStmtCacheAccessCount()))*100
					print 'ratio hit :\t\t\t\t ' + str(hitratio)
					print 'ratio miss : \t\t\t\t ' + str(missratio)
					print '=============================================='
#                                print '=============================================='
                        disconnect()
                except:
			dumpStack()

def usage():
        print sys.argv[0]+" -e {acc|prd|sim} t3://adminurl:port/"
try     :
        opts,args = getopt.getopt(sys.argv[1:],"e:")
except getopt.GetoptError       :
        #print help information and exit        :
        usage()
        sys.exit(2)
for o, a in opts :
	if o == "-e" :
		env = a
if len(args) != 1:
        usage()
        sys.exit(2)
try:
	if env =='acc':
		print 'connect to acc domain'
		configFile=configFileAcc
		keyFile=keyFileAcc
	elif env == 'prd':
		print 'connect to prd domain'
		configFile=configFileProd
                keyFile=keyFileProd
	elif env == 'sim':
		print 'connect to sim domain'			
		configFile=configFileSim
                keyFile=keyFileSim
	else:
		print 'not supported env used : ' + env
		usage()
        #redirect WLST native output to /dev/null
        redirect("/dev/null",'false')
	connecttoadmin(configFile,keyFile,args[0])
	getServerList()
	getdatasourceInfo(configFile,keyFile)
except:
	dumpStack()
	sys.exc_info()
        sys.exit(2)
