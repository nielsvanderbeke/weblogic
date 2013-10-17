#!/bin/bash

topdir=$(readlink -f $(dirname $0))

rpmbuild -bb --define 'dist .el5' --define "_topdir $topdir" --buildroot=$topdir/BUILDROOT  $topdir/SPECS/wls1212.spec
rpmbuild -bb --define 'dist .el6' --define "_topdir $topdir" --buildroot=$topdir/BUILDROOT  $topdir/SPECS/wls1212.spec



