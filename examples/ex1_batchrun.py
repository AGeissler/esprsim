#!/usr/bin/env python3
r"""
Minimal working example
-----------------------

.. topic:: Use 'esprsim' to run and evaluate a model

   * learn of necessary components of 'esprsim'

   * run simulation model and postprocess results

The example model ...

"""
import os
import pathlib

import esprsim as sim

# def _find_repo_root(start=None):
#         p = pathlib.Path(start or os.getcwd()).resolve()
#         for d in [p] + list(p.parents):
#                 if (d / 'pyproject.toml').exists() or (d / '.git').exists() or (d / 'setup.py').exists():
#                         return d
#         return pathlib.Path(os.getcwd()).resolve()

print('\tNow in working directory ' + os.getcwd() + '.\n')

# repo_root = _find_repo_root()
# cfg_path = (pathlib.Path.cwd() / 'examples' / 'model' / 'cfg')
cfg_path = (pathlib.Path.cwd() / 'model' / 'cfg')

if cfg_path and cfg_path.exists():
        os.chdir(str(cfg_path))
        print('\tCurrent working directory ' + os.getcwd() + '.')
else:
        print('\tCould not locate cfg subfolder; staying in ' + os.getcwd() + '.')

# %%
# Define a simulation period master list. This must be present and include at least one
# entry. Having 'year' and 'test' covers many application situations.
PM = { 'year'    : {'FD' : "01", 'FM' : "01", 'TD' : "31", 'TM' : "12", 'PP' : "20" },
       'test'    : {'FD' : "25", 'FM' : "07", 'TD' : "27", 'TM' : "07", 'PP' :  "2" }}


# %%
# Set up model specific dict of dicts. The main keys correspond to model parameter names
# for which a range of values is to be simulated. There must be at least an entry for
# the configuration file 'cfg' and the simulation period 'per'.
variant_dict = {
    "cfg": {"abbrev": "",
            "test": ['PVT_Douala'],
            "list": ['PVT_Douala'],
            "maxlist": ['PVT_Douala']},
    "per": {"abbrev": "_",
            "test": ['test'],
            "list": ['year'],
            "maxlist": list(PM.keys())},
}


# %%
# Set up parameters for desired post-processing. As this is very model specific,
# 'esprsim' has only a few extraction methods for specific metrics. However, the full
# value set according to the model 'input.xml' is available for third-party
# post-processing.
#
# Here we define ...


# %%
# Run simulation for all variants in list 'VARLIST' of dict 'variant_dict'.
VARLIST = 'test'

config_name = variant_dict['cfg'][VARLIST][0]
config_arg = str((cfg_path / config_name)) if 'cfg_path' in globals() \
                                           and cfg_path is not None else config_name
dms = sim.get_domains_key(config_arg)

print(f"dms = {dms}")

# sim.process_variants(variant_dict, PM, the_list=VARLIST, ptstep=6)
