#!/bin/sh
#  Last changed: 7/3/2019
#  Status: development
#  Script rotates model around X0,Y0 by ANG , expects four
#  arguments:
#    1. configuration file name root
#    2. rotation angle (degrees counterclockwise)
#    3. X0 in m
#    4. Y0 in m
#
CONFIG=$1
ROTANGLE=$2
X0=$3
Y0=$4

echo "   Rotating ${CONFIG}.cfg, by $ROTANG degrees ... "

prj -file ${CONFIG}.cfg -mode text > ${CONFIG}_rotate_${ROTANG}.scratch <<XXX

m  # browse/edit/simulate
c  # composition
*  # global tasks
b  # rotate
$ROTANGLE
b  # user specified x & y
$X0
$Y0
*  # all items
-  # exit menu
-  # exit menu
!  # save model
y  # update config file

-
-
XXX

unset CONFIG
unset ROTANGLE
unset X0
unset Y0
