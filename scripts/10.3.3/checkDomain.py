import getopt
import sys


class colorOutput:
    def __init__(self, domainname, v_debug = 0):
                self.debug = v_debug
                self.greenStartCode = '\033[1;32m'
                self.backToNormalCode = '\033[1;m'

    def goodPrint(self, text):
        self.printColor(text, 'green')

    def badPrint(self, text):
        self.printColor(text, 'red')

    def warningPrint(self, text):
        self.printColor(text, 'yellow')

    def infoPrint(self, text):
        self.printColor(text, 'blue')

    def debugPrint(self, text):
        if self.debug == True:
            self.printColor(text, 'teal')

    def printColor(self, text, color):
                log = open(str(domainname)+"Log.log", "a")
                text2 = str(text)
                if color == "green":
                        print ( self.greenStartCode + text2 + self.backToNormalCode)
                        log.write(text2 + '\n')
                elif color == 'red':
                        print ('\033[1;31m' + text2 + '\033[1;m')
                        log.write(text2 + '\n')
                elif color == 'yellow':
                        print ('\033[1;33m' + text2 + '\033[1;m')
                        log.write(text2 + '\n')
                elif color == 'blue':
                        print ('\033[1;34m' + text2 + '\033[1;m')
                        log.write(text2 + '\n')
                elif color == 'teal':
                        print ('\033[1;36m' + text2 + '\033[1;m')
                        log.write(text2 + '\n')
                log.close()

#############


def usage():
        print sys.argv[0]+" -u username -p password -o n/y t3://adminurl:port/"

try     :
        opts,args = getopt.getopt(sys.argv[1:],"u:p:o:")
except getopt.GetoptError       :
        print "help information and exit"
        usage()
        sys.exit(2)
choix="y        "
for o, a in opts :
        if o =="-u" :
                user = a
        if o =="-p" :
                password = a
        if o =="-o" :
                choix = a
if len(args) != 1:
        usage()
        sys.exit(2)
try:
        print "user : " + user + " serveur : " + args[0]
        connect(user, password,args[0])
except:
        usage()
        sys.exit(2)

badCount=0
domainname=cmo.getName()
c = colorOutput(domainname)
log = open(str(domainname)+"Log.log", "w")
log.close()
c.infoPrint('Domain chek : '+domainname+'\n')
servers=cmo.getServers()
#print 'Found '+str(len(servers))+ ' servers'
#Archive configuration count
val=cmo.getArchiveConfigurationCount()
if val == 30:                                                                                   #valeur ok
        c.goodPrint("\t[X]ArchiveConfigurationCount: good")
else:
        c.badPrint("\t[ ]ArchiveConfigurationCount: TO FIX " + str(val)+ " should be 30")
        badCount+=1
#backup activation
val=get('ConfigBackupEnabled')
if val == 1:                                                                                    #valeur ok
        c.goodPrint("\t[X]ConfigBackupEnabled: good")
else:
        c.badPrint("\t[ ]ConfigBackupEnabled: TO FIX " + str(val)+ " should be 1")
        badCount+=1
#console activation
val=get('ConsoleEnabled')
if val == 1:                                                                                            #valeur ok
        c.goodPrint("\t[X]ConsoleEnabled: good")
else:
        c.badPrint("\t[ ]ConsoleEnabled: TO FIX "+ str(val) + " should be 1")
        badCount+=1
#Poducation mode active
val=get('ProductionModeEnabled')
if val == 1:                                                                                    #valeur ok
        c.goodPrint("\t[X]ProductionModeEnabled: good")
else:
        c.badPrint("\t[ ]ProductionModeEnabled: TO FIX "+ str(val) + " should be 1")
        badCount+=1
##Security realm
cd('/SecurityConfiguration/'+domainname)
val=get('ClearTextCredentialAccessEnabled')
if val==1:                                                                                                      #valeur ok
        c.goodPrint("\t[X]ClearTextCredentialAccessEnabled: good")
else :
        c.badPrint("\t[ ]ClearTextCredentialAccessEnabled: TO FIX "+ str(val) + " should be 1")
        badCount+=1
