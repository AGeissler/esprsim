This folder holds documentation associated
with the model e.g. construction documents
lists of assumptions or project goals.

Model description
=================

General
-------
The example model consists of three buildings with varying roof slope (flat, 20°, 40°).

The roof has integrated PV modules of type BISOL BMU-240 (see below for specifications)
which are ventilated. The model has an integrated air flow network (afn) which calculates
resulting air flow due to buoyancy or by forced flow.

Air flow network
----------------
The roof area is split into six individual 'panels', divided into two columns named
'east' and 'west' based on their relative position in the base model orientation which
is north-south. The PV modules with ventilation layer are modelled as thermal zones in
order to allow setting up the air flow network (afn). Several pre-defined afn variants
can be found in the model 'nets' subfolder. The base case uses 'no_flow_S.afn', i.e.
an afn with very small connections between zones that leads to a virtually unventilated
case.

PV modules of type BISOL BMU-240
--------------------------------
The standard module size and cell count is
    1.649 x .991 m2 = 1.634159 m2, 60 cells

The cells are 0.156^2 m2 in size, so only 1.46016 m2 or 89.4 % of the modules are
actually covered with cells.

STC 
P_MPP = 240    W
I_SC  =   8.55 A
U_0C  =  37.90 V
I_MPP =   8.03 A
U_MPP =  29.90 V

For 3 m2 : Factor 1.83581 (2.6806 m2 actually with cells)

110 cells,

STC_3m2
P_MPP = 392    W
I_SC  =   8.55 A
U_0C  =  69.58 V
I_MPP =   8.03 A
U_MPP =  54.89 V
