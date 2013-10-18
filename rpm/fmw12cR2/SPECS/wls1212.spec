
%global         __os_install_post %{nil}
%global         __arch_install_post %{nil}

%define         wls_version          12.1.2
%define         wls_short_version    1212
%define         install_dir          /opt/oracle/fmw/fmw12cR2

Name:           wls-%{wls_short_version}
Version:        %{wls_version}
Release:        2%{?dist}
Summary:        Oracle Weblogic server

Group:          Weblogic
License:        Oracle Weblogic License
URL:            http://www.oracle.com/products/middleware/appserver/index.html
Source0:        wls_%{wls_short_version}00.jar
Source1:        silent.response
source2:        oraInst.loc
Source4:        ojdbc6.jar
source5:        console-weblogic-application.xml

Source10:       p14668913_121200_Generic.zip
AutoReqProv:    no
ExclusiveOS:    linux
Requires:       jdk7
BuildRequires:  jdk7

%description
Oracle Weblogic server %{wls_version}.

%install
umask 007

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{install_dir}
pushd $RPM_BUILD_ROOT%{install_dir}


cat %{SOURCE1} | sed "s:\$BEAHOME:$(pwd):g" > silent.response
cat %{SOURCE2} | sed "s:\$BEAHOME:$(pwd):g" > oraInst.loc
/opt/oracle/jvm/jdk7/bin/java -jar %{SOURCE0} -silent -novalidation -response `pwd`/silent.response -invPtrLoc `pwd`/oraInst.loc
rm silent.response

unzip -o %{SOURCE10} -d patch1212
./OPatch/opatch apply -silent ./patch1212/14668913
rm -rf patch1212
cp %{SOURCE4} oracle_common/modules/oracle.jdbc_11.2.0/.
cp -b %{SOURCE5} wlserver/server/lib/consoleapp/META-INF/weblogic-application.xml

find .  -regex ".*\.\(sh\|xml\|py\|properties\|policy\|cmd\|loc\)" -type f -exec perl -p -i -e "s:$RPM_BUILD_ROOT::g" {} \;

rm -rf logs/*
rm -rf cfgtoollogs/oui/*
rm -rf cfgtoollogs/opatch/*

chmod -R u+w,g+rwX,o+rX .

popd


%clean
rm -rf $RPM_BUILD_ROOT

%post
chown weblogic:weblogic /opt/oracle/fmw
chmod 2775 /opt/oracle/fmw

%files
%defattr(-,weblogic,weblogic,-)
%verify(not size mtime) %{install_dir}
