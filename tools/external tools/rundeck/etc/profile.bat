set RDECK_HOME=/export/home/weblogic/pp/rundeck

set RDECK_BASE=/export/home/weblogic/pp/rundeck

set JAVA_HOME=/opt/oracle/jvm/jrockit-jdk1.6.0_29-R28.2.2-4.1.0/jre

:: Unsetting JRE_HOME to ensure there is no conflict with JAVA_HOME
(set JRE_HOME=)

set Path=%JAVA_HOME%\bin;%RDECK_HOME%\tools\bin;%Path%

set RDECK_SSL_OPTS="-Djavax.net.ssl.trustStore=%RDECK_BASE%\etc\truststore -Djavax.net.ssl.trustStoreType=jks -Djava.protocol.handler.pkgs=com.sun.net.ssl.internal.www.protocol"