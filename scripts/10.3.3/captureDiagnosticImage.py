import getopt

configFileProd='/bea/user_projects/tools/carto/prd.config'
keyFileProd='/bea/user_projects/tools/carto/prd.key'
configFileAcc='/bea/user_projects/tools/carto/acc.config'
keyFileAcc='/bea/user_projects/tools/carto/acc.key'
configFileSim='/bea/user_projects/tools/carto/sim.config'
keyFileSim='/bea/user_projects/tools/carto/sim.key'

def connecttoadmin(configFileProd,keyFileProd,adminurl):
        print '=============================================='
        connect(userConfigFile=configFileProd,userKeyFile=keyFileProd, url=adminurl)
        print '=============================================='

def captureDiagnosticImage():
	currentDrive=currentTree()
	try:
		cd("serverRuntime:/WLDFRuntime/WLDFRuntime/WLDFImageRuntime/Image")
		task=cmo.captureImage()
		Thread.sleep(1000)
		while task.isRunning():
			Thread.sleep(5000)
		cmo.resetImageLockout();
#	except WLSTException:
#		print "Couldn't capture diagnostic image"
#		dumpStack()
#		sys.exc_info()
#		sys.exit(2)
	finally:
		currentDrive()

def listDiagnosticImages():
	# List the available diagnostic image files in the server's image capture dir
	images=getAvailableCapturedImages()
	if len(images) > 0:
		# For each diagnostic image found, retrieve image file, renaming it as
		# the user sees fit
		for image in images:
			saveName=outputDir+File.separator+serverName+'-'+image
			saveDiagnosticImageCaptureFile(image,saveName)

def usage():
        print sys.argv[0]+" -e {acc|prd|sim} t3://adminurl:port/"
try     :
        opts,args = getopt.getopt(sys.argv[1:],"e:d:")
except getopt.GetoptError       :
        #print help information and exit        :
	print "problem getting all options"
        usage()
        sys.exit(2)
for o, a in opts :
	if o == "-e" :
		env = a
	if o == "-d" :
		outputDir = "."
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
	serverRuntime()
	captureDiagnosticImage()
	validateAndShowChanges()
	disconnect()
except:
	dumpStack()
	sys.exc_info()
        sys.exit(2)
