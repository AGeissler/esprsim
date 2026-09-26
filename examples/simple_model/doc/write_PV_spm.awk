#! /opt/local/bin/gawk -f
###! /usr/bin/gawk -f
#
# write_PV_spm.awk - Write a special materials definition file with PV
# entries only (for now!). Convert from one-line-per-entry csv file
#
# Call: ./write_PV_spm.awk <data-file.csv>
# Output: <spm-file.spm>
#
BEGIN {
  if (ARGC<2) {
    printf("  *** Write a spm file with PV ***\n")
    printf("  Call: \n")
    printf("    $ ./write_PV_spm.awk <data-file.csv> \n")
    exit 1
    }

  # Set field separator to <comma>
  FS = ","

  # Say hello ...
  printf("\n   Reading file %s ...\n",ARGV[1])
}
#
{
  if (FNR > 1) {
    for (fn=1; fn<NF; fn++) {
      Field[FNR-1,fn]=$fn
    }
    # The last field contains the newline which should be removed
    sub("\r","",$NF)
    Field[FNR-1,NF]=$NF
  }
}
END {
  # Build output file name
  filename_ext=".spm"
  split(FILENAME,trunk,".") # split at "." ... trunk[1] now contains the root file name
  FILENAME=trunk[1] "_csv" filename_ext

  printf("\n   ... now writing file %s ...\n",FILENAME)

  # Write file head
  printf("# ESP-r special materials file used in\n") > FILENAME
  printf("# configuration file %s\n",Field[1,1]) > FILENAME
  printf(" %3d  # Number of special material nodes.\n",strtonum(Field[1,2])) > FILENAME

  # Write data for each entry
  for (spm=1; spm<=strtonum(Field[1,2]); spm++) {

    printf("# Node No: %3d\n",strtonum(Field[spm,3])) > FILENAME

    printf("%s     # label\n",Field[spm,4]) > FILENAME

    printf("# Zone Surf Node Type Opq/Trn\n") > FILENAME
    for (fn=5; fn<=9; fn++) {
      printf(" %3d",strtonum(Field[spm,fn])) > FILENAME
    }
    printf("\n") > FILENAME

    printf("# Number of data items.\n") > FILENAME

    NFData=strtonum(Field[spm,10])
    printf(" %3d\n",NFData) > FILENAME

    printf("# Data:\n") > FILENAME

    # Print first 10 data items ...
    for (fn=11; fn<=20; fn++) {
      printf("   %s ",Field[spm,fn]) > FILENAME
    }
    printf("\n") > FILENAME

    # Conditionally print next data items
    if (NFData>10) {
      if (NFData<=20) {
        for (fn=21; fn<(11+NFData); fn++) {
          printf("    %s ",Field[spm,fn]) > FILENAME
        }
        printf("\n") > FILENAME
      } else {
        for (fn=21; fn<=30; fn++) {
          printf("    %s ",Field[spm,fn]) > FILENAME
        }
        printf("\n") > FILENAME

        for (fn=31; fn<(11+NFData); fn++) {
          printf("    %s ",Field[spm,fn]) > FILENAME
        }
        printf("\n") > FILENAME
      }
    }
  }

  # Say good buy ...
  printf("   ... done with writing %d entries\n\n",Field[1,2])

}
