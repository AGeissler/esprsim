*Geometry 1.1,GEN,Bath1 # tag version, format, zone name
*date Mon Aug 17 19:18:34 2020  # latest file modification 
Bath1 describes a room for bath
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,16.25002,6.30000,0.00000  #   1
*vertex,15.15000,6.30000,0.00000  #   2
*vertex,15.15000,5.25000,0.00000  #   3
*vertex,14.15000,5.25000,0.00000  #   4
*vertex,14.15000,3.79999,0.00000  #   5
*vertex,16.25000,3.79999,0.00000  #   6
*vertex,16.25002,6.30000,3.00000  #   7
*vertex,15.15000,6.30000,3.00000  #   8
*vertex,15.15000,5.25000,3.00000  #   9
*vertex,14.15000,5.25000,3.00000  #  10
*vertex,14.15000,3.79999,3.00000  #  11
*vertex,16.25000,3.79999,3.00000  #  12
*vertex,15.65000,3.80000,0.00000  #  13
*vertex,15.65000,3.80000,2.25000  #  14
*vertex,14.65001,3.80000,2.25000  #  15
*vertex,14.65001,3.80000,0.00000  #  16
*vertex,16.25001,4.54998,1.75000  #  17
*vertex,16.25000,5.55000,1.75000  #  18
*vertex,16.25000,5.55000,2.25000  #  19
*vertex,16.25001,4.54998,2.25000  #  20
# 
# tag, number of vertices followed by list of associated vert
*edges,10,6,1,7,19,18,17,20,19,7,12  #   1
*edges,6,7,8,9,10,11,12  #   2
*edges,8,1,6,13,16,5,4,3,2  #   3
*edges,4,1,2,8,7  #   4
*edges,8,13,6,12,11,5,16,15,14  #   5
*edges,4,4,5,11,10  #   6
*edges,4,3,4,10,9  #   7
*edges,4,2,3,9,8  #   8
*edges,4,16,13,14,15  #   9
*edges,4,17,18,19,20  #  10
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,Bth_E,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   1 ||< external
*surf,Ceil_Bath1,CEIL,-,PARTN,-,CT_Ceiling,OPAQUE,ANOTHER,008,008  #   2 ||< Ceil_Bath1:Roof
*surf,Grd_Bath1,FLOR,-,-,-,CT_Ground,OPAQUE,GROUND,0,001  #   3 ||< user def grnd profile  1
*surf,Bth_Gar,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,004,004  #   4 ||< Bth_Gar:Garage
*surf,Bd1_Bth_1,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,005,005  #   5 ||< Bd1_Bth_1:BedRoom_1
*surf,Bd1_Bth_2,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,006,006  #   6 ||< Bd1_Bth_2:BedRoom_1
*surf,Bd1_Bth_3,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,007,007  #   7 ||< Bd1_Bth_3:BedRoom_1
*surf,bd1_Bth_4,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,008,008  #   8 ||< bd1_Bth_4:BedRoom_1
*surf,Door_Bd1_Bth,VERT,Bd1_Bth_1,DOOR,UNDERCUT,CT_Int_Door,OPAQUE,ANOTHER,012,009  #   9 ||< Door_Bd1_Bth:BedRoom_1
*surf,Win_Bth1,VERT,Bth_E,C-WINDOW,CRACK,CT_Ext_Window,SCF8783_06nb,EXTERIOR,00,000  #  10 ||< external
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,4.20,0  # zone base
