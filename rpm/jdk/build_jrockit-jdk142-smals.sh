#!/bin/bash

topdir=$(readlink -f $(dirname $0))

rpmbuild -bb --define 'dist .el6' --target i686 --define "_topdir $topdir" --buildroot=$topdir/BUILDROOT  $topdir/SPECS/jrockit-jdk142-smals.spec




