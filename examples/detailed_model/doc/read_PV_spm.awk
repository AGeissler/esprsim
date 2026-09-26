#! /opt/local/bin/gawk -f
###! /usr/bin/gawk -f
#
# read_PV_spm.awk - Read a special materials definition file with PV
# entries only (for now!). Convert to one-line-per-entry csv file for
# editing in Excel
#
# Call: ./read_PV_spm.awk <spm-file>
# Output: <spm-file.csv>
#
BEGIN {
  if (ARGC<2) {
    printf("  *** Read from file ***\n")
    printf("  Call: \n")
    printf("    $ ./read_PV_spm.awk <spm-file> \n")
    exit 1
    }

  entry_line=0
  entry_num=1

  # Set field separator to <whitespace>
  FS = " "

  # Last line number for column header line in input file
  HEAD=3

  # Say hello ...
  printf("\n   Reading file %s ...\n",ARGV[1])
}
#
{
  if (FNR <= HEAD) {
    if (FNR == 2) {
      ConfigFile=$4
    }
    if (FNR == 3) {
      NumEntries=strtonum($1)
      printf("     %d entries in file\n",NumEntries)
    }
  } else {
    entry_line += 1

    if (entry_line == 2) {
      # Read spm name
      PVName[entry_num]=$1
    }
    if (entry_line == 3) {
      # do nothing
    }
    if (entry_line == 4) {
      # Read zone, surf, node, type, opq/trn toggle
      Zone[entry_num]=strtonum($1)
      Surf[entry_num]=strtonum($2)
      Node[entry_num]=strtonum($3)
      Type[entry_num]=strtonum($4)
      TrnOp[entry_num]=strtonum($5)
    }

    if (entry_line == 5) {
      # do nothing
    }

    if (entry_line == 6) {
      # Read number of data items
      Items[entry_num]=strtonum($1)
    }

    if (entry_line == 7) {
      # do nothing
    }

    # First line of data (items 1 through (max.) 10)
    if (entry_line == 8) {
      # Read data items
      NFData1[entry_num]=NF
      for (i=1; i<=NF; i++ ) {
        Data[entry_num,i]=$i
      }
      if (NFData1[entry_num] != 10) {
        printf(" *** WARNING data line 1 entry %d: %d != 10\n",entry_num,NFData1[entry_num])
      }
    }
    #
    # Conditional reading of further data lines
    #
    if (entry_line == 9) {
      # Read data items
      NFData2[entry_num]=NF
      for (i=1; i<=NF; i++ ) {
        Data[entry_num,i+NFData1[entry_num]]=$i
      }
      if (Items[entry_num] > 20) {
        # line should have 10 entries!
        if (NFData2[entry_num] != 10) {
          printf(" *** WARNING data line 2 entry %d: %d != 10\n",entry_num,NFData2[entry_num])
        }
      } else {
        # Last line of this entry,
        NFData3[entry_num]=0
        # increment entry counter
        entry_num += 1
        # and reset entry_line for next entry
        entry_line = 0
      }
    }

    if (entry_line == 10) {
      # Read data items from third data line
      NFData3[entry_num]=NF
      N3offset=NFData1[entry_num]+NFData2[entry_num]
      for (i=1; i<=NF; i++ ) {
        Data[entry_num,i+N3offset]=strtonum($i)
      }
      if (N3offset+NF != Items[entry_num]) {
        printf(" *** WARNING data line 3 entry %d: %d != %d\n",entry_num,N3offset+NF,Items[entry_num])
      }
      # Last line of this entry,
      # increment entry counter
      entry_num += 1
      # and reset entry_line for next entry
      entry_line = 0
    }
  }
}
END {
  # Build output file name
  filename_ext="csv"
  split(FILENAME,trunk,".") # split at "." ... trunk[1] now contains the root file name
  FILENAME=trunk[1] "." filename_ext

  # Write header line
  printf("ConfigFile,Nr. Nodes,Node Nr.,Name,Zone,Surf,Node,Type,OpqTrn,Nr. Items,") > FILENAME
  printf("VocRef,IscRef,VmpRef,ImpRef,Qref,Tref,Alpha,Gamma,Beta,SCell,NPBrch,")>FILENAME
  printf("NPnnls,LodT,Valf,Shad,MiscLossFac,aRef0,aRef40,aRef55,aRef70,aRef80\n") > FILENAME

  # Write data line for each entry
  for (line=1; line<entry_num; line++) {

    printf("%s,%d,%d,%s,",ConfigFile,NumEntries,line,PVName[line]) > FILENAME
    printf("%d,%d,%d,%d,%d,",Zone[line],Surf[line],Node[line],Type[line],TrnOp[line]) > FILENAME
    printf("%d,",Items[line]) > FILENAME

#    for (col=1; col<=NFData1[line]; col++) {
#      printf("%s,",Data[line,col]) > FILENAME
#    }

#    for (col=NFData1[line]+1; col<(NFData1[line]+NFData2[line]); col++) {
    for (col=1; col<(NFData1[line]+NFData2[line]+NFData3[line]); col++) {
      printf("%s,",Data[line,col]) > FILENAME
    }

    printf("%s\n",Data[line,(NFData1[line]+NFData2[line]+NFData3[line])]) > FILENAME

  }

  # Say good buy ...
  printf("   ... done with reading %d entries\n\n",entry_num-1)

}
