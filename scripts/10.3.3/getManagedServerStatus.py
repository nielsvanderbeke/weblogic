##############################################################
#  Script     : manageServers.py
#  Author     : TJ
#  Date       : 11/05/2012
#  Last Edited: 11/05/2012, TJ
#  Description: Start/Stop/Suspend/Resume all the managed servers of a WL domain
##############################################################
# Purpose:
# - Get the current servers status
#
# Requirements:
# - 
#
# Method:
# - 
#
# Syntax: 
# - java weblogic.WLST manageServers.py -u username -p password -a action t3://adminurl:port/
#
# Notes:
# - 
#
# Change List:
# - 
#
##############################################################
import getopt

if __name__ == '__main__': 
    from wlstModule import *#@UnusedWildImport
    
def usage():
        print sys.argv[0]+" -u username -p password -a action t3://adminurl:port/"
try     :
        opts,args = getopt.getopt(sys.argv[1:],"u:p:a:")
except getopt.GetoptError       :
        #print help information and exit        :
        usage()
        sys.exit(2)
for o, a in opts :
        if o =="-u" :
                user = a
        if o =="-p" :
                password = a
        if o =="-a" :
                action = a
if len(args) != 1:
        usage()
        sys.exit(2)
try:
    connect(user,password,args[0])
    domainConfig()
    serverList=cmo.getServers();
    domainRuntime()
    cd('/ServerLifeCycleRuntimes/')
    cpt=0;
    for server in serverList:
        name=server.getName();
        cd(server.getName());
        if cpt!=0 :
            print 'Shutting down "'+ name +'" ->  State "'+cmo.getState()+'"';
            if action == "resume" :
                resume(name,block="true");
            else:
                if action == "suspend" :
                    suspend(name,block="true");
                else:
                    if action== "start" :
                        start(name,block="true");
                    else:
                        if action == "shutdown":
                            shutdown(name,block="true");
           
            print 'Server'+ name +'State :'+cmo.getState()+'"';
            cd('..');   
        else :
            print 'Server "'+ name +'" ->  State "'+cmo.getState()+'"';
            cd('..');
        cpt+=1;
        print "\n############################################"
                
except Exception, e:
    print e 
    print "Error while trying to save and/or activate!!!"
    dumpStack()
    raise  