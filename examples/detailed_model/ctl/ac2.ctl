Window and cooling control, sp 25.5 and 26.0
* Building
Zone cooling for ambient temp above 26 degC
   1  # No. of functions
* Control function    1
# senses the temperature of the current zone.
    0    0    0    0  # sensor data
# actuates air point of the current zone
    0    0    0  # actuator data
    1  # all daytypes
    1  365  # valid Mon-01-Jan - Mon-31-Dec
     1  # No. of periods in day: weekdays    
    0   19   0.000  # ctl type, law (senses ambient dry bulb temperature.), start @
     13.  # No. of data items
  0.000 0.000 5000.000 0.000 0.000 25.500 1.000 -3.000 0.000 0.000 0.000 0.000 26.000
# Function:Zone links
 0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0
* Mass Flow
Natural ventilation by window
   3  # No. of controls
* Control mass    1
# senses ambient dry bulb temperature.
   -3    0    0    0  # sensor data
# actuates flow component:   4 op_win_xlrge
   -4    4    1  # actuator data
    1  # all daytypes
    1  365  # valid Mon-01-Jan - Mon-31-Dec
     1  # No. of periods in day: weekdays    
    0    0   0.000  # ctl type (outside ambient > flow), law (on/off setpoint 25.50 inverse action ON fraction 1.000.), starting @
      3.  # No. of data items
  25.50000 -1.00000 1.00000
Ext_S         salon         op_win_xlrge
* Control mass    2
# senses ambient dry bulb temperature.
   -3    0    0    0  # sensor data
# actuates flow component:   5 op_win_large
   -4    5    4  # actuator data
    1  # all daytypes
    1  365  # valid Mon-01-Jan - Mon-31-Dec
     1  # No. of periods in day: weekdays    
    0    0   0.000  # ctl type (outside ambient > flow), law (on/off setpoint 25.50 inverse action ON fraction 1.000.), starting @
      3.  # No. of data items
  25.50000 -1.00000 1.00000
Ext_S         bed_1         op_win_large
Ext_S         bed_2         op_win_large
Ext_N         kitchen       op_win_large
Ext_N         bed_3         op_win_large
* Control mass    3
# senses ambient dry bulb temperature.
   -3    0    0    0  # sensor data
# actuates flow component:   6 op_win_small
   -4    6    2  # actuator data
    1  # all daytypes
    1  365  # valid Mon-01-Jan - Mon-31-Dec
     1  # No. of periods in day: weekdays    
    0    0   0.000  # ctl type (outside ambient > flow), law (on/off setpoint 25.50 inverse action ON fraction 1.000.), starting @
      3.  # No. of data items
  25.50000 -1.00000 1.00000
Ext_N         wc            op_win_small
Ext_E         bth_1         op_win_small
