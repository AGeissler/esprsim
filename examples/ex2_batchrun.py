#!/usr/bin/env python3
r"""
PV yield and buoyant flow
-------------------------

.. topic:: Use ``esprsim`` to run and evaluate model variants

   * set up desired variants via dict's ``PM`` and ``variant_dict``

   * run simulation model and postprocess results

PV yield for without and with bouyant air flow in the air gap between PV modules and
the roof is compared.

.. image:: ../../examples/simple_model/images/wireframe.png
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
# for which a range of values is to be simulated. The keys 'cfg' and 'per' are mandatory.
variant_dict = {
    "cfg": {"abbrev": "",
            "test": ['PVT_Douala'],
            "list": ['PVT_Douala'],
            "maxlist": ['PVT_Douala']},
    "afn": {"abbrev": "_", # Enter air flow network file names without extension.
            "test": ['no_flow_S'],
            "list": ['no_flow_S', 'buoyant_flow_S'],
            "short": ['nofl_s', 'bouy_s'],
            "maxlist": ['buoyant_flow_N', 'buoyant_flow_S', 'buoyant_flow2_S',
                        'buoyant_flow12_S', 'force_flow_N', 'force_flow_S',
                        'no_flow_N', 'no_flow_S']},
    "per": {"abbrev": "_",
            "test": ['test'],
            "list": ['weeksum'],
            "maxlist": list(PM.keys())},
}

# %%
# Get/set the model configuration path and set 'variant_dict['cfg']['cfg_path']' to this
# path value.
cfg_path = (Path.cwd() / 'simple_model' / 'cfg')
variant_dict['cfg']['cfg_path'] = cfg_path


# %%
# Run simulation for all variants in list 'VARLIST'.
VARLIST = 'list'

results = sim.process_variants(variant_dict, PM, the_list=VARLIST)

# %%
# Available results sets and PV yield comparison for with and without bouyancy air
# flow in the PV air gap.
#
# Results column used::
#
#     "building:spmatl:Z?? ??:misc data:pv power (W)"
#
print(f"Results sets: {list(results.keys())}")

sim.plot_pv_bars_matplotlib(results).show()
