*Geometry 1.1,GEN,BedRoom_1 # tag version, format, zone name
*date Sat Aug 29 14:05:26 2020  # latest file modification 
Room1 describes a main (parent) beedroom
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,15.15000,6.30000,0.00000  #   1
*vertex,11.85000,6.30001,0.00000  #   2
*vertex,11.85000,3.80000,0.00000  #   3
*vertex,11.85000,0.00001,0.00000  #   4
*vertex,16.25000,0.00000,0.00000  #   5
*vertex,16.25000,3.79999,0.00000  #   6
*vertex,14.15000,3.79999,0.00000  #   7
*vertex,14.15000,5.25000,0.00000  #   8
*vertex,15.15000,5.25000,0.00000  #   9
*vertex,15.15000,6.30000,3.00000  #  10
*vertex,11.85000,6.30001,3.00000  #  11
*vertex,11.85000,3.80000,3.00000  #  12
*vertex,11.85000,0.00001,3.00000  #  13
*vertex,16.25000,0.00000,3.00000  #  14
*vertex,16.25000,3.79999,3.00000  #  15
*vertex,14.15000,3.79999,3.00000  #  16
*vertex,14.15000,5.25000,3.00000  #  17
*vertex,15.15000,5.25000,3.00000  #  18
*vertex,15.65000,3.80000,0.00000  #  19
*vertex,14.65001,3.80000,0.00000  #  20
*vertex,14.65001,3.80000,2.25000  #  21
*vertex,15.65000,3.80000,2.25000  #  22
*vertex,12.90000,0.00000,1.00000  #  23
*vertex,14.89998,0.00000,1.00000  #  24
*vertex,14.89998,0.00000,2.25000  #  25
*vertex,12.90000,0.00000,2.25000  #  26
*vertex,11.84999,1.57500,0.00000  #  27
*vertex,11.85000,0.57499,0.00000  #  28
*vertex,11.85000,0.57499,2.25000  #  29
*vertex,11.84999,1.57500,2.25000  #  30
# 
# tag, number of vertices followed by list of associated vert
*edges,4,2,3,12,11  #   1
*edges,8,3,27,30,29,28,4,13,12  #   2
*edges,10,4,5,14,13,26,25,24,23,26,13  #   3
*edges,4,5,6,15,14  #   4
*edges,8,6,19,22,21,20,7,16,15  #   5
*edges,4,7,8,17,16  #   6
*edges,4,8,9,18,17  #   7
*edges,4,9,1,10,18  #   8
*edges,9,10,11,12,13,14,15,16,17,18  #   9
*edges,13,1,9,8,7,20,19,6,5,4,28,27,3,2  #  10
*edges,4,1,2,11,10  #  11
*edges,4,19,20,21,22  #  12
*edges,4,23,24,25,26  #  13
*edges,4,27,28,29,30  #  14
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,Sal_Bd1_1,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,012,001  #   1 ||< Sal_Bd1_1:Salon
*surf,Sal_Bd1_2,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,013,002  #   2 ||< Sal_Bd1_2:Salon
*surf,Bd1_N,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   3 ||< external
*surf,Bd1_E,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   4 ||< external
*surf,Bd1_Bth_1,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,005,005  #   5 ||< Bd1_Bth_1:Bath1
*surf,Bd1_Bth_2,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,006,006  #   6 ||< Bd1_Bth_2:Bath1
*surf,Bd1_Bth_3,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,007,007  #   7 ||< Bd1_Bth_3:Bath1
*surf,bd1_Bth_4,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,008,008  #   8 ||< bd1_Bth_4:Bath1
*surf,Ceil_Bd1,CEIL,-,PARTN,-,CT_Ceiling,OPAQUE,ANOTHER,007,007  #   9 ||< Ceil_Bd1:Roof
*surf,Grd_Bd1,FLOR,-,-,-,CT_Ground,OPAQUE,GROUND,0,003  #  10 ||< user def grnd profile  3
*surf,Bd1_Gar,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,003,011  #  11 ||< Bd1_Gar:Garage
*surf,Door_Bd1_Bth,VERT,Bd1_Bth_1,DOOR,UNDERCUT,CT_Int_Door,OPAQUE,ANOTHER,009,012  #  12 ||< Door_Bd1_Bth:Bath1
*surf,Win_Bd1,VERT,Bd1_N,C-WINDOW,CRACK,CT_Ext_Window,SCF8783_06nb,EXTERIOR,00,000  #  13 ||< external
*surf,Door_Sal_Bd1,VERT,Sal_Bd1_2,DOOR,UNDERCUT,CT_Int_Door,OPAQUE,ANOTHER,018,014  #  14 ||< Door_Sal_Bd1:Salon
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,all_applicable   3 # list of surfs
  3  4 13
# 
*insol_calc,all_applicable   1 # insolation sources
 13
# 
*base_list,0,23.52,0  # zone base
# 
# block entities:
#  *obs = obstructions
*block_start, 20 20 # geometric blocks
*obs,16.2500,0.0000,2.5000,16.2500,1.0000,0.0500,180.00,1.00,bed1_obs CT_wall_obs  # block   1
*end_block
