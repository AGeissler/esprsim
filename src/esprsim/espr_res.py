#!/usr/bin/env python3

# Last changed: 07/11/2022
# Status: development
#
# Module contains following functions calling res for ESP-r:
#
# 17:  def res_supplied_energy(resfile):
#          """ Extract summary of energy delivered.
#
# 55:  def res_PMV(resfile, zone, PMVdat):
#          """Function extracts PMV data from simulation results.
from subprocess import run

"""
Module contains functions for ESP-r res module text mode scripts.
"""
def res_supplied_energy(resfile):
    r"""Extract summary of energy delivered.

    Parameters
    ----------
    resfile : str | Path
        results file name (with relative path w/o extension)

    """

    print("\n\tExtracting summary of energy delivered from")
    print("\t\t" + resfile + ".res,")
    print("\twriting to")
    print("\t\t" + resfile + "_en-deliv.dat ...", end='')
    
    args = [
            "res",
            "-file", resfile + ".res", # executable file
            "-mode", "text",           # opens file in mode text
            ]
    
    cmd = bytes("d\n"  # Enquire about
                ">\n"  # toggle output to file
                + resfile + "en-deliv.dat\n"
                " \n"  # accept default for 3rd party file
                "^\n"  # delim
                "e\n"  # a) normal spaces; c) tab; e) comma
                "f\n"  # energy delivered
                ">\n"  # flush file
                "-\n"  # exit menu
                "-\n", # exit res
                encoding="utf-8")

    f = open(resfile + "en-deliv_res.scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)

    print(" done.")


def res_PMV(resfile, zone, clo, met, veloc):
    r"""Extract PMV data from simulation results.

    Parameters
    ----------
    resfile : str | Path
        results file name (with relative path w/o extension) ($1).
    zone : str
        Zone name for which evaluation is desired ($2).
    clo : float
        Value of clothing level for PMV calculation ($3).
    met : float
        Value of metabolic rate for PMV calculation ($4).
    veloc : float
        Value of relative air velocity for PMV calculation ($5).

    Notes
    -----
    Optionally call with dict: res_PMV(res, z, **PMV[<var>]),
    where <var> is the list variable of the loop going through a list
    of desired key strings var_list = ('key1', 'keyN').

    """

    thefile = resfile + "_" + zone + "_PMV_" + clo + "_" + met + "_" + veloc + ".dat"

    print("\tWriting PMV for zone " + zone + " to")
    print("\t\t" + thefile + " ...", end='')

    args = [
            "res",
            "-file", resfile + ".res", # executable file
            "-mode", "text",           # opens file in mode text
            ]

    cmd = bytes("\n"   # confirm res file
                "c\n"  # Timestep reports
                "4\n"  # Select zones
                + zone + "\n"
                "-\n"  # exit zone select menu
                ">\n"  # switch output to file
                + thefile + "\n"
                "File:" + thefile + "\n"  # title for 3rd party graphic
                "^\n"  # change delimiter
                "e\n"  # e comma, c tabulator
                "g\n"  # performance metrics
                "c\n"  # comfort metrics
                "a\n"  # PMV
                + clo + "\n"
                "a\n"  # activity level in MET
                + met + "\n"
                + veloc + "\n"
                "b\n"  # occupied only, occupt
                "*\n"  # all items in MRT-Sensor list
                "-\n"  # exit this menu
                "*\n"  # toggle time format
                "a\n"  # no mark between days
                "!\n"  # list data
                ">\n"  # switch display to screen ("flush")
                "-\n"  # exit perf metrics
                "-\n"  # exit tab output
                "-\n", # Quit res analysis
                encoding="utf-8")

    f = open(thefile + "_res.scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)

    print(" done.")

