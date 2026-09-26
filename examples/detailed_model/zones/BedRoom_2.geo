*Geometry 1.1,GEN,BedRoom_2 # tag version, format, zone name
*date Sat Aug 29 14:05:31 2020  # latest file modification 
BedRoom_2 describes a room for bed
*previous_rotate   180.00,  13.120,  10.600  # prior rotation angle X Y
# tag, X co-ord, Y co-ord, Z co-ord
*vertex,2.50000,3.65000,0.00000  #   1
*vertex,0.00000,3.65001,0.00000  #   2
*vertex,0.00000,0.00001,0.00000  #   3
*vertex,3.99999,0.00000,0.00000  #   4
*vertex,4.00001,3.64999,0.00000  #   5
*vertex,2.50000,3.65000,3.00000  #   6
*vertex,0.00000,3.65001,3.00000  #   7
*vertex,0.00000,0.00001,3.00000  #   8
*vertex,3.99999,0.00000,3.00000  #   9
*vertex,4.00001,3.64999,3.00000  #  10
*vertex,2.75001,3.65000,0.00000  #  11
*vertex,2.75001,3.65000,2.25000  #  12
*vertex,3.75000,3.65000,2.25000  #  13
*vertex,3.75000,3.65000,0.00000  #  14
*vertex,1.10000,-0.00001,1.00000  #  15
*vertex,3.09999,0.00000,1.00000  #  16
*vertex,3.09999,0.00000,2.25000  #  17
*vertex,1.10000,-0.00001,2.25000  #  18
# 
# tag, number of vertices followed by list of associated vert
*edges,4,1,2,7,6  #   1
*edges,4,2,3,8,7  #   2
*edges,10,3,4,9,17,16,15,18,17,9,8  #   3
*edges,5,6,7,8,9,10  #   4
*edges,7,1,11,14,5,4,3,2  #   5
*edges,4,4,5,10,9  #   6
*edges,8,11,1,6,10,5,14,13,12  #   7
*edges,4,14,11,12,13  #   8
*edges,4,15,16,17,18  #   9
# 
# surf attributes:
#  surf name, surf position VERT/CEIL/FLOR/SLOP/UNKN
#  child of (surface name), useage (pair of tags) 
#  construction name, optical name
#  boundary condition tag followed by two data items
*surf,Bd2_Bth2,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,005,001  #   1 ||< Bd2_Bth2:BathRoom_2
*surf,Bd2_W,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   2 ||< external
*surf,Bd2_N,VERT,-,WALL,-,CT_Ext_Wall,OPAQUE,EXTERIOR,00,000  #   3 ||< external
*surf,Ceil_Bd2,CEIL,-,PARTN,-,CT_Ceiling,OPAQUE,ANOTHER,011,011  #   4 ||< Ceil_Bd2:Roof
*surf,Grd_Bd2,FLOR,-,-,-,CT_Ground,OPAQUE,GROUND,0,003  #   5 ||< user def grnd profile  3
*surf,Sal_Bd2_1,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,008,006  #   6 ||< Sal_Bd2_1:Salon
*surf,Sal_Bd2_2,VERT,-,PARTN,-,CT_Int_Wall,OPAQUE,ANOTHER,007,007  #   7 ||< Sal_Bd2_2:Salon
*surf,Dr_Sal_Bd2,VERT,Sal_Bd2_2,DOOR,UNDERCUT,CT_Int_Door,OPAQUE,ANOTHER,025,008  #   8 ||< Door_Sal_Bd2:Salon
*surf,Win_Bd2,VERT,Bd2_N,C-WINDOW,CRACK,CT_Ext_Window,SCF8783_06nb,EXTERIOR,00,000  #   9 ||< external
# 
*insol,3,0,0,0  # default insolation distribution
# 
# shading directives
*shad_calc,all_applicable   3 # list of surfs
  2  3  9
# 
*insol_calc,all_applicable   1 # insolation sources
  9
# 
*base_list,0,14.60,0  # zone base
# 
# block entities:
#  *obs = obstructions
*block_start, 20 20 # geometric blocks
*obs,16.2500,0.0000,2.5000,16.2500,1.0000,0.0500,180.00,1.00,bed2_obs CT_wall_obs  # block   1
*end_block
