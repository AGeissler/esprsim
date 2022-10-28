"""
espsim Package
Author: gac 2022

Contents of __init__.py is based on SIA 380/1 package from mm
"""

from .espr_ms_sim import *
from .espr_sim import *
from .espr_res import *

import os
import sys
import builtins

import pandas as pd
import matplotlib.pyplot as plt

# make sure we have python 3
assert sys.version_info[0] == 3

# setup some default values for matplotlib
# described here https://matplotlib.org/stable/tutorials/introductory/customizing.html
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["figure.dpi"] = 300
# do not set a font that might not exist, use default
#plt.rcParams["font.family"] = "Inconsolata"
#plt.rcParams["font.weight"] = "light"
#plt.rcParams["font.size"] = 14
plt.rcParams["figure.autolayout"] = True
plt.rcParams["axes.grid"] = True
plt.rcParams["axes.labelpad"] = 20
plt.rcParams["axes.titlepad"] = 30
plt.rcParams["axes.labelweight"] = "light"
plt.rcParams["axes.labelsize"] = 'medium'
plt.rcParams["legend.frameon"] = True
plt.rcParams["legend.facecolor"] = "white"
plt.rcParams["legend.edgecolor"] = "white"
plt.rcParams["axes.axisbelow"] = True
plt.rcParams["lines.markersize"] = 4


# Define your own color map or use a named one,
# see https://matplotlib.org/stable/tutorials/colors/colormaps.html
# plt.rcParams["axes.prop_cycle"] = plt.cycler('color', ['#5d8aa8', '#e32636', '#ffbf00', '#87a96b'])
# plt.rcParams["axes.prop_cycle"] = plt.cycler("color", plt.cm.Set1.colors)

def running_in_ipython() -> bool:
    """Check if we are running in Jupyter."""
    return getattr(builtins, "__IPYTHON__", False)


def fatal_error(filename: str, err: Exception) -> None:
    """A fatal error in the module."""
    filename = os.path.basename(filename)
    e = sys.exc_info()[-1]
    if e is not None:
        lineno = sys.exc_info()[-1].tb_lineno
    else:
        lineno = "--"
    print(f"{filename}:{lineno} -> {err}")
    sys.exit(1)

