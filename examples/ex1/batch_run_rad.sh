#!/bin/sh
#
# Run a series of simulations in "batch" mode

# Following shell scripts need to be copied to the cfg-folder:
#TOOLLIST="QA_report.sh change_a_construction.sh simulate_plt.sh res_slab-output_bs.sh res_slab-output_ff.sh res_slab-output_sf.sh slab_supplied_total.awk"
TOOLLIST="QA_report.sh simulate.sh evaluate_SolInc.awk"

# Blank-separated list of model variants to be evaluated. Call this script from the model
# main folder (e.g. /Leadenhall/). Each variant is completely described in a subfolder
# "var" (e.g. "Base") and the configuration file has the same name (e.g. "base.cfg").
VARLIST="AUE"

# Special materials file list
SPMLIST="dir dif"
#SPMLIST="1"

# Set building simulation time steps and simulation period for all cases
TSTEP=4
FD=1
FM=1
TD=31
TM=12
PP=1

# Run simulation cases
for VAR in $VARLIST
do

  for TOOL in $TOOLLIST
  do
    cp $TOOL cfg/$TOOL
  done

  cd cfg

      for SPM in $SPMLIST
      do

        case $SPM in
          dir) theSPM="dir";;
          dif) theSPM="dif";;
        esac

        # copy input.xml to case SPM
        cp input_${SPM}.xml input.xml
		
        # Give message about current simulation set prior to simulation
        echo " "
        echo "== Simulating case $VAR with h3k output via input_$SPM.xml"

        # Build file name for simulation case
        theFile="${VAR}_${theSPM}"

        # remove old results and contents files
        # ... avoid error messages for non-existent files ...
        [ -f ./${theFile}.res ] && rm ./${theFile}.res
        [ -f ./${theFile}.contents ] && rm ./${theFile}.contents

		# .  ./change_construction.sh ${VAR}.CFG $OLDC $NEWC
        . ./QA_report.sh $VAR.cfg ${theFile}.contents
        . ./simulate.sh $VAR.cfg ./${theFile}.res $FD $FM $TD $TM $PP $TSTEP

        [ -f ${VAR}.csv ] && cp ${VAR}.csv ${theFile}.csv

        # Do NOT use . ./<scriptname> for awk scripts !!
        ./evaluate_SolInc.awk -v NTSTEP=$TSTEP ${theFile}.csv

        echo " "

      done # current SPM / complete list

  # Clean up
  for TOOL in $TOOLLIST
  do
    rm $TOOL
  done

  cd ..

done # current VAR / complete list

echo "... done simulating =="
echo " "

# clean up
unset TOOLLIST
unset VARLIST
unset SPMLIST
unset FD
unset FM
unset TD
unset TM
unset PP
unset TSTEP
