import getopt
import sys

def connectToAdmin(config, key, url):
        #print "Connecting to " + url
        #print(config, key, url)
        connect(userConfigFile=config, userKeyFile=key, url=url)
        #connect(config, key, url)
        #print "Connected to " + url

def getManagedServers():
        domainConfig()
        #print "in domain config"
        a = cmo.getServers()
        #print "servers gotten"
        n = []
        for i in a:
                #print i
                #print i.getName()
                f = i.getName()
                n.append(f)
        #print "servers appended"
        return n


def serverState(serverName):
        #print "Getting Serverstate"
        #domainRuntime()
        #print "in domain runtime"
        cd('/')
        #print "in root"
        #print '/ServerLifeCycleRuntimes/'+serverName
        cd('/ServerLifeCycleRuntimes/'+serverName)
        #print "in serverLifeCycleRuntimes+servername"
        #Print(serverName+ ":" +cmo.getState())
        #print "Server State gotten"
        return cmo.getState()

def getData(serverName):
        #print "managedList"
        managedServers = getManagedServers()
        #print "list gotten"
        #serverState(serverName)
        #print "admin"

        domainRuntime()
        for server in managedServers:
                cd('/')
                #print 'ServerRuntimes/' + str(server)
                try:
                        cd('ServerRuntimes/'+str(server))
                        header = get('ListenAddress')
                        cd('JVMRuntime/'+server)

                        hf = float(get('HeapFreeCurrent'))/1024
                        hs = float(get('HeapSizeCurrent'))/1024
                        hf = hf/1024
                        hs = hs/1024
                        hf = round(hf/1024, 2)
                        hs = round(hs/1024, 2)
                        heapFreePercent = get('HeapFreePercent')

                        heapUsedCurr = hs - hf
                        heapUsedPercent = 100 - heapFreePercent

                        #print "===DATA" + header.split('/')[0] + "==="
                        #print "Heap total: " + str(heapSizeCurr)
                        #print "Heap used: " + str(heapUsedCurr)
                        #print "Heap used percent: " + str(heapUsedPercent)

                        print server + "," + str(hs) + "," + str(heapUsedCurr) + "," + str(heapUsedPercent) + "," + header.split('/')[0] + "," + serverState(server)
                except:
                        print server + " not reachable, possibly shutdown"

################################# USAGE/OPTIONS #######################################################
def usage():
        print sys.argv[0]+" +-n ServerName -a adminUrl(t3://adminurl:port) -c configFile -k keyFile"

def readOptions():
        #print("Reading Options")
        try      :
        #       print("Trying Options")
                opts, args = getopt.getopt(sys.argv[1:],"n:a:c:k:")

        #       print("Testing Options Length")
                # print(len(args))
                # print(len(opts))
                # print(opts)
                # print(args)
                if len(opts) != 4:
                        usage()
                        sys.exit(2)

        #       print("Filling Options")
                for o, a in opts :
                        #print(o, a)
                        if o == "-n" :
                                serverName = a
                        if o == "-a" :
                                adminUrl = a
                        if o == "-c" :
                                configFile = a
                        if o == "-k" :
                                keyFile = a
                returner = []
                returner.append(serverName)
                returner.append(adminUrl)
                returner.append(configFile)
                returner.append(keyFile)

        except getopt.GetoptError          :
                #print help information and exit                :
                usage()
                sys.exit(2)

        return returner

################################# END-USAGE/OPTIONS ###################################################

def run():
        redirect("./getHeapOut.log",'false')
        machines = [line.strip() for line in open("./heapServerList.txt")]
        for machine in machines:
                print "====================" + machine
                a = machine.split(' ')
                configFile = a[3]
                keyFile = a[4]
                adminUrl = "t3://" + a[0] + ":" + a[1]
                serverName = a[2]
                try:
                        connectToAdmin(configFile, keyFile, adminUrl)
                        getData(serverName)
                        disconnect()
                except:
                        print a[0] + " not reachable"




        # listOfOptions = readOptions()

        # configFile = listOfOptions[2]
        # keyFile = listOfOptions[3]
        # adminUrl = listOfOptions[1]
        # serverName = listOfOptions[0]


        exit()

run()
