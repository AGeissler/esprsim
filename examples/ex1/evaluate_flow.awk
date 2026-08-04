#!/usr/bin/env gawk -f
#
# evaluate_flow.awk - Calculate overall flow rate between zones and
# ambient. Input is a .csv file from ESP-r h3k output.
# The file must contain external connection flow values.
#
# Call with one parameter: <file>
#
BEGIN {
  if ((ARGC<2) || (! EXCON) || (! VOL) || (! NTSTEP)) {
    printf("\n  *** Evaluate mass flow network results ***\n")
    printf("  Call: \n")
    printf("    $ ./evaluate_flow.awk -v EXCON=<excon> -v VOL=<vol> -v NTSTEP=<NN>  <file> \n\n")
    exit_invoked=1
    exit 1
    }

  lines=0
  firstdataline=0

  # Set field separator 
  FS = ","

  # Last line number for column header line in input file
  HEAD=1

  NumTS=strtonum(NTSTEP)

  Volume=strtonum(VOL)

  TimeStep="time step"
  ExFlow="Ext " EXCON
  Con=EXCON

  # m3/h (variables "flow" and "flowrate" are in kg/s !)
  VolFR="volflowrate"

  outCol=1

  # Say hello ...
  printf("\n   Evaluating flow results and doing stuff ...\n")
}
#
{
  if (FNR <= HEAD) {
    # get column numbers which are to be extracted (and save column headers)
    for (col=1; col<NF; col++) {
      # find column with timestep
      if ( index($col,TimeStep) > 0 ) {
          theTStepCol = col
          printf("   theTStepCol=%d\n",col)
      }
      # find all columns with external flow
      if ( index($col,ExFlow) > 0 ) {
        # Check if "volflowrate"
        if ( index($col,VolFR) > 0 ) {
          ExFlowCol[outCol] = col
          ExFlowColString[outCol] = $col
          printf("   ExFlowCol[%d]=%d  ==>%s\n",outCol,ExFlowCol[outCol],ExFlowColString[outCol])
          outCol +=1
        }
      }
    }
  }
  if (FNR > 1) {
    TimeCol[FNR-HEAD] = strtonum($theTStepCol)
    # save values ExFlowCol
    for (col=1; col<NF; col++) {
      ExFlowData[FNR-HEAD,col] = strtonum($ExFlowCol[col])
    }
    lines +=1
  } # end if FNR > 1
}
END {
  if (! exit_invoked  ) {
    # Execute END code only if not exit ...

    # subtract last increment from number of columns
    outCol -=1

    # Set output file name
    filename_ORIG=FILENAME
    filename_ext="_ex-flw_" Con ".csv"
    split(FILENAME,trunk,".") # split at "." ... trunk[1] now contains the root file name including "."
    FILENAME=trunk[1] filename_ext

    # Calculate line sums and overall sum
    TotFlow=0
    for (lin=1; lin<=lines; lin++) {
      FlowSum[lin]=0

      for (col=1; col<=outCol; col++) {
        FlowSum[lin]  += ExFlowData[lin,col]
      }
      TotFlow += FlowSum[lin]
    }

    # Write column headers
    printf("# Volume flow rates (ave ACH = %.3f 1/h) based on an air volume of %.2f m^3 ...\n",TotFlow/lines/Volume,Volume) > FILENAME
    printf("# ") > FILENAME

    # Write header line for new file
    printf("Time,") > FILENAME

    # output data column names
    for (col=1; col<outCol; col++) {
      printf("%s,",ExFlowColString[col]) > FILENAME
    }
    printf("%s,FlowSum\n",ExFlowColString[outCol]) > FILENAME

    # Write data
    for (lin=1; lin<=lines; lin++) {

      printf("%d,",TimeCol[lin]) > FILENAME

      for (col=1; col<outCol; col++) {
        printf("%.2f,",ExFlowData[lin,col]) > FILENAME
      }
      printf("%.2f,%.2f\n",ExFlowData[lin,outCol],FlowSum[lin]) > FILENAME

    }

    printf("   Average ACH for simulation period based on an air volume of %.2f m^3: %.3f 1/h\n",Volume,TotFlow/lines/Volume)

#   Say good buy ...
    printf("                                                              ... done\n\n")
  }
}
