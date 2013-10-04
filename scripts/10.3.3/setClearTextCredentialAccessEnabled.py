import getopt

def usage():
	print sys.argv[0]+" -u username -p password -d domainname t3://adminurl:port/"
try	:
	opts,args = getopt.getopt(sys.argv[1:],"u:p:d:")
except getopt.GetoptError	:
	#print help information and exit	:
	usage()
	sys.exit(2)
for o, a in opts :
	if o =="-u" :
		user = a
	if o =="-p" :
		password = a
	if o =="-d" :
		domain = a
if len(args) != 1:
	usage()
	sys.exit(2)
try:
	connect(user, password,args[0])
except:
	usage()
	sys.exit(2)
#print datasource
#easeSyntax()
edit()
goto = 'SecurityConfiguration/' + domain
cd(goto)
startEdit()
set('ClearTextCredentialAccessEnabled','true')
activate()
print 'ClearTextCredentialAccessEnabled -> true'


