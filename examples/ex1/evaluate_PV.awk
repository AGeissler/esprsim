#! /opt/local/bin/gawk -f
###! /usr/bin/gawk -f
#
### #!/bin/sh
### arbitrary_long_name==0 "exec" "/usr/bin/gawk" "--re-interval" "-f" "$0" "$@"

#
# evaluate_PV.awk - Calculate PV power sums for different time intervals
# Input is a .csv file from ESP-r h3k output. The file must contain
# pv_power values (to date only available from WATSUN model (type 5)).
#
# Call with two parameters: -v NTSTEP=<NN> <file>
#
# Version 07/05/2015
#
BEGIN {
  if (ARGC<2) {
    printf("  *** Read from file ***\n")
    printf("  Call: \n")
    printf("    $ ./evaluate_PV.awk -v NTSTEP=<NN>  <file> \n")
    exit 1
    }

  # Max. size for rows x columns (Cygwin restraint); if this size is
  # exceeded, the read/write is split
  MaxSize=12000000
  SplitProcess=0
  WriteHeader=0
  SplitEnd[0]=1
  MonthsWritten[0]=0

  lines=0
  firstdataline=0

  # Set field separator 
  FS = ","

  # Last line number for column header line in input file
  HEAD=1

  TimeStep="time step"
  PV_power="pv power"
  SolDir="direct normal radiation"
  SolDif="diffuse horizontal radiation"
  TotIncRad="incident irradiance:unit area"

  # Timesteps per hour, timestep of data in hours, timestep in minutes
  NTS=strtonum(NTSTEP)
  TS=1./NTS     # Timestep in [h] (e.g. NTS=10, TS=0.1 hours, aka 6 min)
  TSMIN=60/NTS  # Timestep duration in minutes

  outCol=1
  theEnd=0

  # Say hello ...
  printf("\n   Evaluating PV power results and calculating sums ...\n")
}
#
{
  if (FNR <= HEAD) {
    # get column numbers which are to be extracted (and save column headers)
    for (col=1; col<NF; col++) {
      # find column with timestep
      if ( index($col,TimeStep) > 0 ) {
          theTStepCol = col
#          printf("   theTStepCol=%d\n",col)
      }
      # find column with direct solar
      if ( index($col,SolDir) > 0 ) {
          theSolDirCol = col
          printf("   theSolDirCol=%d\n",col)
      }
      # find column with diffuse solar
      if ( index($col,SolDif) > 0 ) {
          theSolDifCol = col
          printf("   theSolDifCol=%d\n",col)
      }
      # find column with total incident solar on ref. panel
      if ( index($col,TotIncRad) > 0 ) {
          theTotIncRadCol = col
          printf("   theTotIncRadCol=%d\n",col)
      }
      # find all columns with PV_power
      if ( index($col,PV_power) > 0 ) {
        PVPowerCol[outCol] = col
        # Strip leading "building:spmatl" and trailing "misc data:pv power (W)"
        # Then build header text for column
        split($col,trunk,":")
        PVPowerColString[outCol] = trunk[3] " [Wh]"
#        printf("   PVPowerCol[%d]=%d contains %s\n",outCol,PVPowerCol[outCol],PVPowerColString[outCol])
        outCol +=1
      }
    }

    # subtract last increment from number of columns
    outCol -=1

  }
  if (FNR > 1) {
    lines +=1

    TimeCol[lines] = strtonum($theTStepCol)
    SolDirCol[lines] = strtonum($theSolDirCol)
    SolDifCol[lines] = strtonum($theSolDifCol)
    TotIncRadCol[lines] = strtonum($theTotIncRadCol)
    # save values PVPowerCol
    for (col=1; col<=outCol; col++) {
      PVPowerData[lines,col] = strtonum($PVPowerCol[col])
    }

    # Check neccessary size of matrix against MaxSize
    if ( lines*NF > MaxSize ) {
      # Increment split count variable
      SplitProcess++
      SplitStart[SplitProcess]=SplitEnd[SplitProcess-1]

      # DEBUG:  printf("Split %d! Size: %d\n",SplitProcess,lines*NF)

      # Split output, set split point index to first hour of current
      # month and write data up to previous hour (last hour of previous month)
      counter = 0
      mon=MonthsWritten[SplitProcess-1]+1
      while ( counter < MaxSize/NF ) {
        counter += NTS*24*DaysInMonth(mon)
        # DEBUG:  printf("mon= %d, counter= %d\n",mon,counter)
        mon++
      }
      SplitEnd[SplitProcess]=counter-NTS*24*DaysInMonth(mon)
      MonthsWritten[SplitProcess]=mon-1

      save_lines=lines

      # DEBUG:  printf("Start %d, End %d, lines %d, months written %d\n",SplitStart[SplitProcess],SplitEnd[SplitProcess],lines,MonthsWritten[SplitProcess])

      lines=SplitEnd[SplitProcess]

      CalcAndWriteAll()

      # Copy lines not yet written to beginning of data storage arrays.
      # Logic assumes less data is *not* written than written!!
      buf_lines = save_lines - SplitEnd[SplitProcess]

      # DEBUG:  printf("\nbuf_lines=%d\n",buf_lines)

      for (line=1; line<=buf_lines; line++) {
        TimeCol[line] = TimeCol[line+lines]
        TotIncRadCol[lines] = TotIncRadCol[line+lines]
        for (col=1; col<=outCol; col++) {
          PVPowerData[line,col] = PVPowerData[line+lines,col]
        }
      }
      # reset lines counter to end of buffered lines
      lines = buf_lines
    }

  } # end if FNR > 1
}
END {

  theEnd=1
  # Dump any data not written yet ...
  CalcAndWriteAll()

  # Say good buy ...
  printf("\n                             ... done\n\n")

}

