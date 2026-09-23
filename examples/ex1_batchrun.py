#!/usr/bin/env python3
r"""
Minimal working example
-----------------------

.. topic:: Use ``esprsim`` to run and evaluate a model

   * learn to set up necessary components of ``esprsim``

   * run simulation model and postprocess results

The example model is a simple set of three buildings with different roof tilt angles.
The roofs feature a PV installation.

.. image:: ../../examples/model/images/scene1.png
   :scale: 30%

"""

# sphinx_gallery_thumbnail_number = -1
from pathlib import Path

import esprsim as sim


# %%
# Define a simulation period master list. This list must be present and include at least
# one entry. Having 'year' and 'test' covers many application situations.
PM = { 'year'    : {'FD' : "01", 'FM' : "01", 'TD' : "31", 'TM' : "12", 'PP' : "20" },
       'test'    : {'FD' : "25", 'FM' : "07", 'TD' : "27", 'TM' : "07", 'PP' :  "2" }}


# %%
# Set up a model specific dict of dicts. The main keys correspond to model parameter
# names for which a range of values is to be simulated. There must be at least an entry
# for the configuration file 'cfg' and the simulation period 'per' as shown below.
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
# Set the model configuration path and set 'variant_dict['cfg']['cfg_path']' to this
# path value.
cfg_path = (Path.cwd() / 'model' / 'cfg')
variant_dict['cfg']['cfg_path'] = cfg_path


# %%
# Set desired variant selection list from 'test'|'list'(|'maxlist') and then run
# simulation for all variants found in this list in dict 'variant_dict' using the method
# 'process_variants'. Beware the total number of simulations that result.
VARLIST = 'test'

results = sim.process_variants(variant_dict, PM, the_list=VARLIST, ptstep=6)


# %%
# Define a simple graph showing ...
#
# .. note::
#    In the example model folder, subfolder 'cfg' the file 'input.xml' can be found.
#    ESP-r must be compiled with 'xml support' for the example to run correctly.
#    The file 'input.xml' defines which variables are written to a .csv output file
#    after the simulation run is finished.
results[list(results.keys())[0]].head()
