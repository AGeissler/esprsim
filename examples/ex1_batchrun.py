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
    "exp": {"abbrev": "_",
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
            "maxlist": list(PM.keys)},
}

# %%
# Set building timesteps per hour 'BTSTEP' and plant time steps per
# building time step 'PTSTEP' as global values.
BTSTEP = "10"
PTSTEP = "6"

# Enter connections file name without extension.
cnn_file = "PreFreb"

# %%
# Define desired PMV base data.
#CLlist = ['CLlo', 'CLme', 'CLhi']
CLlist = ['CLme']

PMV = { 'CLlo': {'clo' : "1.2", 'met' : "1.0", 'veloc' : "0.1"},
        'CLme': {'clo' : "1.3", 'met' : "1.0", 'veloc' : "0.1"},
        'CLhi': {'clo' : "1.4", 'met' : "1.0", 'veloc' : "0.1"}}

# %%
# Run simulations.
for clm in clm_list:

    # Loop through available afn options.
    for afn in afn_list:
        
        # Loop through control options.
        for ctl in ctl_list:
            
            # Loop through setpoint options.
            for setp in setp_list:
                
                # Loop through simulation period options.
                for per in period_list:
                    
                    for ewcon in ew_list:

                        for twcon in tw_list:

                            for twabs in twabs_list:

                                # File name for current simulation set
                                variant = str(config + "_" + clm + "_" + afn + "_" + ctl + "_"
                                                + setp + "_"
                                                + per)
        
                                # Message about current simulation set
                                print("\n")
                                print("\t=========================================================================")
                                if SIMU is True:
                                    print("\tSimulating case " + str(cnt) + "/" + str(numvars) + ": " \
                                                                + variant + ", " + now.strftime("%d/%m %H:%M:%S"))
                                    print("\tThe remaining time is approximately " \
                                                                + humanfriendly.format_timespan(round(remaining,rd)))
                                else:
                                    print("\tEvaluating case " + str(cnt) + "/" + str(numvars) + ": " + variant)
                                    print("\tThe remaining time is approximately " \
                                                                + humanfriendly.format_timespan(round(remaining,rd)))
                                print("\t=========================================================================")
                                print("\twith climate file          : " + clm)
                                print("\twith air flow network file : " + afn + ".afn")
                                print("\twith control file          : " + ctl + ".ctl")
                                print("\twith heating setpoint      : " + setp + " for loop " + loop)
                                print("\tusing external wall        : " + ewcon )
                                print("\tusing trombe wall          : " + twcon )
                                print("\twith solar absorption      : " + twabs )
                                print("\tfor period                 : " + per + "\n")
                                
                                if SIMU is True:
                                    # Set climate file from clm_list, set corresponding ground temperature profiles.
                                    sim.set_clm(config, clm)
                                    sim.set_mgp(config, clm, GTP[clm])

                                    # Set air flow network file from afn_list.
                                    sim.set_afn(config, afn)

                                    # Set control file from ctl_list.
                                    sim.set_ctl(config, ctl)

                                    # Set setpoint from setp_list.
                                    sim.set_ctl_temp_setpt(config, ctl, loop, setp)

                                    # Remove old results and contents files from the cfg-directory.
                                    sim.remove_results(variant, 'STALE')

                                    # Start current simulation set
                                    sim.qa_report(config, variant)
                                    sim.simulate(2, config, variant, BTSTEP, 0, **PM[per])

                                    # Extract results via res.
                                    # PMV for zone "e" (living).
                                    for CL in CLlist:
                                        sim.res_PMV(variant, 'e', **PMV[CL])

                                    # Remove results files if disc space is an issue.
                                    if RUNCLEAN is True:
                                        sim.remove_results(variant, 'RUNCLEAN')

                                    # Rename H3K-output.csv to <variant>.csv, create
                                    # subdirectories for current simulation set and
                                    # move all corresponding files there.
                                    sim.move_files(1, variant)

                                #**** End SIMU=True block

                                # Evaluations via R.
                                cmd='/usr/local/bin/Rscript ../../plot_mult_R_evaluations.r' \
                                        + ' ' + variant + '/' + variant + '.csv' \
                                        + ' ' + str(BTSTEP) + ' ' + now.strftime("%d.%m_%H:%M:%S") \
                                        + ' ' + espr_sim.list_of_files(variant, 'dat')
                                subprocess.call(cmd, shell=True)

                             # twabs-loop closed

                        # twcon-loop closed

                    # wcon-loop closed

                # period-loop closed

            # setp-loop closed

        # ctl-loop closed

    # afn-loop closed
    
    # Optional: set ?? back to default.
    if SIMU is True:

        # Final cleanup.
        sim.move_files(0, variant)

# clm-loop closed
