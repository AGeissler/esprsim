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

# Give position of ESP-r text mode function libraries relative to
# run-directory of this script and import the libraries.
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
import esprsim as sim

# Set working directory to cfg folder.
os.chdir(os.path.join(os.path.dirname(__file__),'cfg'))
#print('\tNow in working directory ' + os.getcwd() + '.')

# Check if "results mode"
#print('** len(sys.argv)= ' + str(len(sys.argv)) + ';')
if (len(sys.argv) > 1) is True:
    SIMU = False
else:
    SIMU = True

# Set clean mode.
RUNCLEAN=True

# Enter configuration file names without extension.
config_list = ['PreFreb']

# Enter connections file name without extension.
cnn_file = "PreFreb"

# %%
# Enter air flow network file names without extension. Use "BD" versions
# with control 9999nov, only (all openings closed)!
#afn_list = ['n06BD', 'n50BD','n15BD']
#afn_list = ['n06', 'n15,'n50']
afn_list = ['n15']

## Enter control file names without extension.
#ctl_list = ['cc9999nov','cs1111nov','cs1122nov','cs1133nov','cs1511nov','cs2511nov','cs3511nov','cs1522nov','cs2522nov','cs3522nov',
#                     'cs1533nov','cs2533nov','cs3533nov','cs2733nov','cs2233nov',
#                     'cg1111nov','cg2222nov','cg3333nov','cl3322nov','cl4322nov','cl5322nov']
#ctl_list = ['cs3511nov_hliv', 'cs3511nov_h3z', 'cs3511nov_hall']
ctl_list = ['cs3511nov_hliv']


## Setpoint temperatures for heating.
#setp_list = ['12', '13', '14', '15']
setp_list = ['14']

## Which control-loop is affected?
loop = 'e'


## Simulation periods master list.
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


## Set desired simulation list.
#period_list = ['win1','weeksum','weekwin']
#period_list = ['weekwin','weeksum']
period_list = ['testwin']

## Climate variation in Ladakh seems to be large, give choice (full
## climate file name necessary, here!).
#clm_list = ['Leh_TMY', 'Dras_MN','Meas_Dras8','Dras_MN8']
clm_list = ['Leh_TMY']
#clm_list = ['Meas_Dras8']
#clm_list = ['Dras_MN8']

## Ground temperature profiles corresponding to climate files,
## calculated according EN 13370:2017.
## Careful, no whitespace may precede the values!

GTP = {'Meas_Dras8' : { 1 : {'JanJun' : "-2.07  1.81  4.62   6.07   9.44  12.19",
                             'JulDez' : "14.25  13.77  11.22  10.03   3.56   -1.17"},
                        2 : {'JanJun' : "-2.07  1.81  4.62   6.07   9.44  12.19",
                             'JulDez' : "14.25  13.77  11.22  10.03   3.56   -1.17"}},
       'Leh_TMY'    : { 1 : {'JanJun' : "-12.72 -12.21  -9.48  -4.45  -1.36  2.14",
                             'JulDez' : "6.17   6.71  3.43   -1.76  -7.45  -12.13"},
                        2 : {'JanJun' : "-12.72 -12.21  -9.48  -4.45  -1.36  2.14",
                             'JulDez' : "6.17   6.71  3.43   -1.76  -7.45  -12.13"}}
}


## External wall ew construction systems.
EWC = { 'ew_PF' : {'cat' : "a", 'con' : "a"},
        'ew_SC' : {'cat' : "a", 'con' : "b"},
        'ew_RE' : {'cat' : "a", 'con' : "d"},
        'ew_AD' : {'cat' : "a", 'con' : "c"}}

## Default wall construction.
def_ewall = 'ew_PF'

## Abbreviations for wall construction systems for file names.
EWCshort = { 'ew_PF'   : "ewp",
             'ew_SC'   : "ews",
             'ew_RE'   : "ewr",
             'ew_AD'   : "ewa"}