###########################################
defRealm=cmo.findDefaultRealm()
#defRealm.setCombinedRoleMappingEnabled(0)
##########################################
#PKI credential mapper
##########################################
# names = ["egovusers","civilservantusers","citizenusers"]
# cd('/')
# securityRealm = cmo.getSecurityConfiguration().getDefaultRealm() #go to default realm
# c.badPrint("locator")
# c.badPrint(securityRealm)
# authProvider = securityRealm.lookupCredentialMapper('PKICredentialMapper')
# c.badPrint(authProvider)
# if authProvider != None:
        # for uName in names:
                # c.debugPrint(uName)
                # c.infoPrint("Ccheking mapping for %(1)s" % {"1" : uName})
        # val=authProvider.listAllKeypairEntryAliases()
        # print "**********************************************"
        # print "PKI " + str(val)
        # print "**********************************************"
    # #else:
     # #   c.warningPrint("%s does not exist, can't create mappings" % credentialMapperName)
      # #  logger.warning("%s does not exist, can't create mappings" % credentialMapperName)


###########################################
#Server part
for serv in servers:
        servername=serv.getName()
        c.infoPrint('\nCheck serveur '+servername+ '\n')
        if len(serv.getListenAddress() ) == 0:
                c.warningPrint('Warning : listen address not set')
        ####test log config
        #log=serv.getLog()
        #print "Log File : " + log.getFileName()
        ###config server
        cd('/Servers/' + servername)
        val=get('AutoRestart')
        if val == 1:                                                            #valeur ok
                c.goodPrint("\t[X]AutoRestart: good")
        else :
                c.badPrint("\t[ ]AutoRestart: TO FIX  " + str(val) + " should be 1")
                badCount+=1
        val=get('GracefulShutdownTimeout')
        if val == 120:                                                          #valeur ok
                c.goodPrint("\t[X]GracefulShutdownTimeout: good")
        else :
                c.badPrint("\t[ ]GracefulShutdownTimeout: TO FIX " + str(val) + " should be 120")
                badCount+=1
        val=get('IdleConnectionTimeout')
        if val == 65:                                                           #valeur ok
                c.goodPrint("\t[X]IdleConnectionTimeout: good")
        else :
                c.badPrint("\t[ ]IdleConnectionTimeout: TO FIX " + str(val) + " should be 65")
                badCount+=1
        val=get('IgnoreSessionsDuringShutdown')
        if val == 1:                                                            #valeur ok
                c.goodPrint("\t[X]IgnoreSessionsDuringShutdown: good")
        else :
                c.badPrint("\t[ ]IgnoreSessionsDuringShutdow: TO FIX " + str(val) + " should be 1")
                badCount+=1
        val=get('ManagedServerIndependenceEnabled')
        if val == 1:                                                            #valeur ok
                c.goodPrint("\t[X]ManagedServerIndependenceEnabled: good")
        else :
                c.badPrint("\t[ ]ManagedServerIndependenceEnabled: TO FIX " + str(val) + " should be 1")
                badCount+=1
        val=get('MaxOpenSockCount')                                     #ancien valeur 1024
        if val == -1 :
                c.goodPrint("\t[X]MaxOpenSockCount: good")
        else :
                c.badPrint("\t[ ]MaxOpenSockCount: TO FIX " + str(val) + " should be -1")
                badCount+=1
        val=get('TransactionLogFilePrefix')
        if val == '../../txlogs/' :
                c.goodPrint("\t[X]TransactionLogFilePrefix: good")
        else :
                c.badPrint("\t[ ]TransactionLogFilePrefix: TO FIX " + str(val) + " should be ../../txlogs/")
                badCount+=1
        val=get('TransactionLogFileWritePolicy')
        if val == 'Direct-Write' :                                              #valeur ok
                c.goodPrint("\t[X]TransactionLogFileWritePolicy: good")
        else :
                c.badPrint("\t[ ]TransactionLogFileWritePolicy: TO FIX " + str(val) + " should be Direct-Write")
                badCount+=1
        val=get('ClasspathServletDisabled')
        if val == 1 :                                                                   #valeur 0
                c.goodPrint("\t[X]ClasspathServletDisabled: good")
        else:
                c.badPrint("\t[ ]ClasspathServletDisabled: TO FIX " + str(val) + " should be 1")
                badCount+=1
        val=get('AdminReconnectIntervalSeconds')                #valeur ok
        if val == 10 :
                c.goodPrint("\t[X]AdminReconnectIntervalSeconds: good")
        else:
                c.badPrint("\t[ ]AdminReconnectIntervalSeconds: TO FIX " + str(val)+ " should be 10")
                badCount+=1
        cd('/Servers/' + servername +'/OverloadProtection/' + servername)
        val=get('SharedCapacityForWorkManagers')
        if val == 2048 :                                                                        #valeur ok
                c.goodPrint("\t[X]SharedCapacityForWorkManagers: good")
        else:
                c.badPrint("\t[ ]SharedCapacityForWorkManagers: TO FIX " + str(val) + " should be 2048")
                badCount+=1
        cd('/Servers/' + servername +'/SSL/'+servername)
        val=get('HostnameVerifier')
        #print ("HostnameVerifier : " + str(val))
        if val ==  "be.smals.weblogic.extensions.security.ssl.SmalsHostnameVerifier" :
                c.goodPrint("\tHostnameVerifier: good (New version) be.smals : " + str(val))
        elif val is None :
                c.infoPrint("\tHostnameVerifier: not define")
        else :
                c.badPrint("\tHostnameVerifier: TO FIX (old version smalsmvm) : " + str(val) )
                badCount+=1
