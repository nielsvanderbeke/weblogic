##############################################################
#  Script     : setWLDFDiagnosticVolume.py
#  Author     : NIV
#  Date       : 08/05/2012
#  Last Edited: 08/05/2012, NIV
#  Description: set the WLDF Diagnostic Volume of a domain instance.
##############################################################
# Purpose:
# - set the WLDF Diagnostic Volume of a domain instance.
#
# Requirements:
# -
#
# Method:
# -
#
# Syntax:
# - java weblogic.WLST setWLDFDiagnosticVolume.py -n node -v niveau -u username -p password t3://serverurl:port/
#
# Notes:
# - Adviced to use LOW in prod
#
# Change List:
# -
#
##############################################################
import getopt

def usage():
    print sys.argv[0]+"-n node -v niveau -u username -p password t3://adminurl:port/"

try :
    opts,args = getopt.getopt(sys.argv[1:],"u:p:v:n:")
except getopt.GetoptError   :
    #print help information and exit    :
    usage()
    sys.exit(2)
for o, a in opts :
    if o =="-u" :
        user = a
    if o =="-p" :
        password = a
    if o =="-v" :
        niveau = a
    if o == "-n" :
        node = a
if len(args) != 1:
    usage()
    sys.exit(2)
try:
    connect(user, password,args[0])
    #redirect WLST native output to /dev/null
    #redirect("/dev/null",'false')
except:
    usage()
    sys.exit(2)

try:
        edit()
        startEdit()
        cd('Servers/' + node + '/ServerDiagnosticConfig/' + node)
        set('WLDFDiagnosticVolume',niveau)
except:
        sys.exit(2)




try:
    validate()
except WLSTException:
    print "Couldn't validate"
    sys.exc_info()
    #stopEdit()
    sys.exit(2)
showChanges()
#stopEdit()
save()
activate()
disconnect()
