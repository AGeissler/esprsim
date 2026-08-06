#!/bin/sh
#
# Run a series of simulations in "batch" mode

Arg1=$1

if [[ -n "$Arg1" ]]; then
  SIMU="FALSE"
else
  SIMU="TRUE"
fi

# Following shell scripts need to be copied to the cfg-folder:
TOOLLIST="set_spm.sh set_afn.sh set_new_rotang.sh QA_report.sh simulate_afn.sh \
          evaluate_PV.awk evaluate_flow.awk \
          plot_mult_R_evaluations.r plot_PV_efficiency.r"

# Blank-separated list of model variants to be evaluated. Call this script from the model
# main folder (e.g. /Leadenhall/). Each variant is completely described in a subfolder
# "var" (e.g. "Base") and the configuration file has the same name (e.g. "base.cfg").
VARLIST="PVT_Douala"

# Special materials file list
SPMLIST="1"
#SPMLIST="1 2 3"

# Air flow networks file list
#AFNLIST="force_flow buoyant_flow no_flow"
#AFNLIST="buoyant_flow buoyant_flow2"
AFNLIST="buoyant_flow"

# Exposition list
#EXPLIST="South North"
EXPLIST="South"

# Simulation period
PERLIST="test"

# Set default values for rotation and back rotation
RX=7.5
RY=3.0
DEFAFN="no_flow_S"

# Set building simulation time steps and simulation period for all cases
TSTEP=10
PP=15

# Run simulation cases
for VAR in $VARLIST
do

  for TOOL in $TOOLLIST
  do
    cp $TOOL cfg/$TOOL
  done

  cd ./cfg

  [ ! -d ./${VAR}_scratchfiles ] && mkdir ${VAR}_scratchfiles

  for EXP in $EXPLIST
  do

    case $EXP in
      South) ROTANG=0
             ROTBACK=0
             ROT="S";;
      North) ROTANG=180
             ROTBACK=180
             ROT="N";;
    esac

    for AFN in $AFNLIST
    do
      case $AFN in
        force_flow)   CURAFN="frce";;
        buoyant_flow) CURAFN="bouy";;
        buoyant_flow2) CURAFN="bouy2";;
        no_flow)      CURAFN="nofl";;
      esac

      for SPM in $SPMLIST
      do

#        case $SPM in
#          1) theSPM="PVtype_${SPM}";;
#          2) theSPM="PVtype_${SPM}";;
#          3) theSPM="PVtype_${SPM}";;
#        esac

        for PER in $PERLIST
        do

          case $PER in
            test)  FD=2
                   FM=2
                   TD=7
                   TM=2
                   PP=3;;
            month) FD=1
                   FM=3
                   TD=31
                   TM=3
                   PP=12;;
            year)  FD=1
                   FM=1
                   TD=31
                   TM=12;;
          esac

          # Build file name for simulation case
          theFile="${VAR}_${ROT}_${CURAFN}_PVtype_${SPM}"

          # Give message about current simulation set prior to simulation
          # (see https://misc.flogisoft.com/bash/tip_colors_and_formatting
          #  for optional bells and whistles ...)
          RightNow=`date`
          echo " "
          echo "=========================================== "
          if [ $SIMU == "TRUE" ]; then
            echo "== Simulating case $theFile, $RightNow "
          else
            echo "== Evaluating case $theFile with R ((not activated!)) "
          fi
          echo "=========================================== "
          echo "     - with exposition $EXP "
          echo "     - using air flow network ${AFN}_${ROT} "
          echo "     - with special material PVtype_${SPM} "
          echo "     - for period $PER "
          echo " "

#=== start simulate block
          if [ $SIMU == "TRUE" ]; then

            # remove old results and contents files
            # ... avoid error messages for non-existent files ...
            [ -f ./${theFile}.res ] && rm ./${theFile}.res
            [ -f ./${theFile}.contents ] && rm ./${theFile}.contents

            # Set model features ...
#            . ./set_spm.sh ${VAR} ${VAR} PVtype_${SPM}.spm
            . ./set_new_rotang.sh ${VAR} ${ROTANG} ${RX} ${RY}
            . ./set_afn.sh ${VAR} ${AFN}_${ROT}

            # Write QA report and simulate
            . ./QA_report.sh ${VAR} ${theFile}.contents
            . ./simulate_afn.sh ${VAR} ${theFile} $FD $FM $TD $TM $PP $TSTEP

            [ -f ${VAR}.csv ] && mv ${VAR}.csv ${theFile}.csv

            # Create subdirectory for current run and move all corresponding
            # files there.
            echo "   Now moving all created files to subdirectory ${theFile} ..."
            if [ -d ${theFile} ]; then
              rm -fr ${theFile}
            fi
            mkdir ${theFile}
            mv ${theFile}*.* ${theFile}
            mv *.scratch ${VAR}_scratchfiles
            mv out.xml ${theFile}
            echo "   ... done"
            echo " "

          fi # closes simulation block starting line 163
#=== end simulate block

          # Do NOT use . ./<scriptname> for awk scripts !!
          ./evaluate_PV.awk -v NTSTEP=$TSTEP ${theFile}/${theFile}.csv
          ./evaluate_flow.awk -v EXCON="N00" -v VOL=0.45 -v NTSTEP=$TSTEP ${theFile}/${theFile}.csv
          ./evaluate_flow.awk -v EXCON="N20" -v VOL=0.45 -v NTSTEP=$TSTEP ${theFile}/${theFile}.csv
          ./evaluate_flow.awk -v EXCON="N40" -v VOL=0.45 -v NTSTEP=$TSTEP ${theFile}/${theFile}.csv

          mv ${theFile}/*.scratch ${VAR}_scratchfiles

          ./plot_mult_R_evaluations.r ${theFile}/${theFile}.csv

        done # current PER / complete list

      done # current SPM / complete list

    done # current AFN / complete list

  done # current EXP / complete list

#=== start simulate block
  if [ $SIMU == "TRUE" ]; then

    # Rotate model back to original position & set default afn
    . ./set_new_rotang.sh ${VAR} ${ROTBACK} ${RX} ${RY}
    . ./set_afn.sh ${VAR} ${DEFAFN}
    mv *.scratch ${VAR}_scratchfiles

  fi # closes simulation block starting line 396
#=== end simulate block

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
unset AFNLIST
unset ROTANGLIST
unset PERLIST
unset FD
unset FM
unset TD
unset TM
unset PP
unset TSTEP
