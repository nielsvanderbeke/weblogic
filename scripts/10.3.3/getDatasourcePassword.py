##############################################################
#  Script     : getDatasourcePassword.py
#  Author     : NIV
#  Date       : 24/06/2011
#  Last Edited: 10/04/2012, NIV
#  Description: get datasource password from weblogic datasource
##############################################################
# Purpose:
# - get datasource password from weblogic datasource
#
# Requirements:
# - 
#
# Method:
# - 
#
# Syntax: 
# - java weblogic.WLST getDatasourcePassword.py -u username -p password -d datasourcename t3://adminurl:port/
#
# Notes:
# - 
#
# Change List:
# - 
#
##############################################################
import getopt
redirect('wlst.log', 'false')
def usage():
        print sys.argv[0]+" -u username -p password -d datasourcename t3://adminurl:port/"
try     :
        opts,args = getopt.getopt(sys.argv[1:],"u:p:d:")
except getopt.GetoptError       :
        #print help information and exit        :
        usage()
        sys.exit(2)
for o, a in opts :
        if o =="-u" :
                user = a
        if o =="-p" :
                password = a
        if o =="-d" :
                datasource = a
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
goto = 'JDBCSystemResources/' + datasource + '/JDBCResource/' + datasource + '/JDBCDriverParams/' + datasource
cd(goto)
print '==========================================='
print datasource + ' password : ' + get('Password')
print '==========================================='