cd('/')
#todo good message
c.infoPrint("\nchek Data source !\n")
db={"authenticatorumoe":0, "db.datasource.Tickets":0, "db.datasource.uam.pep":0, "db.datasource.useraccess_data":0}
jdbcresources=cmo.getJDBCSystemResources()
for jdbcresource in jdbcresources:
    if not jdbcresource.getJDBCResource().getJDBCDataSourceParams().getDataSourceList():
        resName=jdbcresource.getName()
        print 'Checking '+resName
        for cle in db:
                if (resName.find(cle))>-1:
                        db[cle]=db[cle]+1
        cd('/JDBCSystemResources/'+resName+'/JDBCResource/'+resName+'/JDBCConnectionPoolParams/'+resName)
        statement=cmo.getTestTableName()
        sec=cmo.getTestFrequencySeconds()
        test=cmo.isSet('TestConnectionsOnReserve')
        InactiveConnectionTimeoutSeconds = cmo.getInactiveConnectionTimeoutSeconds()
        ConnectionCreationRetryFrequencySeconds = cmo.getConnectionCreationRetryFrequencySeconds()
        if statement is None:
                c.badPrint("\t[ ]TestTableName no test table defined")
                badCount+=1
        if test == 0:
                c.badPrint("\t[ ]TestConnectionsOnReserve is not activated")
                badCount+=1
        if sec != 120:
                c.badPrint("\t[ ]TestFrequencySeconds Adjusted from " + str(sec) + " to "+ str(120) +" sec")
                badCount+=1
        if InactiveConnectionTimeoutSeconds != 30:
                c.badPrint("\t[ ]InactiveConnectionTimeoutSeconds Adjusted from " + str(InactiveConnectionTimeoutSeconds) + " to "+ str(30) +" sec")
                badCount+=1
        if ConnectionCreationRetryFrequencySeconds != 3:
                c.badPrint("\t[ ]ConnectionCreationRetryFrequencySeconds Adjusted from " + str(ConnectionCreationRetryFrequencySeconds) + " to "+ str(3) +" sec")
                badCount+=1

c.infoPrint("\nDate  source information ! \n")
for cle in db:
        if db[cle]==0:
                c.badPrint('\t'+str(cle) + ' datasource missing')
                badCount+=1
        else:
                c.infoPrint('\t'+str(cle)+' '+ str(db[cle])+' datasource occure')


