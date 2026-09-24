#!/usr/bin/env python3
r"""
Minimal working example
-----------------------

.. topic:: Use ``esprsim`` to run and evaluate a model

   * learn to set up necessary components of ``esprsim``

   * run simulation model and postprocess results

The example model is a simple set of three buildings with different roof tilt angles.
The roofs feature an unventilated PV installation. For model details see 'Readme.txt'
in the model doc subfolder.

.. image:: ../../examples/model/images/scene1.png
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
cfg_path = (Path.cwd() / 'model' / 'cfg')
variant_dict['cfg']['cfg_path'] = cfg_path


# %%
# Set desired variant selection list from 'test'|'list'(|'maxlist') and then run
# simulation for all variants found in this list in dict 'variant_dict' using the method
# :py:func:`esprsim.espr_sim.process_variants`. Beware the total number of simulations
# that result.
VARLIST = 'test'

results = sim.process_variants(variant_dict, PM, the_list=VARLIST)


# %%
# We want to show the temperature dependancy of the PV module efficiency. The results
# include following data columns::
#
#     "building:Z20 PVT E2:Top-5:node 04:temperature (oC)"
#     "building:spmatl:Z20 E2:misc data:efficiency %"
#
# The first column containds the time-step data of the temperature of the PV cell, the
# second column contains the cell efficiency. For a x,y graph of these metrics, we need
# to generate data-pairs for each time-step. For this, we define a bespoke function
# (code by Perplexity).
def get_data_pairs(df):
    """Extract specific data-pairs from simulation results dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        Results dataframe from :py:func:`esprsim.espr_sim.process_variants`.

    """
    cols = pd.Series(df.columns, name="column")
    parts = cols.str.split(":", expand=True)

    is_temp = cols.str.contains(":Top-5:node 04:temperature ", regex=False)
    is_eff = cols.str.endswith(":misc data:efficiency %")

    temp_keys = parts.loc[is_temp, 1].str.replace(" PVT", "", regex=False)
    eff_keys = parts.loc[is_eff, 2]

    pairs = pd.concat(
        {"temperature": pd.Series(cols[is_temp].to_numpy(), index=temp_keys),
         "efficiency": pd.Series(cols[is_eff].to_numpy(), index=eff_keys)
         },
        axis=1,
    ).dropna()

    return pairs


# %%
# Define a a bespoke function to generate a simple graph showing cell efficieny vs. cell
# temperature (code by Perplexity). Ignore night-time values (efficiency = 0).
def plot_efficiency_vs_temperature(df, title):
    pairs = get_data_pairs(df)

    fig, ax = plt.subplots(figsize=(9, 6))

    for key, pair in pairs.iterrows():
        ax.scatter(
            df[pair["temperature"]][df[pair["efficiency"]]>0],
            df[pair["efficiency"]][df[pair["efficiency"]]>0],
            label=key,
            alpha=0.7,
        )

    ax.set(
        xlabel="Cell temperature (°C)",
        ylabel="Cell efficiency (%)",
        title=title,
    )
    ax.grid(True, alpha=0.3)
    ax.legend(title="Panel")
    fig.tight_layout()

    return fig

# %%
# .. note::
#    The method :py:func:`esprsim.espr_sim.process_variants` returns a dict containing
#    a `pandas.DataFrame` for each variant, where the variant name is used as key.
#
# In this simple example we have only one variant, therefore we can use the first dict
# entry via index without knowing the key beforehand.
the_variant = list(results.keys())[0]

plot_efficiency_vs_temperature(results[the_variant], the_variant).show()
