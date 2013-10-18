#!/usr/bin/python
#############################################################
#  Script     : getDomainInfo.py
#  Author     : NIV
#  Date       : 24/06/2011
#  Last Edited: 10/04/2012, NIV
#  Description: get domain info
##############################################################
# Purpose:
# - get domain info
#
# Requirements:
# - 
#
# Method:
# - 
#
# Syntax: 
# - 
#
# Notes:
# - 
#
# Change List:
# - 
#
##############################################################
# Necessary library
from pprint import pprint

def connectAS(adminUser, adminPass, adminURL):
    try:
        print "Connecting to AdminServer on " + adminURL + "..."
        connect(username=adminUser, password=adminPass, url=adminURL)
    except WLSTException:
        print "Unable to connect AdminServer with URL " + adminURL
        exit()

def getRunningServerNames():
    return cmo.getServers()
    

def getListApps():
    serverConfig()
    cd('/')
    apps = cmo.getAppDeployments()
    sortedListApps = []
    for appName in apps:
        sortedListApps.append(appName.getName())
    sortedListApps.sort()
    return sortedListApps
    
def getDomainInfo():
    serverConfig()
    cd('/')
    print 'Domain Version        : '+cmo.getConfigurationVersion()
    print 'Domain Root Directory : '+cmo.getRootDirectory()
    print 'Domain in Production  : '+boolean(get('ProductionModeEnabled'))
    admin=cmo.getAdminServerName()
    print '\nServer Details'
    print '--------------'
    for eachServer in serverNames:
        currDir=pwd()
        serverName=eachServer.getName()
        cd('/Servers/' +serverName)
        print 'Server Name : '+serverName
        
        if serverName==admin :
            print '\tServer Type      : Admin Server'
        else:
            print '\tServer Type      : Managed Server'
        
        listenAddress=str(get('ListenAddress'))
        listenPort=str(get('ListenPort'))
        
        msi=boolean(get('ManagedServerIndependenceEnabled'))
        machine = ''
        if get('Machine'):
            machine = cmo.getMachine().getName()
        
        if get('Cluster'):
            cluster = cmo.getCluster().getName()
        
        if listenAddress=="":
            listenAddress="ALL"
        print '\tListen Address   : '+ listenAddress
        print '\tListen Port      : '+ listenPort
        cd('SSL/'+serverName)
        print '\tSSL Listen Port  : '+ str(get('ListenPort'))
        print '\tSSL Enabled      : '+ boolean(get('Enabled'))
        print '\tMSI Enabled      : '+ msi
        print '\tMachine          : '+ machine
        
        cd(currDir)
    cd('../../../../../../../../../../../..')
    clusters=cmo.getClusters()
    if clusters:
        print '\nCluster Details'
        print '---------------'
        for eachCluster in clusters:
            print 'Cluster Name : '+eachCluster.getName()
            print '\tMulticast Address : '+str(eachCluster.getMulticastAddress())
            print '\tMulticast Port    : '+str(eachCluster.getMulticastPort())
            currDir=pwd()
            cd('Clusters/'+eachCluster.getName())
            servers=cmo.getServers()
            if servers:
                print '\n\tMember Servers'
                print '\t--------------'
                for eachServer in servers:
                    print '\t\t\t\t'+eachServer.getName()
            cd(currDir)
            print
            

			def getListAppsServer ():
    print 'Available servers are:'
    for servName in servers:
        print '\t' + servName
    print
    servName = raw_input ('Enter the target server name: ')
    print 'Server name is ' + servName
    if servName not in servers:
        print '!!! Error !!!'
        print 'The server \'' + servName + '\' does not exist in this project'
        exit()
    domainRuntime()
    cd('/ServerRuntimes/' + servName)
    listApps = cmo.getApplicationRuntimes()
    nonUserApps = ['bea_wls9_async_response','bea_wls_cluster_internal','bea_wls_deployment_internal','bea_wls_diagnostics','bea_wls_internal','uddi','uddiexplorer']
    sortedList = []
    for app in listApps:
        appName = app.getName()
        if appName not in nonUserApps:
            sortedList.append(appName)
    sortedList.sort()
    for app in sortedList:
        print app
        

if __name__ == "main":
    print 'test'
    functions = {
    '1' : 'Get list of domains per environment (INT, ACC, SIM, PROD)',\
    '2' : 'Get list of servers per domain',\
    '3' : 'Get list of applications per server in the specified domain',\
    '4' : 'Get domain information',\
    'q|Q' : 'Quit'
    }
    
    print 'What would you like to do? Available functions are: '
    pprint (functions)
    print
    #serverNames = getRunningServerNames()
    
    answer = 'y'            # Default start answer is 'y' to be able to start with something at least once
    while answer.lower() == 'y':
        print
        action = raw_input ('Please choose a number from the list:')
        if action == '1':
            # This is hardcoded in this file. Unluckily, I haven't found a way to retrieve a list of all domains!!!
            # production Solaris domains
            print 'List of domains in production:'
            print prodConnectionUrls.items()
            domainsList = prodConnectionUrls.keys()
            domainsList.sort()
            for dom in domainsList:
                print " ".join((dom, str(prodConnectionUrls[dom])))
            # This works in pure Python but not in WLST :(
            """
            for key, value in (prodConnectionUrls.iteritems(),key = lambda (k,v) : (v,k), reverse=False):
                print "%s %s" % (key, value)
            """
        elif action.lower() == 'q':
            exit()
        else:
            for adminURL in prodConnectionUrls.values():
            # TODO: The username and password can be encrypted if required
                connectAS("system","mon-kiki!", adminURL)
                if action == '2':
                    listServers = getRunningServerNames()
                    for s in listServers:
                        print s.getName()
                    print '****************************'
                disconnect()
    