c.warningPrint(str(badCount)+" properties need change")
if (badCount >0):
        if (choix == "n"):
                disconnect()
        else:
                choix = raw_input('\n\n\tSet as default domain (y/n): ')

        if (str(choix) == "y" or str(choix) == "yes" or str(choix) == "Y"):
                c.infoPrint("Setting environement")
                edit()
                startEdit()
                cmo.setArchiveConfigurationCount(30)
                cmo.setConfigBackupEnabled(1)
                set('ConsoleEnabled', 'true')
                #set('ProductionModeEnabled', 'true')

                cd('/SecurityConfiguration/'+domainname)
                set('ClearTextCredentialAccessEnabled','true')
                # #######idm########
                defRealm=cmo.findDefaultRealm()
                defRealm.setCombinedRoleMappingEnabled(0)

                cd("/")
                # ##server
                servers=cmo.getServers()
                for serv in servers:
                        log=serv.getLog()
                        log.setFileName('../../logs/'+servername+'_%yyyy%_%MM%_%dd%_%hh%_%mm%.log')
                        log.setRotationType('byTime')

                        weblog=serv.getWebServer().getWebServerLog()
                        weblog.setFileName('../../logs/access_'+servername+'_%yyyy%_%MM%_%dd%_%hh%_%mm%.log')

                        weblog.setRotationType('byTime')
                        weblog.setLogFileFormat('extended')
                        weblog.setELFFields('c-ip c-username date time cs-method cs-uri sc-status bytes time-taken')

                        cd('/Servers/' + servername)
                        set('AutoRestart','true')
                        set('GracefulShutdownTimeout',120)
                        set('IdleConnectionTimeout',65)

                        set('ManagedServerIndependenceEnabled', 'true')
                        #set('MaxOpenSockCount', 512)           ####ERRORE

                        set('TransactionLogFilePrefix', '../../txlogs/')
                        set('TransactionLogFileWritePolicy', 'Direct-Write')
                        set('ClasspathServletDisabled', 'true')
                        set('AdminReconnectIntervalSeconds', 10)
                        cd('/Servers/' + servername +'/OverloadProtection/' + servername)
                        set('SharedCapacityForWorkManagers', 2048)

                        cd('/Servers/' + servername +'/SSL/'+servername)

                        #host name verifier
                        #todo say the name of the instance
                        print ("Fixing CustomHostnameVerifier for : "+ servername)
                        print ("\t 1.new version smals ")
                        print ("\t 2. old vesion smalsmvm ")
                        print ("\t 3. None ")
                        choix = raw_input("Qu'elle choix ? : ")
                        if(choix == "1"):
                                set('HostnameVerifier', 'be.smals.weblogic.extensions.security.ssl.SmalsHostnameVerifier')
                        elif(choix == "2"):
                                set('HostnameVerifier', 'be.smalsmvm.common.systemservices.security.ssl.CustomHostNameVerifier')
                        elif(choix == "3"):
                                set('HostnameVerifier', 'NONE')

                # #jdbc

                ##todo good message
                cd('/')
                jdbcresources=cmo.getJDBCSystemResources()
                for jdbcresource in jdbcresources:
                        cd('/JDBCSystemResources/'+resName+'/JDBCResource/'+resName+'/JDBCConnectionPoolParams/'+resName)
                        statement=cmo.getTestTableName()
                        sec=cmo.getTestFrequencySeconds()
                        test=cmo.isSet('TestConnectionsOnReserve')
                        if statement is None:
                                cmo.setTestTableName('SQL SELECT 1 FROM DUAL')
                        if test == 0:
                                cmo.setTestConnectionsOnReserve('true')
                        if sec != 120:
                                cmo.setTestFrequencySeconds(120)

                print ("show change")
                showChanges()
                save()
                activate()
                Print ("Pleace restart your domain")
                #try:
                #       validate()
                #except WLSTException:
                        # print "Couldn't validate"
                        # sys.exc_info()
                        # stopEdit()
                        # sys.exit(2)
                #print ("show change")
                #showChanges()
                #save()
                #activate()
                #stopEdit()
                disconnect()

        elif (str(choix) == "n" or str(choix) == "N" or str(choix) == "no"):
                #c.infoPrint("no")
                disconnect()
        else :
                #c.infoPrint("other")
                disconnect()
