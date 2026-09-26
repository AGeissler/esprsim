*Geometry 1.1,GEN,Garage # tag version, format, zone name
*date Mon Aug 17 19:18:34 2020  # latest file modification 
Garage describes a zone where vehicle can be kept
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,16.25002,11.30000,0.00000  #   1
*vertex,11.84999,11.29998,0.00000  #   2
*vertex,11.84999,9.29998,0.00000  #   3
*vertex,11.85000,6.30001,0.00000  #   4
*vertex,15.15000,6.30000,0.00000  #   5
*vertex,16.25002,6.30000,0.00000  #   6
*vertex,16.25002,11.30000,3.00000  #   7
*vertex,11.84999,11.29998,3.00000  #   8
*vertex,11.84999,9.29998,3.00000  #   9
*vertex,11.85000,6.30001,3.00000  #  10
*vertex,15.15000,6.30000,3.00000  #  11
*vertex,16.25002,6.30000,3.00000  #  12
*vertex,11.84999,6.57500,0.00000  #  13
*vertex,11.85000,7.57500,0.00000  #  14
*vertex,15.55000,11.29999,0.00000  #  15
*vertex,12.55000,11.30000,0.00000  #  16
*vertex,12.55000,11.30000,2.25000  #  17
*vertex,15.55000,11.29999,2.25000  #  18
*vertex,16.25002,7.50000,2.50000  #  19
*vertex,16.25002,10.09998,2.50000  #  20
*vertex,16.25002,10.09998,2.75000  #  21
*vertex,16.25002,7.50000,2.75000  #  22
*vertex,11.84999,6.57500,2.25000  #  23
*vertex,11.85000,7.57500,2.25000  #  24
# 
# tag, number of vertices followed by list of associated vert
*edges,8,1,15,18,17,16,2,8,7  #   1
*edges,4,2,3,9,8  #   2
*edges,4,4,5,11,10  #   3
*edges,4,5,6,12,11  #   4
*edges,10,6,1,7,21,20,19,22,21,7,12  #   5
*edges,6,7,8,9,10,11,12  #   6
*edges,10,1,6,5,4,13,14,3,2,16,15  #   7
*edges,4,15,16,17,18  #   8
*edges,4,19,20,21,22  #   9
*edges,8,13,4,10,9,3,14,24,23  #  10
*edges,4,14,13,23,24  #  11
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,Gar_frt,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   1 ||< external
*surf,Gar_W,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   2 ||< external
*surf,Bd1_Gar,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,011,003  #   3 ||< Bd1_Gar:BedRoom_1
*surf,Bth_Gar,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,004,004  #   4 ||< Bth_Gar:Bath1
*surf,Gar_E,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   5 ||< external
*surf,Ceil_gar,CEIL,-,PARTN,-,CT_Ceiling,OPAQUE,ANOTHER,006,006  #   6 ||< Ceil_gar:Roof
*surf,Grd_gar,FLOR,-,-,-,CT_Ground,OPAQUE,GROUND,0,003  #   7 ||< user def grnd profile  3
*surf,door_gar,VERT,Gar_frt,DOOR,UNDERCUT,CT_Gar_Door,OPAQUE,EXTERIOR,00,000  #   8 ||< external
*surf,glz_gar,VERT,Gar_E,C-WINDOW,OPEN,CT_Ext_Window,SCF8783_06nb,EXTERIOR,00,000  #   9 ||< external
*surf,Cel-Gar,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,005,010  #  10 ||< Cel-Gar:Cellar
*surf,door-Cel_Gar,VERT,Cel-Gar,DOOR,UNDERCUT,CT_Int_Door,OPAQUE,ANOTHER,009,011  #  11 ||< door-Cel_Gar:Cellar
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,none  # no temporal shading requested
# 
*insol_calc,none  # no insolation requested
# 
*base_list,0,22.00,0  # zone base
