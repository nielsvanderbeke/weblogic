#!/bin/sh
SSH_KEY=/export/home/weblogic/pp/.ssh/id_rsa_unencrypted
DESTINATION=/export/home/weblogic/pp/JFR
LOCAL_DIR=/export/home/weblogic/pp/JFR
RD_URL='http://skywalker.smals-mvm.be:4440'
RD_RESOURCES_QUERY=${RD_URL}'/api/3/resources?authtoken=kp1cuDs5DS525k3dUv0C72krRe5665Dk&project=Odysseus&tags=production&format=yaml'
wget -q -O - ${RD_RESOURCES_QUERY} | sed -n 's/hostname: \(.*\)$/\1/p' | for node in `cat -`; do
  JFRS=`ssh -i $SSH_KEY pp@$node ls /var/tmp/\*.jfr`
  if [ $? -eq 0 ]
  then
    for file in $JFRS
    do
    BASE=`basename $file`
    scp -i $SSH_KEY pp@$node:$file $DESTINATION/$BASE
    ssh -i $SSH_KEY pp@$node /bin/rm $file
    done
  fi
done
