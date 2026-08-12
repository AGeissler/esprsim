# -*- coding: utf-8 -*-
"""
This file is part of esprsim.

esprsim is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

esprsim is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with esprsim.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import shutil
import glob
import itertools
from pathlib import Path
from subprocess import run

"""
Module contains functions for ESP-r scripts and auxiliary functions for
batch running of simulations.
"""

def qa_report(config, variant):
    r"""Method which creates a QA report of the model defined in 'config' for the
    variant 'variant' using 'prj'.

    Parameters
    ----------
    config : str | Path
        Configuration file name without extension.
    variant : str
        Variant name (ctl, con, mat)

    Notes
    -----
    The script as-is expects .cfg files in (at least) v 4.2 format (current as of
    ESP-r V13.3.17).

    As of ESP-r V13.3.17 there possibly exists a short-cut to generate the QA-report.

    """

    print("\tQA report         : " + variant + ".contents")

    # Creating QA report
    args = [
            "prj",
            "-mode", "text",  # opens file in mode text
            "-file", config + ".cfg",  # executable file
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
                "!\n"  # generate QA report
                "-\n"  # exit menu
                "-\n"  # exit this menu
                "-\n",  # exit Project Manager
                encoding="utf-8")

    f = open(variant + "_qa.scratch", "w")  # creates scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)

def get_clm_filename(config):
    r"""Read name of climate file from configuration file contents.

    Parameters
    ----------
    config : str | Path
        Configuration file name without extension.

    Returns
    -------
    clm_file : str
        Name of climate file in model without extension.

    """
    # Get domains key.
    file = open(config + '.cfg', "r")
    clm_file = [line.split() for line in file.readlines() if line.startswith('*clm')][0][1]

    return str(Path(clm_file).name)  # .stem for name w/o extension if present

def get_cnn_filename(config):
    r"""Read name of connections file from configuration file contents.

    Parameters
    ----------
    config : str | Path
        Configuration file name without extension.

    Returns
    -------
    cnn_file : str
        Name of connections file in model without extension.

    """
    # Get domains key.
    file = open(config + '.cfg', "r")
    cnn_file = [line.split() for line in file.readlines() if line.startswith('*cnn')][0][1]

    return cnn_file[:-4]

def get_domains_key(config):
    r"""Establish domains key from configuration file contents.

    Parameters
    ----------
    config : str | Path
        Configuration file name without extension.

    Returns
    -------
    dms : int
        Key for model domains.

    """
    # Get domains key.
    file = open(config + '.cfg', "r")
    dms = [line.split() for line in file.readlines() if line.startswith('*indx')][0][1]

    file.seek(0, 0)

    mfr = [line.split() for line in file.readlines() if line.startswith('../nets')]
    if mfr:
        dms = int(dms) + 1
    return dms

def list_dms(dms, variant):
    r"""List results file names of model domains for console reporting.

    Parameters
    ----------
    dms : int
        Mode key for domains in model.
    variant : str
        Simulation variant to be reported on.

    Returns
    -------
    String containing results file names for simulation model domains.

    """
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
    r"""Return results file names for simulation domains.

    Parameters
    ----------
    dms : int
        Mode key for domains in model.
    variant: str
        Simulation variant for which results file names are returned.

    Returns
    -------
    Byte-encoded string with results file names for simulation model domains.

    """
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
    r"""Return time step values for simulation domains.

    Parameters
    ----------
    dms : int
        Mode key for domains in model.
    BTSTEP : int
        Number of time-steps per hour for building domain.
    PTSTEP : int
        Number of time-steps per building time-step for plant domain.

    """
    switcher = {
    1: bytes("" + str(BTSTEP) + "\n",
             encoding= 'utf-8' ),
    2: bytes("" + str(BTSTEP) + "\n",
             encoding= 'utf-8' ),
    3: bytes("" + str(BTSTEP) + "\n"
             "" + str(PTSTEP) + "\n",
             encoding= 'utf-8' ),
    4: bytes("" + str(BTSTEP) + "\n"
             "" + str(PTSTEP) + "\n",
             encoding= 'utf-8' ),
    }
    return switcher.get(dms, "Error in dms - ts")


def simulate(dms, config, variant, BTSTEP, PTSTEP, FD, FM, TD, TM, PP):
    r"""Method which runs a single simulation for a model with 'dms' domains involved
    based on configuration file 'config' using 'bps'.

    Parameters
    ----------
    dms : int
        Mode key for domains in model.
    config : str
        Configuration file name without extension.
    variant : str
        Simulation variant name.
    BTSTEP : int
        Building simulation time steps per hour.
    PTSTEP : int
        Plant time steps per building time step, not used for models w/o plant.
    FD, FM, TD, TM, PP : int
        Start- and end dates for simulation period and number of days for start-up
        period duration. Typically passed via dict reference (**PM[key]).

    Notes
    -----
    Required output files depend on simulation mode.
    1 building only, .res
    2 building and afn, .res, .mfr
    3 building and plant, .res, .plr
    4 building, afn and plant, .res, .plr, .mfr
    ... (eln, ??)

    """

    print("\tRun bps with      : " + config + ".cfg")
    print(list_dms(dms, variant))
    print("\tSimulation period : " + FD + "." + FM + ". to "
          + TD + "." + TM + ". with startup " + PP + " days using")
    if ((dms == 1) | (dms == 2)) is True:
        print("\t                    " + str(BTSTEP) + " building ts per hour.")

    if ((dms == 3) | (dms == 4)) is True:
        print("\t                    " + str(BTSTEP) + " building ts per hour and "
              + str(PTSTEP*BTSTEP) + " plant ts per hour.")

    # Set up command line arguments to run simulation.
    args = [
        "bps",
        "-mode", "text",  # open file in mode text
        "-file", config + ".cfg",  # model configuration file to run.
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

    f = open(variant + "_bps.scratch", "w")  # create scratch file

    # Run bps (args[0]), execute commands (cmd), write scratch file (f).
    run(args, input=cmd, stdout=f)

    # Postprocessing
    for line in open(variant + "_bps.scratch"):
        if "CPU time:" in line:
            print("\n\t" + line)
            # if "XML postprocessor cpu runtime" in line:
            #     print(line)

    # for file in glob.glob("../tmp/" + variant + ".*"):
    #     shutil.move(file, './')



def simulate_variant(**kwargs):
    r"""Wrapper for esprsim.simulate() to simulate a single variant.

    Parameters
    ----------
    kwargs : dict
        Dict of parameters for variant.

    Notes
    -----
    The dict of parameters contains at least 'cfg' (the configuration file name w/o
    extension) and 'per' (selected simulation period from 'PM') which are defined in
    a user script via 'variant_dict'.

    The parameters 'btstep', 'ptstep' and 'PM' are set in esprsim.process_variants() via
    method parameters at call in the user script.

    The parameter 'variant' is used as results file name root and variant subdirectory.
    The value is constructed from the variant parameters.

    """
    run_clean = kwargs['run_clean']

    # Set building timesteps per hour 'BTSTEP' and plant time steps per
    # building time step 'PTSTEP'.
    BTSTEP = kwargs['btstep']
    PTSTEP = kwargs['ptstep']
    PM = kwargs['PM']

    # Set configuration file name with (optional) path but w/o extension.
    config = str(kwargs['cfg_path'] / kwargs['cfg'])

    per = kwargs['per']

    dms = get_domains_key(config)

    variant = kwargs['variant']

    if 'cnn' in kwargs:
        cnn_file = kwargs['cnn']
    else:
        cnn_file = get_cnn_filename(config)

    if 'clm' in kwargs:
        clm = kwargs['clm']
        set_clm(config, clm)
    else:
        clm = get_clm_filename(config)

    # Optionally set various parameters.
    if 'ctl' in kwargs:
        ctl = kwargs['ctl']
        set_ctl(config, ctl)
    if 'afn' in kwargs:
        afn = kwargs['afn']
        set_afn(config, afn)
    if 'setp' in kwargs:
        setp = kwargs['setp'][0][0]
        loop = kwargs['setp'][0][1]
        set_ctl_temp_setpt(config, ctl, loop, setp)
    if 'spm' in kwargs:
        spm = kwargs['spm']
        set_spm(config, cnn_file, spm)
    if 'rot' in kwargs.keys():
        rotdat = kwargs['rot']
        set_new_rotangle(config, rotdat[0], rotdat[1], rotdat[2])
    if 'gtp' in kwargs.keys():
        GTP=kwargs['gtp_main']
        set_gtp(config, clm, GTP[clm])

    # Optionally Set moisture file for zone. ((see project 'Keller'))
    # if 'mst' in kwargs.keys():
    #     mst_file = kwargs['mst'][0]
    #     zone = kwargs['mst'][1]
    #     set_mst(config, mst_file, zone)

    # Message about current simulation set
    print("\n")
    print("\t=========================================================================")
    print("\tSimulating case " + "" + "/" + "" + ": " \
                                + variant + ", " + "")
    print("\t=========================================================================")
    print("\twith climate file          : " + clm)
    if 'ctl' in kwargs:
        print("\twith control file          : " + ctl + ".ctl")
    if 'afn' in kwargs:
        print("\twith air flow network file : " + afn + ".afn")
    if 'setp' in kwargs:
        print("\twith heating setpoint      : " + setp + " for loop " + loop)
    print("\tfor period                 : " + per + "\n")

    # Remove old results and contents files from the cfg-directory.
    remove_results(variant, kwargs['cfg_path'])

    # Start current simulation set.
    qa_report(config, variant)

    simulate(dms, config, variant, BTSTEP, PTSTEP, **PM[per])

    # Extract results via res.
    # PMV for zone "e" (living).
    # for CL in CLlist:
    #     res_PMV(variant, 'e', **PMV[CL])

    # Remove results files if disc space is an issue.
    if run_clean is True:
        remove_results(variant, kwargs['cfg_path'], run_clean)

    # Rename H3K-output.csv to <variant>.csv, create subdirectories for current
    # simulation set and move all corresponding files there.
    move_files(1, variant, kwargs['cfg_path'])

    # Final cleanup.
    move_files(0, variant, kwargs['cfg_path'])


def process_variants(dict_of_variants, pm, the_list='list', btstep=10, ptstep=0,
                     run_clean=False):
    r"""Method which processes variants based on dynamic nested for-loops using the
    dict-of-dicts parameter 'dict_of_variants'.

    Parameters
    ----------
    dict_of_variants : dict
        Dict of variables which are dicts containing variant values.
    pm : dict
        Simulation period master list.
    the_list : str
        Name of list to take from 'dict_of_variants'.
    btstep : int (optional, default: 10)
        Building time-steps per hour.
    ptstep : int (optional, default: 0)
        Plant time-steps per building time-step.

    """
    keys = list(dict_of_variants.keys())
    lists = [d[the_list] for d in dict_of_variants.values()]
    strings = {key: d['abbrev'] for key, d in dict_of_variants.items()}

    for variant in itertools.product(*lists):
        args = {keys[i]: variant[i] for i in range(len(keys))}

        # BAS_2010_RCP00_DRY_25_1w_0.2_r0_st23_ht20.5_gp0.5_gs0.1_200
        # Concatenate the string entries to generate a variant name.
        variant_name = "".join(strings[key] + (
                              str(args[key])) for key in keys) + "_"

        # Add addtional parameters to the arguments for passing to single simulation
        # function.
        args['variant'] = variant_name[:-1]
        args['cfg_path'] = dict_of_variants['cfg']['cfg_path']
        # args['resdir'] = resdir
        args['btstep'] = btstep
        args['ptstep'] = ptstep
        args['PM'] = pm
        if 'gtp' in dict_of_variants:
            args['gtp_main'] = dict_of_variants['gtp']['gtp_main']
        args['run_clean'] = run_clean

        simulate_variant(**args)


def set_ctl(config, ctl_file):
    r"""Method which sets the control file in .cfg of model using 'prj'.

    Parameters
    ----------
    config : str
        Configuration file name without extension.
    ctl_file : str
        Control file name without extension.

    """

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
    r"""Method which sets the climate file in .cfg of model using 'sed'(!).

    Parameters
    ----------
    config : str
        Configuration file name without extension.
    clm_file : str
        Climate file name *including* extension

    """

    print("\tSet clm file      : " + clm_file)

    # Setting CLM-file
    # args = [
    #         "prj",
    #         "-file", config + ".cfg",  # executable file
    #         "-mode", "text",  # opens file in mode text
    #         ]

    # Change climate file via sed ((hack due to bug in prj text mode))

    wd=os.getcwd() # must be <modelpath>/cfg <<check?>>

    cmd1='cp ' + config + '.cfg temp.cfg'

    new_clm='*clm ../dbs/' + clm_file

    cmd2=r'sed \'s%\*clm ../dbs/.*%' + new_clm + r'%\' temp.cfg > ' + config + '.cfg'

    cmd3='rm temp.cfg'

    run(cmd1, shell=True, cwd=wd)
    run(cmd2, shell=True, cwd=wd)
    run(cmd3, shell=True, cwd=wd)

    # cmd = bytes("b\n"  # db management
    #             "a\n"  # annual weather
    #             "b\n"  # select another
    #             "<\n"  # other weather file
    #             "../dbs/" + clm_file + "\n"
    #             "y\n"  # update model (lat/long)
    #             "y\n"  # update model clm year
    #             "-\n"  # exit menu
    #             "r\n"  # save model (!)
    #             "-\n",  # exit module
    #             encoding="utf-8")
    #
    # f = open(config + "_set_" + clm_file + ".scratch", "w")  # creates scratch file
    # run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)


def set_gtp(config, clm_file, gtp):
    r"""Method which sets monthly ground temperatures according to the climate file in
    .cfg using 'prj'.

    Parameters
    ----------
    config : str
        Configuration file name without extension.
    clm_file : str
        Name of climate file, must be available as key in gtp.
    gtp : Nested dict
        Nested dict of available ground temperature profiles for climate 'clm_file' with
        the structure given below (the string keys *may not*\ (!) begin with whitespace!).

    Notes
    -----
    .. code:: python

        GTP = {'clm_file1': {1: {'JanJun': "0.47  -1.09  -0.77  0.52  4.75  8.58",
                                 'JulDez': "11.64  13.28  12.93  10.78  7.29  3.59"},
                             2: {'JanJun': "3.12  1.53  1.18  1.66  4.06  6.64",
                                 'JulDez': "9.00  10.65  11.03  10.10  8.05  5.55"}},
               'clm_file2': ... }

    Example usage.
       set_gtp(var, clm, GTP[clm])

    """

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
                 "\n"   # accept current .cfg
                 "\n"   # accept current .cnn
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
    r"""Method which sets special materials file in .cfg using 'prj'.

    Parameters
    ----------
    config : str
        Configuration file name without extension.
    cnn_file : str
        Connections file name without extension.
    spm_file : str
        Special materials file name without extension.

    """

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
    r"""Method which sets air flow network file in .cfg using 'prj'.

    Parameters
    ----------
    config : str
        Configuration file name without extension.
    afn_file : str
        Air flow network file name without extension.

    """

    print("\tSet afn file      : " + afn_file + ".afn")

    # Setting AFN-file
    args = [
            "prj",
            "-mode", "text",  # opens file in mode text
            "-file", config + ".cfg",  # executable file
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
    r"""Method which changes plant network file in .cfg using 'prj'.

    Parameters
    ----------
    config : str
        Configuration file name w/o extension.
    plant : str
        Plant file name w/o extension.
    plant_db : str | Path
        Plant component database used (with path).

    """

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

    # run prj (args), execute commands (cmd), write scratch file (f)
    run(args, input=cmd, stdout=f)


def set_obs_dim(config, zone, obs, width, depth, height):
    r"""Method which sets (existing) obstruction dimensions in zone 'zone' using 'prj'.

    Parameters
    ----------
    config : str
        Configuration file name (with relative path)
    zone : str (tbc)
        Zone name.
    obs : int (tbc)
        Obstruction entry
    width : str
        Width of obstruction as string.
    depth : str
        Depth of obstruction as string.
    height : str
        Height of obstruction as string.

    """

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
    r"""Method which changes a construction globally for all model zones using 'prj'.

    Parameters
    ----------
    config : str
        Configuration file name without extension.
    cnn_file : str
        Connections file name without extension.
    old_con_str : str
        Old construction name.
    old_class : str
        Old construction category, single character.
    old_con : str
        Old construction entry, single character.
    new_class : str
        New construction category, single character.
    new_con : str
        New construction entry, single character.

    """

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


def set_new_rotangle(config, rotangle, x0, y0):
    """Method which rotates the whole model around point (x0,y0) by 'rotangle' degrees
    using 'prj'. The rotation is counterclockwise.

    Parameters
    ----------
    config : str | Path
        Configuration file name or path+name without extension
    rotangle : float
        Desired rotation angle (degrees counterclockwise).
    x0 : float
        X-coordinate of rotation centre in m
    y0 : float
        Y-coordinate of rotation centre in m

    """

    print(f"\n\tRotating model {Path(config).stem}.cfg by {rotangle} degrees ...")

    args = [
            "prj",
            "-mode", "text",
            "-file", config + ".cfg"
            ]

    cmd = bytes("m\n"  # browse / edit / simulate
                "c\n"  # composition
                "*\n"  # global tasks
                "b\n"  # rotate
                + rotangle + "\n"
                "b\n"  # user specified x & y
                + x0 + "\n"
                + y0 + "\n"
                "*\n"  # all items
                "-\n"  # exit menu
                "-\n"  # exit menu
                "!\n"  # save model
                "y\n"  # update config file
                "-\n"
                "-\n",  # quite module
                encoding="utf-8")

    f = open(config + "_rotate_" + rotangle + ".scratch", "w")  # create scratch file

    run(args, input=cmd, stdout=f)  # runs prj (args), executes commands (cmd), writes scratch file (f)

    print("done.")


def set_ctl_temp_setpt(config, ctl_file, loop, h_setpoint, c_setpoint='99'):
    """Method which changes the setpoint temperature for building control in ctl_file
    using 'prj'.

    Parameters
    ----------
    config : str
         Configuration file name without extension.
    ctl_file : str
        Control file name w/o extension.
    loop : int
        Loop number to be edited (?)
    h_setpoint : str
        Heating setpoint temperature value as string
    c_setpoint : str (optional, default: '99')
        Cooling setpoint temperature value as string

    """

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

    # Build command string.
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


def list_of_files(path, ext):
    r"""Method which creates a list of files in 'path' that have extension 'ext'.

    Parameters
    ----------
    path : str | Path
        Path to search for files with 'ext'.
    ext : str
        Extension to search for

    Returns
    -------
    List of files in 'path' with extension 'ext'.

    """

    file_list=''
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)) and f.endswith(ext):
            file_list = file_list + ' ' + path + '/' + f
    return (file_list)


def remove_results(variant, cfg_dir, run_clean=False):
    r"""Remove old binary results files from the tmp-directory and contents files from
    the cfg-directory to avoid conflicts with "espr_sim.qa_report()" and
    "espr_sim.simulate()" or to avoid disc space issues for runs with many variants.

    Parameters
    ----------
    variant : str
        Simulation variant of interest.
    cfg_dir : Path
        Path to model cfg directory.
    run_clean : bool (optional, default : False)
        Toggle for 'clean-up' mode, i.e. removal of results files.

    """
    res_dir = Path('/' + '/'.join(cfg_dir.parts[1:-1]) + '/tmp')

    extension_list = ['.res', '.mfr', '.plr', '.contents']

    if run_clean:
        for ext in extension_list:
            # Go through tmp directory.
            if Path(str(res_dir) + '/' + variant + ext).exists():
                # delete!
                Path(str(res_dir) + '/' + variant + ext).unlink(missing_ok=True)
            # Go through cfg directory.
            if Path(str(cfg_dir) + '/' + variant + ext).exists():
                # delete!
                Path(str(cfg_dir) + '/' + variant + ext).unlink(missing_ok=True)

    if run_clean is False:
        # No space issue, only avoid qa_report issues.
        if Path(str(cfg_dir) + '/' + variant + '.contents').exists():
            # delete!
            Path(str(cfg_dir) + '/' + variant + '.contents').unlink(missing_ok=True)


def move_files(mode, variant, cfg_dir):
    r"""Rename <config>.csv to <variant>.csv, create subdirectories for
    current simulation set and move all corresponding files there.
    Also, do some cleanup.

    Parameters
    ----------
    mode : int
        Mode toggle for which files are to be moved.
    variant : str
        Simulation variant to be addressed.
    cfg_dir : Path
        Path to model cfg directory.

    """

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

def move_clm_files(clm):
    r"""Move climate file to subdirectory named 'clm_eval'.

    Parameters
    ----------
    clm : str | Path
        Climate file to be moved.

    """

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
