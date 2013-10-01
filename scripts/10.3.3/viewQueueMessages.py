"""
#############################################################################
#
# @author Copyright (c) 2010 - 2011 by Middleware Magic, All Rights Reserved.
#
#############################################################################

connect('weblogic','weblogic','t3://localhost:7001')
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



cd domainRuntime
cd ServerRuntimes
for server in suppliedServers:
    cd domainRuntime
    cd ServerRuntimes
    cd server
    cd JRMRUNTIME/server.jms/JMSServers/
"""


def askPossibleList(question, possibilities):
    counter = 0
    for i in possibilities:
        print ("{0}: {1}".format(counter, i))
        counter += 1
    choices = raw_input(question).split(',')
    for i in targets:
        i = i.strip()
        print i


#@ ask where are the JMS-servers are targetted(choice between clusters and single instances)
#@ if single instance
  #@ ask which JMSservers(multiple allowed by csv)
    #@ for each JMSServer list the destinations and ask which should be given
      #@ for each destination, give current and pending messages
#@ if cluster
    #@ for each instance: do single instance work




















