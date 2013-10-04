#!/usr/bin/env python
from time import sleep
from java.util import Date
from java.text import SimpleDateFormat

username='system'
password='****'
adminurl='t3://host:port'
connect(username,password,adminurl)
domainRuntime()
servers=['server1','server2']
df=SimpleDateFormat('yyyy.MM.dd HH:mm:ss S')
fh = open('threads_mon.log', 'w')
while true:
	now=df.format(Date())
	for server in servers:
		cd('ServerRuntimes/'+server+'/ThreadPoolRuntime/ThreadPoolRuntime')
		compReq = cmo.getCompletedRequestCount()
		status = cmo.getHealthState()
		hoggingThreads = cmo.getHoggingThreadCount()
		totalThreads = cmo.getExecuteThreadTotalCount()
		idleThrds = cmo.getExecuteThreadIdleCount()
		pending = cmo.getPendingUserRequestCount()
		qLen = cmo.getQueueLength()
		thruput = cmo.getThroughput()
		outline="%s %s %3d %3d %3d %3d %6.2f\n" % (now,server,totalThreads,idleThrds,pending,qLen,thruput)
		#print '%s %s %d %d %d %d %f' % (now,server,totalThreads,idleThrds,pending,qLen,thruput)
		fh.write(outline)
	sleep(15)
	fh.flush()
disconnect()
