
%global         __os_install_post %{nil}
%global         __arch_install_post %{nil}

%define         jdk_version        1.6.0_51
%define         jdk_short_version  6u51
%define         install_dir        /opt/oracle/jvm/jdk6

Name:           jdk6
Version:        %{jdk_version}
Release:        1%{?dist}
Summary:        Oracle JDK

Group:          Java
License:        Oracle Binary Code License
URL:            http://www.oracle.com/technetwork/java/index.html
Source0:        jdk-%{jdk_short_version}-linux-x64.bin
Source2:        jce_policy-6.zip

AutoReqProv: no
ExclusiveOS: linux

%description
The Oracle 6 JVM.

%install
umask 007
chmod +x %{SOURCE0}

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/oracle/jvm
pushd $RPM_BUILD_ROOT/opt/oracle/jvm

echo | %{SOURCE0}
mv jdk%{jdk_version} jdk6
popd

pushd $RPM_BUILD_ROOT%{install_dir}
unzip -o -j %{SOURCE2} *.jar -d jre/lib/security
perl -p -i -e "s#^securerandom.source=.*#securerandom.source=file:/dev/./urandom#g" jre/lib/security/java.security
rm src.zip

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

