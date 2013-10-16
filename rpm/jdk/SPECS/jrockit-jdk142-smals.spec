
%global         __os_install_post %{nil}
%global         __arch_install_post %{nil}

%define         jdk_version      1.4.2_30
%define         jrockit_version  27.6.9
%define         install_dir      /opt/oracle/jvm/jrockit-jdk142

Name:           jrockit-jdk142-smals
Version:        %{jrockit_version}
Release:        2%{?dist}
Summary:        Oracle JRockit JDK

Group:          Smals/Java
License:        Oracle Binary Code License
URL:            http://www.oracle.com/technetwork/middleware/jrockit/index.html
Source0:        p11931237_276900_LINUX.zip
Source2:        jce_policy-1_4_2.zip

AutoReqProv:    no
ExclusiveOS:    linux
Requires:       libXp(x86-32) libXt(x86-32) gtk2-engines(x86-32) libcanberra-gtk2(x86-32) PackageKit-gtk-module(x86-32)
BuildRequires:  rpm >= 4.6.0

%description
The Oracle JRockit 142 JVM.

%install
umask 007

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/oracle/jvm
pushd $RPM_BUILD_ROOT/opt/oracle/jvm

unzip %{SOURCE0}
mv jrockit-jdk%{jdk_version} jrockit-jdk142
popd

pushd $RPM_BUILD_ROOT%{install_dir}
unzip -o -j %{SOURCE2} *.jar -d jre/lib/security
perl -p -i -e "s#^securerandom.source=.*#securerandom.source=file:/dev/./urandom#g" jre/lib/security/java.security
rm src.zip
rm -rf demo 
rm -rf missioncontrol/samples

find . -type f -exec chmod ugo-x {} \;
find . -type f -name "*.so" -exec chmod u+x {} \;
chmod u+x bin/*
chmod u+x jre/bin/*

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

