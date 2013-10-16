
%global         __os_install_post %{nil}
%global         __arch_install_post %{nil}

%define         jdk_version      1.6.0_51
%define         jrockit_version  28.2.8
%define         install_dir      /opt/oracle/jvm/jrockit-jdk6

Name:           jrockit-jdk6
Version:        %{jrockit_version}
Release:        1%{?dist}
Summary:        Oracle JRockit JDK

Group:          Java
License:        Oracle Binary Code License
URL:            http://www.oracle.com/technetwork/middleware/jrockit/index.html
Source0:        p16863120_2828_Linux-x86-64.zip
Source2:        jce_policy-6.zip

AutoReqProv: no
ExclusiveOS: linux

%description
The Oracle JRockit 6 JVM.

%install
umask 007

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/oracle/jvm
pushd $RPM_BUILD_ROOT/opt/oracle/jvm

unzip %{SOURCE0}
mv jrockit-jdk%{jdk_version} jrockit-jdk6
popd

pushd $RPM_BUILD_ROOT%{install_dir}
unzip -o -j %{SOURCE2} *.jar -d jre/lib/security
perl -p -i -e "s#^securerandom.source=.*#securerandom.source=file:/dev/./urandom#g" jre/lib/security/java.security
rm src.zip
rm -rf demo 
rm -rf missioncontrol/samples
rm -rf sample

find . -type f -exec chmod ugo-x {} \;
find . -type f -name "*.so" -exec chmod u+x {} \;
chmod u+x bin/*
chmod u+x jre/bin/*
chmod u+x jre/lib/jexec
chmod u+x lib/jexec

chmod -R u+w,g+rwX,o+rX .
popd

%clean
rm -rf $RPM_BUILD_ROOT

%post
chown weblogic:weblogic /opt/oracle/jvm
chmod 2775 /opt/oracle/jvm

%files
%defattr(-,weblogic,weblogic,-)
%verify(not size mtime) %{install_dir}

%verifyscript
#!/bin/bash
numfiles=4
checkdir=%{install_dir}/jre/lib/ext

count=`ls -1 $checkdir/*.jar | wc -l`
if [ $count -gt $numfiles ] ; then
    echo "more than $numfiles entries found in $checkdir" >&2
fi

