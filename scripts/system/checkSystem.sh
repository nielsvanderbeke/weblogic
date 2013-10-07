#===================================
# FileName: CheckSystem.sh
#!/bin/bash
PATH=$PATH:/usr/ccs/bin:/usr/share/lib:/sbin:/usr/sbin:/usr/local/bin:/bin
export PATH
 
os=`uname`
case $os in
SunOS)
 nproc=`psrinfo |wc -l` ;
 prspeed=` psrinfo -v | grep -i Hz |awk '{print $6" " $7}'|uniq  `
 inet_addrs=`ifconfig -a |grep -i inet | awk '{print $2}' `
 mem=`prtconf |grep -i size`
 ;;
Linux)
 nproc=`cat /proc/cpuinfo |grep -i processor |wc -l`
 prspeed=`cat /proc/cpuinfo |grep -i model |grep -i hz |awk '{print $7 }'|uniq  `
 inet_addrs=`ifconfig -a |grep -i inet | awk '{print $2}' |cut -d ":" -f 2`
 mem=`cat /proc/meminfo |grep -i MemTotal`
 ;;
esac
hname=`hostname`

echo "Host name : $hname"
echo "Operating system is $os release `uname -r `"
echo "Number of CPU : $nproc with the speed of $prspeed"
echo "RAM Size: " $mem

for IPAddr in $inet_addrs
do
 if [ $IPAddr != "127.0.0.1" ]
 then 
  if [ $os = "Linux" ]
  then
   
   IPAddr_name=`nslookup $IPAddr|grep -i name |awk '{print $4}'`
  else
   IPAddr_name=`nslookup $IPAddr|grep -i name |awk '{print $4}'`
  fi
  if [ ! -z ${IPAddr_name} ]; then 
   echo $IPAddr === $IPAddr_name 
  fi 

 fi
done