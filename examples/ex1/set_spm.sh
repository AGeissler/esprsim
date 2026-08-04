#!/bin/sh
#  Last changed: 26/09/2017
#  Status: development
#  Script changes special materials file in .cfg. <set_spm> expects three
#  arguments:
#    1. configuration file name w/o ending
#    2. connections file name w/o ending (!!)
#    2. special materials file name (full name incl. ending)
#
CONFIG=$1
CNNFIL=$2
SPMFIL=$3

echo "   In ${CONFIG}.cfg, setting special materials file to: $SPMFIL ... "

prj -file ${CONFIG}.cfg -mode text > ${CONFIG}_set_${SPMFIL}.scratch <<XXX

m  # browse/edit/simulate
c  # composition
n  # active materials
y  # does spm exist?
../dbs/$SPMFIL
-  # exit
-  # exit
!  # save model
${CONFIG}.cfg
${CNNFIL}.cnn
-  # exit
-
XXX

unset CONFIG
unset CNNFIL
unset SPMFIL
