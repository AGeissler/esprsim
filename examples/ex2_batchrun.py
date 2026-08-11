#!/usr/bin/env python3
r"""
PV yield comparison
-------------------

.. topic:: Use 'esprsim' to run and evaluate model variants

   * set up desired variants

   * run simulation model and postprocess results

PV yield ...

"""

# sphinx_gallery_thumbnail_number = -2
import os
import pathlib

import esprsim as sim

def _find_repo_root(start=None):
        p = pathlib.Path(start or os.getcwd()).resolve()
        for d in [p] + list(p.parents):
                if (d / 'pyproject.toml').exists() or (d / '.git').exists() or (d / 'setup.py').exists():
                        return d
        return pathlib.Path(os.getcwd()).resolve()

print('\tNow in working directory ' + os.getcwd() + '.\n')

repo_root = _find_repo_root()
cfg_path = (repo_root / 'examples' / 'ex1' / 'cfg') if repo_root is not None else None

if cfg_path and cfg_path.exists():
        os.chdir(str(cfg_path))
        print('\tCurrent working directory ' + os.getcwd() + '.')
else:
        print('\tCould not locate cfg subfolder; staying in ' + os.getcwd() + '.')

# %%
# Define a simulation period master list. This must be present and include at least one
# entry.
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
    "setp": {"abbrev": "_",
             "test": [('14', 'e')],  # variant_dict['setp']['list'][0][1] = 'e' (loop)
             "list": [('14', 'e')],
             "maxlist": [('12', 'e'), ('13','e')]},
    "spm": {"abbrev": "_",
            "test": ['PV_panels_1'],
            "list": ['PV_panels_1'],
            "maxlist": ['PV_panels_1']},
    "rot": {"abbrev": "_",
            "test": [(0, 7.5, 3.0, 'S')],
            "list": [(0, 7.5, 3.0, 'S')],
            "maxlist": [(0, 7.5, 3.0, 'S'), (180, 7.5, 3.0, 'N')]},
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
# Define desired PMV base data.
#CLlist = ['CLlo', 'CLme', 'CLhi']
CLlist = ['CLme']

PMV = { 'CLlo': {'clo' : "1.2", 'met' : "1.0", 'veloc' : "0.1"},
        'CLme': {'clo' : "1.3", 'met' : "1.0", 'veloc' : "0.1"},
        'CLhi': {'clo' : "1.4", 'met' : "1.0", 'veloc' : "0.1"}}


# %%
# Run simulation for all variants in list 'VARLIST'.
VARLIST = 'test'

# config_name = variant_dict['cfg'][VARLIST][0]
# config_arg = str((cfg_path / config_name)) if 'cfg_path' in globals() \
#                                            and cfg_path is not None else config_name
# sim.get_domains_key(config_arg)

# sim.process_variants(variant_dict, PM, the_list=VARLIST, ptstep=6)
