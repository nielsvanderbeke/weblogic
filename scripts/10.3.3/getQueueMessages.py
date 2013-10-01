##############################################################
#  Script     : getQueueMessages.py
#  Author     : niv
#  Date       : 16/04/2013
#  Last Edited: 16/04/2013, niv
#  Description: Get jms queue info
##############################################################
# Purpose:
# - Get jms queue info
#
# Requirements:
# -
#
# Method:
# -
#
# Syntax:
# - java weblogic.WLST getServerStatus.py -u username -p password t3://adminurl:port/
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
        print sys.argv[0]+" -u username -p password t3://adminurl:port/"
try     :
        opts,args = getopt.getopt(sys.argv[1:],"u:p:")
except getopt.GetoptError       :
        #print help information and exit        :
        usage()
        sys.exit(2)
for o, a in opts :
        if o =="-u" :
                user = a
        if o =="-p" :
                password = a
if len(args) != 1:
        usage()
        sys.exit(2)
try:
    connect(user,password,args[0])
    servers = domainRuntimeService.getServerRuntimes();
    if (len(servers) > 0):
        for server in servers:
            jmsRuntime = server.getJMSRuntime();
            jmsServers = jmsRuntime.getJMSServers();
            for jmsServer in jmsServers:
                destinations = jmsServer.getDestinations();
                for destination in destinations:
                    print '  BytesCurrentCount           ' ,  destination.getBytesCurrentCount()
                    print '  BytesHighCount              ' ,  destination.getBytesHighCount()
                    print '  BytesPendingCount           ' ,  destination.getBytesPendingCount()
                    print '  BytesReceivedCount          ' ,  destination.getBytesReceivedCount()
                    print '  BytesThresholdTime          ' ,  destination.getBytesThresholdTime()
                    print '  ConsumersCurrentCount       ' ,  destination.getConsumersCurrentCount()
                    print '  ConsumersHighCount          ' ,  destination.getConsumersHighCount()
                    print '  ConsumersTotalCount         ' ,  destination.getConsumersTotalCount()
                    print '  ConsumptionPausedState      ' ,  destination.getConsumptionPausedState()
                    print '  '
                    print '  DestinationInfo             ' ,  destination.getDestinationInfo()
                    print '  '
                    print '  DestinationType             ' ,  destination.getDestinationType()
                    print '  InsertionPaused             ' ,  destination.isInsertionPaused()
                    print '  InsertionPausedState        ' ,  destination.getInsertionPausedState()
                    print '  MessagesCurrentCount        ' ,  destination.getMessagesCurrentCount()
                    print '  MessagesDeletedCurrentCount ' ,  destination.getMessagesDeletedCurrentCount()
                    print '  MessagesHighCount           ' ,  destination.getMessagesHighCount()
                    print '  MessagesMovedCurrentCount   ' ,  destination.getMessagesMovedCurrentCount()
                    print '  MessagesPendingCount        ' ,  destination.getMessagesPendingCount()
                    print '  MessagesReceivedCount       ' ,  destination.getMessagesReceivedCount()
                    print '  MessagesThresholdTime       ' ,  destination.getMessagesThresholdTime()
                    print '  Parent                      ' ,  destination.getParent()
                    print '  Paused                      ' ,  destination.isPaused()
                    print '  ProductionPaused            ' ,  destination.isProductionPaused()
                    print '  ProductionPausedState       ' ,  destination.getProductionPausedState()
                    print '  State                       ' ,  destination.getState()
                    print '  Type                        ' ,  destination.getType()
except Exception, e:
    print e
    print "Error while trying to save and/or activate!!!"
    dumpStack()
    raise