## Internal iwall_1 i1 construction systems.
i1C = { 'i1_PF'  : {'cat' : "b", 'con' : "a"},
        'i1_SC'  : {'cat' : "b", 'con' : "d"},
        'i1_RE'  : {'cat' : "b", 'con' : "f"},
        'i1_AD'  : {'cat' : "b", 'con' : "h"}}

## Abbreviations for iwall_1 construction systems for file names.
i1Cshort = { 'i1_PF'   : "i1p",
             'i1_SC'   : "i1s",
             'i1_RE'   : "i1r",
             'i1_AD'   : "i1a"}

## Internal iwall_2 i2 construction systems.
i2C = { 'i2_PF'  : {'cat' : "b", 'con' : "b"},
        'i2_SC'  : {'cat' : "b", 'con' : "e"},
        'i2_RE'  : {'cat' : "b", 'con' : "g"},
        'i2_AD'  : {'cat' : "b", 'con' : "i"}}

## Abbreviations for iwall_2 construction systems for file names.
i2Cshort = { 'i2_PF'   : "i2p",
             'i2_SC'   : "i2s",
             'i2_RE'   : "i2r",
             'i2_AD'   : "i2a"}

## Internal floor living fl construction systems; currently
## identical floor living constructions for AD, RE and SC.
flC = { 'fl_PF'  : {'cat' : "h", 'con' : "a"},
        'fl_SC'  : {'cat' : "h", 'con' : "d"},
        'fl_RE'  : {'cat' : "h", 'con' : "d"},
        'fl_AD'  : {'cat' : "h", 'con' : "d"}}

## Abbreviations for floor living construction systems for file names.
flCshort = { 'fl_PF'   : "flp",
             'fl_SC'   : "fla",
             'fl_RE'   : "fla",
             'fl_AD'   : "fla"}

##
## Overall construction system combinations.
CCL = { 'ew_PF' : {'iw1' : "i1_PF", 'iw2' : "i2_PF", 'fl' : "fl_PF"},
        'ew_SC' : {'iw1' : "i1_SC", 'iw2' : "i2_SC", 'fl' : "fl_SC"},
        'ew_RE' : {'iw1' : "i1_RE", 'iw2' : "i2_RE", 'fl' : "fl_RE"},
        'ew_AD' : {'iw1' : "i1_AD", 'iw2' : "i2_AD", 'fl' : "fl_AD"}}

## Create construction lists.
#ew_list    = ['ew_PF', 'ew_SC','ew_RE','ew_AD']
#ew_list    = ['ew_SC','ew_RE']
ew_list    = ['ew_PF']

## Trombe wall construction systems.
TWC = { 'trombe_wall'  : {'cat' : "b", 'con' : "b"},
        'TW_heavy'     : {'cat' : "b", 'con' : "d"}}

## Default Trombe wall construction.
def_twall = 'trombe_wall'

## Abbreviations for Trombe wall construction systems for file names.
TWCshort = { 'trombe_wall': "twm",
             'TW_heavy'   : "twh"}

## Create Trombe wall construction lists.
#tw_list    = ['trombe_wall', 'TW_heavy']
tw_list    = ['trombe_wall']

## Solar absorption.
SOLABS = { 'low' : { 'mcl' : "b", 'mat' : "s", 'abs' : "0.75"},
           'med' : { 'mcl' : "b", 'mat' : "s", 'abs' : "0.80"},
           'hig' : { 'mcl' : "b", 'mat' : "s", 'abs' : "0.95"}}
twabs_list = ['low']

## Set building timesteps per hour 'BTSTEP' and plant time steps per
## building time step 'PTSTEP' as global values.
BTSTEP = "10"
PTSTEP = "6"

## Define desired PMV base data.
PMV = { 'CLlo': {'clo' : "1.2", 'met' : "1.0", 'veloc' : "0.1"},
        'CLme': {'clo' : "1.3", 'met' : "1.0", 'veloc' : "0.1"},
        'CLhi': {'clo' : "1.4", 'met' : "1.0", 'veloc' : "0.1"}}

#CLlist = ['CLlo', 'CLme', 'CLhi']
CLlist = ['CLme']

