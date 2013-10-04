#!/bin/bash
##############################################################
#  Script     : getPatchReport.sh
#  Author     : NIV
#  Date       : 31/01/2013
#  Last Edited: 31/01/2013, NIV
#  Description: get bsu report or list of all installed weblogic patches
##############################################################
# Purpose:
# - get report of all installed weblogic patches for this machine
#
# Requirements:
# - weblogic installed and bsu available
#
# Method:
# - generateview   :  generate simple view
# - generateraport : generate detaild raport (shows all classes changed by patches)
#
# Syntax:
# - ./getPatchReport.sh -t {view|rapport} [-p <location patch-client.jar>]
#
# Notes:
#
# Change List:
# - v1 31/01/2013 : Initial script
#
##############################################################

function generateview() {
        if [ -e "/opt/oracle/fmw/fmw11gR1PS2/utils/bsu/patch-client.jar" ] ; then
                cd /opt/oracle/fmw/fmw11gR1PS2/utils/bsu/
                java -Xms256m -Xmx512m -jar /opt/oracle/fmw/fmw11gR1PS2/utils/bsu/patch-client.jar -view -status=applied -prod_dir=/opt/oracle/fmw/fmw11gR1PS2/wlserver_10.3/
                cd -
        else
                echo "can't find /opt/oracle/fmw/fmw11gR1PS2/utils/bsu/patch-client.jar , try giving exact path patch-client.jar with option -p <location patch-client.jar>"
                usage
        fi
}

function generateraport(){
        if [ -e "/opt/oracle/fmw/fmw11gR1PS2/utils/bsu/patch-client.jar" ] ; then
                cd /opt/oracle/fmw/fmw11gR1PS2/utils/bsu/
                java -Xms256m -Xmx512m -jar /opt/oracle/fmw/fmw11gR1PS2/utils/bsu/patch-client.jar -report
                cd -
        else
                echo "can't find /opt/oracle/fmw/fmw11gR1PS2/utils/bsu/patch-client.jar , try giving exact path patch-client.jar with option -p <location patch-client.jar>"
                usage
        fi
}

function usage() {
        echo "Usage: $0 -t {view|rapport} [-p <location patch-client.jar>]"
        exit 1
}


while getopts ":t:p:" opt; do
        case $opt in
                t)
                        typerapport=$OPTARG
                        if [ $typerapport == 'view' ]; then
                                generateview
                        elif [ $typerapport == 'rapport' ]; then
                                generateraport
                        else
                                echo "Invalid option for -t : $OPTARG"
                                usage
                        fi
                        ;;
                p)
                        if [ -n "$OPTARG" ]; then
                                patchjar="$OPTARG"
                        else
                                usage
                        fi
                        ;;
                \?)
                        echo "Invalid option : -$OPTARG"
                        usage
                        ;;
                :)
                        echo "Option -$OPTARG requires an argument."
                        usage
                        ;;
                *)
                        usage
                        ;;
        esac
done

[[ -n $typerapport ]] || { echo "need type of report {view|rapport}"; usage;}

