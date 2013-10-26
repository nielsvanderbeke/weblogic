##############################################################
#  Script     : setXPoweredByHeaderLevel.py
#  Author     : NIV
#  Date       : 06/05/2013
#  Last Edited: 06/05/2013, NIV
#  Description: set XPoweredByHeaderLevel to None (secyrity reason)
##############################################################
# Purpose:
# - set XPoweredByHeaderLevel to None (secyrity reason)
#
# Requirements:
# - 
#
# Method:
# -
#
# Syntax:
# - java weblogic.WLST setXPoweredByHeaderLevel.py -e {acc|prd|sim} t3://adminurl:port/
#
# Notes:
# - GENERAL VERSION ( SOLARIS AND LINUX )
#
# Change List:
# - 06/05/2012 V1 : Inital version
#
##############################################################
import getopt

configFileProd='prd.config'
keyFileProd='prd.key'
configFileAcc='acc.config'
keyFileAcc='acc.key'
configFileSim='sim.config'
keyFileSim='sim.key'

def connecttoadmin(configFileProd,keyFileProd,adminurl):
        print '=============================================='
        connect(userConfigFile=configFileProd,userKeyFile=keyFileProd, url=adminurl)
        print '=============================================='

def desactivateXPoweredByHeaderLevel()
        try:
                cd('/')
                domainName = cmo.getName()
                cd('/WebAppContainer/' + domainName)
                print '=============================================='
                print 'XPoweredByHeaderLevel before : ' +  cmo.getXPoweredByHeaderLevel()
                print 'desactivate XPoweredByHeaderLevel ...'
                cmo.setXPoweredByHeaderLevel('NONE')
                print 'XPoweredByHeaderLevel after  : ' +  cmo.getXPoweredByHeaderLevel()
                print '=============================================='
        except:
                dumpStack()

def validateAndShowChanges():
        try:
                validate()
        except WLSTException:
                print "Couldn't validate"
                dumpStack()
                sys.exc_info()
                sys.exit(2)
        print '============== changes ======================'
        showChanges()
        print '=============================================='
        try:
                save()
        except WLSTException:
                print "Couldn't save"
                dumpStack()
                sys.exc_info()
                sys.exit(2)
        try:
                activate()
        except WLSTException:
                print "Couldn't activate"
                dumpStack()
                sys.exc_info()
                sys.exit(2)

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
                connecttoadmin(configFileAcc,keyFileAcc,args[0])
        elif env == 'prd':
                print 'connect to prd domain'
                connecttoadmin(configFileProd,keyFileProd,args[0])
        elif env == 'sim':
                print 'connect to sim domain'
                connecttoadmin(configFileSim,keyFileSim,args[0])
        else:
                print 'not supported env used : ' + env
                usage()
        #redirect WLST native output to /dev/null
        #redirect("/dev/null",'false')
        edit()
        startEdit()
        desactivateXPoweredByHeaderLevel()
        validateAndShowChanges()
        disconnect()
except:
        dumpStack()
        sys.exc_info()
        sys.exit(2)