###############################################################################
#
#
function CalcAndWriteAll() {

#  CalcAndWrite(1,"1min") # NTS=60 => TSMIN = 1
                         # NTS=10 => TSMIN = 6

#  CalcAndWrite(5,"5min")

#  CalcAndWrite(12,"12min")

#  CalcAndWrite(15,"15min")

  CalcAndWrite(NTS*TSMIN,"1hour")        # Number of TS per hour * Time step in min

  CalcAndWrite(NTS*TSMIN*24,"1day")      # Number of TS per hour * Time step in min * 24 h

  CalcAndWrite(NTS*TSMIN*24*30,"1month")  # Number of TS per hour * Time step in min * 24 h * 30 days

  CalcAndWrite(NTS*TSMIN*24*365,"1year") # Number of TS per hour * Time step in min * 24 h * 365 days

  WriteHeader=1  # header should only be written once in each file

}

###############################################################################
# Calculate sums and write to file.
# Parameters:
#   Intvl  :  Length of evaluation interval in minutes. Values are summed up for
#             these intervals and derived metrics calculated for these sums.
#   sIntvl :  Output file name extension used.
#
function CalcAndWrite(Intvl,sIntvl) {
  printf("\n      Evaluating %s ...  ",sIntvl)
  Interval=Intvl/TSMIN
  sInterval=sIntvl

  MinutesInMonth=NTS*TSMIN*24*30

  # Check if number of time steps allows interval
  if (Intvl < TSMIN) {
    printf("   > Simulation time step %d min too large for evaluation at interval length %s!\n",TSMIN,sIntvl)
    return;
  }

  # Check, if enough data available
  if (lines<Intvl/TSMIN) {
    printf("   > Not enough data for evaluation at interval length %s!\n",sIntvl)
    return;
  }

  # Set output file name
  filename_ORIG=FILENAME
  filename_ext="_" sInterval ".dat"
  split(FILENAME,trunk,".") # split at "." ... trunk[1] now contains the root file name including "."
  FILENAME=trunk[1] filename_ext

  if (WriteHeader == 0) {

    # Print column headers
    printf("# Electric energy production in [Wh] for time intervals of %s\n",sInterval) > FILENAME
    printf("# ") > FILENAME

    # Write header line for new file
    printf("Time,") > FILENAME

    # Output data column names
    for (col=1; col<outCol; col++) {
      printf("%s,",PVPowerColString[col]) > FILENAME
    }
    printf("%s,Sum [Wh],SunHours [h],TotIncRad [Wh/m2]\n",PVPowerColString[outCol]) > FILENAME
  } # Write header

  # Calculate metrics for desired interval lengths
  # and write to file
  if (SplitProcess == 0) {
    CurMonth=0
  } else {
    if (theEnd == 0)
      # Intermediate split process
      CurMonth=MonthsWritten[SplitProcess-1]
    else
      # Dump of remaining data in "End" block
      CurMonth=MonthsWritten[SplitProcess]-1
  }
  StartNextMonth=1

  # DEBUG:  printf("CurMonth= %d, lines= %d\n",CurMonth,lines)

  # NOTE: "<lines" and not "<=" because of empty line at end of file ...
  for (line=1; line<lines; line++) {
    # Set interval length for calculation of sums over interval
    # For "monthly" evaluation, "Interval" should be set according to
    # the month lenghts!
    if (Intvl == MinutesInMonth) {
      # we are doing monthly values ...
      if (line == StartNextMonth) {
        CurMonth +=1
         if (CurMonth > 12) { printf("\n\n ** month > 12 !! ***\n\n"); exit; }
        Interval = NTS*24*DaysInMonth(CurMonth)
        StartNextMonth += Interval
        # DEBUG:  printf("CurMonth=%d, Interval=%d, StartNextMonth=%d, line=%d\n",CurMonth,Interval,StartNextMonth,line)
      }
    }
    intmax=line+Interval-1;

    for (col=1; col<=outCol; col++) {
      PVProductionSum[col] = 0.
      SunTS[col] = 0
    }
    TotIncRadSum = 0.

    for (col=1; col<=outCol; col++) {
      for (linsum=line; linsum<=intmax; linsum++) {
        # Electrical energy production in timestep, [Wh]
        PVProductionSum[col]  += PVPowerData[linsum,col]*TS
        if (col==1) {
          # Only add up once!
          TotIncRadSum += TotIncRadCol[linsum]*TS
        }
        if ( (SolDirCol[linsum]+SolDifCol[linsum]) > 0. ) {
          # Number of Timesteps with solar > 0
          SunTS[col] +=1
        }
      } # for linsum
    }
    # set "line" for jump to next interval
    line=linsum-1

    printf("%d,",TimeCol[intmax]) > FILENAME

    SumOfLine=0.

    for (col=1; col<outCol; col++) {
      if (SunTS[col] > 0) {
        SumOfLine +=PVProductionSum[col]
        printf("%.2f,",PVProductionSum[col]) > FILENAME
      } else {
        printf("%.2f,",0.) > FILENAME
      }
    }
    if (SunTS[outCol] > 0) {
      SumOfLine +=PVProductionSum[outCol]
      printf("%.2f,%.2f,%.1f,%.2f\n",PVProductionSum[outCol],SumOfLine,SunTS[outCol]*TS,TotIncRadSum) > FILENAME
    } else {
      printf("%.2f,%.2f,%.1f,%.2f\n",0.,0.,0.,0.) > FILENAME
    }

  } # for (line ...

  FILENAME=filename_ORIG

} # End function CalcAndWrite()


function ABS(value)
{
  return (value<0?-value:value);
}

function DaysInMonth(month)
{
    _tm_months[0,1] = _tm_months[1,1] = 31
    _tm_months[0,2] = 28; _tm_months[1,2] = 29
    _tm_months[0,3] = _tm_months[1,3] = 31
    _tm_months[0,4] = _tm_months[1,4] = 30
    _tm_months[0,5] = _tm_months[1,5] = 31
    _tm_months[0,6] = _tm_months[1,6] = 30
    _tm_months[0,7] = _tm_months[1,7] = 31
    _tm_months[0,8] = _tm_months[1,8] = 31
    _tm_months[0,9] = _tm_months[1,9] = 30
    _tm_months[0,10] = _tm_months[1,10] = 31
    _tm_months[0,11] = _tm_months[1,11] = 30
    _tm_months[0,12] = _tm_months[1,12] = 31

   return(_tm_months[0,month]);
}
