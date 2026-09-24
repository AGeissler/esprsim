#!/usr/bin/env python3
r"""
PV yield comparison
-------------------

.. topic:: Use ``esprsim`` to run and evaluate model variants

   * set up desired variants

   * run simulation model and postprocess results

PV yield ...

.. image:: ../../examples/model/images/wireframe.png
   :scale: 25%

"""

# sphinx_gallery_thumbnail_number = -1
from pathlib import Path

import esprsim as sim


# %%
# Define a simulation period master list. This must be present and include at least one
# entry.
PM = {'year'    : {'FD' : "01", 'FM' : "01", 'TD' : "31", 'TM' : "12", 'PP' : "20" },
      'test'    : {'FD' : "25", 'FM' : "07", 'TD' : "27", 'TM' : "07", 'PP' :  "2" },
      'weeksum' : {'FD' : "20", 'FM' : "07", 'TD' : "27", 'TM' : "07", 'PP' :  "2" },
      'weekwin' : {'FD' : "10", 'FM' : "01", 'TD' : "17", 'TM' : "01", 'PP' :  "2" }}


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
            "list": ['no_flow_S', 'bouyant_flow_S'],
            "maxlist": ['bouyant_flow_N', 'bouyant_flow_S', 'bouyant_flow2_S',
                        'bouyant_flow12_S', 'force_flow_N', 'force_flow_S',
                        'no_flow_N', 'no_flow_S']},
    "rot": {"abbrev": "_",
            "test": [(0, 7.5, 3.0, 'S')],
            "list": [(0, 7.5, 3.0, 'S')],
            "maxlist": [(0, 7.5, 3.0, 'S'), (180, 7.5, 3.0, 'N')]},
    "per": {"abbrev": "_",
            "test": ['test'],
            "list": ['weeksum'],
            "maxlist": list(PM.keys())},
}

# %%
# Set the model configuration path and set 'variant_dict['cfg']['cfg_path']' to this
# path value.
cfg_path = (Path.cwd() / 'model' / 'cfg')
variant_dict['cfg']['cfg_path'] = cfg_path


# %%
# Run simulation for all variants in list 'VARLIST'.
VARLIST = 'list'

results = sim.process_variants(variant_dict, PM, the_list=VARLIST, ptstep=6)
