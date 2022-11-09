#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Last changed: 22/09/2020
# Status: Should work ...
# Module contains following functions for ESP-r:
#
# 27:  def qa_report(config, variant):
#            Create QA report.
# 118: def simulate(mode, config, variant, start_day, start_month,
#                         end_day, end_month, pre_days, time_steps):
#            Simulate a model, building domain, only.
# 202: def set_ctl(config, ctl_file):
#            Set the control file to "ctl_file".
# 232: def set_clm(config, spm_file):
#            Set climate file to "clm_file".
# 271: def set_spm(config, cnn_file, spm_file):
#            Set special materials file to "spm_file".
# 441: def set_plant(config, plant, plant_db):
#            Set plant network file in .cfg.
# 481: def set_obs_dim(config, zone, obs, width, depth, height):
#            Set obstruction dimensions.
# 522: def set_con(config, cnn_file, old_roomclass, old_roomcon,
#                                    new_roomclass, new_roomcon):
#            Switch a construction ...
# 609: def set_ctl_temp_setpt()
#            Set setpoint temperature for building domain control.

"""
Module contains functions for ESP-r scripts and auxiliary functions for
batch running of simulations.
"""

def qa_report(config, variant):
    """Create QA report.

    arguments:
    [1] configuration file name without extension
    [2] variant name (ctl, con, mat)"""

    from subprocess import run

    print("\tQA report         : " + variant + ".contents")

    # Creating QA report
    args = [
            "prj",
            "-file", config + ".cfg",  # executable file
            "-mode", "text",  # opens file in mode text
            ]

    cmd = bytes("m\n"  # browse/ edit/ simulate
                "u\n"  # QA reporting
                "N\n"  # Format the contents report in Markdown? [Y/N]
                "a\n"  # site info (toggle)
                "c\n"  # model context (toggle)
                "d\n"  # controls (toggle)
                "g\n"  # zone selection
                "*\n"  # all items
                "-\n"  # exit menu
                "m\n"  # file names (toggle)
                ">\n"  # QA report to
                + variant + ".contents\n"  # model contents file
                + config + ".cnn\n"        # cnn file
                "!\n"  # generate QA report
                "-\n"  # exit menu
                "-\n"  # exit this menu
                "-\n",  # exit Project Manager
                encoding="utf-8")

    f = open(variant + "_qa.scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)


""" ============================================
    Auxiliary functions for simulation domain management """
def list_dms(dms, variant):
    switcher = {
        1: "\tbuilding results  : " + variant + ".res",
        2: "\tbuilding results  : " + variant + ".res\n" +
           "\tair flow results  : " + variant + ".mfr",
        3: "\tbuilding results  : " + variant + ".res" +
           "\tplant results     : " + variant + ".plr",
        4: "\tbuilding results  : " + variant + ".res\n" +
           "\tplant results     : " + variant + ".mfr\n" +
           "\tair flow results  : " + variant + ".plr"
    }
    return switcher.get(dms, "Error in dms")

def rf_dms(dms, variant):
    switcher = {
    1: bytes("" + variant + ".res\n",  # zone results library name
             encoding= 'utf-8' ),
    2: bytes("" + variant + ".res\n"  # zone results library name
             "" + variant + ".mfr\n",  # mass flow results library name
             encoding= 'utf-8' ),
    3: bytes("" + variant + ".res\n"  # zone results library name
             "" + variant + ".plr\n",  # plant results library name
             encoding= 'utf-8' ),
    4: bytes("" + variant + ".res\n"  # zone results library name
             "" + variant + ".mfr\n"  # plant results library name
             "" + variant + ".plr\n",  # mass flow results library name
             encoding= 'utf-8' ),
    }
    return switcher.get(dms, "Error in dms - rf")

def ts_dms(dms, BTSTEP, PTSTEP):
    switcher = {
    1: bytes("" + str(BTSTEP) + "\n",  # building time-steps (per hour)
             encoding= 'utf-8' ),
    2: bytes("" + str(BTSTEP) + "\n",  # building time-steps (per hour)
             encoding= 'utf-8' ),
    3: bytes("" + str(BTSTEP) + "\n"   # building time-steps (per hour)
             "" + str(PTSTEP) + "\n",  # plant time-steps (per hour)
             encoding= 'utf-8' ),
    4: bytes("" + str(BTSTEP) + "\n"   # building time-steps (per hour)
             "" + str(PTSTEP) + "\n",  # plant time-steps (per hour)
             encoding= 'utf-8' ),
    }
    return switcher.get(dms, "Error in dms - ts")
""" End auxiliary functions 
    ============================================= """    


def simulate(dms, config, variant, BTSTEP, PTSTEP, FD, FM, TD, TM, PP):
    """Function runs simulation for model with dms domains involved.

    Required output files depending on simulation mode.
    1 building only, .res
    2 building and afn, .res, .mfr
    3 building and plant, .res, .plr
    4 building, afn and plant, .res, .plr, .mfr
    ... (eln, ??)

    Arguments:
    [1]      key for domains in model
    [2]      configuration file name without extension
    [3]      variant name (ctl, con, mat)
    [4]      number of days for start-up period duration
    [5]      building simulation time steps per hour
    [6]      plant time steps per building time step
    [7 to 10] start- and end dates for simulation period via dict
    """

    from subprocess import run
    import glob
    import shutil

    print("\tRun bps with      : " + config + ".cfg")
    print(list_dms(dms,variant))
    print("\tSimulation period : " + FD + "." + FM + ". to "
          + TD + "." + TM + ". with startup " + PP + " days using")
    if ((dms == 1) | (dms == 2)) is True:
        print("\t                    " + BTSTEP + " building ts per hour.")
        
    if ((dms == 3) | (dms == 4)) is True:
        print("\t                    " + BTSTEP + " building ts per hour and "
              + PTSTEP*BTSTEP + " plant ts per hour.")

    # Running Simulation
    args = [
        "bps",
        "-file", config + ".cfg",  # executable file (should be passed as variable from run_all)
        "-mode", "text",  # opens file in mode text
    ]

    """
    Build command for text mode.
    """
    cmd1 = bytes("\n"  # skip "model configuration file?"
                 "c\n",  # initiate simulation
                 encoding="utf-8")
    
    cmd2 = rf_dms(dms, variant)
    
    cmd3 = bytes("" + FD + " " + FM + "\n"  # start day & month (DD MM)
                 "" + TD + " " + TM + "\n"  # end day & month (DD MM)
                 "" + PP + "\n",  # start-up period duration (days)
                 encoding="utf-8")

    cmd4 = ts_dms(dms, BTSTEP, PTSTEP)

    cmd5 = bytes("N\n"  # hourly results integration? [Y/N]
                 "*\n"  # Save 3
                 "*\n"  # Save 4
                 "s\n"  # commence simulation
                 "Y\n"  # use suggested control file [Y/N]
                 "Run:" + variant + "\n"  # result-set description
                 "Y\n"  # continue with simulation? [Y/N]
                 "Y\n"  # save simulation results? [Y/N]
                 "-\n"  # exit menu
                 "-\n", # quit module
                 encoding="utf-8")

    cmd = cmd1.decode('utf-8')   \
          + cmd2.decode('utf-8') \
          + cmd3.decode('utf-8') \
          + cmd4.decode('utf-8') \
          + cmd5.decode('utf-8')
    
    cmd = cmd.encode('utf-8')

    f = open(variant + "_bps.scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs bps (args), executes commands (cmd), writes scratch file (f)

    # Postprocessing
    for line in open(variant + "_bps.scratch"):
        if "CPU time:" in line:
            print("\n\t" + line)
#        if "XML postprocessor cpu runtime" in line:
#            print(line)

    for file in glob.glob("../tmp/" + variant + ".*"):
        shutil.move(file, './')


def set_ctl(config, ctl_file):
    """Function sets control file in .cfg of model.

    arguments:
    [1] configuration file name without extension
    [2] control file name without extension"""

    from subprocess import run

    print("\tSet control file  : " + ctl_file + ".ctl")

    # Setting control file
    args = [
            "prj",
            "-file", config + ".cfg",  # executable file
            "-mode", "text",  # opens file in mode text
            ]

    cmd = bytes("m\n"  # browse/ edit/ simulate
                "i\n"  # controls: zones
                "../ctl/" + ctl_file + ".ctl\n"  # control file?
                "-\n"  # exit this menu
                "Y\n"  # ctl-functions have not yet been associated w/ zones. exit anyway? [Y/N]
                "Y\n"  # save changes to control file? [Y/N]
                "Y\n"  # overwrite this file? [Y/N]
                + config + ".cnn\n"  # cnn file
                "-\n"  # exit this menu
                "-\n", # exit Project Manager
                encoding="utf-8")

    f = open(config + "_set_" + ctl_file + ".scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)


def set_clm(config, clm_file):
    """Function sets climate file
    
    Arguments:
    [1] configuration file name without extension
    [2] full climate file name """
    
    import os
    from subprocess import run
    
    print("\tSet clm file      : " + clm_file)
    
    # Setting SPM-file
#    args = [
#            "prj",
#            "-file", config + ".cfg",  # executable file
#            "-mode", "text",  # opens file in mode text
#            ]

        # Change climate file via sed ((hack due to bug in prj text mode))
        
    wd=os.getcwd() # must be <modelpath>/cfg <<check?>>
    
    cmd1='cp ' + config + '.cfg temp.cfg'

    new_clm='*clm ../dbs/' + clm_file
    
    cmd2='sed \'s%\*clm ../dbs/.*%' + new_clm + '%\' temp.cfg > ' + config + '.cfg'
        
    cmd3='rm temp.cfg'

    run(cmd1, shell=True, cwd=wd)
    run(cmd2, shell=True, cwd=wd)
    run(cmd3, shell=True, cwd=wd)

#    cmd = bytes("b\n"  # db management
#                "a\n"  # annual weather
#                "b\n"  # select another
#                "<\n"  # other weather file
#                "../dbs/" + clm_file + "\n"
#                "y\n"  # update model (lat/long)
#                "y\n"  # update model clm year
#                "-\n"  # exit menu
#                "r\n"  # save model (!)
#                "-\n",  # exit module
#                encoding="utf-8")
#
#    f = open(config + "_set_" + clm_file + ".scratch", "w")  # creates scratch file
    
#    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)


def set_mgp(config, clm_file, gtp):
    """Function sets ground temperatures according to climate file.
    
    Arguments:
    [1] configuration file name without extension
    [2] dict with the following structure (the string *may not*(!)
        begin with whitespace!)
    
    GTP = {'clm_file' : { 1 : {'JanJun' : "0.47  -1.09  -0.77   0.52   4.75   8.58",
                               'JulDez' : "11.64  13.28  12.93  10.78   7.29   3.59"},
                          2 : {'JanJun' : "3.12   1.53   1.18   1.66   4.06   6.64",
                               'JulDez' : "9.00  10.65  11.03  10.10   8.05   5.55"}},
           ... }
    }

    Call:
       set_mgp(var, clm, GTP[clm]) """

    from subprocess import run

    print("\tSet ground temperature profiles to values corresponding to climate file "\
           + clm_file)

    nprof=len(gtp)

    args = [
            "prj",
            "-file", config + ".cfg",  # executable file
            "-mode", "text",  # opens file in mode text
            ]

    cmd1 = bytes("m\n"  # browse / edit / simulate
                 "b\n", # context
                 encoding="utf-8")
    
    cmd_ = bytes("m\n"  # ground temperature profiles
                 "b\n", # edit
                 encoding="utf-8")
    s = ''
    
    for n in range(nprof):
        s += cmd_.decode('utf-8')          \
             + str(n+1) + "\n"             \
             + gtp[(n+1)]['JanJun'] + "\n" \
             + gtp[(n+1)]['JulDez'] + "\n"

    cmd2 = s.encode('utf-8')
    
    cmd3 = bytes("-\n"  # exit menu
                 "!\n"  # save model
                 "\n"   # accept current .cfg
                 "\n"   # accept current .cnn
                 "-\n"  # exit menu
                 "-\n", # quit module
                 encoding="utf-8")

    cmd = cmd1.decode('utf-8')   \
          + cmd2.decode('utf-8') \
          + cmd3.decode('utf-8')

    cmd = cmd.encode('utf-8')

    f = open(config + "_set_mgp.scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)


def set_spm(config, cnn_file, spm_file):
    """Function sets special material

    Arguments:
    [1] configuration file name without extension
    [2] connections file name without extension
    [3] special materials file name without extension"""

    from subprocess import run

    print("\tSet spm file      : " + spm_file + ".spm")

    # Setting SPM-file
    args = [
            "prj",
            "-file", config + ".cfg",  # executable file
            "-mode", "text",  # opens file in mode text
            ]

    cmd = bytes("m\n"  # browse/ edit/ simulate
                "c\n"  # composition
                "n\n"  # active materials
                "Y\n"  # does a special components file exist? [Y/N]
                "../dbs/" + spm_file + ".spm\n"  # special components filename?
                "-\n"  # exit
                "-\n"  # exit this menu
                "!\n"  # save model
                + config + ".cfg\n"  # update system configuration file?
                + cnn_file + ".cnn\n"  # surface connections file name? 
                + cnn_file + ".cnn\n"  # surface connections file name?
                "-\n"  # exit this menu
                "-\n",  # exit Project Manager
                encoding="utf-8")

    f = open(config + "_set_" + spm_file + ".scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)

def set_afn(config, afn_file):
    """Function sets air flow network file.

    Arguments:
    [1] configuration file name without extension
    [2] air flow network file name without extension"""

    from subprocess import run

    print("\tSet afn file      : " + afn_file + ".afn")

    # Setting AFN-file
    args = [
            "prj",
            "-file", config + ".cfg",  # executable file
            "-mode", "text",  # opens file in mode text
            ]

    cmd = bytes("m\n"  # browse/ edit/ simulate
                "e\n"  # flow network
                "e\n"  # new flow network
                "a\n"  # menues & lists
                "../nets/" + afn_file + ".afn\n"  # afn filename?
                "n\n"  # no synopsis
                "!\n"  # save network
                "\n"   # accept filename!
                "y\n"  # overwrite this file
                "n\n"  # save 3d file?
                "-\n"  # Exit
                "n\n"  # save changes
                "-\n"  # exit menu
                "-\n", # quit module
                encoding="utf-8")

    f = open(config + "_set_" + afn_file + ".scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)

def set_plant(config, plant, plant_db):
    """ Script changes plant network file in .cfg.
    
    Arguments:
    1. configuration root file name
    2. plant root file name
    3. plant component database used (with path)"""

#[ ! -f ../nets/${PLANT}.pln ] && echo " ** ERROR ** Plant file inexistant!"
#[ ! -f ${PLANTDB} ] && echo " ** ERROR ** Plantdb inexistant!"

    print("   In " + config + ", setting plant file to: " + plant + "... ")

    args = [
            "prj",
            "-file", config + ".cfg",  # executable file
            "-mode", "text",  # opens file in mode text
            ]
    
    cmd = bytes("m\n"  # browse/edit/simulate
                "d\n"  # plant & systems
                "b\n"  # plant model? (b explicit)
                "../nets/" + plant + ".pln\n"
                "y\n"  # Use or modify?
                "n\n"  # Display synopsis
                + plant_db + "\n"
                "-\n"  # Exit
                "y\n"  # save changes
                "../nets/" + plant + ".pln\n"
                "y\n"  # Overwrite this file?
                "-\n"  # exit plant model selection
                "-\n"  # exit this menu
                "-\n",  # exit Project Manager
                encoding="utf-8")

    f = open(config + "_set_" + plant + ".scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)


def set_obs_dim(config, zone, obs, width, depth, height):
    """ Set obstruction dimensions.

    Arguments:
     1. configuration file name (with relative path)
     2. zone
     3. obstruction entry
     4. width
     5. depth
     6. height """

    from subprocess import run

    print("\tSet obstruction dimension in zone " + zone + ".")
    print("\t\tObstruction" + obs + ", width, depth, height is " \
                            + width + ", " + depth + ", " + height + "m.")

    # Setting lam for mat
    args = [
            "prj",
            "-file", config + ".cfg",  # executable file
            "-mode", "text",  # opens file in mode text
            ]

    cmd = bytes("m\n"  # browse/edit/simulate
                "c\n"  # composition
                "a\n"  # geometry & attribution
                + zone + "\n"
                "h\n"  # solar obstruction
                "a\n"  # dimensional input
                + obs + "\n"
                "b\n"  # block W D H
                + width + " " + depth + " " + height + "\n"
                "-\n"  # exit
                "-\n"  # exit menu
                "a\n"  # recalculate (silent)
                "-\n"  # exit menu
                "-\n"  # exit menu
                "-\n"  # exit menu
                "-\n"  # exit menu
                "-\n", # quite module
                encoding="utf-8")

    f = open(config + "_set_" + zone + "_" + obs + "_obs.scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)


def set_con(config, cnn_file, old_con_str, old_class, old_con, new_class, new_con):
    """Function changes construction globally for model zones.

    Arguments:
    [1] configuration file name without extension
    [2] connections file name without extension
    [3] old construction name (string)
    [4] old construction category (letter)
    [5] old construction entry (letter)
    [6] new construction category (letter)
    [7] new construction entry (letter) """

    import os
    from subprocess import run

    print("\n\tChange construction \"" + old_con_str + "\" in model " + config + ".cfg globally,")
    print("\t\tsearch for " + old_class + " / " + old_con)
    print("\t\treplace by " + new_class + " / " + new_con + " ... ", end='')

# Get number of .geo lines that contain construction "old_con_str"
# which corresponds to the number of changes to be accepted.
    cmd='grep -c -w "' + old_con_str + '" ../zones/*.geo \
             | cut -d ":" -f 2 \
             | awk \'{c+=$1} END{print c+0}\''

    wd=os.getcwd() # must be <modelpath>/cfg <<check?>>
    
    nc = run(cmd, shell=True, cwd=wd, capture_output=True).stdout.strip()
    nc = nc.decode('utf-8')
    
    # Changing construction
    args = [
            "prj",
            "-file", config + ".cfg",  # executable file
            "-mode", "text",  # opens file in mode text
            ]

    cmd1 = bytes("m\n"  # browse/ edit/ simulate
                 "c\n"  # composition
                 "*\n"  # global tasks
                 "f\n"  # search & replace
                 "c\n"  # continue
                 + old_class + "\n"  # old construction category
                 + old_con + "\n"  # old construction name
                 + new_class + "\n"  # new construction category
                 + new_con + "\n"  # new construction name
                 "*\n"  # search zones (* all zones)
                 "-\n",  # exit this menu
                 encoding="utf-8")

    cmd2 = bytes("y\n",  # apply construction to zone:con? [Y/N]
                 encoding="utf-8")

    s = ''
    for i in range(int(nc)):
        s += cmd2.decode('utf-8')
    
    cmd2 = s.encode('utf-8')

    cmd3 = bytes("-\n"  # exit menu
                 "!\n"  # save model
                 + config + ".cfg\n"  # Update system configuration file?
                 + cnn_file + ".cnn\n"  # Surface connections file name?
                 "-\n"  # exit menu
                 "-\n", # quit module
                 encoding="utf-8")

    cmd = cmd1.decode('utf-8')   \
          + cmd2.decode('utf-8') \
          + cmd3.decode('utf-8') \

    cmd = cmd.encode('utf-8')

    f = open(config + "_set_roomcon_" + new_con + ".scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)

    print("done.")


def set_ctl_temp_setpt(config, ctl_file, loop, h_setpoint, c_setpoint='99'):
    """Function changes the setpoint temperature for building control.
    
    Arguments:
    [1] configuration file name without extension
    [2] control file name w/o extension
    [3] loop to be edited (?)
    [4] heating setpoint (number)
    [5] cooling setpoint (number)
    
    """
    from subprocess import run
    
    print("\n\tSetting new temperature setpoints in " + config + ".cfg for")
    print("\t\theating to " + h_setpoint + " degC and for")
    print("\t\tcooling to " + c_setpoint + " degC")
    print("\t\tin control file " + ctl_file + ".ctl.")
    
    # Set arguments w/ config file.
    args = [
            "prj",
            "-file", config + ".cfg",  # executable file
            "-mode", "text",  # opens file in mode text
            ]
    
    # Build command string.
    cmd = bytes("m\n"  # browse/ edit/ simulate
                "j\n"  # zones control
                "../ctl/" + ctl_file + ".ctl\n"  # control file?
                + loop + "\n"
                "c\n"  # period data
                "a\n"  # first (only) period
                "f\n"  # heating setpoint
                + h_setpoint + "\n"
                "g\n"  # cooling setpoint
                + c_setpoint + "\n"
                "-\n"  # exit period data
                "Y\n"  # accept changes
                "-\n"  # exit
                "-\n"  # exit Editing options
                ">\n"  # save control data
                "../ctl/" + ctl_file + ".ctl\n"  # control file?
                "Y\n"  # overwrite file
                "-\n"  # exit controls
                "N\n"  # save changes (already done above!)
                "-\n"  # exit browse / edit / simulate
                "-\n", # quite module (prj)
                encoding="utf-8")
    
    # Create and open scratch file.
    f = open(config + "_set_hc_setp" + ".scratch", "w")
    
    # Run prj (args), executes commands (cmd), writes scratch file (f).
    run(args, input=cmd, stdout=f)


##############################################
### A u x i l i a r y    f u n c t i o n s.
##############################################

def list_of_files(path,ext):
    import os
    
    file_list=''
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)) and f.endswith(ext):
            file_list = file_list + ' ' + path + '/' + f
    return (file_list)

# Remove old results and contents files from the cfg-directory to
# avoid conflicts with "espr_sim.qa-report" and espr_sim.simulate"
# or to avoid disc space issues for runs with many variants ('RUNCLEAN').
def remove_results(variant, mode):
    import os

    if os.path.exists("./" + variant + ".res"):
                  os.remove("./" + variant + ".res")
    if os.path.exists("./" + variant + ".mfr"):
                  os.remove("./" + variant + ".mfr")
    if os.path.exists("./" + variant + ".plr"):
                  os.remove("./" + variant + ".plr")

    if mode == 'RUNCLEAN' is False:
        if os.path.exists("./" + variant + ".contents"):
            os.remove("./" + variant + ".contents")


# Rename H3K-output.csv to <variant>.csv, create subdirectories for
# current simulation set and move all corresponding files there.
# Also, do some cleanup.
def move_files(mode, variant):
    import os
    import shutil

    if (mode == 1) is True:
        if os.path.isdir("./" + variant) is True:
            shutil.rmtree("./" + variant)
            os.mkdir("./" + variant)
        else:
            os.mkdir("./" + variant)
    
        if os.path.isdir("./" + variant + "_scratchfiles") is True:
            shutil.rmtree("./" + variant + "_scratchfiles")
            os.mkdir("./" + variant + "_scratchfiles")
        else:
            os.mkdir("./" + variant + "_scratchfiles")

    files = os.listdir(os.getcwd())

    for f in files:
        if f.startswith(variant + "."):
            shutil.move(f, "./" + variant)
        elif f.endswith(".csv"):
            os.rename(f, variant + ".csv")
            shutil.move(variant + ".csv", "./" + variant)
        elif f.endswith(".dat"):
            shutil.move(f, "./" + variant)
        elif f.endswith(".scratch"):
            if (mode == 1) is True:
                shutil.move(f, "./" + variant + "_scratchfiles")
            else:
                shutil.move(f, "./" + variant + "_scratchfiles" + "/" + f + "2")
        # Cleanup.
        elif f.startswith("fort."):
            os.remove(f)
        elif f.startswith("graphic."):
            os.remove(f)

#    if os.path.exists("./out.xml"):
#        shutil.move("./out.xml", "./" + variant)
#    if os.path.exists(config + ".summary"):
#        os.remove("./" + config + ".summary")
#    if os.path.exists("./out.summary"):
#        os.rename("./out.summary", config + ".summary")
#    if os.path.exists("./out.dictionary"):
#        shutil.move("./out.dictionary", "./" + variant)

# Rename H3K-output.csv to <variant>.csv, create subdirectories for
# current simulation set and move all corresponding files there.
# Also, do some cleanup.
def move_clm_files(clm):
    import os
    import shutil

    clmpath='./' + clm + '_eval'

    if os.path.isdir(clmpath) is True:
        shutil.rmtree(clmpath)
        os.mkdir(clmpath)
    else:
        os.mkdir(clmpath)

    files = os.listdir(os.getcwd())

    for f in files:
        if f.startswith(clm + "_"):
            shutil.move(f, clmpath)
