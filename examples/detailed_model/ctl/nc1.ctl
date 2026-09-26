*CONTROL
*cdoc Window control only - sp 26.5
*mass flow
*fdoc Natural ventilation by window
   3                        # number of loops
*loop   1 flow_loop_01
   -3    0    0    0        # senses ambient dry bulb temperature.
   -4    4    1             # actuates flow component:   4 op_win_xlrge
    1                       # all day types have same control
    1  365    1             # valid Mon-01-Jan - Mon-31-Dec, periods in weekdays
    0    0   0.000   3.     # type (outside ambient > flow), law (on / off), start@
26.50000 -1.00000 1.00000  # on/off setpoint 26.50 inverse action ON fraction 1.000.
# node   to   node    via   component     supplemental
Ext_S         salon         op_win_xlrge
*loop   2 flow_loop_02
   -3    0    0    0        # senses ambient dry bulb temperature.
   -4    5    4             # actuates flow component:   5 op_win_large
    1                       # all day types have same control
    1  365    1             # valid Mon-01-Jan - Mon-31-Dec, periods in weekdays
    0    0   0.000   3.     # type (outside ambient > flow), law (on / off), start@
26.50000 -1.00000 1.00000  # on/off setpoint 26.50 inverse action ON fraction 1.000.
# node   to   node    via   component     supplemental
Ext_S         bed_1         op_win_large
Ext_S         bed_2         op_win_large
Ext_N         kitchen       op_win_large
Ext_N         bed_3         op_win_large
*loop   3 flow_loop_03
   -3    0    0    0        # senses ambient dry bulb temperature.
   -4    6    2             # actuates flow component:   6 op_win_small
    1                       # all day types have same control
    1  365    1             # valid Mon-01-Jan - Mon-31-Dec, periods in weekdays
    0    0   0.000   3.     # type (outside ambient > flow), law (on / off), start@
26.50000 -1.00000 1.00000  # on/off setpoint 26.50 inverse action ON fraction 1.000.
# node   to   node    via   component     supplemental
Ext_N         wc            op_win_small
Ext_E         bth_1         op_win_small
