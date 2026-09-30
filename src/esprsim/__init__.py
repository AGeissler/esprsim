# SPDX-FileCopyrightText: 2026 Achim Geissler <achim.geissler@acatalepsy.ch>
# SPDX-License-Identifier: GPL-3.0-or-later
from .__about__ import __version__

import matplotlib.pyplot as plt

from .espr_utilfun import *
from .espr_ms_sim import *
from .espr_sim import *
from .espr_res import *

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