## Run simulation cases.
cnt = 0
config = 'PreFreb'

## Available lists:
## clm_, afn_, ctl_, setp_, ew_, tw_, period_
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
                        
                        old_ewclass  = EWC[def_ewall]['cat']
                        old_ewcon    = EWC[def_ewall]['con']
                        old_iw1class = i1C[CCL[def_ewall]['iw1']]['cat']
                        old_iw1con   = i1C[CCL[def_ewall]['iw1']]['con']
                        old_iw2class = i2C[CCL[def_ewall]['iw2']]['cat']
                        old_iw2con   = i2C[CCL[def_ewall]['iw2']]['con']
                        old_flclass  = flC[CCL[def_ewall]['fl']]['cat']
                        old_flcon    = flC[CCL[def_ewall]['fl']]['con']
            
                        for twcon in tw_list:
            
                            old_twclass = TWC[def_twall]['cat']
                            old_twcon   = TWC[def_twall]['con']
        
                            for twabs in twabs_list:
    
                                # File name for current simulation set
                                variant = str(config + "_" + clm + "_" + afn + "_" + ctl + "_"
                                                + setp + "_"
                                                + TWCshort[twcon] + "_"
                                                + EWCshort[ewcon] + "_"
#                                                + i1Cshort[CCL[ewcon]['iw1']] + "_"
#                                                + i2Cshort[CCL[ewcon]['iw2']] + "_"
#                                                + flCshort[CCL[ewcon]['fl']] + "_"
                                                + SOLABS[twabs]['abs'] + "_"
                                                + per)
        
                                # Bookkeeping for simulation duration message.
                                if (cnt == 0) is True:
                                        # Store starttime for series.
                                        now0 = datetime.now()
                                        now  = now0
                                        # Calculate total number of variants.
                                        numvars = len(clm_list)*len(afn_list)*len(ctl_list) \
                                                  *len(ctl_list)*len(period_list)*len(ew_list)*len(tw_list) \
                                                  *len(twabs_list)
                                        remaining = 86400
                                        rd = -2
                                else:
                                # Get current datetime and calculate difference.
                                    now = datetime.now()
                                    averagetime = (now-now0).total_seconds() / cnt
                                    remaining = (numvars-cnt)*averagetime
                                    rd = -1*min(math.floor(math.log10(remaining)),2)
                                cnt = cnt + 1
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
                                    espr_sim.set_clm(config, clm)
                                    espr_sim.set_mgp(config, clm, GTP[clm])
                                    
                                    # Set air flow network file from afn_list.
                                    espr_sim.set_afn(config, afn)
                                    
                                    # Set control file from ctl_list.
                                    espr_sim.set_ctl(config, ctl)
                                    
                                    # Set setpoint from setp_list.
                                    espr_sim.set_ctl_temp_setpt(config, ctl, loop, setp)
                                    
                                    # Conditionally set constructions based on external wall construction.
                                    if (ewcon == def_ewall) is False:
                                        espr_sim.set_con(config, cnn_file, def_ewall,
                                                            old_ewclass, old_ewcon,
                                                            EWC[ewcon]['cat'],EWC[ewcon]['con'])
                                        
                                        espr_sim.set_con(config, cnn_file, CCL[def_ewall]['iw1'],
                                                            old_iw1class, old_iw1con,
                                                            i1C[CCL[ewcon]['iw1']]['cat'],
                                                            i1C[CCL[ewcon]['iw1']]['con'])
                                        
                                        espr_sim.set_con(config, cnn_file, CCL[def_ewall]['iw2'],
                                                            old_iw2class, old_iw2con,
                                                            i2C[CCL[ewcon]['iw2']]['cat'],
                                                            i2C[CCL[ewcon]['iw2']]['con'])
                                        
                                        espr_sim.set_con(config, cnn_file, CCL[def_ewall]['fl'],
                                                            old_flclass, old_flcon,
                                                            flC[CCL[ewcon]['fl']]['cat'],
                                                            flC[CCL[ewcon]['fl']]['con'])
                                    
                                    # Conditionally set trombe wall construction.
                                    if (twcon == def_twall) is False:
                                        espr_sim.set_con(config, cnn_file, def_twall,
                                                            old_twclass, old_twcon,
                                                            TWC[twcon]['cat'], TWC[twcon]['con'])
                                    
                                    # Set outside absorption coefficient for trombe wall material.
                                    espr_ms_sim.set_abs_o(config, SOLABS[twabs]['mcl'],
                                                                  SOLABS[twabs]['mat'],
                                                                  SOLABS[twabs]['abs'])
                                    
                                    # Remove old results and contents files from the cfg-directory.
                                    espr_sim.remove_results(variant, 'STALE')
                                    
                                    # Start current simulation set
                                    espr_sim.qa_report(config, variant)
                                    espr_sim.simulate(2, config, variant, BTSTEP, 0, **PM[per])
                                    
                                    # Extract results via res.
                                    # PMV for zone "e" (living).
                                    for CL in CLlist:
                                        espr_res.res_PMV(variant, 'e', **PMV[CL])
                                    
                                    # Remove results files if disc space is an issue.
                                    if RUNCLEAN is True:
                                        espr_sim.remove_results(variant, 'RUNCLEAN')
                                    
                                    # Rename H3K-output.csv to <variant>.csv, create
                                    # subdirectories for current simulation set and
                                    # move all corresponding files there.
                                    espr_sim.move_files(1,variant)
                                
                                #**** End SIMU=True block
                                
                                # Evaluations via R.
                                cmd='/usr/local/bin/Rscript ../../plot_mult_R_evaluations.r' \
                                        + ' ' + variant + '/' + variant + '.csv' \
                                        + ' ' + str(BTSTEP) + ' ' + now.strftime("%d.%m_%H:%M:%S") \
                                        + ' ' + espr_sim.list_of_files(variant, 'dat')
                                subprocess.call(cmd, shell=True)
                                
                                # Set Trombe wall constructions back to default.
                                if SIMU is True:
                                    if (twcon == def_twall) is False:
                                        espr_sim.set_con(config, cnn_file, twcon,
                                                            TWC[twcon]['cat'], TWC[twcon]['con'],
                                                            old_twclass, old_twcon)
                            # twabs-loop closed
                        
                        # twcon-loop closed
                        
                        # Set constructions based on external wall back to default.
                        if SIMU is True:
                            if (ewcon == def_ewall) is False:
                                espr_sim.set_con(config, cnn_file, ewcon,
                                                 EWC[ewcon]['cat'], EWC[ewcon]['con'],
                                                 old_ewclass, old_ewcon)
     
                                espr_sim.set_con(config, cnn_file, CCL[ewcon]['iw1'],
                                                 i1C[CCL[ewcon]['iw1']]['cat'],
                                                 i1C[CCL[ewcon]['iw1']]['con'],
                                                 old_iw1class, old_iw1con)
    
                                espr_sim.set_con(config, cnn_file, CCL[ewcon]['iw2'],
                                                 i2C[CCL[ewcon]['iw2']]['cat'],
                                                 i2C[CCL[ewcon]['iw2']]['con'],
                                                 old_iw2class, old_iw2con)
    
                                espr_sim.set_con(config, cnn_file, CCL[ewcon]['fl'],
                                                    flC[CCL[ewcon]['fl']]['cat'],
                                                    flC[CCL[ewcon]['fl']]['con'],
                                                    old_flclass, old_flcon)
                    
                    # wcon-loop closed
                
                # period-loop closed
            
            # setp-loop closed
        
        # ctl-loop closed
    
    # afn-loop closed
    
    # Optional: set ?? back to default.
    if SIMU is True:

        # Final cleanup.
        espr_sim.move_files(0,variant)

    # Evaluate climate data.
  #  cmd='/usr/local/bin/Rscript ../../plot_clm_data.r' \
   #                             + ' ' + variant + '/' + variant + '.csv' \
   #                             + ' ' + str(BTSTEP)
   # subprocess.call(cmd, shell=True)
   # espr_sim.move_clm_files(clm)

# clm-loop closed
