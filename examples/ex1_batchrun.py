r"""
PV yield comparison
-------------------

.. topic:: Use 'esprsim' to run and evaluate model variants

   * set up desired variants

   * run simulation model and postprocess results

PV yield ...
"""

import os
import shutil
import sys
import math
import subprocess
from pathlib import Path
import humanfriendly
from datetime import datetime
from datetime import timedelta

import esprsim as sim

# Set clean mode.
RUNCLEAN=True

# %%
# Define a simulation period master list.
PM = { 'sum'     : {'FD' : "16", 'FM' : "04", 'TD' : "15", 'TM' : "10", 'PP' : "20" },
       'win1'    : {'FD' : "01", 'FM' : "01", 'TD' : "03", 'TM' : "01", 'PP' : "20" },
       'win2'    : {'FD' : "16", 'FM' : "10", 'TD' : "31", 'TM' : "12", 'PP' : "20" },
       'year'    : {'FD' : "01", 'FM' : "01", 'TD' : "31", 'TM' : "12", 'PP' : "20" },
       'trnsum'  : {'FD' : "01", 'FM' : "04", 'TD' : "15", 'TM' : "06", 'PP' : "20" },
       'trnwin'  : {'FD' : "15", 'FM' : "08", 'TD' : "31", 'TM' : "10", 'PP' : "20" },
       'testsum' : {'FD' : "27", 'FM' : "07", 'TD' : "05", 'TM' : "08", 'PP' :  "5" },
       'testwin' : {'FD' : "27", 'FM' : "01", 'TD' : "05", 'TM' : "02", 'PP' :  "5" },
       'test'    : {'FD' : "25", 'FM' : "07", 'TD' : "27", 'TM' : "07", 'PP' :  "2" },
       'weeksum' : {'FD' : "20", 'FM' : "07", 'TD' : "27", 'TM' : "07", 'PP' :  "2" },
       'weekwin' : {'FD' : "10", 'FM' : "01", 'TD' : "17", 'TM' : "01", 'PP' :  "2" },
       'measwin' : {'FD' : "01", 'FM' : "01", 'TD' : "31", 'TM' : "03", 'PP' :  "20" }}

# %%
# Set up model specific dict of dicts. The main keys correspond to model parameter names
# for which a range of values is to be simulated.
variant_dict = {
    "cfg": {"abbrev": "",
            "test": ['PVT_Douala'],
            "list": ['PVT_Douala'],
            "maxlist": ['PVT_Douala']},
    "cnn": {"abbrev": "",
            "test": ['PVT_Douala'],
            "list": ['PVT_Douala'],
            "maxlist": ['PVT_Douala']},
    "afn": {"abbrev": "_", # Enter air flow network file names without extension.
            "test": ['no_flow_S'],
            "list": ['no_flow_S'],
            "maxlist": ['bouyant_flow_N', 'bouyant_flow_S', 'bouyant_flow2_S',
                        'bouyant_flow12_S', 'force_flow_N', 'force_flow_S',
                        'no_flow_N', 'no_flow_S']},
    "ctl": {"abbrev": "_",
            "test": ['PVT_Douala'],
            "list": ['PVT_Douala'],
            "maxlist": ['PVT_Douala']},
    "spm": {"abbrev": "_",
            "test": ['PV_panels_1'],
            "list": ['PV_panels_1'],
            "maxlist": ['PV_panels_1']},
    "rot": {"abbrev": "_",
            "test": ['South'],
            "list": ['South'],
            "maxlist": ['South', 'North']},
    "clm": {"abbrev": "_",
            "test": ['Douala'],
            "list": ['Douala'],
            "maxlist": ['Douala']},
    "per": {"abbrev": "_",
            "test": ['test'],
            "list": ['year'],
            "maxlist": list(PM.keys())},
}

# %%
# Set building timesteps per hour 'BTSTEP' and plant time steps per
# building time step 'PTSTEP' as global values.
BTSTEP = "10"
PTSTEP = "6"

# Enter connections file name without extension.
VARLIST = 'test'

the_resdir = Path("espresults/")


# %%
# Define desired PMV base data.
#CLlist = ['CLlo', 'CLme', 'CLhi']
CLlist = ['CLme']

PMV = { 'CLlo': {'clo' : "1.2", 'met' : "1.0", 'veloc' : "0.1"},
        'CLme': {'clo' : "1.3", 'met' : "1.0", 'veloc' : "0.1"},
        'CLhi': {'clo' : "1.4", 'met' : "1.0", 'veloc' : "0.1"}}


# %%
# Run simulations.

def simulate_variant(**kwargs):
    r"""Simulate a single variant.

    """

    config = kwargs['cfg']
    cnn_file = kwargs['cnn']

    dms = sim.get_domains_key(config)

    variant = kwargs['variant']

    clm = kwargs['clm']
    sim.set_clm(config, clm)

    if 'ctl' in kwargs.keys():
        ctl = kwargs['ctl']
        sim.set_ctl(config, ctl)
    if 'afn' in kwargs.keys():
        afn = kwargs['afn']
        sim.set_afn(config, afn)
    # if 'setp' in kwargs.keys():
    #     setp = kwargs['setp']
    #     sim.set_ctl_temp_setpt(config, ctl, loop, setp)
    if 'spm' in kwargs.keys():
        spm = kwargs['spm']
        sim.set_spm(config, cnn_file, spm)
    # if 'rot' in kwargs.keys():
    #     rotval = kwargs['rot']
    #     sim.set_rotation(config, rot)
    if 'per' in kwargs.keys():
        per = kwargs['per']

    # Set ground temperature profiles for clm.
    # if 'gtp' in kwargs.keys():
    #     sim.set_mgp(config, clm, GTP[clm])

    # File name for current simulation set
    # variant = str(config + "_" + clm + "_" + afn + "_" + ctl + "_"
    #                 + setp + "_"
    #                 + per)

    # Message about current simulation set
    print("\n")
    print("\t=========================================================================")
    print("\tSimulating case " + "" + "/" + "" + ": " \
                                + variant + ", " + "")
    print("\t=========================================================================")
    print("\twith climate file          : " + clm)
    if 'ctl' in kwargs.keys():
        print("\twith control file          : " + ctl + ".ctl")
    if 'afn' in kwargs.keys():
        print("\twith air flow network file : " + afn + ".afn")
    # if 'setp' in kwargs.keys():
    #     print("\twith heating setpoint      : " + setp + " for loop " + loop)
    print("\tfor period                 : " + per + "\n")


    # Remove old results and contents files from the cfg-directory.
    sim.remove_results(variant, 'STALE')

    # Start current simulation set
    sim.qa_report(config, variant)
    sim.simulate(dms, config, variant, BTSTEP, 0, **PM[per])

    # Extract results via res.
    # PMV for zone "e" (living).
    for CL in CLlist:
        sim.res_PMV(variant, 'e', **PMV[CL])

    # Remove results files if disc space is an issue.
    if RUNCLEAN is True:
        sim.remove_results(variant, 'RUNCLEAN')

    # Rename H3K-output.csv to <variant>.csv, create subdirectories for current
    # simulation set and move all corresponding files there.
    sim.move_files(1, variant)

    # Optional: set ?? back to default.
    # if SIMU is True:

    # Final cleanup.
    sim.move_files(0, variant)


# %%
# Simulate all variants in list 'VARLIST'.
sim.process_variants(the_resdir, variant_dict, simulate_variant, the_list=VARLIST)

