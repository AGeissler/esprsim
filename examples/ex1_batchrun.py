#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Achim Geissler <achim.geissler@acatalepsy.ch>
# SPDX-License-Identifier: GPL-3.0-or-later
r"""
Minimal working example
-----------------------

.. topic:: Use ``esprsim`` to run and evaluate a model

   * learn to set up necessary components of ``esprsim``

   * run simulation model and postprocess results

The example model is a simple set of three buildings with different roof tilt angles.
The roofs feature an unventilated PV installation. For model details see 'Readme.txt'
in the model doc subfolder.

.. image:: ../../examples/simple_model/images/scene1.png
   :scale: 30%

"""

# sphinx_gallery_thumbnail_number = -1
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

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
cfg_path = (Path.cwd() / 'simple_model' / 'cfg')
variant_dict['cfg']['cfg_path'] = cfg_path


# %%
# Set desired variant selection list from 'test'|'list'(|'maxlist') and then run
# simulation for all variants found in this list in dict 'variant_dict' using the method
# :py:func:`esprsim.espr_sim.process_variants`. Beware the total number of simulations
# that result.
VARLIST = 'test'

results = sim.process_variants(variant_dict, PM, the_list=VARLIST)


# %%
# Temperature dependancy of the PV module efficiency is of interest. The results include
# following data columns::
#
#     "building:Z?? PVT ??:Top-5:node 04:temperature (oC)"
#     "building:spmatl:Z?? ??:misc data:efficiency %"
#
# The first column contains time-step data of the temperature of the PV cell, the second
# column contains cell efficiency. For a x,y graph of these metrics, data-pairs for each
# time-step are required. For this, the bespoke function
# :py:func:`~esprsim.espr_utilfun.get_data_pairs` is available. Based the data pairs,
# a simple  graph showing cell efficieny vs. cell temperature is created using
# :py:func:`~esprsim.espr_utilfun.plot_efficiency_vs_temperature`. Night-time values
# (efficiency = 0) are ignored.
#
# .. note::
#    The method :py:func:`~esprsim.espr_sim.process_variants` returns a dict containing
#    a `pandas.DataFrame` for each variant, where the variant name is used as key.
#
# In this simple example we have only one variant, therefore we can use the first dict
# entry via index without knowing the key beforehand.
the_variant = list(results.keys())[0]

sim.plot_efficiency_vs_temperature(results[the_variant], the_variant).show()
