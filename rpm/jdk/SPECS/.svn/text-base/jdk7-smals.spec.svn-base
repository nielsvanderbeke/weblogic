
%global         __os_install_post %{nil}
%global         __arch_install_post %{nil}

%define         jdk_version        1.7.0_40
%define         jdk_short_version  7u40
%define         install_dir        /opt/oracle/jvm/jdk7

Name:           jdk7-smals
Version:        %{jdk_version}
Release:        1%{?dist}
Summary:        Oracle JDK

Group:          Smals/Java
License:        Oracle Binary Code License
URL:            http://www.oracle.com/technetwork/java/index.html
Source0:        jdk-%{jdk_short_version}-linux-x64.tar.gz
Source2:        UnlimitedJCEPolicyJDK7.zip

AutoReqProv: no
ExclusiveOS: linux

%description
The Oracle 7 JVM.

%install
umask 007

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/oracle/jvm
pushd $RPM_BUILD_ROOT/opt/oracle/jvm

tar -zxvf %{SOURCE0} --exclude=src.zip
mv jdk%{jdk_version} jdk7
popd

pushd $RPM_BUILD_ROOT%{install_dir}
unzip -o -j %{SOURCE2} *.jar -d jre/lib/security
perl -p -i -e "s#^securerandom.source=.*#securerandom.source=file:/dev/./urandom#g" jre/lib/security/java.security

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
numfiles=6
checkdir=%{install_dir}/jre/lib/ext

count=`ls -1 $checkdir/*.jar | wc -l`
if [ $count -gt $numfiles ] ; then
    echo "more than $numfiles entries found in $checkdir" >&2
fi

