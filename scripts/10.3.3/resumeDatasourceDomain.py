##############################################################
#  Script     : resumeDatasourceDomain.py
#  Author     : NIV
#  Date       : 03/05/2012
#  Last Edited: 21/02/2013, NIV
#  Description: resume all datasources off a weblogic domain
##############################################################
# Purpose:
# - resume all datasources off a weblogic domain
#
# Requirements:
# - WLST
#
# Method:
# -
#
# Syntax:
# - java weblogic.WLST resumeDatasourceDomain.py -e {acc|prd|sim} t3://adminurl:port
#
# Notes:
# - Does not yet work for sim domains
#
# Change List:
# - 11/04/2012 V4 : Last working version
# - 21/02/2013 V5 : add function -e to specifie env (needed for password)
#
##############################################################
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

def datasourceState(configFile,keyFile):
        for svr,url in urldict.items():
                try:
                        connect(userConfigFile=configFile,userKeyFile=keyFile, url=url)
                        serverRuntime()
                        dsMBeans = cmo.getJDBCServiceRuntime().getJDBCDataSourceRuntimeMBeans()
                        for ds in dsMBeans:
                                print '=============================================='
                                print 'Name : \t '+ svr + ' => ' + ds.getName()
                                print 'Stat before resume : \t ' +ds.getState()
                                print 'Test Pool before resume :'
                                try:
                                        print ds.testPool()
                                except:
                                        dumpStack()
                                try:
                                        print 'TRY RESUME DATASOURCE'
                                        print ds.resume()
                                except:
                                        dumpStack()
                                print  'Test Pool after resume : '
                                try:
                                        print ds.testPool()
                                except:
                                        dumpStack()
                                print 'Stat after resume : \t ' +ds.getState()
                                print '=============================================='
                        disconnect()
                except:
                        dumpStack()
                        print "Skipping " + svr
                continue



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
        redirect("/dev/null",'false')
        connecttoadmin(configFile,keyFile,args[0])
        getServerList()
        datasourceState(configFile,keyFile)
except:
        usage()
        sys.exit(2)
